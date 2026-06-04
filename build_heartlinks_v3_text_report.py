from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import pandas as pd


WORKBOOK = Path("/Users/zeke/Documents/New project 2/heartlinks_keyword_quality_analysis_enriched.xlsx")
OUT = Path("/Users/zeke/Documents/New project 2/HeartLinks ABA - Keyword Quality Summary Report - V3 Draft.md")
GA_GEO_REF = Path("/Users/zeke/Downloads/HeartLinks Georgia Geo Analysis Report [SHARED].md")
TARGET_REF = Path("/Users/zeke/Downloads/for reference Google Campaigns – List of Targeted Cities [SHARED].md")
INDIANA_REF = Path("/Users/zeke/Downloads/2026-04-27_Heartlinks_Indiana_Lead_Source_Analysis - Version 2.md")

MARKET_ORDER = [
    "Atlanta",
    "Indianapolis",
    "Baltimore",
    "New Jersey",
    "Charlotte",
    "Raleigh",
    "Other NC / Needs Review",
]

MARKET_LABEL = {
    "Atlanta": "Georgia / Atlanta",
    "Indianapolis": "Indiana / Indianapolis",
    "Baltimore": "Maryland / Baltimore",
    "New Jersey": "New Jersey",
    "Charlotte": "North Carolina / Charlotte",
    "Raleigh": "North Carolina / Raleigh",
    "Other NC / Needs Review": "North Carolina / Other NC / Needs Review",
}

NON_GA_TARGET_SUMMARY = {
    "Indianapolis": "Target reference: radius around Indianapolis up to 35 miles.",
    "Baltimore": "Target reference: Baltimore, MD.",
    "New Jersey": "Target reference: Lakewood radius plus Bergen, Brick, Essex, Hudson, Middlesex, Monmouth, Ocean, Toms River, and Union geos.",
    "Charlotte": "Target reference: Charlotte, NC.",
    "Raleigh": "Target reference: Raleigh-Durham/Fayetteville, Wake County, Raleigh, and 15 miles around Morrisville.",
    "Other NC / Needs Review": "Target reference: NC records not confidently assigned to Charlotte or Raleigh need review.",
}


def norm(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def clean_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", norm(value).lower()).strip()


def normalize_stage(value) -> str:
    text = norm(value).lower()
    if "client" in text:
        return "Client"
    if "opportunity" in text:
        return "Opportunity"
    if "lead" in text and "subscriber" not in text:
        return "Lead"
    if "subscriber" in text:
        return "Subscriber"
    return norm(value) or "Unknown"


def yes_mask(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str).str.strip().str.lower().eq("yes")


def pct(n: int, d: int) -> str:
    return "0.0%" if not d else f"{(n / d) * 100:.1f}%"


def md_table(headers: list[str], rows: list[list[object]]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        cleaned = []
        for value in row:
            text = str(value).replace("\n", " ").replace("|", "/").strip()
            cleaned.append(text)
        out.append("| " + " | ".join(cleaned) + " |")
    return "\n".join(out)


def load_data() -> pd.DataFrame:
    df = pd.read_excel(WORKBOOK, sheet_name="Record-Level Keyword Extract")
    df["Lifecycle Normalized"] = df["Lifecycle Stage"].map(normalize_stage)
    df["Primary Keyword"] = df["Primary Keyword"].fillna("No keyword found").astype(str).str.strip()
    df["State / Location"] = df["State / Location"].fillna("Unknown").astype(str).str.strip()
    df["Campaign"] = df["Campaign"].fillna("Unknown").astype(str).str.strip().replace("", "Unknown")
    df["Campaign Target Location Match"] = df["Campaign Target Location Match"].fillna("Unknown").astype(str).str.strip().replace("", "Unknown")
    df["Campaign Target Location Notes"] = df["Campaign Target Location Notes"].fillna("").astype(str)
    df["Out-of-Area Reason"] = df["Out-of-Area Reason"].fillna("").astype(str)
    df["Create Date Parsed"] = pd.to_datetime(df["Create Date"], errors="coerce")
    df["Month"] = df["Create Date Parsed"].dt.strftime("%b").fillna("Unknown")
    df["City Clean"] = df["City"].fillna("").astype(str).map(clean_key)
    df["Zip Clean"] = df["Zip Code"].fillna("").astype(str).str.extract(r"(\d{5})", expand=False).fillna("")
    return df


def parse_ga_reference() -> dict[str, dict[str, str]]:
    text = GA_GEO_REF.read_text(encoding="utf-8", errors="ignore")
    refs: dict[str, dict[str, str]] = {"zip": {}, "city": {}, "zip_city": {}}

    current_loc = ""
    current_miles = ""
    current_closest = ""

    def commit_location() -> None:
        nonlocal current_loc, current_miles, current_closest
        raw_loc = current_loc.strip()
        if not raw_loc:
            return
        if raw_loc.startswith("**") or "removed" in raw_loc.lower() or "holding" in raw_loc.lower():
            return
        zip_match = re.search(r"\b(\d{5})\b", raw_loc)
        city = re.sub(r"\([^)]*\)", "", raw_loc)
        city = re.sub(r"\b\d{5}\b", "", city)
        city = city.replace("GA", "").replace(",", "").strip()
        parts = []
        if current_miles:
            parts.append(f"Miles from Atlanta: {current_miles}")
        if current_closest:
            parts.append(f"Closest targeted city: {current_closest}")
        note = "; ".join(parts)
        if city and note:
            refs["city"][clean_key(city)] = note
            if zip_match:
                refs["zip_city"][f"{zip_match.group(1)}|{clean_key(city)}"] = note
                refs["zip"].setdefault(zip_match.group(1), note)

    for raw_line in text.splitlines():
        line = raw_line.strip().rstrip("\\").strip()
        if line.startswith("* "):
            commit_location()
            current_loc = line[2:].strip()
            current_miles = ""
            current_closest = ""
        elif current_loc and line.startswith("Miles from Atlanta:"):
            current_miles = line.split(":", 1)[1].strip()
        elif current_loc and line.startswith("Closest targeted city:"):
            current_closest = line.split(":", 1)[1].strip()
    commit_location()

    in_target = text.split("## **2) GA In-Target", 1)
    if len(in_target) == 1:
        in_target = text.split("## **2\\) GA In-Target", 1)
    if len(in_target) > 1:
        block = in_target[1].split("## **3", 1)[0]
        for city, zip_code in re.findall(r"\* ([^—\n]+?)\s*—\s*(\d{5})", block):
            note = "GA reference: in-target closed-won location."
            city_key = clean_key(city.replace(", GA", ""))
            refs["city"][city_key] = note
            refs["zip_city"][f"{zip_code}|{city_key}"] = note
            refs["zip"].setdefault(zip_code, note)

    not_targeted = text.split("## **3) GA Not Targeted", 1)
    if len(not_targeted) == 1:
        not_targeted = text.split("## **3\\) GA Not Targeted", 1)
    if len(not_targeted) > 1:
        block = not_targeted[1].split("\n\n", 2)[0] + "\n" + not_targeted[1].split("\n\n", 2)[1]
        for line in re.findall(r"\* ([^\n]+)", block):
            zip_match = re.search(r"\b(\d{5})\b", line)
            city = re.split(r"—|-", line)[0].replace(", GA", "").strip()
            detail = re.sub(r"^\s*[^—-]+[—-]\s*", "", line).strip()
            note = f"GA reference: not targeted closed-won location ({detail})." if detail else "GA reference: not targeted closed-won location."
            city_key = clean_key(city)
            refs["city"][city_key] = note
            if zip_match:
                refs["zip_city"][f"{zip_match.group(1)}|{city_key}"] = note
                refs["zip"].setdefault(zip_match.group(1), note)
    return refs


def stage_counts(group: pd.DataFrame) -> dict[str, int]:
    counts = group["Lifecycle Normalized"].value_counts()
    return {
        "Clients": int(counts.get("Client", 0)),
        "Opps": int(counts.get("Opportunity", 0)),
        "Leads": int(counts.get("Lead", 0)),
        "Subscribers": int(counts.get("Subscriber", 0)),
    }


def top_values(series: pd.Series, limit: int = 3) -> str:
    vals = [norm(v) or "Unknown" for v in series]
    vals = ["Unknown" if v.lower() in {"nan", "none", ""} else v for v in vals]
    counts = Counter(vals)
    return "; ".join(f"{display_campaign(k)}: {v}" for k, v in counts.most_common(limit))


def display_campaign(value: str) -> str:
    value = norm(value) or "Unknown"
    if re.fullmatch(r"\d{6,}", value):
        return f"{value} (numeric URL campaign ID)"
    return value


def location_label(row: pd.Series) -> str:
    city = norm(row.get("City"))
    state = norm(row.get("State/Region"))
    zip_code = norm(row.get("Zip Code"))
    if zip_code and zip_code.lower() != "nan":
        zip_match = re.search(r"\b\d{5}\b", zip_code)
        if zip_match:
            zip_code = zip_match.group(0)
        else:
            zip_code = ""
    place = ", ".join([p for p in [city, state] if p and p.lower() != "nan"])
    return f"{place} {zip_code}".strip() if zip_code else place or "Unknown location"


def top_locations(group: pd.DataFrame, limit: int = 4) -> str:
    if group.empty:
        return "None in this bucket"
    counts = Counter(location_label(row) for _, row in group.iterrows())
    return "; ".join(f"{k}: {v}" for k, v in counts.most_common(limit))


def human_theme(row: pd.Series) -> list[str]:
    lower = norm(row.get("Message")).lower()
    themes: list[str] = []
    checks = [
        ("Message Mentions ABA", "ABA therapy or service options"),
        ("Message Mentions Autism / ASD", "autism / ASD support"),
        ("Message Mentions Diagnosis", "diagnosis, evaluation, or assessment help"),
        ("Message Mentions In-Home", "in-home ABA care"),
        ("Message Mentions Behavior", "behavior, communication, or social support"),
        ("Message Mentions School / IEP", "school, IEP, or after-school scheduling"),
        ("Message Mentions ST / OT", "speech / OT alongside ABA"),
        ("Message Mentions Insurance", "insurance or Medicaid questions"),
        ("Message Mentions Schedule / Availability", "schedule or availability questions"),
        ("Message Mentions Referral / Provider", "provider referral or care coordination"),
        ("Message Mentions Spanish", "Spanish-language or interpreter needs"),
    ]
    for col, label in checks:
        if row.get(col, "") == "Yes":
            themes.append(label)
    if re.search(r"\b(hiring|job|career|position|resume|recruit)\b", lower):
        themes.append("career/staffing inquiry, not family intake")
    if row.get("Message Phone-Only Flag", "") == "Yes":
        themes.append("phone-only CTM call record")
    if row.get("Message Empty Flag", "") == "Yes":
        themes.append("no message captured")
    if not themes:
        msg_type = norm(row.get("Message Primary Type")) or "other message context"
        themes.append(msg_type)
    deduped = []
    for theme in themes:
        if theme not in deduped:
            deduped.append(theme)
    return deduped


def theme_summary(group: pd.DataFrame, limit: int = 5) -> str:
    if group.empty:
        return "No message context in this bucket"
    counts: Counter[str] = Counter()
    for _, row in group.iterrows():
        for theme in human_theme(row):
            counts[theme] += 1
    return "; ".join(f"{k}: {v}" for k, v in counts.most_common(limit))


def trend_summary(group: pd.DataFrame) -> str:
    rows = []
    for month in ["Jan", "Feb", "Mar", "Apr", "May"]:
        mg = group[group["Month"] == month]
        if mg.empty:
            continue
        sc = stage_counts(mg)
        rows.append(f"{month}: {sc['Clients']}C/{sc['Opps']}O/{sc['Leads']}L/{sc['Subscribers']}S")
    return "; ".join(rows) if rows else "No dated records"


def targeting_notes(group: pd.DataFrame, ga_refs: dict[str, dict[str, str]], market: str, limit: int = 3) -> str:
    notes: list[str] = []
    if market == "Atlanta":
        for _, row in group.iterrows():
            note = ""
            zip_code = norm(row.get("Zip Clean"))
            city_key = norm(row.get("City Clean"))
            if zip_code and city_key and f"{zip_code}|{city_key}" in ga_refs.get("zip_city", {}):
                note = ga_refs["zip_city"][f"{zip_code}|{city_key}"]
            elif city_key and city_key in ga_refs["city"]:
                note = ga_refs["city"][city_key]
            elif zip_code and zip_code in ga_refs["zip"]:
                note = ga_refs["zip"][zip_code]
            if not note:
                note = norm(row.get("Campaign Target Location Notes")) or norm(row.get("Out-of-Area Reason"))
            if note and note not in notes:
                notes.append(note)
            if len(notes) >= limit:
                break
    else:
        summary = NON_GA_TARGET_SUMMARY.get(market, "")
        if summary:
            notes.append(summary)
        for note in list(group["Campaign Target Location Notes"]) + list(group["Out-of-Area Reason"]):
            note = re.sub(r"\s+", " ", norm(note))
            if note and note not in notes:
                notes.append(note)
            if len(notes) >= limit:
                break
    if not notes:
        return "No specific location note available from allowed references/workbook fields."
    return " / ".join(notes[:limit])


def keyword_rollup(df: pd.DataFrame, ga_refs: dict[str, dict[str, str]], market: str | None = None) -> pd.DataFrame:
    g = df[df["Primary Keyword"] != "No keyword found"].copy()
    if market:
        g = g[g["State / Location"] == market].copy()
    rows = []
    for keyword, kg in g.groupby("Primary Keyword", sort=False):
        sc = stage_counts(kg)
        quality_g = kg[kg["Lifecycle Normalized"].isin(["Client", "Opportunity"])]
        low_g = kg[kg["Lifecycle Normalized"].isin(["Lead", "Subscriber"])]
        market_for_notes = market or norm(kg["State / Location"].mode().iloc[0])
        rows.append(
            {
                "Keyword": keyword,
                "Records": len(kg),
                **sc,
                "Quality": sc["Clients"] + sc["Opps"],
                "Low": sc["Leads"] + sc["Subscribers"],
                "Quality Rate": (sc["Clients"] + sc["Opps"]) / len(kg) if len(kg) else 0,
                "Low Rate": (sc["Leads"] + sc["Subscribers"]) / len(kg) if len(kg) else 0,
                "No-DX": int(yes_mask(kg["No-DX Flag"]).sum()),
                "Out-of-area": int(yes_mask(kg["Out-of-Area Lead"]).sum()),
                "Needs review": int(kg["Campaign Target Location Match"].eq("Needs Review").sum()),
                "Five-Month Trend": trend_summary(kg),
                "Client/Opp Cities": top_locations(quality_g),
                "Lower-Quality Cities": top_locations(low_g),
                "Targeting Status / Range Notes": targeting_notes(kg, ga_refs, market_for_notes),
                "Campaigns": top_values(kg["Campaign"], 3),
                "What Families Asked About": theme_summary(quality_g if not quality_g.empty else kg),
                "Lower-Quality Themes": theme_summary(low_g if not low_g.empty else kg),
            }
        )
    return pd.DataFrame(rows)


def client_driving_keywords(df: pd.DataFrame, ga_refs: dict[str, dict[str, str]], market: str | None, n: int) -> pd.DataFrame:
    roll = keyword_rollup(df, ga_refs, market)
    if roll.empty:
        return roll
    roll = roll[roll["Quality"] > 0].copy()
    if roll.empty:
        return roll
    roll["Score"] = roll["Clients"] * 5 + roll["Opps"] * 3 + roll["Quality Rate"] + roll["Records"] * 0.05
    return roll.sort_values(["Score", "Clients", "Opps", "Quality Rate", "Records"], ascending=False).head(n)


def weak_keywords(df: pd.DataFrame, ga_refs: dict[str, dict[str, str]], market: str | None, n: int) -> pd.DataFrame:
    roll = keyword_rollup(df, ga_refs, market)
    if roll.empty:
        return roll
    candidates = roll[
        (roll["Records"] >= 2)
        & (
            (roll["Quality"] == 0)
            | ((roll["Low Rate"] >= 0.70) & (roll["Low"] >= 3))
            | (roll["No-DX"] > 0)
            | (roll["Out-of-area"] > 0)
            | (roll["Needs review"] > 0)
        )
    ].copy()
    if candidates.empty:
        return candidates
    candidates["Score"] = candidates["Low"] * 2 + candidates["No-DX"] * 2 + candidates["Out-of-area"] * 2 + candidates["Needs review"] - candidates["Quality"] * 1.5
    return candidates.sort_values(["Score", "Low", "Records"], ascending=False).head(n)


def keyword_rows(frame: pd.DataFrame, weak: bool = False) -> list[list[object]]:
    rows = []
    for _, r in frame.iterrows():
        base = [
            r["Keyword"],
            int(r["Records"]),
            int(r["Clients"]),
            int(r["Opps"]),
            int(r["Leads"]),
            int(r["Subscribers"]),
            r["Five-Month Trend"],
            r["Client/Opp Cities"],
            r["Lower-Quality Cities"],
            r["Targeting Status / Range Notes"],
            r["Campaigns"],
        ]
        base.append(r["Lower-Quality Themes"] if weak else r["What Families Asked About"])
        rows.append(base)
    return rows


def market_summary_rows(df: pd.DataFrame) -> list[list[object]]:
    rows = []
    for market in MARKET_ORDER:
        g = df[df["State / Location"] == market]
        if g.empty:
            continue
        sc = stage_counts(g)
        quality = sc["Clients"] + sc["Opps"]
        rows.append(
            [
                MARKET_LABEL[market],
                len(g),
                sc["Clients"],
                sc["Opps"],
                sc["Leads"],
                sc["Subscribers"],
                f"{quality} ({pct(quality, len(g))})",
                int(yes_mask(g["No-DX Flag"]).sum()),
                int(yes_mask(g["Out-of-Area Lead"]).sum()),
            ]
        )
    return rows


def narrative_for_market(market: str, good: pd.DataFrame, weak: pd.DataFrame) -> str:
    if good.empty:
        quality_words = "No keyword with Client/Opportunity signal stood out in this market."
    else:
        quality_words = ", ".join(f"`{k}`" for k in good["Keyword"].head(4))
    if weak.empty:
        weak_words = "No major lower-quality keyword cluster stood out."
    else:
        weak_words = ", ".join(f"`{k}`" for k in weak["Keyword"].head(4))

    label = MARKET_LABEL[market]
    if market == "Atlanta":
        return (
            f"{label}: the strongest keyword story is around {quality_words}. The main location read should be tied back to the Georgia Geo Analysis Report: "
            "protect validated in-target win geos, and treat added/not-targeted Georgia cities as expansion decisions rather than automatic core targeting. "
            f"The lower-quality or review queue is led by {weak_words}, often because Subscriber/Lead records, No-DX rows, or location-review notes dilute the quality signal."
        )
    if market == "Indianapolis":
        return (
            f"{label}: quality keywords are led by {quality_words}. Subscriber volume needs careful interpretation because the Indiana reference explains that CTM can create HubSpot Subscriber contacts from hangups, voicemails, wrong numbers, and calls that did not reach intake. "
            f"The review list is led by {weak_words}; those terms should be read together with CTM and attribution leakage, not as pure keyword failure."
        )
    if market in {"Charlotte", "Raleigh", "Other NC / Needs Review"}:
        return (
            f"{label}: keep this bucket separate from the rest of North Carolina. Quality keywords are led by {quality_words}. "
            f"The review queue is led by {weak_words}, with campaign/location conflicts especially important because Charlotte and Raleigh target areas are distinct in the target-location reference."
        )
    return (
        f"{label}: quality keywords are led by {quality_words}. The review queue is led by {weak_words}. "
        "The main action is to protect the keywords with clear Client/Opportunity city evidence and separately review terms that are mostly Subscriber/Lead-heavy or location-review-heavy."
    )


def campaign_notes(df: pd.DataFrame) -> list[str]:
    numeric = sorted({c for c in df["Campaign"].dropna().astype(str) if re.fullmatch(r"\d{6,}", c)})
    pmax = df[df["Campaign"].astype(str).str.contains("PMax", case=False, na=False)]
    no_kw = df[df["Primary Keyword"] == "No keyword found"]
    notes = []
    if numeric:
        sample = ", ".join(numeric[:8])
        notes.append(
            f"Numeric campaign values observed: {sample}. In this report they are labeled as numeric URL campaign IDs because the supplied references do not directly map them to friendly campaign names."
        )
    if not pmax.empty:
        sc = stage_counts(pmax)
        notes.append(
            f"PMax produced {sc['Clients']} Clients and {sc['Opps']} Opportunities in the workbook, but it is campaign-level evidence because PMax often has limited raw keyword visibility."
        )
    notes.append(
        f"Records without usable keyword attribution: {len(no_kw)} total. These are excluded from keyword tables, but retained in the attribution discussion because they affect how complete the keyword story can be."
    )
    return notes


def build_report(df: pd.DataFrame, ga_refs: dict[str, dict[str, str]]) -> str:
    lines: list[str] = []
    no_kw = df[df["Primary Keyword"] == "No keyword found"]
    keyword_df = df[df["Primary Keyword"] != "No keyword found"]

    lines.extend(
        [
            "# HeartLinks ABA - Keyword Quality Summary Report",
            "",
            "**V3 Draft - Keyword quality, city/location context, and inquiry themes**",
            "",
            "## Executive Summary",
            "",
            "This draft answers the core question: **which keywords are working, and which keywords are not?** Working keywords are the raw keywords tied to Clients and Opportunities. Weaker keywords are the raw keywords that mostly stay in Lead or Subscriber records, carry No-DX issues, or create location-review/out-of-target questions.",
            "",
            f"The analysis uses {len(df):,} records and {df['Record ID'].nunique():,} unique Record IDs from Jan. 1 through May 30, 2026. Keyword tables exclude records without a usable raw keyword so the report stays focused on actual keywords. Attribution gaps are explained separately.",
            "",
            "The most useful keywords are the ones that combine strong Client/Opportunity counts with clear city evidence and family-service intent: ABA therapy/services, autism or ASD support, diagnosis/evaluation help, in-home ABA, behavior/communication support, and schedule or school-related care needs.",
            "",
            "Important caveat: Subscriber-heavy keywords are not automatically bad. The Indiana source-analysis reference explains that CTM can auto-create Subscriber contacts from inbound calls, including hangups, voicemails, info-only calls, wrong numbers, and calls that never reached intake. That caveat applies directionally anywhere CTM phone-only records are present.",
            "",
            "## Definitions Used in This Report",
            "",
            "- **Higher quality:** Client or Opportunity lifecycle stage.",
            "- **Lower quality:** Lead or Subscriber lifecycle stage, with Subscriber interpreted carefully because CTM may create records before intake engagement.",
            "- **Out of target:** a lead/client/opportunity location that is outside the documented campaign target geography or is not validated by the supplied target-location references.",
            "- **Location matching:** ZIP match first when the allowed references give ZIP evidence; otherwise City + State match. No outside geocoding or web lookups were used.",
            "",
            "## Market Snapshot",
            "",
            md_table(["Market", "Records", "Clients", "Opps", "Leads", "Subs", "Higher Quality", "No-DX", "Out-of-target"], market_summary_rows(df)),
            "",
            "## Overall Client-Driving Keywords",
            "",
        ]
    )

    headers = [
        "Keyword",
        "Records",
        "Clients",
        "Opps",
        "Leads",
        "Subs",
        "Five-Month Trend",
        "Client / Opportunity Cities",
        "Lower-Quality Cities",
        "Targeting Status / Range Notes",
        "Campaigns",
        "What Families Asked About",
    ]
    weak_headers = headers[:-1] + ["Lower-Quality Inquiry Themes"]
    overall_good = client_driving_keywords(df, ga_refs, None, 15)
    lines.append(md_table(headers, keyword_rows(overall_good)))
    lines.extend(["", "### What the strongest keywords are telling us", ""])
    for _, row in overall_good.head(8).iterrows():
        lines.append(
            f"- `{row['Keyword']}` produced {int(row['Clients'])} Clients and {int(row['Opps'])} Opportunities. The strongest quality cities were {row['Client/Opp Cities']}. Families were most often asking about {row['What Families Asked About']}."
        )

    lines.extend(["", "## Overall Keywords Not Working as Well", ""])
    overall_weak = weak_keywords(df, ga_refs, None, 15)
    lines.append(md_table(weak_headers, keyword_rows(overall_weak, weak=True)))
    lines.extend(["", "### What the weaker keywords are telling us", ""])
    for _, row in overall_weak.head(8).iterrows():
        reasons = []
        if int(row["No-DX"]):
            reasons.append(f"No-DX {int(row['No-DX'])}")
        if int(row["Out-of-area"]):
            reasons.append(f"out-of-target {int(row['Out-of-area'])}")
        if int(row["Needs review"]):
            reasons.append(f"location review {int(row['Needs review'])}")
        if not reasons:
            reasons.append("Lead/Subscriber-heavy")
        lines.append(
            f"- `{row['Keyword']}` needs review because it is {', '.join(reasons)}. Lower-quality cities were {row['Lower-Quality Cities']}. Lower-quality message themes were {row['Lower-Quality Themes']}."
        )

    lines.extend(["", "## Per-Market Detail", ""])
    for market in MARKET_ORDER:
        g = df[df["State / Location"] == market]
        if g.empty:
            continue
        good = client_driving_keywords(df, ga_refs, market, 8)
        weak = weak_keywords(df, ga_refs, market, 8)
        lines.extend(
            [
                f"### {MARKET_LABEL[market]}",
                "",
                narrative_for_market(market, good, weak),
                "",
                "#### Client / Opportunity keyword trend",
                "",
            ]
        )
        if good.empty:
            lines.append("No keyword with Client/Opportunity signal in this market.")
        else:
            lines.append(md_table(headers, keyword_rows(good)))
        lines.extend(["", "#### Lead / Subscriber-heavy or review keywords", ""])
        if weak.empty:
            lines.append("No major lower-quality keyword cluster in this market.")
        else:
            lines.append(md_table(weak_headers, keyword_rows(weak, weak=True)))
        lines.append("")

    lines.extend(
        [
            "## Campaign and Attribution Notes",
            "",
        ]
    )
    for note in campaign_notes(df):
        lines.append(f"- {note}")
    lines.extend(
        [
            "- `486763454` appears in the workbook as a numeric URL campaign ID, primarily from paid URLs. Because the supplied reference files do not map it to a friendly campaign name, this draft does not rename it.",
            "- For Georgia location interpretation, this draft uses the Georgia Geo Analysis Report language only: in-target closed-won geos, not-targeted closed-won geos, and the listed miles-from-Atlanta / closest-targeted-city notes.",
            "- For non-GA markets, this draft uses the Google Campaigns targeted-city reference and the enriched workbook's existing location notes.",
            "",
            "## Attribution Gaps",
            "",
            f"- `Primary Keyword = No keyword found`: {len(no_kw):,} records do not have a usable raw keyword and are excluded from keyword tables.",
            f"- Of those, {int(no_kw['Campaign'].astype(str).str.contains('PMax', case=False, na=False).sum()):,} are tied to PMax campaign paths, where keyword visibility is inherently limited.",
            f"- {int((no_kw['Message Phone-Only Flag'] == 'Yes').sum()):,} no-keyword records are phone-only CTM-style records. These can still be real inbound signals, but they should not be treated as keyword-level proof.",
            "- Direct/untracked or blank-keyword records matter because they can hide quality that came through call extensions, GMB/CTM paths, PMax, direct traffic, or forms where UTM/keyword values were not retained.",
            "",
            "## Methodology",
            "",
            "- Counts come from the enriched workbook only.",
            "- Raw keywords are not normalized, grouped, rewritten, or inferred from Message.",
            "- Message detail is summarized as client-safe themes from the Message helper flags; raw intake text is not copied into the report.",
            "- Location context is limited to the Google Campaigns target reference, the Georgia Geo Analysis Report, and enriched workbook location fields/notes.",
            "- Keyword tables exclude blank/unavailable keyword records; attribution gaps are discussed separately.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    df = load_data()
    ga_refs = parse_ga_reference()
    OUT.write_text(build_report(df, ga_refs), encoding="utf-8")
    print(f"Wrote: {OUT}")
    print(f"Rows: {len(df)}")
    print(f"Unique Record IDs: {df['Record ID'].nunique()}")
    print(f"No keyword found: {int((df['Primary Keyword'] == 'No keyword found').sum())}")
    print(f"Charlotte: {int((df['State / Location'] == 'Charlotte').sum())}")
    print(f"Raleigh: {int((df['State / Location'] == 'Raleigh').sum())}")


if __name__ == "__main__":
    main()
