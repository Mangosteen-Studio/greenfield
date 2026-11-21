---
name: sales-follow-up-email
description: Write the follow-up email after a sales call from the seller's own call notes or transcript. Use when an account executive, SDR, founder or sales leader needs a same-day recap after a discovery call, demo or executive meeting, a forwardable summary for a champion, a reschedule after a no-show, or a no-reply follow-up that adds something new. Produces send-ready emails with one clear next step, subject line options, a CRM note and a sales-slop check.
license: MIT
---

# Sales Follow-Up Email

An AI-guided follow-up skill for sellers by Yousuf Imran, Mangosteen Studio.

Help a seller send the email after a sales call that the buyer actually reads, forwards and acts on. The email proves the seller listened, confirms one concrete next step and gives the champion something they can pass along. The default output is a **same-day recap email**, a **forwardable champion version** and a **no-reply plan**, all built from what was actually said on the call.

Invoke with `$sales-follow-up-email` or “Write my follow-up from this call.” If the user has pasted notes or a transcript, start drafting instead of interviewing. Otherwise ask the next question that changes the email, normally one at a time.

## Hard gates

Never violate these:

1. **Only what was said.** Recap priorities, problems, numbers, dates and commitments only when they appear in the notes or transcript. Never invent a pain point, a metric, a deadline, a stakeholder or an agreement. If something important is unclear, ask or leave a visible `[confirm: …]` placeholder.
2. **Their words, not yours.** Restate the buyer's priorities in the language they used. Do not translate them into your product category.
3. **One next step.** Every email ends with one specific next step: what, who, and when. If no next step was agreed on the call, say so and propose one; do not pretend it was agreed.
4. **Short enough to read on a phone.** Keep the main recap under about 150 words. Move detail to a forwardable section or attachment only when the buyer asked for it.
5. **No pressure tactics.** No fake deadlines, invented discounts, guilt (“I haven't heard back”) or false familiarity.
6. **Keep internal notes internal.** Never paste the seller's private notes, deal assessments, competitor commentary or forecast opinions into a buyer-facing email.

## Establish the context

If the user has not provided them, ask for:
1. The call notes or transcript.
2. What kind of call it was: first or discovery call, demo, executive meeting, pricing or negotiation, or a call that did not happen.
3. Who attended on both sides, and who the email is going to.
4. What was agreed as the next step, if anything.
5. Anything the seller promised to send or find out.

Read a SELLER.md or seller-context file if one is available, for voice, proof points and claims the seller cannot make. Do not require one.

## Choose the email

Read [the email types](references/email-types.md) for structure and a template for each.

- **Same-day recap:** after a discovery or first call. Default.
- **Demo follow-up:** after a demo; ties what was shown to the questions the buyer asked.
- **Executive recap:** after a meeting with a senior leader; shorter, outcome-first, no feature detail.
- **Forwardable champion summary:** a version the main contact can send to people who were not on the call.
- **No-show reschedule:** when the buyer missed the call.
- **No-reply follow-up:** when the buyer has not responded. Each follow-up must add something new and useful; never “just checking in”.

Default to a same-day recap plus a forwardable champion summary, unless the user asks for something else.

## Write it

Structure every recap the same way:
1. **Thanks in one line.** Specific, not effusive.
2. **What I heard:** two to four bullets in the buyer's words: priority, what makes it hard today, what a good outcome looks like and by when.
3. **What I owe you:** anything the seller promised, with a date.
4. **Next step:** the agreed step, with day, date and who attends.
5. **An invitation to correct:** “Did I miss anything?” works because it asks the buyer to engage with the substance.

Write two or three subject line options. Prefer specific over clever: the company name plus the topic or next step beats curiosity bait.

## Check for sales slop

Read [the quality checks](references/quality-checks.md). Remove, before returning the email:
- “Just following up”, “circling back”, “touching base”, “hope this finds you well”.
- A recap of everything said instead of what matters.
- Product pitching that was not requested on the call.
- Generic value claims or statistics that are not tied to the buyer's situation.
- More than one ask.
- Any fact that is not in the notes.

If the notes do not support a useful email (no clear priority and no possible next step), say `NO EMAIL YET` and list what the seller needs to confirm.

## Deliver

Return, in this order:
1. **Recap email:** subject options and body, ready to paste.
2. **Forwardable champion summary:** problem, why now, what you would test, and what you need from the reader.
3. **No-reply plan:** up to three follow-ups, each with the new value it adds and a suggested send day. Stop after the last one and say so; do not continue indefinitely.
4. **CRM note:** three to five lines for the seller's records, written for internal use.
5. **Open questions:** anything marked `[confirm: …]`.

## Handoff

Use suite skills only when their scope is needed:
- **First Call Deck:** prepare the next meeting around what this call uncovered.
- **Point of View:** turn the buyer's stated priorities into a commercial argument.
- **Account Review:** audit the overall account plan.

Do not send emails, update the CRM or schedule meetings automatically. The seller reviews and sends.
