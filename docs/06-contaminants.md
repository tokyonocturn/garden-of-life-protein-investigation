# 06. Contaminants: heavy metals, pesticides, PFAS, phthalates, microbes

## 6.1 The regulatory vacuum

There is **no US federal limit on lead, cadmium, arsenic or mercury in protein powder or in dietary supplements generally.**

- The FDA regulates supplements under DSHEA (1994) and the cGMP rule at 21 CFR 111, which requires manufacturers to set and verify contaminant limits, but does not specify numeric limits for these metals in this product category.
- The FDA has **interim reference levels** for lead in food intended for children (2.2 µg/day) and for women of childbearing age (8.8 µg/day), but no general adult value and no action level for protein powder.
- California's Proposition 65 sets a **maximum allowable dose level** of 0.5 µg/day for lead (reproductive toxicity) and 4.1 µg/day for oral cadmium. Exceeding it requires a **warning**, not a recall.
- USP publishes voluntary **permissible daily exposures** for supplements: lead 10 µg, cadmium 5 µg, inorganic arsenic 15 µg, mercury 15 µg.
- NSF's certified-supplement program uses roughly 10 µg/day lead and 4.1 µg/day cadmium as pass lines.

The gap between 0.5 and 10 µg/day is a factor of twenty. **Every claim about this product's metal safety is a claim about which line you draw.** This report therefore reports the measured level, the concentration, and the ratio to each benchmark, and does not convert them into a single verdict word.

Ratios computed from the datasets: [`docs/generated/contaminant-ratios.md`](generated/contaminant-ratios.md).

## 6.2 Every independent result found

| Study (date) | Product | Lead | Cadmium | Arsenic | Mercury | Other | Verdict |
|---|---|---:|---:|---:|---:|---|---|
| **Consumer Reports** (Oct 2025) | SPORT Organic Plant-Based, Vanilla, 45 g | **2.76 µg** (61 ppb) | 1.93 µg | 1.33 µg (inorganic) | 0.01 µg | n/a | **564%** of CR's 0.5 µg/day level; **~1¼ servings/week**; 3rd-worst of 23 |
| **Labdoor** (retail test) | Raw Organic Meal, Vanilla | not published | not published | not published | not published | 35 analytical tests | **"Heavy Metal Screenings: Fail"**; overall score 73.7/100 |
| **Mamavation** (Sep 2024) | Organic Creamy Protein with Oatmilk, Chocolate Brownie, 46 g | **1.59 µg** | **6.55 µg** | not above Prop 65 | not detected | PFOA 0.462 ppb; PFBA 0.800 ppb; total phthalates 181 ppb; propiconazole 0.016 ppm | Lead **318%** and cadmium **160%** of Prop 65 MADLs |
| **Clean Label Project** (2018) | Raw Organic Meal, Chocolate Cacao | n/a | n/a | n/a | n/a | 134 products tested | One of the **five worst** products; GOL's five products averaged **1.8 stars (3rd-lowest brand)** |
| **Clean Label Project** (2025) | 10 Garden of Life SKUs, category level | n/a | n/a | n/a | n/a | 160 products, 258 analytes | Organic plant powders ~**3× lead, 2× cadmium** vs non-organic; **79%** of organic over Prop 65 lead |
| **As You Sow / CA AG** (2015) | RAW Organic Protein, RAW Fit, RAW Meal, Organic Plant Protein (all flavors) | above Prop 65 (alleged) | above Prop 65 (alleged) | n/a | n/a | Prop 65 notice + consent judgment | **$175,000** payment; injunctive relief to **reduce lead and cadmium or warn** |

Two things are notable about this table. First, **every independent lab that has looked has found something**, there is no independent dataset in which Garden of Life's plant proteins come back clean across the board. Second, the **one Garden of Life product that did come back clean** in Clean Label Project's 2025 work was the **SPORT Grass-Fed Whey Vanilla**, which was non-detect for all four metals and made the "Clean Sixteen". The problem tracks the plant matrix, not the brand's entire operation.

## 6.3 Reading the Consumer Reports result properly

CR's 2.76 µg per 45 g serving is **61 ppb**, the article states 61 ppb, and the arithmetic checks: 2.76 ÷ 45 × 1000 = 61.3.

Against each benchmark:

| Benchmark | 0.5 µg/day | 2.2 µg/day | 8.8 µg/day | 10 µg/day |
|---|---:|---:|---:|---:|
| 2.76 µg as % of benchmark | **552%** (CR publishes 564%, from unrounded data) | 125% | 31% | 28% |

So the same number is "5.6× over a strict California warning level", "slightly over the FDA's children's reference level", and "well under the USP/NSF adult limit". All three statements are true. Which one is *relevant* depends on who is drinking it and how often.

**CR's own risk framing:** it used 0.5 µg/day as a "level of concern" per serving, then converted to a weekly serving limit: `0.5 × 7 ÷ 2.76 = 1.27`, rounded to **1¼ servings per week**. This is a deliberately conservative screening approach, not a toxicological verdict. CR says so explicitly: "we're not making any legal statements here… no Prop 65 conclusions can be drawn from our results."

**The counter-case.** A 2021 peer-reviewed risk assessment using CR and Clean Label Project data calculated hazard quotients and hazard indices for arsenic, cadmium and mercury and found **HI < 1 for all products at 1 and 3 servings/day**, and modeled blood lead levels **below the CDC's 5 µg/dL guidance value** in every scenario. Its own stated limitations: lead has no RfD and was modeled separately; the approach does not capture aggregate exposure from all foods; and non-carcinogenic risk ignores lead's cardiovascular and developmental effects at low doses, for which **no safe threshold is established**. The same paper notes that protein powder contributes less arsenic, cadmium and lead than the average diet overall.

**Synthesis:** the acute and conventional toxicological risk from one serving a day is low. The reason to care is that lead has **no known safe level**, that effects at low exposure are probabilistic and cumulative, and that a daily habit is exactly the exposure pattern that matters. "Low risk" is not "no risk", and the product is not necessary.

## 6.4 Why plant protein carries more metal

1. **Soil uptake.** Cadmium and lead are taken up by roots; rice additionally accumulates inorganic arsenic via phosphate transporters under flooded conditions; cocoa accumulates cadmium in the bean.
2. **Concentration during isolation.** Producing 22 g of protein from peas and rice means processing several hundred grams of seed. Metals that were in that seed largely stay with the protein fraction or the fiber.
3. **Organic fertility.** Manure, compost and rock phosphate can contain cadmium; organic systems rely on them.
4. **Flavor matters.** Cocoa is a cadmium accumulator. Clean Label Project found chocolate powders far higher in cadmium than vanilla, and this is consistent with the dark-chocolate literature. If you want to minimize cadmium, **choose vanilla or unflavored, not chocolate**.
5. **Processing water.** Rice-protein production uses large volumes of water; arsenic in water ends up in the protein.

The organic premium does not change any of this. It may make it slightly worse, because organic matter retains metals and because yields are lower (more land and more biomass per gram of protein).

## 6.5 Arsenic speciation and the rice problem

Most labs report **total arsenic**; only inorganic arsenic is the carcinogen of concern. CR reports inorganic arsenic, which is why its 1.33 µg figure for SPORT is usable. The 1.33 µg is **13% of Prop 65's 10 µg/day** oral MADL, not a level of concern by that benchmark.

Rice protein is the ingredient most associated with inorganic arsenic. Garden of Life uses **sprouted brown rice protein** in the flagship, Meal, Fit, Protein & Greens and Creamy Oatmilk; SPORT uses no rice, which may partly explain its different (though still lead-high) profile. There is no published speciated arsenic result for the flagship Raw Organic Protein, a gap in the public record, not evidence of absence.

## 6.6 Cadmium: the chronic concern

Cadmium has a biological half-life of **10–30 years** and accumulates in the kidney, where it causes tubular damage. It is classified **IARC Group 1** (carcinogenic to humans, lung cancer via inhalation; evidence for prostate and kidney). Food is the main source for non-smokers; rice, leafy vegetables, cocoa and shellfish are the usual drivers.

The Mamavation result of **6.55 µg per serving** in the Creamy Oatmilk Chocolate Brownie is **160% of the 4.1 µg/day oral MADL** and 131% of USP's 5 µg/day. One serving a day of that product would put a regular consumer over the cadmium benchmark from a single food, before rice, chocolate or vegetables.

The 1.93 µg in SPORT is 47% of the MADL, meaningful but not over the line on its own.

## 6.7 Lead: why "below the limit" is not reassuring

Lead has no established safe threshold. At low doses it is associated with:

- increased blood pressure and hypertension;
- reduced kidney function;
- adverse cardiovascular outcomes;
- in pregnancy, reduced fetal growth and neurodevelopmental effects;
- in children, cognitive effects at blood lead levels once considered harmless.

The FDA's own children's benchmark (2.2 µg/day) is a *total daily* budget across all food, not a per-product allowance. A single serving of SPORT at 2.76 µg **exceeds the entire children's daily budget**, which is why the product label says "not intended for children" and why CR's advice is to limit it.

For an adult, 2.76 µg is a modest fraction of typical dietary lead intake (the risk assessment above estimated mean dietary lead exposure from three servings of powder at 3.52 µg/day, against a much larger background). But it is not zero, and it is avoidable.

## 6.8 Pesticides, PFAS, phthalates, BPA

**Pesticides.** Mamavation's 587-pesticide panel found **propiconazole 0.016 ppm** in the Garden of Life Creamy Oatmilk Chocolate Brownie and **no glyphosate**. Propiconazole is a fungicide not permitted in organic production; 0.016 ppm is low and its significance is unclear without a tolerance comparison. It is nonetheless a residue in a certified organic product.

**PFAS.** Mamavation detected **PFOA 0.462 ppb and PFBA 0.800 ppb** in the same product. PFAS are ubiquitous; detection at sub-ppb levels is common in food and does not by itself establish a health risk. The finding is consistent with the broader pattern that plant proteins concentrate contaminants from water and soil.

**Phthalates.** **181 ppb total phthalates** in the same product; 7 of 11 powders tested had detectable phthalates. Packaging and processing are the likely sources. There is no regulatory limit for phthalates in protein powder.

**BPA.** Clean Label Project's 2018 study found BPA in 55% of 134 protein powders, with some far above its 3 µg limit; its 2023–24 study found BPA/BPS in only 3 of 160, a genuine improvement. No public BPA result exists for a specific Garden of Life plant SKU.

**Interpretation:** these are real detections but weak evidence of product-specific harm. They matter chiefly as a counterweight to "organic = pure" and as a reason to prefer brands that publish lot data.

## 6.9 Microbial contamination

Protein powders are not sterile. They are dry, low-water-activity foods, but *Salmonella* survives drying and has caused repeated outbreaks in supplements and spices.

**The 2016 Garden of Life outbreak is the key event:**

- *Salmonella* Virchow, **33 illnesses in 23 states, 6 hospitalizations, no deaths** (CDC).
- Recalled products: RAW Meal Organic Shake & Meal in chocolate, original, vanilla and vanilla chai; initial recall **29 January 2016**, expanded **12 February 2016**; roughly **61 lots** across the two actions; Class I (reasonable probability of serious adverse health consequences).
- FDA traced the contamination to **organic moringa leaf powder** from a supplier.
- The products were subsequently renamed (Raw Meal → Raw Organic Meal) and relabelled.
- Distribution was nationwide plus **13 international markets** (AU, BG, CA, CZ, DE, GB, HK, IE, IN, SE, SG, NL).

There is no public evidence of a pathogen recall on the Raw Organic Protein line itself. The 2016 event nonetheless establishes that the supply chain has, at least once, delivered a pathogen into a finished powdered product sold as a health food.

**Other recalls:** 2017 Baby Organic Liquid probiotic (Class I, choking hazard from viscosity); 2023 RM-10 mushroom capsules (Class II, undeclared soy). The 2024 FDA inspection was classified **NAI, no action indicated**.

## 6.10 Lot-to-lot variation: the thing a single test cannot tell you

CR averaged 2–3 lots. Mamavation tested one sample. Labdoor tests one purchase. A result is a property of **the lots tested**, not of the product name forever.

Two consequences:

1. **A pass does not protect your tub.** A brand can publish a certificate for lot A while lot B is over.
2. **A failure is not proof your tub is contaminated**, but it is proof the process can produce a contaminated tub, which is what a safety program is supposed to prevent.

Garden of Life does not publish lot certificates for protein powders (its public COA page covers CBD softgels only). That means a consumer cannot check the tub in hand against a test. This is the single most actionable transparency gap in the report.

## 6.11 What would change the conclusion

- Published, lot-level COAs for every protein SKU, tested to Prop 65 MADLs by an ISO 17025 lab, with the actual numbers (not "below applicable limits").
- A reformulation that reduces lead in SPORT and cadmium in the chocolate/oatmilk lines.
- Independent retesting of the flagship Raw Organic Protein Vanilla and Chocolate, which have not had a public, per-product, speciated metal result since the 2018 CLP brand-level score.

Until then, the honest summary is: **detectable, benchmark-dependent, not acutely dangerous, not "clean", and worse than whey.**
