# HeartLinks Keyword Quality Production Report - Cloud Handoff

## Objective

Continue from the local V3 draft and create a **production-ready Markdown report** for HeartLinks ABA. The report should answer the client's main question:

**Which raw keywords are working, meaning they produce higher-quality Clients or Opportunities, and which raw keywords are not working as well, meaning they mostly produce Leads, Subscribers, No-DX, out-of-target, or location-review records?**

The output should be copy/paste-ready for Google Docs.

## Current Workspace Files To Attach / Upload

Use these local files as the working package:

- `/Users/zeke/Documents/New project 2/heartlinks_keyword_quality_analysis_enriched.xlsx`
- `/Users/zeke/Documents/New project 2/HeartLinks ABA - Keyword Quality Summary Report - V3 Draft.md`
- `/Users/zeke/Documents/New project 2/build_heartlinks_v3_text_report.py`
- `/Users/zeke/Downloads/for reference Google Campaigns – List of Targeted Cities [SHARED].md`
- `/Users/zeke/Downloads/HeartLinks Georgia Geo Analysis Report [SHARED].md`
- `/Users/zeke/Downloads/2026-04-27_Heartlinks_Indiana_Lead_Source_Analysis - Version 2.md`

Optional context files if available:

- `/Users/zeke/Downloads/Heartlinks ABA — Keyword brief 2026 so far (1).md`
- `/Users/zeke/Downloads/Heartlinks - 2026-Q1 Meeting Notes (3).md`
- `/Users/zeke/Downloads/Heartlinks - 2026-Q2 Meeting Notes (2).md`
- `/Users/zeke/Downloads/for reference of Heartlinks ABA - Paid Search  - Timeline (1).csv`
- `/Users/zeke/Downloads/for reference Heartlinks - SQR - (2_25_26 - 3_23_26) - Heartlinks - SQR - March 2026.csv`

## Current State

The existing V3 draft already includes:

- One Markdown report.
- 1,317 workbook records and 1,317 unique Record IDs.
- Separate Charlotte and Raleigh sections.
- Raw keyword tables only; `No keyword found` is excluded from keyword tables.
- `No keyword found` appears only in the Attribution Gaps section.
- Location context limited to:
  - enriched workbook fields and notes;
  - `for reference Google Campaigns – List of Targeted Cities [SHARED].md`;
  - `HeartLinks Georgia Geo Analysis Report [SHARED].md`.
- Sanitized message themes, not raw intake quotes.

## Production Revision Plan

Create a new final file:

`HeartLinks ABA - Keyword Quality Summary Report - Production Ready.md`

Do not overwrite the V3 draft unless explicitly asked.

### Add Richer Summary / Interpretation

For each city/market section, add short **Interpretation** blocks in the style of the Georgia Geo Analysis Report.

Use language similar to:

- These are high-intent, service-ready caregivers.
- The strongest themes are autism/ASD relevance, ABA service intent, in-home care, school/IEP context, ST/OT involvement, behavior/communication support, schedule needs, and insurance/Medicaid questions.
- CTM/call influence is meaningful where phone-only or call-tracking records are present.
- Localized healthcare search intent matters when keywords include city/market terms.
- Out-of-target winners are not automatically low quality; if they produce Clients or Opportunities, they may represent valid converting demand outside the current targeting boundary.

The goal is to paint a clear picture from the keywords and data, not just list counts.

### Add Recommendations

For each market, add a **Recommendation** subsection:

- Protect in-target keywords/cities producing Clients or Opportunities.
- Review lower-quality terms that are mostly Leads/Subscribers.
- Call out out-of-target expansion candidates when a city has:
  - at least 2 quality records; or
  - 1 Client plus supporting Lead/Subscriber volume.

For Georgia, include this known location context from the Georgia Geo Analysis Report / user note:

- Grayson: holding for now.
- Milton: holding for now.
- Tyrone: holding for now.
- Dallas, GA: added.
- Clarkston, GA: added.
- Ellenwood, GA: added.
- Union City, GA: added.
- Riverdale: well-covered / covered by other targets.

Only use Georgia location/range language from the Georgia Geo Analysis Report and workbook notes. Do not introduce new geocoding.

### Add Marked-for-Review Breakdown

Add a section titled:

`Why Keywords Were Marked for Review`

For each criterion, show the raw keywords that triggered it and a brief interpretation:

- **No Client or Opportunity signal:** keyword has records, but none reached Client or Opportunity.
- **Lead/Subscriber-heavy:** at least 70% of the keyword's records are Leads or Subscribers and there are at least 3 lower-quality records.
- **No-DX present:** any records for that keyword have `Qualification = No DX`.
- **Out-of-target present:** any records are flagged outside the documented target geography.
- **Location needs review:** any records have `Campaign Target Location Match = Needs Review`.

For each criterion, include examples of the exact raw keywords and explain what that type of issue means.

### Preserve Raw Keyword Rule

Do not clean, normalize, group, rewrite, or infer keywords from Message.

Examples:

- `aba home` stays separate from `in home aba`.
- `aba therapy near me` stays separate from `aba services near me`.
- `links aba` stays separate from `heartlinks aba`.
- `aba therapy charlotte nc` stays separate from `aba therapy`.
- Odd values like `in home aba%` stay as-is.

Narrative can mention keyword families, but all counts and tables must use exact raw keyword values.

### Attribution / Campaign Notes

Keep a separate Attribution Gaps section.

- Keep `No keyword found` out of all keyword tables.
- Explain records without attribution separately.
- Explain CTM Subscriber inflation using the Indiana source-analysis caveat.
- Explain PMax as campaign-level quality with limited raw keyword visibility.
- Numeric campaign IDs such as `486763454` should stay labeled as numeric URL campaign IDs unless a supplied reference explicitly maps them to a friendly campaign name.

## Verification Checklist

Before handing off the production-ready file, verify:

- The final Markdown file exists and is nonempty.
- Total records reconcile to `1,317`.
- Unique Record IDs reconcile to `1,317`.
- Charlotte and Raleigh remain split separately.
- Raw keyword tables exclude `No keyword found`.
- `No keyword found` appears only in the Attribution Gaps section.
- No raw names, emails, phone numbers, DOBs, or detailed child-specific intake quotes appear.
- Message content is sanitized into themes only.
- Every review criterion section includes triggering raw keywords.
- Georgia location language comes only from the Georgia Geo Analysis Report and workbook notes.
- Out-of-target expansion recommendations meet the agreed threshold: 2+ quality records, or 1 Client plus supporting volume.

## Final Response Needed

Return a link to:

`HeartLinks ABA - Keyword Quality Summary Report - Production Ready.md`

Include a brief verification summary.
