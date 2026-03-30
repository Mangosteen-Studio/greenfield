---
name: accounthack
description: Structured AI-guided interrogation skill for breaking into greenfield accounts. Use when the user wants to research a target account, identify urgency signals and warm paths, map stakeholders, and draft persona-specific outreach before outbound.
---

# AccountHack

Use [ACCOUNT_HACK.md](./ACCOUNT_HACK.md) as the canonical workflow for this skill.

## Required workflow

1. Open [ACCOUNT_HACK.md](./ACCOUNT_HACK.md) before starting any run.
2. Follow its stage order, branching logic, LinkedIn CSV co-pilot flow, access and verification gate, and final output schema.
3. If a tool or source mentioned there is not available in the current session, adapt the action plan and mark unsupported claims `UNVERIFIED` instead of implying access you do not have.
4. If this file and [ACCOUNT_HACK.md](./ACCOUNT_HACK.md) ever diverge, [ACCOUNT_HACK.md](./ACCOUNT_HACK.md) is canonical.

## Invocation

When the user asks to run AccountHack, start with the exact opener defined in [ACCOUNT_HACK.md](./ACCOUNT_HACK.md) and continue from there.
