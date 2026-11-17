# Output contract

## Citation format

Cite inline as `[Item 7, p. 42: "we expect to complete the migration in fiscal 2027"]`. Keep quotes under 25 words. For HTML filings without page numbers, use the section heading: `[Item 7, Liquidity and Capital Resources, p. n/a: "..."]`.

Every citation must name the filing once at the top of the brief: company, form type, fiscal year end, filing date and URL when known.

## Fit table

Markdown table with these columns, ranked strongest first:

`# | Segment | Filing signal (cited) | Seller capability | Evidence (stated / inferred) | Owner | Why it matters | Discovery question`

## Fit map HTML

The template at `assets/fit-map.html` draws the map from a single `DATA` object. Replace only the contents between `/* DATA:START */` and `/* DATA:END */`. Do not edit the rest of the file.

Schema:

```js
const DATA = {
  example: false,                         // true only for the bundled fictional example
  company: { name, ticker, form, fiscalYear, filed, filingUrl },
  seller: { name, product },
  segments: [{ id, name, revenue, share, cite }],   // revenue/share as disclosed strings, or null
  signals: [{ id, kind, text, segment, cite }],     // kind: "priority" | "risk" | "spend"
  capabilities: [{ id, name }],
  owners: [{ id, name, title, cite }],
  fit: [{ capability, signal, owner, evidence, why, ask }], // evidence: "stated" | "inferred"; owner: id or null
  citations: { c1: { item, page, quote } },
  gaps: ["What the filing could not tell you"]
}
```

Rules:
- `segment`, `signal`, `capability` and `owner` fields reference the `id` of another entry.
- `cite` references a key in `citations`.
- Use `null` for anything not disclosed. Never fill a field with an estimate.
- Write strings in plain text. Do not include HTML.

## What not to say

List three to five lines the seller should avoid, for example:
- “I read in your risk factors that you're struggling with…” (risk factors are disclosures, not admissions)
- Any claim about budget, vendors or team structure that the filing does not state.
- Quoting a figure without its period.
