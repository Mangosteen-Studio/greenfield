# AccountHack

Free MIT-licensed AI account research skill for greenfield enterprise prospecting.

AccountHack helps account executives, SDRs, founders, and GTM operators research a target account before outreach. Instead of starting with generic cold messaging, you use the skill to build a structured account brief first: timing signals, warm paths, stakeholders, messaging hooks, and a concrete execution plan.

## What It Does

AccountHack is designed to turn one target account into a working outbound plan. A strong run should help you:

- identify timing signals and "why now" triggers
- find warm paths before defaulting to cold outreach
- map executives, champions, and technical buyers
- translate company research into persona-specific messaging
- produce a usable 30-day account plan instead of a loose pile of notes

## Install Or Use It

Use any one of these options.

### 1. Install as a skill for Claude Code, Gemini CLI, Antigravity, or Codex

```bash
npx skills add mangosteen-studio/accounthack
```

Then prompt:

```text
Use $accounthack to research [Company Name] and build an Account War Room before outreach.
```

### 2. Use the raw prompt file directly

```bash
curl -O https://raw.githubusercontent.com/mangosteen-studio/accounthack/main/ACCOUNT_HACK.md
```

Then paste the file into Claude, ChatGPT, Gemini, Cursor, or another capable assistant and say:

```text
Run AccountHack on [Company Name]
```

### 3. Read the installable skill file

The Codex-native version lives in [SKILL.md](./SKILL.md).

## What You Get From One Run

A good run should produce:

- a company snapshot and current strategic moment
- a `Why Now Score` with urgency-tagged triggers
- target personas with specific hooks
- a ranked warm-path priority list
- an account wedge: pain, stakeholder, initiative, and rationale
- first-message drafts by persona and channel
- LinkedIn / Sales Navigator search strings
- intelligence gaps and next actions
- a 30-day execution plan

## How It Works

AccountHack uses an 11-stage research process:

1. Trigger Radar
2. Internal Intelligence
3. Company Website and Product Analysis
4. Hiring Signals and Growth Intelligence
5. Market and Financial Intelligence
6. Leadership Deep Dive
7. LinkedIn and Change Agent Intelligence
8. Relationship and Warm Path Mapping
9. Technical Landscape and Competitive Intelligence
10. Industry Language and the One Level Deeper Rule
11. Persona-Driven Messaging

The end result is an Account War Room plus a 30-day execution OS.

## Operating Principles

AccountHack is opinionated about research quality:

- no generic output
- branch on the AE's real answers
- go one level deeper than surface industry language
- distinguish verified facts from assumptions
- cite evidence or label claims `Unverified`
- adapt to available tools instead of pretending every system is accessible

## Best Results Come From Real Inputs

AccountHack works best when you can provide or verify:

- current company news
- job postings
- earnings transcripts or investor materials
- LinkedIn or Sales Navigator research
- CRM history
- customer or partner context
- raw pasted source material for synthesis

If browsing or source material is not available, company-specific claims should be treated as hypotheses until verified.

## Repository Contents

- [SKILL.md](./SKILL.md): installable Codex skill
- [ACCOUNT_HACK.md](./ACCOUNT_HACK.md): portable markdown prompt for Claude, ChatGPT, Gemini, Cursor, and similar tools
- [agents/openai.yaml](./agents/openai.yaml): UI metadata for skill installers
- [LICENSE](./LICENSE): MIT license

## Website

Landing page: [accounthack.tools](https://accounthack.tools)

Mangosteen Studio: [mangosteen.studio](https://mangosteen.studio)

## License

AccountHack is released under the MIT License. See [LICENSE](./LICENSE).
