# Codex Reader Guide for `prod_report`

Use this file before editing `prod_report`.

The `prod_report` file is long and table-heavy. Codex must not rely only on the opening section or the first visible chunk. The report contains important later sections that explain market-level keyword quality, review flags, expansion candidates, attribution gaps, and methodology.

## Primary task

Update `prod_report` so it becomes a clearer, story-driven keyword quality report.

Primary audience: the paid search colleague who manages keywords.
Secondary audience: the HeartLinks ABA client.

The stakeholder question the report must answer is:

> “I especially would love to see if there are any trends on what keywords are working (have higher quality leads/clients) and what aren't! trends on what keywords are working (have higher quality leads/clients) and what aren't!”

This means the report should focus first on keyword quality, with geo/location context used to explain whether the keyword demand is serviceable, expandable, noisy, or not useful.

## Before editing: read `prod_report` fully

Do not rewrite `prod_report` after reading only the Executive Summary or the first table.

Read the full file in this order:

1. Opening context and definitions
2. Market Snapshot
3. Overall Client-Driving Keywords
4. Overall High-Intent Lead Keywords Worth Watching
5. Overall Keywords Not Working as Well
6. Out-of-Target Expansion Watchlist
7. Per-Market Detail
   - Georgia / Atlanta
   - Indiana / Indianapolis
   - Maryland / Baltimore
   - New Jersey
   - North Carolina / Charlotte
   - North Carolina / Raleigh
   - North Carolina / Other NC / Needs Review
8. Why Keywords Were Marked for Review
   - No Client or Opportunity signal
   - Lead/Subscriber-heavy
   - No-DX present
   - Out-of-target present
   - Location needs review
9. Complete Raw Keyword Inventory
10. Campaign and Attribution Notes
11. Attribution Gaps
12. Methodology

If the file is too large to inspect in one pass, use heading-based or chunked reading. Do not assume the first 100-150 lines are enough.

## Report sections that matter most

### 1. Executive Summary

The existing report already says it answers which exact raw keywords produce higher-quality Clients or Opportunities and which produce Leads, Subscribers, No-DX, out-of-target, or location-review records.

Rewrite this section so it directly answers the paid search stakeholder question:

- Which raw keywords are working?
- Which raw keywords are bringing higher-quality Leads, Opportunities, and Clients?
- Which raw keywords are not proving quality?
- Which raw keywords are valuable but noisy?
- Where are the best keyword/location paths coming from?
- What should the paid search team do next?

### 2. Overall Client-Driving Keywords

This is the main source for the highest-quality keyword story.

Use it to build a new narrative section called:

```markdown
## Keyword Story: What Is Actually Working?
```

Then add:

```markdown
## Top Winning Keyword Paths
```

Use this section to identify keyword paths like:

- `heartlinks aba`
- `aba home`
- `aba therapy near me`
- `aba pediatric therapy`
- `aba therapy children`
- `aba therapy services`
- `in home aba`
- `aba services near me`
- `links aba`
- `links aba therapy`
- `atlanta autism center`

For each keyword, explain:

- Clients produced
- Opportunities produced
- Lead volume
- Subscriber volume
- locations where quality appeared
- why the keyword matters
- whether it should be protected, reviewed, expanded, or not scaled

### 3. High-Intent Lead Keywords

The report has high-intent Lead sections, but they need more explanation.

Add a section called:

```markdown
## High-Intent Leads Worth Watching
```

Explain that a Lead is not automatically low quality. A Lead may be high intent when the keyword and message theme show service-ready demand, even if the record has not yet become an Opportunity or Client.

Use this section to separate:

- Lead-stage demand worth nurturing
- Lead-stage demand that is noisy
- Lead-stage demand that needs intake or location validation

### 4. Keywords Not Proving Quality

The report has review sections, but it should be more decisive for paid search.

Add a section called:

```markdown
## Keywords That Are Clearly Not Proving Quality Yet
```

Organize into categories:

1. No Client or Opportunity signal
2. Lead/Subscriber-heavy with weak quality
3. No-DX-heavy or qualification concern
4. Out-of-target with no quality justification
5. Location/campaign mismatch or tracking artifact

Important distinction:

Do not call a keyword bad if it has produced Clients or Opportunities. Instead, call it valuable but noisy and recommend review/segmentation.

Example:

- `heartlinks aba` is not a bad keyword because it produced Clients/Opps, but it is noisy because it also produced many Subscribers and review flags.
- `links aba` / `links aba therapy` may be valuable but CTM/Subscriber-heavy.
- Keywords with no Client/Opp signal and mostly Subscriber-only records should not be expanded without separate evidence.

### 5. Out-of-Target Expansion Watchlist

The existing report has expansion watchlist data, but it needs a decision framework.

Add a section called:

```markdown
## Expansion Candidates: Keyword + Location Opportunities
```

Use three confidence levels:

#### High-confidence expansion candidates

Criteria:

- Produced Client or Opportunity
- Location appears serviceable or near target
- Keyword has strong service intent
- Not Subscriber-only

#### Needs validation before expansion

Criteria:

- Produced quality, but city/ZIP/campaign location is inconsistent
- Campaign appears to belong to another market
- Small sample size
- Location may be a data-quality issue

#### Do not expand yet

Criteria:

- Subscriber-only
- No Client/Opp signal
- No-DX-heavy
- Clearly outside service area
- CTM-only or no message captured

Preserve any existing report statement that a market had no expansion candidate meeting the agreed threshold.

### 6. Per-Market Detail

Before each detailed market table, add a short story section.

Use this format:

```markdown
### [Market] — Keyword Story

- Best quality signals:
- High-intent Leads:
- Review/noise:
- Location story:
- Action:
```

Keep each market story concise. The detailed tables can remain below for audit/detail.

### 7. January-May trend story

The report contains month-by-month trend strings, but they are hard to read.

Add a section called:

```markdown
## Keyword Trend Read: January through May
```

Create a table with:

- Raw Keyword
- Jan-May Quality Pattern
- Trend Interpretation
- Action

Use simple trend language:

- Consistent quality signal
- Quality in early months, noisy later
- Lead-heavy but worth nurturing
- Subscriber-heavy / CTM noise
- One-off Client/Opp signal; validate before scaling
- No Client/Opp signal; do not expand yet

Do not overstate causation. Use wording like “suggests,” “indicates,” “worth reviewing,” and “needs validation.”

### 8. Attribution Gaps

Preserve the attribution gap section.

The report notes that many records have `Primary Keyword = No keyword found`. These records are excluded from keyword tables but still matter to the broader story.

Explain this clearly near the top:

- Keyword-level conclusions are directional.
- Some real demand may be hidden in PMax, CTM, GMB, direct/untracked, or missing UTM paths.
- Do not treat keyword tables as the complete story of all paid-search demand.

### 9. Methodology and privacy

Preserve the methodology and privacy rules:

- Use exact raw keywords only.
- Do not normalize, merge, or rewrite keywords.
- Do not infer keywords from Message field.
- Message context should remain client-safe themes only.
- Do not include names, emails, phone numbers, DOBs, or child-specific quotes.
- Keep counts grounded in the enriched workbook/report data.

## Desired new top-level structure for `prod_report`

Reorder or add sections so the report reads like this:

```markdown
# HeartLinks ABA - Keyword Quality Summary Report

## Executive Summary

## How to Read This Report

## Keyword Story: What Is Actually Working?

## Top Winning Keyword Paths

## Keyword Trend Read: January through May

## High-Intent Leads Worth Watching

## Keywords That Are Clearly Not Proving Quality Yet

## Expansion Candidates: Keyword + Location Opportunities

## Market Snapshot

## Market-by-Market Keyword Story

### Georgia / Atlanta — Keyword Story
[short narrative]
[detailed tables]

### Indiana / Indianapolis — Keyword Story
[short narrative]
[detailed tables]

### Maryland / Baltimore — Keyword Story
[short narrative]
[detailed tables]

### New Jersey — Keyword Story
[short narrative]
[detailed tables]

### North Carolina / Charlotte — Keyword Story
[short narrative]
[detailed tables]

### North Carolina / Raleigh — Keyword Story
[short narrative]
[detailed tables]

### North Carolina / Other NC / Needs Review — Keyword Story
[short narrative]
[detailed tables]

## Why Keywords Were Marked for Review

## Complete Raw Keyword Inventory

## Campaign and Attribution Notes

## Attribution Gaps

## Methodology
```

## Output rules

- Update `prod_report` directly.
- Do not invent counts.
- Do not delete detailed tables unless they are exact duplicates or obviously broken.
- Add narrative sections above detailed tables.
- Keep markdown Google Docs friendly.
- Use concise tables for decision summaries.
- Use bullets for market stories.
- Keep the report practical for a paid-search colleague.

## Final quality check

After editing, the report should clearly answer:

1. What keywords are bringing the highest-quality people?
2. What locations are those quality keywords coming from?
3. What keywords are producing high-intent Leads worth watching?
4. What keywords are mostly noise or not producing quality?
5. What out-of-area keyword/location combinations might be expansion candidates?
6. How did keyword quality trend from January through May?
7. What should the paid search colleague do next?
