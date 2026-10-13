# Demo data and interaction contract

Read when building/editing HTML. The JSON example at `../assets/tim-demo.json` is executable documentation; the builder validates required fields. All visible strings are plain text, not HTML.

## Input

Top level: `title`, `product`, `persona` (`name`, `role`), `scenarioLabel`, `evidence` (array of `id`, `claim`, `source`, `status`), `scenes`.

Each scene: unique `id`, `chapter`, `headline`, `body`, `seconds` (3–30), `visualLabel`, `cards` (1–5 objects containing `label`, `value`, `detail`), `narration`, `question`, `notes`, `evidenceIds`.

Optional scene fields: `imagePath` (local PNG/JPEG/WebP relative to the brief), `imageAlt`; `choices` (two or three objects with `label`, `result`), and `defaultChoice` (zero-based). Choice outcomes are local what-if alternatives, not live product execution or hidden assertions. Reset choices on chapter entry. Timed play uses the authored default.

Optional top level `cta`: `label`, `url` (HTTPS). Omit when no destination is supplied. Never invent a booking or product URL.

Status values: `documented`, `user-confirmed`, `illustrative`. IDs must resolve. Status is not an automatic verifier: review whether the cited evidence actually supports the action. This schema is a lightweight authoring model, not a promise of a universal product simulator.

## Presenter copy

No automatic progression by default. Space toggles play; arrows change chapters when focus is not on an input; Home/End select first/last chapter. Provide visible controls too. Notes open only when requested. Do not screen-share open private notes.

## Buyer copy

Generated independently by allowlisting fields. Omit internal notes and the private evidence ledger from both DOM and JSON; do not merely hide them with CSS. Visible copy/captures still require review for confidentiality. No notes toggle, private local paths, credentials, analytics or default outbound requests. Show captions/narrative without audio. Explicit play may advance chapters; arrival must never autoplay sound.

## Motion and accessibility

Use scene-local elapsed seconds, with finite animations. Frame state must be independent of previously visited chapters. Pausing freezes the motion; scrubbing sets a stable state. Honor OS reduced motion and the visible override. In reduced motion, show all work objects immediately; do not obscure information behind animation. Use real buttons, labeled progress control, focus indicators, text alternatives, and readable contrast. Keep the story understandable with motion disabled. Maintain touch targets and reflow on mobile.

## Delivery

Produce independent, offline HTML files with embedded data/assets, plus authoring JSON. For a simple image only, preserve its aspect ratio and avoid disguising generated UI as a real capture. Request/obtain product captures through authorized access; do not scrape authenticated applications outside the task scope. Browser render verification is required before claiming the demo works.

Share only the reviewed `send.html` file with a buyer. `present.html` and `storyboard.json` are authoring artifacts and may contain private notes. Never publish the whole output directory as the buyer experience. If browser policy prevents testing a file URL, report offline execution as unverified and verify the permitted local HTTP preview separately; do not bypass the policy.
