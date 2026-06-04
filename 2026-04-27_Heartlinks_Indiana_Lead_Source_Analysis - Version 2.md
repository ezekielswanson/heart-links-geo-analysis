**Heartlinks ABA — Indiana Lead Source Analysis**

*HubSpot Export | Data through 2026-04-27 | Prepared 2026-04-29*

# **Headline**

Indiana lead volume in HubSpot has trended down each month from a Q4 2025 peak. The decline is concentrated in Paid Search (22 → 11 from March → April, a 50% MoM drop) — Organic / SEO has held flat at 8–12/month all year. Two things to keep in mind reading these numbers:

* **HubSpot data only became reliable for source attribution starting August 2025\.** The Heartlinks–HubSpot integration went live in September 2025, and CTM (call-tracking) attribution didn't start populating into HubSpot until late August 2025\. June and July 2025 show zero organic leads — which is implausible and reflects missing attribution, not actual zero volume.

* **HubSpot's contact count is higher than intake's lead count by design.** CTM auto-creates a HubSpot contact for every inbound call (including hangups, voicemails, info-only calls, wrong numbers, and any call that didn't reach intake). Those records show up as Subscriber lifecycle stage. The intake team's count reflects parents they actually contacted; HubSpot's count reflects every CTM-captured signal. Both are correct — different filters.

# **Methodology**

* **Indiana filter:** State/Region \= "Indiana" or "IN," OR phone area code matches an Indiana area code (219, 260, 317, 463, 574, 765, 812, 930). Combined definition picks up 34 contacts where the State field was blank but the phone is clearly Indiana — total 514 IN contacts in the dataset.

* **Lifecycle stage definitions (per Heartlinks):** Subscriber \= inbound call captured by CTM. Lead \= inbound form fill, not yet qualified. Opportunity \= qualified lead. Client \= signed/paying.

* **Source classification:** Paid \= Original/Latest Traffic Source contains Paid Search/Paid Social, OR Google/Microsoft ad click ID present, OR CTM Source in {Google Ads, Bing Paid, Ad Extension, Ad Extension \- Microsoft, Microsoft Location Extension, GMB Paid}. Organic \= Original/Latest Traffic Source contains Organic, OR CTM Source in {GMB Profile, Google My Business, Multi-Organic Search}. Both \= matches both rules. Direct/Untracked \= everything else (mostly Offline Sources and Direct Traffic with blank CTM).

# **Indiana Inbound Volume by Month and Source**

\*April 2026 reflects partial month (data through 2026-04-27).

| Month | Total | Paid | Organic | Both | Direct/Untracked |
| :---- | :---: | :---: | :---: | :---: | :---: |
| **2025-06** | 14 | 8 | 0 | 0 | 6 |
| **2025-07** | 50 | 15 | 0 | 0 | 35 |
| **2025-08** | 56 | 30 | 12 | 0 | 14 |
| **2025-09** | 58 | 28 | 21 | 0 | 9 |
| **2025-10** | 66 | 30 | 25 | 1 | 10 |
| **2025-11** | 48 | 26 | 8 | 0 | 14 |
| **2025-12** | 45 | 21 | 18 | 0 | 6 |
| **2026-01** | 55 | 25 | 12 | 0 | 18 |
| **2026-02** | 49 | 24 | 12 | 0 | 13 |
| **2026-03** | 40 | 22 | 10 | 0 | 8 |
| **2026-04\*** | 33 | 11 | 9 | 0 | 13 |

Note the cliff between July 2025 (0 organic) and August 2025 (12 organic) — that's the point at which CTM/GMB attribution started flowing into HubSpot, not a sudden surge in organic activity. Organic inbound likely existed in June/July as well; HubSpot just couldn't tag it.

# **Indiana Inbound by Lifecycle Stage**

This is the same volume from the table above, broken out by HubSpot lifecycle stage. Useful for comparing against the intake team's working count, since intake will primarily see Forms \+ Qualified \+ Signed (Lead \+ Opp \+ Client), and a portion of Calls (Subscribers) where the call actually reached intake.

| Month | Total | Calls (Sub) | Forms (Lead) | Qualified (Opp) | Signed (Client) | Qual. Rate |
| :---- | :---: | :---: | :---: | :---: | :---: | :---: |
| **2025-08** | 56 | 35 | 4 | 14 | 3 | 30% |
| **2025-09** | 58 | 39 | 5 | 9 | 5 | 24% |
| **2025-10** | 66 | 39 | 7 | 13 | 7 | 30% |
| **2025-11** | 48 | 24 | 7 | 16 | 1 | 35% |
| **2025-12** | 45 | 33 | 4 | 7 | 1 | 18% |
| **2026-01** | 55 | 25 | 6 | 16 | 8 | 44% |
| **2026-02** | 49 | 29 | 3 | 10 | 7 | 35% |
| **2026-03** | 40 | 26 | 4 | 6 | 4 | 25% |
| **2026-04\*** | 33 | 16 | 9 | 7 | 1 | 24% |

# **Why HubSpot's Indiana Total Is Higher Than Intake's Count**

Avi noted that intake's expected April count was closer to 20 vs. HubSpot's 31–33. The gap is the Subscriber bucket — specifically, CTM-created Subscriber records that never reached intake.

* CTM auto-generates a HubSpot contact for every call to the GBP number or any Google/Microsoft call extension, regardless of whether the call connected to intake.

* In April 2026 alone, several Subscriber records have caller-ID stub names like "WIRELESS CALLER," "INDIANAPOLIS IN," or "RUSHVILLE IN" — meaning no name was captured during the call (likely hangups, voicemails, or callers who didn't engage).

* 267 of 309 Indiana Subscribers all-time are tagged "Non-marketing contact" in HubSpot (HubSpot's own flag for low-engagement records).

* Recommended fix: send us a list of HeartLinks staff phone numbers to add to the CTM exclusion list so staff/internal calls stop generating Subscriber records.

# **Are GBP / Organic Records Unique New Leads?**

Avi asked how we determined the 34 GBP organic records are unique new leads vs. existing clients, repeat callers, or staff. Honest read on the data:

* **Existing clients — verified.** Of 43 Indiana organic contacts in 2026 Jan–Apr, only 1 was already tagged Client in HubSpot. The other 42 were net-new contacts.

* **Repeat callers — verified.** HubSpot deduplicates inbound calls to the same phone number into a single contact. Across 176 Indiana contacts in Jan–Apr 2026, only 7 phone numbers appeared more than once (one of which is an obvious test entry, "1212121212"). Repeat-caller pollution is roughly 4%.

* **Internal/staff calls — cannot verify automatically.** CTM has no way to distinguish a staff call from a parent call to the tracked number. This is a real gap. A staff phone exclusion list from Heartlinks is the only durable fix.

# **Jan–April 2026 Funnel by Source**

Lifecycle by source for the four months in question.

## **Opportunities (qualified leads, by Create Date month)**

| Month | Total | Paid | Organic | Direct/Untracked |
| :---- | :---: | :---: | :---: | :---: |
| **2025-08** | 14 | 8 | 0 | 6 |
| **2025-09** | 9 | 5 | 0 | 4 |
| **2025-10** | 13 | 5 | 1 | 7 |
| **2025-11** | 16 | 7 | 1 | 8 |
| **2025-12** | 7 | 2 | 0 | 5 |
| **2026-01** | 16 | 6 | 0 | 10 |
| **2026-02** | 10 | 4 | 2 | 4 |
| **2026-03** | 6 | 3 | 0 | 3 |
| **2026-04\*** | 7 | 1 | 1 | 5 |

## **Clients (signed, by Date Entered Client)**

| Month | Total | Paid | Organic | Direct/Untracked |
| :---- | :---: | :---: | :---: | :---: |
| **2025-09** | 3 | 0 | 0 | 3 |
| **2025-10** | 4 | 1 | 0 | 3 |
| **2025-11** | 5 | 1 | 0 | 4 |
| **2025-12** | 2 | 1 | 1 | 0 |
| **2026-01** | 2 | 1 | 0 | 1 |
| **2026-02** | 8 | 2 | 1 | 5 |
| **2026-03** | 8 | 2 | 0 | 6 |
| **2026-04\*** | 5 | 3 | 0 | 2 |

Worth flagging: February–April 2026 are the three best months on record for Indiana client closes since the integration went live (8, 8, and 5 signed clients respectively). Lead volume is down, but qualification and close rates have held up strongly.

# **What's Driving Each Source**

## **Paid Search**

* Largest tracked source. Volume dropped sharply in April (22 → 11\) — aligns with paused under-performing ad groups, bid strategy changes, and elevated Indianapolis CPCs, all of which were already in motion on the PPC side.

* Conversion is healthy: 6 signed Indiana clients from Paid Search in 2026 Jan–Apr.

## **Organic / SEO**

* Volume is steady (8–12/month). No decline.

* 34 of 38 Indiana organic leads come through CTM Source \= "GMB Profile" — phone calls from the Google Business Profile. Only 4 came via on-site SEO content. Indiana organic is essentially GMB-driven, not blog/content-driven.

* Suggests doubling down on city-level Indiana location pages (Indianapolis, Fort Wayne, Evansville) and Indiana-specific autism/ABA content. The /locations/indiana/ template clearly works.

## **Direct / Untracked**

* 13 of 19 Indiana clients in 2026 Jan–Apr came from this bucket. It's where most closes happen but where attribution is weakest.

* Most are Original Source \= "Offline Sources" with blank CTM Source. These are CTM calls where the source value didn't populate, plus form fills without UTM tracking.

* January 2026 had 18 of 47 (38%) untracked — the highest in the dataset. Worth a quick attribution audit (CTM tag firing, thank-you page event, GA→HubSpot UTM passing).

# **SEO Landing Page Insight**

Of 113 Organic \+ Both Indiana leads all-time, only 10 have a tracked First Page Seen / Landing Page URL. The rest came in as phone calls through GMB and never hit the website.

| Landing / First Page (Organic \+ Both, all-time) | Leads |
| :---- | :---: |
| **heartlinksaba.com/locations/georgia/** | 3 |
| **heartlinksaba.com/locations/indiana/** | 3 |
| **heartlinksaba.com/indiana-autism-initiatives-and-financial-support/** | 1 |
| **heartlinksaba.com/high-functioning-autism-defiance/** | 1 |
| **heartlinksaba.com/** | 1 |
| **heartlinksaba.com/understanding-autistic-hand-gestures-in-babies/** | 1 |
| **(no landing page tracked — phone-call leads via GMB / CTM)** | 103 |

The Indiana state location page is the strongest on-site SEO converter. Worth building city-level child pages and Indiana-specific content on top of that template.

# **CTM Source Detail (Jan–Apr 2026\)**

| Source class | CTM Source | Lead count |
| :---- | :---: | :---: |
| **Direct/Untracked** | (blank) | 48 |
| **Paid** | (blank — gclid only) | 39 |
| **Organic** | GMB Profile | 34 |
| **Paid** | Ad Extension (Google) | 24 |
| **Paid** | GMB Paid | 7 |
| **Paid** | Google Ads | 3 |
| **Organic** | Multi-Organic Search | 3 |
| **Paid** | Microsoft Location Extension | 2 |
| **Paid** | Ad Extension \- Microsoft | 1 |
| **Direct/Untracked** | Print | 1 |
| **Organic** | Google My Business | 1 |

# **Pre-Sep 2025 HubSpot Caveat**

Heartlinks–HubSpot integration went live in September 2025, with CTM attribution starting late August 2025\. As a result:

* Indiana clients with Date Entered Client before Sep 9, 2025 are essentially absent — the lifecycle stage was backfilled on Sep 9 for the first three Indiana clients.

* June and July 2025 show 0 organic leads, which is implausible and reflects missing attribution rather than no organic activity.

* To compare 2026 Indiana client volume against a real baseline, the most reliable source is Heartlinks's pre-HubSpot client records (likely from Avi). Pulling Indiana signed clients by month for the 12 months preceding the HubSpot integration would give a clean year-over-year comparison.

# **Recommended Next Steps**

* PPC: Continue what Sara has in motion — paused under-performers, CPC/bid optimization, monitoring April recovery.

* Staff exclusion list: Request a list of HeartLinks staff phone numbers from Avi to add to CTM exclusion. Removes a known source of Subscriber inflation.

* Pre-HubSpot baseline: Request from Avi a month-by-month Indiana signed-client count for \~12 months before September 2025, so 2026 has a true historical comparison.

* Reporting cadence: Going forward, report Indiana volume two ways — (a) total HubSpot inbound contacts, and (b) intake-engaged subset (Lead \+ Opportunity \+ Client lifecycle stages) — so Heartlinks sees both the marketing-side picture and the intake-side picture.

* SEO: Build out city-level Indiana location pages and 2–3 Indiana-specific content pieces (financial support / eligibility themes have already produced leads). The location page template is proven.

* Attribution audit: Investigate why \~30% of Indiana 2026 leads land in HubSpot with no traffic source. Confirm thank\_you\_contact event firing, CTM source field propagation, and GA→HubSpot UTM passing.