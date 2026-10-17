# Optional interactive account-plan application

Use when chosen by the candidate or explicitly required. Meet required slides/documents first. The bundled builder creates a clickable, offline HTML account plan, not a simulated live sales product.

## Authoring contract

Create `plan.json` with nonempty plain-text `title`, `candidate`, `company` and a nonempty `sections` array. Each section has nonempty `title` and `body`, optional `evidence` (public source/status text), and optional `notes` (private speaker notes). Optional top-level `privateNotes` holds panel preparation. No field accepts HTML. See [fictional-plan.json](../assets/fictional-plan.json) for an executable example.

Use sections suited to the exercise: POV, buyer map, discovery, proposed use case, execution and evidence. Put visible assumption labels in the body and supporting citations/status in evidence; don't hide uncertainty in private notes. Include only approved public information in title, candidate, company, body and evidence. An allowlist cannot detect confidential prose placed in a public field.

Run:
```
python3 scripts/build_account_plan.py /absolute/path/plan.json --out /absolute/path/output
```
Resolve the script relative to this skill's directory. The script validates structure, escapes all text, and builds independent files. Sources render as text; navigation is clickable. No network dependencies, analytics or scripts are required.

## Two audiences

- `present.html`: private presenter copy, explicit warning, expandable speaker notes and panel preparation. Do not screen-share open private notes.
- `send.html`: independently generated allowlist; no private notes in HTML, hidden elements, scripts, JSON or comments. Review visible copy for accidental sensitive content as well.

Keep plan.json and present.html private. Redact confidential customer/employer information before building a panel copy. Do not publish the output directory. If hosting is authorized, stage only the reviewed send.html as index.html in a separate publish folder. Confirm domain spelling, audience and any needed access control. The noindex directive discourages indexing but does not protect access. A company-inspired address must not suggest official company ownership.

## Verify and deliver

Render both copies in an available browser. Check section navigation and next/previous links, keyboard focus, note expansion in the presenter, no notes in the panel, readable mobile layout, and no horizontal overflow. Search the entire panel file for distinctive private-note strings; structural separation is necessary but not sufficient for confidentiality. Verify offline execution when possible; distinguish HTTP preview testing from file-mode testing.

Provide the reviewed panel copy, private presenter copy and their usage instructions separately. Report any untested rendering or hosting limits. Hosting and domain purchase are optional external actions, not consequences of creating a local app.
