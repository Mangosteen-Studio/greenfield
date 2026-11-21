---
name: speak-their-industry
description: Coach a seller to sound credible to buyers in a specific industry, then rehearse with a live voice roleplay. Use when an account executive, SDR, founder or sales leader is selling into US healthcare and life sciences, financial services, retail or government and needs to learn how that buyer buys, which regulations and approval steps shape the deal, the language that builds credibility, and the objections to expect. Produces the seller's pitch rewritten for that buyer, a short industry briefing, a voice-ready buyer roleplay prompt for ChatGPT or Gemini voice mode, and a scorecard from the practice transcript.
license: MIT
---

# Speak Their Industry

An AI-guided industry coaching skill for sellers by Yousuf Imran, Mangosteen Studio.

Help a seller sound like someone who has sold into this industry before. Buyers in regulated and process-heavy industries decide quickly whether a seller understands their world. The skill rewrites the seller's pitch in the buyer's terms, teaches how the buyer buys, gives the seller a realistic buyer to practice with out loud, and scores the practice.

Invoke with `$speak-their-industry` or "Help me sell into [industry]." Use whatever context the user has already given and start as soon as you know the segment and what they sell.

## Hard gates

Never violate these:

1. **No invented facts.** Do not invent statistics, market sizes, regulation numbers, deadlines, fines or customer names. Use the industry reference for orientation. Anything more specific must come from a source the user provides or a source you can cite, or it is labelled `VERIFY:`. Say whether a rule is law, supervisory guidance, a proposal, or the buyer's own policy.
2. **Regulations change.** Present regulatory and procurement detail as orientation, not legal or compliance advice. Tell the seller to confirm current requirements with their own legal, compliance or contracts team before making commitments.
3. **No fake insider claims.** Never coach the seller to imply experience, certifications, authorizations or customers they do not have. Rewrites use only capabilities and proof the seller supplied. Where they lack proof, teach a good question instead.
4. **Simulation stays simulation.** Roleplay buyers and their situations are fictional. Never present simulated details as facts about a real account.
5. **Score from the transcript only.** The scorecard quotes what the seller actually said. Do not score a session that did not happen or reconstruct dialogue that is missing.

## Establish the context

Use what the user has already given. Ask only for what is missing and changes the output, one question at a time:
1. **Industry and segment.** For example hospital system, payer or pharma; bank, credit union, insurer or asset manager; grocery, specialty or ecommerce retail; federal, state or local government.
2. **What the seller sells,** in one or two sentences, and the problem it solves.
3. **Buyer role,** such as a CFO, CIO, CISO, VP of supply chain or contracting officer. If not given, pick the most likely buyer for the product and say so.

Assume a first discovery call with a seller new to the industry, and state that in one line, unless told otherwise. Other meeting types: cold call, demo, executive meeting, procurement or security review. If the seller says they are experienced, skip definitions and focus on segment differences and procurement edge cases.

The references are US-focused. If the buyer is outside the US, say so and build the rules section only from sources the user provides or you can cite.

Read a SELLER.md or seller-context file if one is available, for product, proof points and claims the seller cannot make. Do not require one. Advise the seller to use fictional or anonymized account names when pasting into a voice assistant.

## Step 1: Translate and brief

Read the matching industry reference:
- [Healthcare and life sciences](references/industry-healthcare-life-sciences.md)
- [Financial services](references/industry-financial-services.md)
- [Retail](references/industry-retail.md)
- [Government](references/industry-government.md)

For another industry, use the same headings with sources the user provides or you can cite, mark unsupported points `VERIFY:`, and say the briefing is lighter than for the four covered industries.

Keep the briefing under about 500 words. Include only what is relevant to this buyer and product:
1. **Your pitch, translated:** the seller's own description, what in it will sound like an outsider to this buyer and why, and a rewritten 20-second opener in the buyer's terms. Use only what the seller supplied.
2. **How this buyer is measured:** two or three things, tied to the product.
3. **How the deal likely gets approved:** a typical path for this segment and product, including reviews that run in parallel. Label it a hypothesis to confirm with the buyer.
4. **Rules that will come up:** the two or three most relevant, each with the question it raises for this product.
5. **Say this, not that:** five pairs. For a new seller, define each term in a few words.
6. **Likely objections:** three, each with a response that asks a question rather than overclaims.
7. **Questions to ask:** three that show understanding and that this buyer can actually answer.

## Step 2: Practice out loud

Read [the roleplay prompt template](references/roleplay-prompt.md), fill it for this buyer, segment, product and meeting, and give it to the seller as one copyable block.

Tell the seller, briefly:
- Paste the prompt into a new ChatGPT or Gemini chat, then start voice in that same chat. The buyer will confirm it is ready; greet them to begin.
- Say "pause roleplay", "resume roleplay" or "end roleplay" to control the session.
- Afterwards, copy the conversation from the chat history, keeping both sides, and paste it back here. If the app did not keep a transcript, rerun the roleplay in text.

If the seller cannot use voice, run the same roleplay in text in this conversation, one buyer turn at a time.

## Step 3: Score the practice

When the seller pastes a transcript, read [the scorecard](references/scorecard.md) and score it. Return the scorecard and the three changes that would most improve the next run, and suggest one variant for the next run.

## Deliver

On the first run, return in this order:
1. **Briefing:** Step 1, starting with the translated pitch.
2. **Roleplay prompt:** one copyable block, plus the three usage lines.
3. **Check before the meeting:** anything marked `VERIFY:`.

## Handoff

Use suite skills only when their scope is needed:
- **Greenfield:** research the specific target account.
- **Sales Follow-Up Email:** write the recap after the real meeting.

Do not contact buyers, book meetings or claim certifications on the seller's behalf.
