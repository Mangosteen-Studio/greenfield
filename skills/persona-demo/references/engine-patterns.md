# Patterns to borrow; engines to choose deliberately

Reviewed October 7, 2026. These are design influences, not runtime integrations or copies of proprietary assets.

- **Storylane:** use guided steps over real captured product UI, concise contextual explanations, and buyer-controlled navigation. Its HTML capture records editable product interfaces. Our skill does not claim to reproduce that capture infrastructure. Sources: https://docs.storylane.io/recording-demos/recording-html-demos and https://docs.storylane.io/editing-demos/adding-and-editing-guided-steps
- **Remotion:** derive visible state from time/frame and reusable, parameterized scenes. This makes seeking and revision predictable. Use an existing Remotion project if requested; read current docs before creating its adapter. Source: https://www.remotion.dev/docs/use-current-frame and https://www.remotion.dev/docs/ai/skills
- **HyperFrames:** structured HTML scenes, explicit timing and seekable animation. Its rendering/runtime contract is distinct from this standalone browser starter; native HTML must be adapted before HyperFrames rendering. If selected, load the installed HyperFrames entrypoint and core/slideshow workflows. Sources: https://hyperframes.heygen.com/ and https://github.com/heygen-com/hyperframes/blob/main/packages/core/docs/core.md
- **Three.js:** only when spatial understanding is part of the buyer's task, such as a physical asset or facility. Ordinary cases, records and handoffs rarely justify a 3D scene. Read current official documentation if selected.

Keep the seller's inputs at the level of person, situation, product and outcome. Framework selection is an implementation decision unless the user expresses a preference. Do not promise improved sales results from animation alone.
