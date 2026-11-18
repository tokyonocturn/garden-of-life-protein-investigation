# 01. Methodology

## 1. Question

Not "is this product good?" but four separable questions, because they have different answers:

1. **Composition**, what is in it, in what amount, per labeled serving?
2. **Safety**, what contaminants are present, at what level, against which benchmark?
3. **Efficacy**, does the protein (and the added actives) do what is claimed, in humans?
4. **Value**, what does a gram of delivered protein cost, and what else could that money buy?

The investigation was designed to falsify the marketing rather than confirm it. The prior was: *organic certification says nothing about heavy-metal content, and plant protein concentrates tend to carry more cadmium and lead than whey.* Everything below tests that prior.

## 2. Evidence hierarchy used

| Tier | Source type | Weight in conclusions |
|---|---|---|
| 1 | Peer-reviewed human RCTs, systematic reviews, meta-analyses | Highest for efficacy |
| 2 | Government measurement and regulation (FDA, USDA, CDC, EPA, California OEHHA, EFSA, JECFA) | Highest for limits and exposure |
| 3 | Independent laboratory testing with published methods (Consumer Reports 2025, Clean Label Project, Labdoor, Mamavation) | Highest for contamination |
| 4 | Manufacturer labels, certifications, and published specifications | Used for composition; treated as claims, not evidence |
| 5 | Retailer listings, review sites, blogs, press coverage | Used only to locate primary data or to establish price |
| 6 | Brand marketing, influencer content | Recorded as claims to be tested |

A manufacturer's statement that a product "is tested for heavy metals" is Tier 4. It is not evidence of a low result, and this report does not treat it as such. The distinction matters here because Garden of Life's public position, "all products are tested for heavy metals and the levels are below any established food safety thresholds", is literally compatible with a result 5.6× above Consumer Reports' level of concern, since no federal threshold exists for lead in protein powder.

## 3. Product selection

The unit of analysis is the **SKU (product line × flavor × size)**, because panels, sweeteners and serving sizes differ by flavor, and contamination differs by flavor (cocoa and plant protein are both metal accumulators).

Garden of Life's US protein category listed 43 items on 18 Nov 2026. Restricting to **organic plant-based protein powders** yields six lines and 19 flavors (see `data/gol_products.csv`). Excluded from the main analysis but noted where relevant:

- SPORT Certified Grass-Fed Whey (dairy; non-organic protein)
- Organic Whey Protein (dairy)
- Collagen and bone-broth products (not protein powder in the same sense)
- Bars, ready-to-drink shakes, and the "Raw Organic Meal" single-serve trays

## 4. Nutrition data

Panels were taken from the current Garden of Life product pages where rendered, and otherwise from dated retailer labels (Vitacost, Swanson, PureFormulas, Fullscript, H-E-B), cross-checked against at least two independent listings where possible. Conflicting labels are recorded rather than averaged, because the conflicts are themselves findings: the Raw Organic Protein scoop has migrated from 29 g to 33–35 g, calories from 110 to 130–140, and fiber from 1 g to 3–5 g across label versions. A 2019 review and a 2026 review of "the same product" may therefore be describing different powders.

`data/gol_products.csv` carries a `panel_confidence` field: `high` (two concordant current listings), `medium` (single current listing or a known transition), `low` (older label or unverified).

## 5. Amino acid scoring (the calculation this report adds)

Garden of Life publishes "typical amino acid profiles" per serving but **no PDCAAS or DIAAS** for any protein product. To estimate protein quality reproducibly:

1. Convert each labeled amino acid to **mg per gram of labeled protein**.
2. Divide by the **FAO/WHO 2013 adult indispensable amino acid scoring pattern** (mg/g protein): His 15, Ile 30, Leu 59, Lys 45, SAA (Met+Cys) 22, AAA (Phe+Tyr) 38, Thr 23, Trp 6, Val 39.
3. The **amino acid score (AAS)** is the minimum ratio. PDCAAS caps that at 1.00.
4. **PDCAAS estimate** = AAS × assumed fecal true digestibility of 0.90–0.97 (range for isolated plant proteins).
5. **DIAAS estimate** = AAS × assumed true ileal digestibility of 0.85–0.92.

This is a **label-based estimate, not a measurement**. It assumes the printed "typical" profile is accurate and representative, which is not guaranteed; batch-to-batch variation in plant protein blends is real, and the profiles for Raw Organic Protein and Protein & Greens are mutually inconsistent in methionine content (1.1% vs 3.5% of protein) for blends that share a base. The scores should be read as *upper-bound, best-case* values derived from the manufacturer's own numbers.

Benchmarks for comparison are taken from published values: whey isolate PDCAAS 1.00 / DIAAS 1.09–1.18; pea protein concentrate PDCAAS 0.89 / DIAAS 0.82; rice protein concentrate PDCAAS 0.42 / DIAAS 0.37; pea isolate measured DIAAS 1.00 in a 2022 human ileal digestibility trial (a higher value than earlier estimates, illustrating method dependence).

## 6. Contaminant assessment

### 6.1 Benchmarks (see `data/gol_thresholds.csv`)

| Benchmark | Lead | Cadmium | Inorganic arsenic | Mercury | Status |
|---|---|---|---|---|---|
| California Prop 65 MADL (oral, reproductive) | 0.5 µg/day | 4.1 µg/day | 10 µg/day | none set | Requires a warning above this; not a ban |
| Consumer Reports "level of concern" (2025) | 0.5 µg/day | 4.1 µg/day | 10 µg/day | n/a | CR's own risk assessment, derived from Prop 65 numbers but not a Prop 65 conclusion |
| FDA interim reference level | 2.2 µg/day (children), 8.8 µg/day (women 16–49) | n/a | n/a | n/a | Benchmark, not a regulation; no general adult value |
| USP permissible daily exposure (supplements) | 10 µg/day | 5 µg/day | 15 µg/day | 15 µg/day | Voluntary compendial standard |
| NSF certified supplement limit (as reported by CR) | ~10 µg/day | ~4.1 µg/day | n/a | n/a | Certification pass line |

The spread between 0.5 and 10 µg/day is a factor of 20. **Any claim that a product is "safe" or "unsafe" on heavy metals is therefore a claim about which benchmark is being used.** This report reports the number, the concentration, the benchmark, and the ratio, and refuses to collapse them into a single word.

### 6.2 Units and arithmetic

- Laboratory results are commonly reported in **ppb (µg/kg)**. To convert to µg per serving: `ppb × serving_g / 1000`.
- Example: 61.4 ppb lead × 45 g ÷ 1000 = **2.76 µg**.
- Reverse: 2.76 µg ÷ 45 g × 1000 = **61.3 ppb**, matching CR's published 61 ppb, which is how the CR figure was cross-validated.
- "Servings per week before exceeding a daily benchmark" = `benchmark × 7 ÷ µg per serving`.

### 6.3 Study quality notes

- **Consumer Reports (Oct 2025)**: 23 products, 2–4 lots each, purchased anonymously Nov 2024–Jan 2025, tested at an ISO-accredited lab by ICP-MS; results averaged across lots. Strength: multiple lots, blind purchase. Weakness: one flavor per product; averages can hide lot variance.
- **Clean Label Project (2018, 2025)**: retail-purchased, third-party lab (Ellipse Analytics), 134 and 160–165 products. Weakness: methodology white paper is thin on detection limits and lot handling; industry bodies dispute it. Strength: breadth and repeated finding that organic/plant products test higher.
- **Labdoor**: retail purchase, FDA-registered lab, 35 analytical tests, publishes a pass/fail heavy-metal screen and an overall score. Weakness: underlying per-metal numbers are behind a paywall; only the screen outcome is public.
- **Mamavation (2024)**: 11 chocolate powders, two EPA-certified labs, EPA 1633 for PFAS, LC-MS/MS for glyphosate, 587 pesticides, ICP-MS for metals. Weakness: small n, one flavor, advocacy framing. Strength: unusually broad analyte panel and transparent methods.
- **As You Sow / Prop 65 (2014–2015)**: legal filings, not a study; but the settlement is a documented admission that lead and cadmium reductions were required.

## 7. Price methodology

- **Price per serving** = listed price ÷ servings per container.
- **Price per gram protein** = price per serving ÷ labeled protein per serving.
- **Price per 25 g protein** normalizes across products with different protein doses, because 20 g and 30 g servings are not comparable.
- Prices are Garden of Life's own US list prices on 18 Nov 2026, before tax and shipping; the 15% subscription discount (20% after the fourth order) is noted but not tabulated separately, because it varies by promotion. Competitor prices are the lowest published list price found on the cited source in Nov 2026 and are marked approximate.

## 8. Verification performed

1. Every arithmetic result in the docs is recomputed by `scripts/analyze.py` from the CSVs.
2. Contaminant conversions were checked in both directions against CR's published ppb and µg values (see §6.2).
3. Amino acid sums were checked for internal consistency: the labeled amino acids must sum to approximately the labeled protein. Raw Organic Protein sums to 21.67 g per 22 g protein; SPORT to 29.55 g per 30 g; Protein & Greens to 19.21 g per 20 g. All are plausible (protein is ~94–99% amino acid by mass after water is accounted for).
4. Links are checked with `scripts/check_links.py`.
5. Where a secondary source reported a primary number, the primary was preferred. Where the primary was paywalled, the secondary is cited as such.

## 9. Limitations (stated up front, not buried)

- **No new laboratory testing was commissioned.** This report synthesizes existing independent testing; it does not add a new lot to the evidence.
- **Contamination is lot-specific.** A 2024 result does not prove what is in a 2026 tub. Conversely, a manufacturer's 2026 certificate does not erase a 2025 failure.
- **Heavy-metal speciation is unknown.** Total arsenic is not inorganic arsenic; total mercury is mostly not methylmercury in plant protein. CR reports inorganic arsenic; most other studies do not speciate.
- **Bioavailability of lead from a powder matrix is assumed (20%), not measured.**
- **Protein quality is estimated from labels**, not measured by ileal digestibility or a rat assay.
- **The "typical amino acid profile" is not a per-batch certificate.**
- **Efficacy of the added probiotics and enzymes at the doses in these products is largely unproven.**
- **Publication and litigation bias**: both advocacy labs and manufacturers have incentives. The report relies on the convergence of independent sources rather than any single one.
