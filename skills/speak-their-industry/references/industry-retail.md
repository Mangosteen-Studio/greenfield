# Retail

Orientation, last reviewed 21 November 2026 against the sources linked below. Items marked *(changing)* were in flux at that date: treat them as `VERIFY:` in any briefing. Confirm current requirements with the seller's legal or compliance team before making commitments. Do not add statistics unless the user supplies a source.

## Segments behave differently

- **Grocery and convenience:** very thin margins, high volume, perishables, store labor.
- **Big box and general merchandise:** scale, supply chain, private label, retail media networks.
- **Specialty and apparel:** brand, assortment, seasonality, markdowns.
- **Ecommerce and direct-to-consumer brands:** acquisition cost, conversion, fulfillment, returns.
- **Restaurants and quick service** often get grouped with retail but buy around franchisees and store operations.

Selling *to* a retailer differs from selling to the brands that supply them. Supplier-facing products meet vendor onboarding, EDI requirements and chargeback rules.

Ask about the operating model: corporate-owned stores versus franchise changes who decides.

## Buyers and what they are measured on

- **Merchandising (VP or chief merchant):** sales, gross margin, sell-through, markdowns, assortment performance.
- **Supply chain / logistics:** inventory turns, in-stock rate, fulfillment cost, forecast accuracy.
- **Store operations:** labor cost and scheduling, shrink, store execution, customer experience.
- **Loss prevention / asset protection:** shrink, organized retail crime, store safety.
- **Ecommerce / digital:** conversion, average order value, fulfillment speed, returns.
- **CMO / loyalty:** customer acquisition and retention, loyalty program engagement, retail media revenue.
- **CIO / CTO / CISO:** platform stability, peak season readiness, PCI compliance, integration load.
- **CFO:** comparable sales, operating margin, working capital tied up in inventory.

## How deals get approved (typical, varies by retailer)

1. A business sponsor (merchandising, operations, digital) owns the problem and the budget.
2. A **pilot** in a subset of stores, regions or categories is common, with agreed success metrics. Define the measurement before the pilot starts.
3. **IT and security review**, including PCI scope if payment data is involved.
4. Finance approval, usually based on margin, labor or inventory impact.
5. **Rollout** is often phased by region or store cluster.

**Timing:** many retailers restrict system changes during peak season, commonly a **holiday freeze** from roughly October through early January. Many use a **4-5-4 retail calendar** with a fiscal year ending around late January or early February. Ask about both rather than assuming.

## Rules that shape the deal

- **PCI DSS (v4.0.1):** card payment data security. Ecommerce teams now manage controls on payment-page scripts (requirements 6.4.3 and 11.6.1). Question: does the product touch card data, add scripts to checkout pages, or change the retailer's PCI scope?
- **Consumer privacy laws (state privacy laws such as California's CCPA/CPRA, and GDPR for EU customers):** question: what customer data does the product collect, and how does it support consent and deletion requests?
- **Accessibility (ADA and web accessibility expectations):** question for customer-facing digital products: how do you support accessibility?
- **Labor and scheduling rules** (some cities and states have predictive scheduling laws): question for workforce products: does it support local scheduling rules?
- **Product safety and labelling** in some categories (food, children's products, cosmetics).

## Words that build credibility (use correctly)

Comparable (comp) sales, gross margin, sell-through, markdowns, inventory turns, in-stock, shrink, open-to-buy, GMROI, planogram, omnichannel, BOPIS (buy online, pick up in store), retail media, store labor hours, peak season, 4-5-4 calendar.

## Outsider phrases to avoid

- "We'll go live in Q4" (peak season; most retailers will not change systems then).
- "Store associates will love another app" (store teams have little time; talk about minutes saved per shift).
- Talking about revenue without margin (a retailer will ask what it does to margin).
- "Customers" when the buyer means shoppers, guests or members (use their word).

## Common objections

- "We can't touch anything until after the holidays." Ask when planning for next year happens and propose preparing a pilot for that window.
- "Prove it in a pilot first." Agree, and ask which stores, which metric and what result would justify rollout.
- "Our margins are too thin for this." Ask where margin is leaking today (shrink, markdowns, labor) and tie the product to one of those.
- "Our stores are all different." Ask how they handle variation today and propose a representative pilot set.
- "IT is focused on the platform migration." Ask what the migration timeline is and whether the product reduces or adds integration work.

## Questions that show understanding

1. How does this show up in your comp sales or margin this year?
2. When is your freeze window, and when does planning for next year happen?
3. If we ran a pilot, which stores or categories would be representative, and what result would justify rolling out?
4. Who owns the budget for this: merchandising, operations or digital?
5. What did the last tool you rolled out to stores get right or wrong?
