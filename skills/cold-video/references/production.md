# Production brief and acceptance

Top-level JSON: `title`, `product`, `persona`, `scenarioLabel`, `evidence`, `shots`. Persona has `name`, `role`. Evidence objects have unique `id`, `claim`, `source`, `status` (`documented`, `user-confirmed`, `illustrative`).

Each shot: `id`, `seconds` (2–20), `headline`, `narration`, `visual`, `mediaType` (`product-capture`, `diagram`, `generated-scene`, `title`), `evidenceIds`. Optional `assetPath` points to a local licensed/reviewed image/video; `generationPrompt` describes an optional generated scene. Evidence must support the capability, not merely mention the product. No API credentials or private seller notes in the brief that will be shared.

The preparation helper checks the format, estimates narration pace and emits a render specification. Keep each shot's copy readable at its planned duration. It rejects a script exceeding 190 words per minute overall or per shot; slower is usually better. This is a rough drafting limit, not a voice timing measurement.

For `generated-scene`, `generationPrompt` is required. The helper emits a separate `provider-plan.json` with unresolved provider, model, access, price and budget fields. Null values are preparation placeholders, never permission to submit or spend. The plan contains only shots needing generation. Match each editorial shot duration to the selected provider's supported generation lengths; budget for generated duration, then trim in assembly. Local assets are copied into the production package; the helper does not upload them.

Recommended scene design:
- Recognizable human event: a message, queue item, case, order or account.
- One information change per shot; purposeful highlights and transitions.
- Keep case/person/customer identifiers consistent through all shots.
- Let real product UI carry feature claims; treat generated workplace shots as illustrative.
- On-screen words support the action, not a second competing narration.
- End on a relevant question that invites correction or interest.

For most prospect videos, start with 16:9 at 1920×1080, captions within safe margins and a clear poster. Recompose for vertical delivery rather than cropping essential product controls. Normalize speech and keep any music below it. Do not invent a voice clone or real-person endorsement.

Final acceptance: claims supported; prospect assumptions labeled; actual video opens; correct duration/size; no blank frames or accidental pauses; final frame holds; text readable on a small screen; captions synchronized; intelligible audio without clipping; muted comprehension; asset rights recorded; no credentials/private author notes. Keep measured results separate from hypotheses about sales effectiveness.
