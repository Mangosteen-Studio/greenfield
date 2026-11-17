---
name: 10k-xray
description: Turn a public company's 10-K into a cited product-fit map for sales. Use when an account executive, SDR, founder or sales leader wants to understand a target account's business segments, stated priorities, risks and spending signals from its annual report, and see where their product credibly fits. Produces a 10-K X-Ray Brief, a cited fit table, discovery questions and an animated fit-map HTML file.
license: MIT
---

# 10-K X-Ray

An AI-guided annual-report skill for sellers by Yousuf Imran, Mangosteen Studio.

Help a seller read a target company's 10-K the way a strategist would, then show exactly where their product fits inside that business: which segment, which stated priority or risk, which executive owns it, and which question to ask next. The default output is a **10-K X-Ray Brief**, a cited fit table and a filled fit map built from [the fit-map template](assets/fit-map.html).

Invoke with `$10k-xray` or “X-Ray [Company]'s 10-K for [what I sell].” Ask the next question that changes the result, normally one at a time. If the user has already supplied the filing and their product, start reading instead of interviewing.

## Hard gates

Never violate these:

1. **Every fact carries a citation.** Each segment figure, priority, risk, spending signal and executive name cites its Item (or note) and a short verbatim quote. Add the page number when the filing shows one; for HTML filings without pages, cite the section heading and mark the page `n/a`. If it cannot be quoted, mark it `UNVERIFIED` or leave it out.
2. **No invented numbers.** Copy figures exactly as disclosed, with their units and period. If a segment's revenue is not disclosed, write `not disclosed`. Never derive a budget for the seller's category from total capex, opex or revenue.
3. **The filing states priorities; the seller supplies the fit.** Keep what the company said separate from the seller's hypothesis about how their product helps. A fit row is a hypothesis to test in discovery, not a finding.
4. **“No supported fit” is a valid answer.** Do not force a mapping. Tell the seller when the filing gives them no credible reason to engage, and say what other evidence would change that.
5. **Owners come from the filing.** Name an executive only when the 10-K's executive officers list, the proxy statement (DEF 14A) or the user supplies them. Otherwise write `owner to validate`. Executive compensation goals show what leaders are measured on; they are not proof of purchasing authority.

## Establish the target

Start with two things: the target company and what the seller sells. If either is missing, ask for it.

Then check the filing gate:
- **Files a 10-K** (US-listed public company): continue.
- **Files a 20-F or 40-F** (foreign issuer): continue, mapping the equivalent sections. Say which form you used.
- **Subsidiary or division of a public company:** use the parent's 10-K, limit the analysis to the relevant segment and state that the parent filing may not describe the division's own priorities.
- **Private company, no SEC filings:** stop the X-Ray. Say so plainly and suggest Greenfield or Quick Scan for public-signal research. Do not fabricate a 10-K-style analysis from news.

Then resolve only what matters for fit:
- The seller's product, the two to five capabilities that matter most, and the buyer roles it usually serves.
- Any proof the seller can safely use, and claims they cannot make.
- Whether this is a new-logo, expansion or renewal account.

## Get the filing in

Read [the filing map](references/filing-map.md) for what each section contains and what to extract.

Use the most recent annual report unless the user asks for a different year. In order of preference:
1. **Browsing available:** find the filing on SEC EDGAR from the company name or ticker, and confirm the company, form type, fiscal year and filing date before reading.
2. **User supplies a link or PDF:** read the supplied file.
3. **Paste:** ask for one section per message, in this order: Item 1 (Business), Item 1A (Risk Factors), Item 7 (MD&A), the segment-information note in the financial statements, then the executive officers list. Write a short running summary after each section so the full filing never needs to fit in context.

Never ask the user to paste the whole 10-K. Item 1, 1A and 7 plus the segment note carry almost everything this skill needs.

## Read for sellers, not investors

Extract these, each with a citation:
- **Segments:** name, revenue and share of total for the period, exactly as disclosed.
- **Stated priorities:** strategic initiatives, investments and goals in the company's own words. Look for “we plan”, “we are investing”, “our strategy”, “we expect” and named programs.
- **Risks that matter to the seller's category:** prefer company-specific language over generic legal boilerplate. Every 10-K lists cybersecurity, competition and macro risk; only a specific, detailed or newly added risk is a strong signal. If the prior year's 10-K is available, flag what is new or changed.
- **Spending signals:** capex plans, restructuring, cost programs, acquisitions, system migrations and hiring or headcount statements, as stated.
- **Owners:** executive officers and their titles.

Skip valuation, stock performance and investment conclusions. This skill does not give investment advice.

## Map the fit

For each seller capability, look for a stated priority, risk or spending signal it could credibly support. Record each mapping as one fit row:

| Field | Content |
|---|---|
| Segment | Where in the business this applies |
| Filing signal | The priority, risk or spending signal, with citation |
| Seller capability | What the seller's product does that is relevant |
| Evidence | `stated`: the filing directly names the need. `inferred`: the link is the seller's reasoning |
| Owner | Executive from the filing, or `owner to validate` |
| Why it matters | One sentence, in the buyer's language |
| Discovery question | What the seller should ask to test the hypothesis |

Prefer three strong rows over ten weak ones. Rank rows by how directly the filing supports them, then by the size of the segment.

## Deliver the X-Ray

Use [the output contract](references/output-contract.md). Render in this order:

1. **The read:** three to five sentences on how this company makes money and what it says it is focused on.
2. **Segment snapshot:** each segment's revenue and share, cited.
3. **Fit table:** the ranked fit rows.
4. **Fit map:** fill the `DATA` block in [the fit-map template](assets/fit-map.html) and return the complete HTML file. In Claude, render it as an artifact. Elsewhere, return it in a fenced `html` block and tell the user to save it as `10k-xray.html` and open it in a browser. The fit table above remains the complete deliverable if the HTML cannot be used.
5. **Discovery questions:** the best five, each tied to a fit row.
6. **What not to say:** lines that would sound like the seller is reading the buyer's risk factors back at them, or claiming knowledge the filing does not support.
7. **Evidence and gaps:** citations list, `UNVERIFIED` items, and what the 10-K could not tell you (for example, budget, current vendors, team structure).

Before finalizing, check that every number and quote appears in the cited section, segment shares are copied rather than computed unless the filing gives both figures, owners are sourced, inferred rows are labeled, and each fit row has a discovery question. If the result fails, say `NO X-RAY YET` and list what is missing.

## Handoff

Use suite skills only when their scope is needed:
- **Point of View:** turn the strongest fit rows into a customer argument.
- **Leadership Intel:** research the executives behind the priorities.
- **First Call Deck:** build the first meeting around the fit hypothesis.
- **Greenfield:** build the full account entry plan.

Do not require these skills to complete an X-Ray. No outreach or CRM change follows automatically.
