# 04. Protein quality, amino acids, digestibility and bioavailability

## 4.1 The claim being tested

Garden of Life says each serving delivers "22 g of complete protein", "4 g BCAAs", "all essential amino acids", and that "Raw matters because heat can denature proteins, reducing their availability to your body."

Three separate questions hide in that:

1. Is the protein **complete** (all nine indispensable amino acids present in adequate amounts)?
2. Is it **high quality** (digestible, bioavailable, and able to support muscle protein synthesis)?
3. Does **low-temperature processing** improve any of this?

## 4.2 Amino acid score from the manufacturer's own numbers

Garden of Life prints a "typical amino acid profile" per serving. Dividing each amino acid by the labeled protein and comparing with the FAO/WHO 2013 adult pattern gives a reproducible estimate:

| Product | Limiting amino acid | AAS | Est. PDCAAS | Est. DIAAS |
|---|---|---:|---:|---:|
| Raw Organic Protein | Methionine + cysteine | **0.91** | 0.82–0.88 | 0.77–0.84 |
| SPORT Organic Plant-Based | none (all ≥1.00) | 1.00 | 0.90–0.97 | 0.85–0.92 |
| Raw Organic Protein & Greens | none (all ≥1.00) | 1.00 | 0.90–0.97 | 0.85–0.92 |

Full ratios and the arithmetic: [`docs/generated/amino-acid-scores.md`](generated/amino-acid-scores.md), produced by `scripts/analyze.py`.

**Reading this honestly:**

- The flagship is **not** a 1.0 protein. Its sulfur amino acids sit at 91% of the adult pattern. That is normal for a pea-dominant blend, and it is still a good plant protein, but "complete" means "contains all nine", not "scores 1.0".
- The PDCAAS/DIAAS numbers are **estimates from a label**, not measurements. Garden of Life has published no PDCAAS, DIAAS, PER or nitrogen-balance study for any of these products. That absence is itself a finding: a company that markets "complete protein" heavily does not provide the standard metric for protein quality.
- The three labeled profiles are **mutually inconsistent**. Raw Organic Protein lists methionine at 240 mg (1.1% of protein) and cysteine at 200 mg; Protein & Greens lists 396 mg and 312 mg (3.5% combined) for a blend with the same pea/rice base. Either the formulations differ materially or the "typical" profiles are not tightly controlled. Either way, a labeled profile is not a batch certificate.

## 4.3 Benchmarks: where this sits

| Protein | PDCAAS | DIAAS | Limiting AA |
|---|---:|---:|---|
| Whey protein isolate | 1.00 | 1.09–1.18 | Val / Met+Cys |
| Milk protein concentrate | 1.00 | 1.18 | Met+Cys |
| Soy protein isolate | 0.98 | 0.90 | Met+Cys |
| Pea protein concentrate | 0.89 | 0.82 | Met+Cys |
| **Raw Organic Protein (est.)** | **0.82–0.88** | **0.77–0.84** | **Met+Cys** |
| Rice protein concentrate | 0.42 | 0.37 | Lys |

Sources: Herreman et al. 2020 (DIAAS compilation); Frontiers in Nutrition 2022 summary table; FAO 2013 scoring pattern. Pea isolate DIAAS 1.00 was measured in a 2022 human ileal digestibility trial, the spread between 0.82 and 1.00 for "pea protein" shows how much method and processing matter.

**Practical translation:** 22 g of Raw Organic Protein delivers roughly the anabolic equivalent of 18–19 g of whey isolate, not 22 g. For most people eating enough total protein, that difference is irrelevant. For a vegan athlete at 1.6 g/kg/day, it is absorbed by eating ~10% more.

## 4.4 Leucine and muscle protein synthesis

Leucine is the key trigger for muscle protein synthesis. Raw Organic Protein provides **1,800 mg leucine per 22 g protein** (82 mg/g protein); SPORT provides **2,527 mg per 30 g** (84 mg/g). Whey provides ~100–110 mg/g.

The threshold often cited for a maximal MPS response in young adults is ~2–3 g leucine per dose. One serving of the flagship is **below** that at 1.8 g; SPORT clears it at 2.5 g. A 2024 trial found that a plant protein isolate matched whey for MPS **only when leucine was added**, and a 2021 trial found that a high-protein vegan diet (~1.6 g/kg/day, soy-supplemented) matched an omnivorous diet for hypertrophy and strength over 12 weeks. The consistent picture:

- **Total daily protein and leucine dose matter more than source.**
- Plant protein at the same grams tends to produce a smaller acute MPS response, especially in adults over 65.
- Blending (as Garden of Life does) narrows the gap; adding leucine closes it.

## 4.5 Digestibility and the "raw" claim

**What "raw" means here:** ingredients are processed below ~115 °F (46 °C) and the powders are not extruded or cooked.

**What the science says:**

- Protein **denaturation is not a loss of nutritional value**, it is the first step of digestion. Heating unfolds proteins, exposes peptide bonds, and generally **increases** digestibility by inactivating protease inhibitors (trypsin inhibitor in legumes, for example).
- Cooking legumes and grains reliably improves protein digestibility-corrected scores. Raw legume flour typically has *lower* digestibility than cooked.
- The claim that heat "reduces availability to your body" is the opposite of the general finding for plant proteins. It is true only in extreme cases (Maillard browning at high heat with reducing sugars, which can reduce lysine availability).
- **Sprouting**, which Garden of Life does use, has a real and modest benefit: it reduces phytate, improves mineral bioavailability, and can increase free amino acids. That benefit does not depend on the product being "raw".

**Conclusion:** "raw" is a processing story, not a nutritional advantage. It may preserve some heat-labile vitamins and enzymes, but the enzyme contribution is unproven (§4.6), and the protein-quality effect is neutral-to-negative relative to ordinary cooking.

## 4.6 Do the added enzymes improve absorption?

The label lists 13 enzymes including protease, peptidase, aspergillopepsin, bromelain and papain, with **no activity units**. For an enzyme to matter it must survive gastric acid, reach the small intestine active, and hydrolyse protein faster than endogenous proteases already do.

- Gastric pH 1.5–3.5 denatures most dietary enzymes; fungal acid proteases (aspergillopepsin) are more acid-stable, which is presumably why it is included.
- There is no published human trial of this product's enzyme blend showing increased amino acid appearance or reduced GI symptoms.
- The "easily digested" experience many users report is more plausibly explained by the protein being an isolate (low fiber at the protein dose, low phytate) and by the product being low-FODMAP relative to whole legumes.

**Verdict:** plausible mechanism, no product-specific evidence, undisclosed dose. Marketing, not established efficacy.

## 4.7 Protein content and "spiking"

Protein is measured by nitrogen content (Kjeldahl/Dumas). Adding free amino acids or non-protein nitrogen inflates the number. CR's 2025 test found **all 23 products met or exceeded their labeled protein**, and Labdoor measured **20 g protein in Raw Organic Meal against a 20 g label**. There is no evidence of protein spiking in these products. The labeled amino acid totals also sum to 94–99% of labeled protein (21.67 g vs 22 g; 29.55 vs 30; 19.21 vs 20), which is internally consistent.

**Verdict:** the protein number is honest.

## 4.8 Bioavailability of the contaminants (the other side of "plant protein")

Plant proteins are not just lower quality per gram; they are also **carriers of cadmium, lead and inorganic arsenic** because the plants take metals up from soil and concentrate them in protein bodies. Rice is the archetype for arsenic and cadmium; cocoa for cadmium; peas and other legumes for cadmium and lead. This is why the contaminant section ([06](06-contaminants.md)) is inseparable from the protein-quality section: the same concentration step that gives you 22 g of protein per scoop also concentrates what was in the soil.

The organic premium does not fix this. Organic fertilizers (manures, composts, rock phosphate) can themselves contain cadmium, and organic certification sets no limit on heavy metals in the finished product.

## 4.9 Summary scorecard

| Question | Answer | Confidence |
|---|---|---|
| Contains all essential amino acids? | Yes | High (label + independent protein verification) |
| Protein content accurate? | Yes | High |
| PDCAAS/DIAAS published? | No | High (absence verified) |
| Estimated quality vs whey | ~15–20% lower per gram | Moderate (label-based estimate) |
| Estimated quality vs pea isolate | Similar to slightly lower | Moderate |
| Leucine per serving ≥2.5 g? | Only SPORT | High |
| "Raw" improves protein value? | No | High |
| Enzymes improve absorption? | Unproven | Moderate |
| Contaminant load per gram protein | Higher than whey; typical for plant protein | High |
