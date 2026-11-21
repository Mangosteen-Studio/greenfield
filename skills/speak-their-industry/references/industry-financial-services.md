# Financial services

Orientation, last reviewed 21 November 2026 against the sources linked below. Items marked *(changing)* were in flux at that date: treat them as `VERIFY:` in any briefing. Regulations and supervisory guidance change: confirm current requirements with the seller's legal or compliance team before making commitments. Do not add statistics unless the user supplies a source.

## Segments behave differently

- **Banks and credit unions:** retail, commercial and community banks, and credit unions. Deposits, lending, risk and regulatory exams dominate. Credit unions are supervised by the NCUA and state regulators, not the OCC.
- **Insurance:** property and casualty, life and annuities, health. Underwriting, claims, loss ratios and distribution dominate.
- **Capital markets and asset management:** broker-dealers, investment banks, asset and wealth managers. Assets under management, trading, client experience and compliance dominate.
- **Fintech and payments:** often faster-moving, but still bound by partner bank, card network and regulator requirements.

Size matters: a community bank and a global bank buy very differently.

## Buyers and what they are measured on

- **CFO / finance:** efficiency ratio, cost to serve, net interest margin (banks), capital and liquidity.
- **Chief risk officer:** enterprise risk, credit and operational risk, exam readiness.
- **CISO / CIO:** security, resilience, vendor risk, legacy core system constraints.
- **Chief compliance officer:** regulatory findings, anti-money-laundering (AML) and know-your-customer (KYC) programs, complaints.
- **Business line leaders (lending, deposits, claims, wealth):** growth, loss rates, cycle time, customer retention.
- **Head of procurement / third-party risk:** vendor due diligence, concentration risk, contract terms.

## How deals get approved (typical, varies by institution)

1. A business or operations sponsor owns the problem.
2. **Third-party risk management (TPRM)** due diligence: security questionnaires, financial review of the vendor, business continuity, subcontractors. This often takes longer than the commercial decision.
3. **Information security review**, often requesting a SOC 2 Type II report and penetration test results.
4. **Model risk management** review if the product uses models, scoring or AI that inform decisions.
5. **Legal and compliance review** of contract terms, data use, audit rights and regulator access.
6. Committee or executive approval; larger institutions may involve board-level risk committees for critical vendors.

## Rules that shape the deal

- **Interagency guidance on third-party relationships (US bank regulators, 2023):** banks remain responsible for risks from vendors. Question: what due diligence and ongoing monitoring will you support? *(changing)* In September 2026 the OCC, Federal Reserve, FDIC and NCUA proposed replacing this guidance with a more risk-tailored version; comments closed November 16, 2026 ([NCUA](https://ncua.gov/newsroom/press-release/2026/agencies-seek-comment-proposed-third-party-risk-management-guidance-and-issue-statement-community)).
- **Model risk management guidance (SR 26-2, April 2026, which replaced SR 11-7):** risk-based supervisory guidance for models used in decisions. Generative and agentic AI are outside its formal scope, but banks still govern them through their own AI and risk policies ([Federal Reserve](https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm)). Question: can you explain how the model works, how it is validated and monitored, and how the bank governs AI tools today? Saying "SR 11-7" to a risk leader now sounds dated.
- **Gramm-Leach-Bliley Act (GLBA):** customer financial data privacy and safeguards. Question: what customer data does the product access, and where is it stored?
- **PCI DSS (v4.0.1):** card payment data security. Question: does the product store, process or transmit card data?
- **AML / BSA and KYC requirements:** question for compliance-facing products: how does this help the institution meet its obligations and show it to examiners?
- **Fair lending and consumer protection (ECOA and Regulation B adverse action notices, UDAAP):** question for lending or customer-facing AI: how do you test for bias and explain decisions? *(changing)* Federal enforcement priorities have shifted; state attorneys general and state regulators may be the more active enforcers. Ask the buyer what their compliance team is focused on.
- **NYDFS Part 500 (New York regulated firms) and the EU's DORA (EU financial entities):** cybersecurity and operational resilience requirements that reach critical vendors.
- **SEC and FINRA rules** for broker-dealers and advisers, including communications recordkeeping.

## Words that build credibility (use correctly)

Third-party risk management, due diligence, exam findings, matters requiring attention (MRA), efficiency ratio, net interest margin, loss ratio, combined ratio (insurance), AUM, core system, model risk, operational resilience, KYC/AML.

## Outsider phrases to avoid

- "Move fast and disrupt" (risk leaders hear "unmanaged risk").
- "We're compliant with all regulations" (be specific about what you support and what remains the institution's responsibility).
- "It's a black box but it works" (model risk will stop the deal).
- Calling every buyer a "bank" when they are an insurer or asset manager.

## Common objections

- "Your company is too small / too new for our vendor risk team." Ask what the TPRM process requires; offer financials, references, insurance and continuity plans if available.
- "We'd have to integrate with our core." Ask which core and what integration approach their IT team prefers.
- "Our regulators would ask questions." Ask which regulator and what they would want to see; offer documentation, never guarantees.
- "We already built something internally." Ask what it costs to maintain and what it does not cover.
- "Not this budget cycle." Ask when planning starts and who sets priorities.

## Questions that show understanding

1. What does your third-party risk process look like for a vendor in this category, and how long does it usually take?
2. Have recent exams or audits raised anything related to this area?
3. Which core or platform would this need to work with?
4. Who in risk or compliance would need to be comfortable before you could move forward?
5. How do you measure success for this team this year?
