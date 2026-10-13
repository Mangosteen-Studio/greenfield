---
name: cold-video
description: Create a short personalized prospecting video using a paid external video service such as Runway or fal.ai, built around one buyer persona and a verified product capability. Use for cold videos, video cold emails and prospect-specific solution videos. Prepare the story, provider prompts and cost estimate before paid generation, then assemble and verify the video. Sending is separate. For interactive HTML use Persona Demo.
---

# Cold Video

Make a short video in which the prospect recognizes their team's work and sees a credible future with the seller's solution. Personalization means relevant role, situation, vocabulary and workflow, not just a logo or first-name overlay.

This skill is independent of Persona Demo. It can start from product/prospect URLs, a sales brief, a script, actual captures, or an existing Persona Demo storyboard. Do not require a deck first. Do not build an interactive presentation when the user asks for a finished video.

**Production model:** the user supplies access to a paid external video service, such as Runway or fal.ai. This skill supplies the sales story, generation direction, assembly and quality checks; it does not include provider credits or an authenticated connector. Local planning is available before connecting or paying. Provider generation and final assembly are separate stages.

## Establish the story

Use available context first. Resolve seller/product, buyer role, one concrete scenario, supported capability and intended next action. If missing, ask the highest-value question and continue research that does not depend on the answer. Prefer one persona and one incident for the first draft.

Read supplied websites with available tools and save dated source URLs for factual claims. Separate publicly documented business context, user-confirmed context and illustrative assumptions. A prospect website cannot establish their private systems, employee frustrations or buying intent. Do not imply a fictional persona is a real employee. If evidence is thin, use conditional language and label the scenario rather than inventing research.

Default to roughly 30–60 seconds, adapting to the user's goal. Open on a recognizable event, show the obstacle briefly, spend most of the runtime on the future workflow, and end with one useful question or specific invitation. A workable 45-second rhythm is event (0–7), obstacle (7–13), product-enabled action (13–30), handoff/result (30–39), question (39–45). This is a starting point, not a fixed template.

Keep the claim chain explicit: product capability → observable action → plausible immediate result. Quantified time savings, revenue, named customer results and ROI require supporting evidence. Avoid fabricated prospect quotations and surveillance-like opening lines. Do not call a generic logo swap a custom scenario.

## Prepare a renderable brief

Read [production and quality](references/production.md). Write the brief using `assets/tim-video.json` as a format example. It is wholly fictional and not evidence for a real product. Run:

```sh
python3 <skill-dir>/scripts/prepare_video.py --input <brief.json> --output <new-output-dir>
```

This validates timing/evidence links and produces `storyboard.html`, `render-spec.json`, `provider-plan.json`, `narration.txt`, `captions-draft.vtt`, and `poster.svg`. These are production inputs, **not a finished video**. If adapting Persona Demo, explicitly rewrite its scene captions/narration for an independent viewer and remove speaker notes; do not just accelerate a live deck.

Create local drafts without inserting a mandatory approval stop. Present a concrete storyboard/script when user review is needed, particularly before paid generation or external disclosure.

## Produce the video

Read [paid providers](references/providers.md). Resolve the user's provider preference, available authenticated access and budget. Prepare exact prompts, references, shot count, duration, output format, price source/date and a maximum spend including any regeneration allowance. Verify current provider/model pricing. If spend is already authorized within that scope, proceed; otherwise ask for the missing budget approval with this concrete package. Creating or installing this skill does not authorize paid generation. Never ask the user to paste API secrets into chat.

Generate through the chosen provider using its current supported connector, API or authorized browser workflow. Read [Runway](references/runway.md) or [fal.ai](references/fal.md) for the relevant route. Save job IDs and outputs so a timeout cannot trigger a duplicate paid request. Review generated footage before paying for further variants.

Then read [assembly routing](references/engines.md) and select one available renderer. Honor an explicit engine preference. Otherwise prefer the installed HyperFrames workflow for final assembly; read its entrypoint and current core/CLI contracts before authoring. Reuse an existing Remotion project where appropriate. These resources are optional capabilities, not dependencies the skill can assume are installed.

Use actual product captures to demonstrate real interfaces. Use typography, callouts and transitions to connect the human situation to product action. A generated interface is a labeled concept, never proof of a feature. If captures are missing, continue with a labeled diagram/storyboard and report the missing evidence.

Use paid generation for the human/workplace narrative and visual continuity. Compose exact product screens, logos, typography and captions separately so generative footage does not corrupt them. Do not upload private prospect information or imitate a real person without appropriate authorization. If the scenario does not benefit from generated footage, explain that before spending and offer a capture-led video variant.

Finish with a deterministic rendered composition: stable scene order, deliberate timing, readable captions, licensed assets and controlled sound. Audio is optional; the story must work muted. When narration is supplied/generated, retime captions against the actual audio. `captions-draft.vtt` contains estimated scene cues and is not final synchronized caption evidence.

## Verify and deliver

Inspect an actual final render at opening, each transition, product steps and ending; listen through if audio exists. Confirm duration, dimensions, playability, legibility, caption timing, product fidelity, sources and removal of private notes. Use the renderer's lint/check tools as well; a build passing is not visual verification.

Deliver the MP4, poster, final captions, editable composition, source/assumption notes and actual provider spend when available. If access, budget or rendering is unavailable, deliver the completed production package and state what is missing; do not call a storyboard an MP4 or silently substitute a free animation for the requested generated video. Never silently change provider or increase the approved budget.

For outreach, draft an optional one-line introduction if useful. Most email clients do not support a dependable embedded interactive video; use a poster linked to an authorized hosted playback page or attach a video when appropriate. No fake play button pointing to unrelated content. Hosting, sending messages, enrolling sequences, publishing and analytics installation require separate user scope/authorization. A request for a video is not a request to email prospects.

Measure attention and replies separately: a play is not a completed view, a completed view is not a positive reply, and a reply is not pipeline. Do not add a tracking pixel or identify viewers by default.
