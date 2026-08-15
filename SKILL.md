---
name: greenfield
description: |
  Structured AI-guided interrogation skill for breaking into greenfield accounts.
  Use when the user wants to research a target account, identify urgency signals
  and warm paths, map stakeholders, build an Account Brief, and draft persona-specific outreach before outbound.
---

# Greenfield

Use [GREENFIELD.md](./GREENFIELD.md) as the canonical workflow for a full run.

## Required workflow

1. Before starting any run, read the guardrails:
   - [QUALITY_GATES.md](./guardrails/QUALITY_GATES.md) — stage checkpoints to enforce
   - [VOICE.md](./guardrails/VOICE.md) — output quality and anti-slop rules
   - [VERIFICATION.md](./guardrails/VERIFICATION.md) — verification discipline
2. Follow GREENFIELD.md's stage order, branching logic, LinkedIn CSV co-pilot flow, access and verification gate, and final output schema.
3. Run the relevant quality gate checkpoint before advancing to each new stage.
4. If a tool or source mentioned there is not available in the current session, adapt the action plan and mark unsupported claims `UNVERIFIED` instead of implying access you do not have.
5. If this file and [GREENFIELD.md](./GREENFIELD.md) ever diverge, [GREENFIELD.md](./GREENFIELD.md) is canonical.

## Skill Routing

When the user's request matches a focused skill, route to it instead of running the full workflow:

| Request Pattern | Skill | Path |
|---|---|---|
| "Quick scan," "is this worth pursuing," "triage this account" | Quick Scan | [skills/quick-scan/SKILL.md](./skills/quick-scan/SKILL.md) |
| "Check urgency," "any triggers," "why now," "is this urgent" | Trigger Radar | [skills/trigger-radar/SKILL.md](./skills/trigger-radar/SKILL.md) |
| "Find warm paths," "who do I know," "LinkedIn connections," "warm intro" | Warm Path | [skills/warm-path/SKILL.md](./skills/warm-path/SKILL.md) |
| "Executive research," "leadership deep dive," "exec outreach," "earned right" | Leadership Intel | [skills/leadership-intel/SKILL.md](./skills/leadership-intel/SKILL.md) |
| "Review this account brief," "score my account plan," "audit my research" | Account Review | [skills/account-review/SKILL.md](./skills/account-review/SKILL.md) |
| "Run Greenfield," "full run," "hack this account" | Full Run | [GREENFIELD.md](./GREENFIELD.md) |

If no specific pattern matches, default to the full run.

## Suite Handoffs

Greenfield is for breaking into new-logo accounts. If the user's real need is outside that motion, route cleanly instead of forcing the Greenfield workflow:

- **POV** — use when the user already has account evidence and needs a financially grounded point of view, business case, cold email, LinkedIn DM, warm intro ask, or internal approval narrative.
- **Executive Briefing** — use when the user is selling, qualifying, or preparing an executive meeting, executive demo, or briefing.
- **Account Expansion** — use when the account is already a customer and the user needs to evaluate expansion readiness, whitespace, relationship health, and risk.
- **QBR** — use when the user needs an internal sales QBR, customer QBR, EBR, renewal review, value review, pipeline review, or next-quarter performance plan.

## Invocation

When the user asks to run Greenfield, start with the exact opener defined in [GREENFIELD.md](./GREENFIELD.md) and continue from there.

## Completion Status

Every skill run must end with:
```
STATUS: DONE | DONE_WITH_CONCERNS | INCOMPLETE | BLOCKED
```
For full Greenfield runs, append the JSON sidecar defined in [GREENFIELD.md](./GREENFIELD.md) immediately after the human status block. See [QUALITY_GATES.md](./guardrails/QUALITY_GATES.md) for the full Completion Status Protocol.
