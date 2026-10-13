# fal.ai generation workflow

Use the current official model page for the specific video endpoint; fal hosts multiple models with different schemas, prices, durations and rights. Do not treat fal as a single video model. This file is workflow guidance, not an installed or authenticated connector.

1. Inspect available authorized access. For API use, follow current SDK setup and keep `FAL_KEY` in the approved secret environment, never in a brief or generated HTML. Do not read or print credential values to prove they exist.
2. Check the selected model's schema, input assets, duration, dimensions, output format and current billing units. Fill the provider plan and obtain any missing spending authorization.
3. Submit the approved shot to the queue once. Persist its `request_id` immediately with the model/shot mapping.
4. Poll the same request using bounded waits and provider retry guidance. A timeout is not proof of failure. Retrieve results and inspect provider error fields even when the queue status is completed.
5. Review footage for continuity, anatomy, misleading product details and legibility before assembly. Record actual usage when exposed; otherwise label spend as estimated.
6. Preserve completed results. Do not switch endpoint, duplicate an uncertain submission, add variants or increase the spend ceiling without applicable authorization.

Official references checked October 7, 2026:
- Queue submission, status and result retrieval: https://fal.ai/docs/documentation/model-apis/inference/queue
- Pricing and model selection: https://fal.ai/pricing

Without provider access or budget approval, complete the prompts, shot list and storyboard and identify generation as pending. Never represent the planning package as a generated video.
