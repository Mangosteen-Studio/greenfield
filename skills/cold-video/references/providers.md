# Paid provider plan

Cold Video is a paid-generation workflow. The skill itself carries no credits or keys. Choose Runway or fal.ai based on user preference, existing access and the current model's ability to produce the required shots. Do not generate the same draft on both by default.

Before any paid submission, complete `provider-plan.json` from the preparation helper:
- Provider and specific model/endpoint, verified from current official documentation.
- Access route: supported connector, authenticated service UI or API with an environment-based credential.
- Exact prompts, approved reference assets, duration, aspect ratio and count per shot.
- Current unit price, units, currency, price-source URL/date, estimated first-pass cost.
- Maximum authorized spend and permitted number of regeneration attempts. Include audio/upscaling/assembly charges when relevant; do not assume every cost is included in the generation rate.
- A plain-language approval record referencing actual user authorization. A JSON boolean alone is never evidence of user consent.

Preparation is free of provider calls; the helper intentionally leaves pricing and authorization unresolved. Budget null means unapproved, not unlimited. If the provider does not expose a reliable price, report that limitation and obtain a bounded spending instruction before using it.

Keep job ID, shot ID, prompt version, request time, status, asset location and reported cost in a local generation log. Submit once and resume polling the same job after interruptions. Do not run automatic paid regeneration loops. Check actual cost before proceeding to the next batch. Existing approval remains valid within its scope.

Official references, checked October 7, 2026; recheck at execution:
- Runway setup: https://docs.dev.runwayml.com/guides/setup/
- Runway pricing: https://docs.dev.runwayml.com/guides/pricing/
- fal pricing: https://fal.ai/pricing
- fal queue lifecycle: https://fal.ai/docs/documentation/model-apis/inference/queue
