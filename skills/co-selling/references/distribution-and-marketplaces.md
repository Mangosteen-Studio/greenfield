# Distribution routes and marketplace mechanics

This is a research and operating guide, not a promise of eligibility. Provider examples below were checked on 2026-09-07. Recheck current official documentation and relevant customer terms when running a plan; names, conditions, rates, caps, and transaction flows can change. Public rules do not establish a particular customer's eligibility.

## Select the route

Start with customer footprint, problem fit, seller access, technical compatibility, economics, and purchasing preference. Use AWS, Microsoft, and Google Cloud as the initial hyperscaler research set when no platform is selected. Broaden where relevant; this is workflow prioritization, not a researched market-size ranking.

| Distribution family | Role to investigate | Questions that distinguish the route |
|---|---|---|
| AWS, Microsoft, Google Cloud | Account teams, ecosystem partners, marketplace procurement, cloud workload adoption | Who creates demand; what qualifies for co-sell and commitment treatment; which offer and buyer account transact? |
| Salesforce and other large SaaS ecosystems | Installed-base access, workflow extensions, marketplace discovery and potentially transactions | Is this a directory, transactable offer, private offer, or direct vendor purchase; does any common billing or commitment benefit actually exist? |
| Data and AI platforms, including Snowflake and Databricks | Data/app distribution, technical integrations, platform sales relationships, provider-specific commercial programs | Is the product listed and eligible; who collects payment; is a benefit automatic, enrolled, or validated after purchase? |
| AI infrastructure ecosystems, such as NVIDIA and relevant model, inference, or GPU platforms | Validated solution relationships, workload demand, OEM/channel arrangements, technical and field collaboration | Is there a usable distribution and seller-engagement route at all; where does the transaction occur? Do not assume every ecosystem has a marketplace |
| Services companies, SIs, consultancies, MSPs | Buyer access, solution design, implementation, operation, and sometimes resale | What is their actual commercial role? Do not treat a services company as a hyperscaler-like distribution platform without evidence |

A services firm can recommend or carry a product, but the default here is to assess it as a solution and delivery participant. Investigate selling through it only when that arrangement is requested or evidenced.

Keep separate in every plan: **relationship channel → product supplier → hosting platform → transaction marketplace/reseller → contracting/billing entities → implementation/support owners**. One deal can involve several ecosystems. Do not count the same revenue twice or promise benefits from multiple programs without confirming compatibility.

## Provider starting points

These concise snapshots identify mechanics to investigate. They are not a universal eligibility checklist.

### AWS

AWS's co-sell resources describe ACE opportunity collaboration and ISV Accelerate. Program participation and an engaged account team are separate facts. Research the applicable program, partner status, and joint opportunity workflow. [AWS co-sell](https://aws.amazon.com/partners/co-sell-with-aws/), [ISV Accelerate](https://aws.amazon.com/partners/programs/isv-accelerate/).

Private offers support negotiated purchasing through AWS Marketplace; identify the buyer account and actual invoice/payment schedule. Verify any committed-spend treatment against the customer's agreement and current offer eligibility rather than hardcoding a generic rate. [Buyer private offers](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html).

AWS promotional credit terms exclude Marketplace charges unless AWS authorizes otherwise. Do not equate a customer's promotional credit balance with available third-party software budget. [AWS promotional credit terms](https://aws.amazon.com/awscredits/).

### Microsoft

Distinguish co-sell-ready status, applicable Azure IP co-sell requirements, offer eligibility, and actual field engagement. Check which applies before promising access or incentives. [Co-sell requirements](https://learn.microsoft.com/en-us/partner-center/referrals/co-sell-requirements), [Opportunity management](https://learn.microsoft.com/en-us/partner-center/referrals/manage-co-sell-opportunities).

Microsoft documents MACC contribution for eligible offers, with conditions on deployment and the purchasing subscription/route. It distinguishes these purchases from Azure prepayment and excludes direct credit-card Marketplace checkout from MACC contribution. Verify the offer badge, customer agreement, Azure usage requirements, and checkout route. [MACC benefit](https://learn.microsoft.com/en-us/marketplace/azure-consumption-commitment-benefit).

### Google Cloud

Investigate the current partner program and Cloud Marketplace participation separately from account-team commitment. [Partner program](https://partners.cloud.google.com/), [Marketplace selling](https://cloud.google.com/marketplace/sell).

Google's commitment policy ties qualifying purchases to deployment, commitment periods, and applicable drawdown rules. The reviewed policy has a cumulative 25% cap; reseller purchases require specific association with the customer and have exclusions. Installment timing can affect when amounts count. Recheck the policy and linked rates/exclusions for the actual purchase. [Commitment policy](https://cloud.google.com/terms/marketplace/commit-policy), [Rates and exclusions](https://docs.cloud.google.com/marketplace/docs/commit-drawdown). The policy was retrieved; the linked rates page was not retrievable in the initial research, so no rate or exclusion list is asserted here.

### Salesforce / AppExchange ecosystem

Salesforce's reviewed partner page presents AgentExchange as a unified marketplace including AppExchange apps and advertises private offers with billing and provisioning features. Its Checkout documentation also describes a Stripe-connected purchase path. Identify the actual listing and transaction method rather than treating all listings alike. Neither source establishes blanket hyperscaler-like committed-spend drawdown. [Salesforce partners](https://www.salesforce.com/partners/), [Checkout FAQ](https://help.salesforce.com/s/articleView?id=000389622&language=en_US&type=1).

### Snowflake

Snowflake documents Marketplace Capacity Drawdown for enrolled customers with qualifying committed-capacity contracts, subject to availability and program conditions. Investigate enrollment, eligible products, remaining allocation, and billing. Keep Snowflake capacity separate from the customer's underlying hyperscaler agreement. [Capacity drawdown](https://docs.snowflake.com/en/collaboration/marketplace-capacity-drawdown).

### Databricks

The reviewed documentation describes a Universal Commit drawdown program for eligible partner products, capped at 10%. Its guide describes payment to the partner directly or through a cloud marketplace, then invoice submission, partner validation, and Databricks approval. This is materially different from assuming checkout instantly draws down a balance. Check dates, active usage, remaining cap, submission deadlines, and treatment of prepaid commitments. Eligibility is not guaranteed until validation. [Marketplace overview](https://docs.databricks.com/aws/en/marketplace), [Invoice submission guide](https://docs.databricks.com/aws/en/assets/files/marketplace-purchase-partner-products-34d350e3f4e8e36a6fc15ae912a8d334.pdf).

### Other AI infrastructure and SaaS partners

Use the selected provider's official partner resources to determine the real technical, field, and transaction paths. [NVIDIA partner resources](https://www.nvidia.com/en-us/about-nvidia/partners/) is a discovery starting point, not evidence of marketplace billing or commitment benefits. Apply the same research to another provider only when relevant to the product and customers. Do not infer a commercial benefit from an integration badge or ecosystem membership.

## Explain the system from listing to renewal

For the selected route, describe the actual flow and what remains unverified:

1. **Discover and qualify:** Listing or partner discovery; customer problem and product fit; field seller involvement.
2. **Establish readiness:** Required program/offer status, technical integration, region, buyer eligibility, and actual co-sell process.
3. **Structure the offer:** Public versus private offer, seller-direct versus channel offer, scope, term, price, payment schedule, renewal, and who approves each.
4. **Approve and accept:** Correct purchasing entity, tenant/account/subscription, marketplace permissions, procurement controls, negotiated terms, security review, and authorized acceptor.
5. **Bill and recognize benefits:** Invoicing entity and schedule, currency/tax handling, eligible charges, credit/commitment rules, cap, timing, validation/submission steps, and owner checking the result.
6. **Activate and deliver:** Entitlements, vendor registration if required, deployment, customer success criteria, and implementation handoff.
7. **Support and renew:** Escalation path, SLA owner, usage/adoption reporting, renewal owner, and revalidation of terms or benefits at renewal.

Produce the sequence as an account-specific checklist with owners and dependencies. A marketplace route can simplify purchasing while leaving vendor terms, technical validation, or deployment work necessary.

## Customer-benefit qualification

Translate the customer's phrase “credits” into the actual instrument before making a claim:

| Instrument | What to establish |
|---|---|
| Spend commitment | Contractual spending obligation, eligible spend, period, remaining obligation, marketplace allowance, and recognition timing |
| Prepaid balance / committed capacity | Whether money is already paid, eligible products, allocation, depletion and renewal treatment |
| Promotional / startup / migration credit | Award terms, service exclusions, expiry, applicable account, and specific authorization if needed |
| Product consumption units | Where units can be redeemed; do not assume they buy another vendor's product |
| Seller quota credit | Internal compensation/attribution rules; unrelated to the customer's payment balance |

Create a benefit ledger for every plan:

| Proposed benefit | Mechanism | Evidence and customer-specific conditions | Status: confirmed / conditional / unavailable / unknown | Approved wording or validation action |
|---|---|---|---|---|
| Simplified billing | Purchase uses the customer's established billing route | Correct entity, invoice arrangement, payer account, schedule and services included | | |
| Commitment drawdown | Eligible charges count toward an existing obligation | Agreement, offer, deployment, period, rate, remaining cap, and verification owner | | |
| Usable prepaid funds or credits | Specific program permits eligible charges to use the balance | Instrument and terms, remaining amount, exclusions, expiry | | |
| Clear accountability | A named party owns an agreed delivery/support scope | Contract or accepted operating agreement, SLA and escalation ownership | | |
| Faster purchasing | Existing process removes identified steps | Customer procurement confirmation; remaining reviews still identified | | |
| Better solution value | Specialized product closes a real customer gap | Product proof, success metric, implementation costs, alternatives | | |

One bill does not establish one contract, one vendor, or one accountable support party. Use “one accountable owner” only for the scope actually owned. Do not claim that marketplace presence removes security/legal review or guarantees lower prices.

For the product seller, explain the customer outcome first, then a verified or conditional purchasing benefit: “This solves [need]. If this offer and purchasing account qualify under your agreement, the eligible amount can count toward your existing commitment.”

For the hyperscaler seller, explain the specialist contribution, why it fits the customer's environment, and any verified purchasing benefit: “This partner addresses [validated gap] within the proposed solution; we can validate the eligible purchase against your existing agreement.” Link seller/platform benefit to demonstrated adoption, account success, or applicable incentives. Do not promise all third-party spend becomes cloud workload consumption.

## Quantify without calling drawdown free money

Collect price and term, product/services/cloud cost split, forecast platform spend without this deal, commitment period and remaining amount, remaining marketplace allowance, applicable rate, payment/recognition dates, and any separately approved incentive. Compare direct and marketplace routes, including fees, discounts, implementation, support, administrative effort, and cash timing.

For a simple single-period spend-commitment model, after eligibility is verified:

- Eligible contribution = eligible recognized purchase amount × applicable drawdown rate, bounded by remaining applicable allowance and remaining commitment.
- Forecast shortfall without the purchase = max(0, remaining commitment − forecast other eligible spend).
- Potential shortfall reduction = min(eligible contribution, forecast shortfall without the purchase).

Use provider-specific period, rate, and cap mechanics rather than forcing complex contracts into this model. Missing inputs remain unknown. A commitment reduction is not a cash discount; financial savings require a supported counterfactual, including actual shortfall consequences and whether the customer would buy the product anyway. Do not double count product spend, native cloud usage, avoided shortfall, prepaid capacity, and incentives. A separate prepaid-capacity or credit model may be needed.

Even an eligible purchase may have little commitment-management benefit if the customer already expects to meet its commitment. Lead with the customer outcome, not pressure to consume funds.
