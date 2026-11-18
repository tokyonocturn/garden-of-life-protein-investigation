# 10 — Price per serving and per gram of protein

## 10.1 Method

- **Price per serving** = list price ÷ servings per container.
- **Price per gram protein** = price per serving ÷ labeled protein per serving.
- **Price per 25 g protein** normalizes a 20 g serving against a 30 g serving, because "cheap per scoop" is meaningless when scoops differ.
- Prices are Garden of Life US list prices on **18 November 2026**, excluding tax and shipping. The 15% subscription discount is shown where the site publishes it.

Full generated table: [`docs/generated/price-table.md`](generated/price-table.md). Source data: [`data/gol_products.csv`](../data/gol_products.csv).

## 10.2 The range at a glance

| Product | $/serving | $/g protein | $/25 g protein | Subscription $/g |
|---|---:|---:|---:|---:|
| Raw Organic Meal (all flavors) | $1.06 | **$0.0528** | $1.32 | $0.0449 |
| Raw Organic Fit (Original/Vanilla/Chocolate) | $2.08 | $0.0743 | $1.86 | $0.0632 |
| SPORT Organic Plant-Based | $2.53 | $0.0842 | $2.10 | $0.0716 |
| Organic Creamy Protein with Oatmilk | $1.80 | $0.0900 | $2.25 | n/a |
| Raw Organic Protein (all flavors) | $2.04 | $0.0927 | $2.32 | $0.0788 |
| Raw Organic Protein & Greens | $2.04 | $0.1020 | $2.55 | n/a |
| Raw Organic Fit Coffee (10-serving tub) | $4.16 | $0.1485 | $3.71 | $0.1262 |

**Cheapest per gram:** Raw Organic Meal at **$0.053/g**.
**Most expensive per gram:** Fit Coffee at **$0.149/g** — an artefact of a 10-serving tub sold at the 20-serving price.

## 10.3 What a year costs

At one serving per day, 365 days:

| Product | Annual cost | Annual protein |
|---|---:|---:|
| Raw Organic Meal | $387 | 7.3 kg |
| Raw Organic Fit | $759 | 10.2 kg |
| SPORT | $923 | 11.0 kg |
| Raw Organic Protein | $745 | 8.0 kg |
| Protein & Greens | $745 | 7.3 kg |

At two servings a day, double it. A daily SPORT habit costs about **$1,850/year**.

## 10.4 The premium over whey and cheaper plant protein

Using published competitor prices (see [11](11-comparisons.md) for sources and caveats):

| Product | $/g protein | Multiple of whey reference |
|---|---:|---:|
| Naked Pea (unflavored, 5 lb) | ~$0.028 | 0.7× |
| Optimum Nutrition Gold Standard Whey | ~$0.040 | 1.0× (reference) |
| Orgain Organic Protein | ~$0.091 | 2.3× |
| **Garden of Life Raw Organic Protein** | **$0.093** | **2.3×** |
| **Garden of Life SPORT** | **$0.084** | **2.1×** |
| **Garden of Life Meal** | **$0.053** | **1.3×** |
| Vega Sport | ~$0.114 | 2.9× |
| Ritual Essential Protein | ~$0.147 | 3.7× |

Garden of Life sits in the **middle-to-upper** part of the premium plant protein market: not the most expensive (Ritual, Vega Sport), not the cheapest (Naked Pea, Meal). It is roughly **2× the cost per gram of protein of a basic whey concentrate** and **3× the cost of unflavored pea protein**.

## 10.5 What the premium buys

| Feature | Worth paying for? |
|---|---|
| USDA Organic | Only if pesticide avoidance/GMO avoidance matters to you |
| Non-GMO Project Verified | Marginal; most soy/pea protein is non-GMO anyway |
| NSF Certified for Sport (SPORT only) | Yes, if you are a drug-tested athlete |
| 14 sprouted ingredients | No; the protein comes from pea and rice |
| Probiotics + enzymes | No; doses are subclinical and unproven |
| Fiber (5–9 g) | Yes, if you want satiety and don't have IBS |
| No artificial sweeteners/colors | Yes, for people who avoid them |
| "Raw" | No demonstrated benefit |
| Heavy-metal testing | **You cannot verify it** — no numbers published |

## 10.6 Cost per gram of *delivered, usable* protein

The label says 22 g; the amino acid score says the protein is ~91% as good as the reference pattern at the limiting amino acid, and digestibility is ~90–97%. A rough "digestible, score-corrected protein" figure is:

`22 g × 0.91 × 0.93 ≈ 18.6 g`

That makes the effective cost **$2.04 ÷ 18.6 = $0.110/g** of usable protein — about **2.7×** the cost of whey on the same basis (whey: 24 g × 1.00 × 0.95 ≈ 22.8 g; $0.95 ÷ 22.8 = $0.042/g).

This is an estimate, not a measurement, but it captures something the label does not: **you are paying a premium for a protein that is slightly less usable per gram.** The gap is not large enough to matter nutritionally for most people; it is large enough to matter economically.

## 10.7 Is it worth it?

**As protein:** no. Cheaper whey, pea isolate, or soy delivers the same or better protein for half to a third of the cost.

**As a product:** maybe. If you want an organic, vegan, low-sugar, high-fiber powder with no artificial sweeteners, and you value the certifications, the price is within the normal range for that category. You are paying for formulation and certification, not for protein.

**As a "clean" product:** the premium is not justified by the contaminant data. You are paying organic prices for plant-protein metal exposure that is statistically worse than conventional whey.

## 10.8 Price volatility and pack-size traps

- **Fit Coffee** is the clearest trap: 465 g / 10 servings at $41.59, versus 922 g / 20 servings at the same price for Fit Chocolate. Check the net weight, not the shelf position.
- **Raw Organic Protein** has been re-scooped from 29 g to 33–35 g. A tub that once delivered 22 servings now delivers 20 at the same price — a hidden ~10% price increase.
- **Subscription pricing** (15% off, then 20% after the fourth order) is the cheapest legitimate route, but it locks you into recurring purchases of a product with a contested contaminant profile.
- **Retail vs direct:** Amazon and Vitamin Shoppe frequently undercut Garden of Life's list price by 15–30%. The $/g figures here are list prices and therefore **overstate** what a careful shopper pays; the ranking between products is unaffected.

## 10.9 Summary

| Question | Answer |
|---|---|
| Cheapest GOL plant protein per gram | Raw Organic Meal, $0.053/g |
| Most expensive | Fit Coffee, $0.149/g (pack-size artefact) |
| Flagship cost | $2.04/serving, $0.093/g, ~$745/year at 1/day |
| Premium vs whey | ~2.3× per gram; ~2.7× per gram of usable protein |
| Premium vs cheapest pea | ~3.3× |
| Does the premium buy better protein? | No |
| Does it buy certifications and formulation? | Yes |
| Is it good value? | **No, unless organic/vegan/no-artificial-sweetener is a hard requirement** |
