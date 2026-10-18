---
name: account-tiering
description: Tier and prioritize an account executive's assigned territory using product fit, credible opportunity, buying signals, customer obligations and available selling time. Use for AE territory reviews, mixed prospect/customer books and weekly account coverage plans. Produces an evidence-backed account register and realistic priorities for the AE's selling week.
license: MIT
---

# Account Tiering

An AI-guided territory planning skill by Yousuf Imran, Mangosteen Studio.

Help an account executive decide where to spend time within their assigned territory, explain why, and state what evidence would change that decision. Support new-logo territories, existing-customer books and mixed books. The default output is a populated **Account Tiering Brief**, a sortable account register and a feasible weekly coverage plan.

Invoke with `$account-tiering` or “Tier my accounts for [product] over [planning horizon].” Reuse supplied context and ask the next question that changes the decision, normally one at a time. Do not make the user finish an interview before inspecting a supplied account list.

## Establish the decision

Start with the seller's product and the book of accounts. If both are missing, ask: “What do you sell, and can you share the account list you want to tier?” If available, read the list first and ask about the missing objective: new revenue, expansion, retention, a mixed target or a specific coverage constraint.

Resolve only what matters:
- Product/use case, customers it can serve, hard disqualifiers and relevant geography or ownership constraints.
- Planning horizon, what success means, and any existing company tier definitions.
- Whether the book contains prospects, customers, active deals or several of these.
- Available account-working hours, mandatory customer/deal commitments and research capacity.
- Data access: supplied CSV/spreadsheet, CRM, seller context, account briefs, usage, support, relationship history and public research.

The unit of planning is one AE and their assigned book, not a company-wide ICP or territory-allocation exercise. Use the employer's ICP, official account tiers, ownership rules and sales targets as context. Preserve official tiers alongside recommended AE coverage when their meanings differ; flag misassigned accounts for resolution rather than redesigning territories or reassigning ownership.

State what you can inspect. CSV-only tiering is valid, but missing access must remain visible. Use available browsing for fresh external facts and date the sources. Do not require a paid data tool or claim access to unavailable CRM, email, usage or support data.

## Keep the decisions separate

Maintain these distinct fields; do not collapse them into a single opaque score:

| Dimension | What it answers |
|---|---|
| Entity and eligibility | Is this the correct company/business unit, in this seller's book, and eligible for this offer? |
| Lifecycle | Prospect, existing customer, former customer or unknown |
| Workstream | New logo, expansion, renewal/retention, active opportunity or research; several can apply |
| Account fit / potential | How well does the use case fit, and what value could credibly be addressed? |
| Coverage tier | What level of sustained seller attention is justified? |
| Current priority | What deserves action within this planning horizon? |
| Evidence confidence | How well is this decision supported, and what is still unknown? |

Partner involvement, named-account status and open opportunities are overlays, not mutually exclusive lifecycle categories. An existing customer may have a renewal and an expansion opportunity at once. Keep one account record with distinct workstreams rather than inflating the account count.

A strong-fit account without a current reason to act can retain a high coverage tier while receiving a small monitoring allocation. A low-potential customer with an urgent service or renewal issue can receive immediate attention without being relabeled a high-value expansion target. Keep managerial attention separate from account ownership and seller priority.

## Prepare the account universe

Read [data and evidence](references/data-and-evidence.md) when ingesting a list, reconciling records or exporting results.

Preserve source IDs and input values; create normalized fields separately. Resolve names, domains, parent/subsidiary relationships, lifecycle and territory ownership before comparing accounts. Flag possible duplicates for review; a shared parent or domain alone does not justify merging buying centers. A funding announcement, acquisition, rebrand or dormant CRM record alone does not prove that the account is invalid.

Place confirmed duplicates, disqualified entities and ownership conflicts in an explicit **Resolve / exclude from this working book** queue with the evidence and recommended correction. Do not delete records or use Tier 3 as a bucket for bad data. Unknown eligibility belongs in **Needs validation**, not confirmed disqualification.

Report input rows, unique account entities, unresolved identities, exclusions and accounts actually evaluated. If the list is large, first normalize and assess available fields across it; then deepen research where a finding could change a tier or allocation. Agree or state the review scope and limits. Never describe a sampled or partial research pass as complete coverage of the whole territory.

## Define the tiering contract before applying it

Read [decision model](references/decision-model.md). Propose a short, product-specific contract with the user’s terminology and observable reasons for each tier. Treat initial definitions as a working model, not an industry standard.

Unless a company model already exists, use three coverage tiers plus a validation queue:
- **Tier 1 — focused coverage:** Strong use-case fit and credible upside or explicitly justified strategic importance warrant a named plan and sustained attention.
- **Tier 2 — selective coverage:** Viable fit warrants bounded development, targeted discovery or monitoring, with a clear condition for deeper investment.
- **Tier 3 — light coverage:** Eligible account with limited evidenced return from intensive coverage in the current strategy; retain a low-cost route and a reopening trigger.
- **Needs validation:** Critical facts are missing or conflicting. Give it a bounded validation task and a provisional tier only if the known facts justify one.

Separately assign current priority: **Act now**, **Validate next**, **Monitor**, or **Blocked / deferred**. Give a reason and a next decision date or observable trigger. “Act now” can mean retention, resolving a blocker or testing a hypothesis; it does not automatically mean sending outreach.

Do not force a fixed percentage of the book into Tier 1. Do not equate company revenue, employee count, funding or brand prestige with addressable opportunity. A firmographic screen can suggest fit; it does not establish need, budget or buying intent.

Use qualitative evidence by default. If numerical scoring is requested or supplied, document weights, scales, missing-data treatment, thresholds and disqualifiers. Label an uncalibrated score as a heuristic, never a conversion probability. Do not let a strong aggregate score override a hard constraint. Examine borderline cases and whether a reasonable weight change reverses the recommendation.

## Assess in the right selling motion

Evaluate the following without inventing precision:
- **Prospect:** Use-case fit, credible addressable scope, trigger, actual access, incumbent/switching constraints, buyer relevance and effort to reach a useful decision.
- **Existing customer:** Contracted footprint, demonstrated value/adoption, credible whitespace, relationship health, service risk, renewal timing and effort to serve. Separate protecting existing revenue from earning incremental revenue.
- **Active opportunity:** Customer-confirmed stage evidence, next commitment, buyer access, blockers, close timing and incremental seller effort. A CRM close date or rep activity count is not buyer commitment.
- **Former customer:** Why the relationship ended, what changed, any unresolved obligations and whether re-entry is credible. Do not treat all former customers as cold new logos.
- **Partner-assisted account:** Relevant access, willing field seller and a workable joint use case. A marketplace listing or partner badge alone does not demonstrate a usable route.

Do not infer account health from silence, a high outreach count or a lack of public news. Explicitly distinguish zero from unknown for spend, usage and opportunity value. Preserve contradictory facts and explain which one governs the current decision.

## Allocate the week

Convert recommendations into a time budget, not just a sorted list. Reserve time for customer obligations and committed deal work before discretionary prospecting and research. Include a buffer only as an explicit assumption, not as a hidden deduction.

Use the seller's capacity and approximate task effort. If capacity is missing, produce a ranked action queue and label hours illustrative or leave them unallocated; do not claim a feasible calendar. Avoid universal contact cadences or arbitrary “top 20” limits.

For each allocated action, state account, workstream, owner, action, expected decision/output, estimated effort, dependency and review trigger. Count shared research or partner meetings once. Keep total allocated effort within the stated budget and show overflow explicitly. If obligations exceed capacity, surface the shortfall and propose a tradeoff, reassignment or escalation; do not silently drop customer commitments.

When comparing a greenfield pursuit with a customer opportunity, compare credible incremental outcomes, effort and dependencies over the same horizon. Do not add the full renewal amount to expansion potential or total bookings twice. Without defensible values/probabilities, compare decision value and effort qualitatively; do not manufacture expected-revenue math.

Keep a small, explicit validation allocation for unknown accounts where research could change the coverage decision. Do not let already well-documented accounts absorb all attention simply because they have more data.

## Deliver and make change explainable

Use [output contract](references/output-contract.md). Include a concise recommendation first, followed by the account register, tier rationale, evidence gaps and capacity plan. Produce an actual populated result when data is supplied. An empty template or unexplained score is not a completed tiering run.

Assign both a confidence level and its reason to consequential decisions. Use **confirmed from supplied material**, **externally verified**, **inferred** or **unknown**, with source and relevant date. User-provided estimates remain estimates even when faithfully copied.

Before finalizing, check: entity counts reconcile; proposed merges/exclusions are justified; customer obligations are visible; tiers and priorities differ where warranted; upside is not double-counted; uncertain accounts are not automatically pushed down; time allocations reconcile; and every priority account has a concrete next action.

For a refresh, retain the previous tier, priority and rationale. Show what changed, the dated evidence, the new recommendation and the effective review period. Distinguish genuine changes from corrections or more complete data. A new headline alone does not justify promotion; a lack of fresh news alone does not justify demotion. Honor manager overrides but record the reason, capacity cost and expiry/review trigger.

## Handoff

Use available suite skills only when their scope is needed:
- **Greenfield:** Deepen the entry plan for a selected prospect.
- **Account Expansion:** Build a relationship-led growth plan for a selected customer.
- **Co-Selling:** Validate and activate a partner route.
- **Point of View:** Turn supported account evidence into a relevant narrative.
- **QBR:** Incorporate the tier changes, risks and coverage decisions into a portfolio review.

Do not require these skills to complete tiering. This skill produces a working plan and proposed record changes. CRM writes, ownership changes, deleting/merging accounts, calendar invitations, sharing account data and outreach require authorization for those actions; respect authorization already provided. No automatic outreach follows a tier assignment.
