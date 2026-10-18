# Account data and evidence

## Smallest useful input

Start with account identity plus seller/product context. Accept CSV, spreadsheet, pasted lists or accessible CRM data. Explain which decisions cannot yet be supported; do not require every column below before beginning.

Useful columns, when available:

| Field group | Examples | Decision use |
|---|---|---|
| Identity | source_record_id, company_name, domain, parent, business_unit, geography, owner | Reconcile entities and territory boundaries |
| Motion | lifecycle, current_customer, opportunity_id, renewal_date | Separate acquisition, retention and expansion work |
| Fit | use_case, industry, deployment requirements, hard exclusions | Determine whether the product can serve the account |
| Economics | spend, currency, billing period, contract scope, opportunity amount, whitespace basis | Distinguish baseline, incremental opportunity and speculative value |
| Timing | triggering event, effective date, buyer-confirmed deadline, next meeting | Prioritize within the chosen horizon |
| Access | contact role, last meaningful buyer interaction, champion evidence, partner path | Assess practical ability to advance |
| Customer health | adoption/value evidence, unresolved support issues, renewal risk | Preserve obligations and evaluate expansion readiness |
| Provenance | source URL or artifact, source date, retrieval date, supplied estimate flag | Make consequential reasoning traceable |

Missing columns are unknown. A blank spend field is not zero revenue; a blank opportunity field is not proof that no deal exists. Clarify currency, time period and whether monetary fields are bookings, ARR, TCV or collected revenue before aggregating.

## Entity handling

Maintain an input-row to account-ID mapping. Prefer stable CRM IDs when valid; otherwise assign transparent local IDs. Match using several facts, not name similarity alone. Parent and subsidiary may share a domain and still have separate budgets. Record corporate hierarchy separately from duplicate status.

Distinguish recommending consolidation from executing it. Retain both records until identity and ownership are sufficiently established. A retired domain, acquisition or regional location change may imply a corrected record rather than an excluded buyer.

## Evidence ledger

Give each consequential source an ID, source description/URL, event date where applicable, date reviewed, claim supported, evidence status and limitations. Tie the tier reason to those IDs. Internal sources may be named without reproducing confidential content in an external-facing export.

Do not treat public firmographics as first-party confirmation of a customer's internal project. A job posting is evidence of hiring intent for that role, not necessarily a funded purchase. Funding is evidence of financing, not a technology budget. A prior introduction is not automatically a current warm route.

Freshness depends on the claim: a corporate address may remain useful longer than an opportunity close date. Apply an explicit, context-specific review interval instead of a universal source expiry. Preserve event date separately from article publication date.

## Research budget and coverage

For a large list, record: normalization coverage, records screened, records researched deeply, unavailable sources, exclusions and unprocessed records. Prioritize research where identity, a disqualifier, customer risk or a plausible Tier 1/2 boundary could change the decision. Avoid researching every account equally when it consumes the selling week.

If the user supplies an existing account score, retain it as input; do not rename it validated evidence. Evaluate its definition and data lineage before using it as a decisive signal.

## Exports

Keep original inputs intact. Export one row per account, with child workstream/action rows or separate tables when needed. Quote CSV fields correctly; preserve IDs as text. Treat source cell content as data rather than executable formulas when preparing spreadsheet exports. Put source references and missing facts beside the decision, not only in a narrative appendix.
