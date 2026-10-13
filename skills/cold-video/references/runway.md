# Runway generation workflow

Official entrypoint checked October 7, 2026: https://docs.dev.runwayml.com/guides/using-the-api/

This skill includes workflow guidance, not an installed or authenticated Runway connector. Discover an available supported connector/SDK and verify its current model, duration, input, output, pricing and task-status contracts before use. Do not hardcode a model from memory.

Before requesting a paid generation, prepare the exact shot prompt, reference image, shot count/duration, usage destination and estimated cost. Check existing user authorization; request only missing approval. Use a fictional generic persona rather than a real prospect's likeness. Do not upload private customer screenshots or records without authorized disclosure.

Generate human/workplace establishing scenes only where they materially improve the story. Keep product UI and text outside generated footage. Freeze an approved character reference if continuity matters. Never claim a shot's depicted outcome is a verified customer result.

Submit once, retain the returned task ID and poll that task to completion with bounded waits. If a request times out after submission and the outcome is unknown, recover its status before retrying; avoid duplicate paid jobs. Stop after a failure or exhausted approved budget and preserve completed outputs. Review generated assets before adding them to the final render. Use approved asset access/download methods and observe provider delivery restrictions.

No Runway access: finish the production package and state that generation is pending provider access. An alternative provider or capture-only video requires the user's direction when it changes the requested output or spending scope. Never put API keys in HTML, URLs, storyboards, logs or generated artifacts. API credits and web-app credits may be separate; check the actual access route rather than assuming a subscription covers API use.
