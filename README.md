# Garden of Life Organic Protein Powder — An Independent Scientific Investigation

**A source-first audit of every Garden of Life organic plant protein SKU: nutrition, protein quality, organic certification, contaminants, additives, evidence, regulation, price, and verdict.**

Research cut-off: **18 November 2026**. All prices, labels and test results are dated in the datasets; formulations change, so check the tub in your hand.

---

## Bottom line first

| Question | Short answer |
|---|---|
| Is it a real protein source? | **Yes.** 20–30 g of complete plant protein per serving, label claims verified by Consumer Reports' 2025 test (all products met or exceeded protein claims). |
| Is it "clean"? | **Not reliably.** Independent labs have found lead in every Garden of Life plant line tested, at 3.2–5.6× Consumer Reports' 0.5 µg/day lead level of concern. |
| Does organic make it safer? | **No.** Organic is a farming-process claim. Independent testing consistently finds *more* lead and cadmium in organic/plant protein than in whey. |
| Is it good value? | **No.** $0.074–$0.102 per gram of protein versus roughly $0.03–0.05 for whey and cheaper plant isolates. |
| Would I buy it? | **Only for a narrow use case** — see [the verdict](docs/12-verdict.md). Grade: **C (5.1/10)**. |

### The five findings that matter

1. **The lead signal is consistent, not a one-off.** Consumer Reports (Oct 2025) measured **2.76 µg lead per 45 g serving** of SPORT Organic Plant-Based Protein Vanilla — **564% of its 0.5 µg/day level of concern**, the 3rd-worst of 23 products and high enough that CR advised **no more than ~1¼ servings per week**. CR also reported **61 ppb lead** in the product, versus 15 ppb in Orgain.
2. **Other independent labs agree.** Clean Label Project's 2018 study ranked Garden of Life's five tested products **third-worst overall (1.8 stars)**, and its Raw Organic Meal Chocolate Cacao was one of the **five worst products in 134**. Labdoor's own testing of Raw Organic Meal records **"Heavy Metal Screenings: Fail"**. Mamavation's 2024 EPA-certified lab test of the Chocolate Brownie oatmilk powder found **6.55 µg cadmium and 1.59 µg lead per serving**, plus PFAS and 181 ppb total phthalates.
3. **Garden of Life has known about this since at least 2014.** A California Proposition 65 action by As You Sow covering "RAW Organic Protein (all flavors and varieties)", RAW Fit, RAW Meal and Organic Plant Protein was **settled in 2015 with a $175,000 payment and injunctive relief requiring reduction of lead and cadmium or a cancer/reproductive-harm warning**. Lead is still detectable above Prop 65's MADL in 2025.
4. **The nutrition is genuinely decent; the marketing is not.** Complete amino acid profile, 0 g sugar, 3–7 g fiber, no artificial colors or sweeteners, NSF Certified for Sport on the SPORT line. But "raw matters because heat can denature proteins" is **scientifically meaningless** — denaturation is what digestion does, and cooking usually *improves* protein digestibility. "Burns fat" and "helps you stay full longer" are unverified structure/function claims.
5. **Protein quality is mid-tier, and Garden of Life publishes no PDCAAS or DIAAS.** From the label's own amino acid profile, the flagship Raw Organic Protein is **first-limited by methionine + cysteine at ~0.91 of the FAO 2013 adult pattern**, implying a PDCAAS of roughly **0.82–0.88** and a DIAAS of roughly **0.70–0.80** — below whey (1.0/1.09–1.18) and below pea isolate alone on DIAAS.

---

## Scope: 19 plant SKUs across 6 product lines

| Line | Flavors covered | Protein/serving | Why it exists |
|---|---|---|---|
| Raw Organic Protein | Unflavored, Vanilla, Chocolate, Vanilla Chai | 22 g | Flagship "raw sprouted" protein |
| Raw Organic Meal | Vanilla, Chocolate, Lightly Sweet, Vanilla Spiced Chai | 20 g | Meal replacement with 44 "superfoods" + vitamins |
| Raw Organic Fit | Original, Vanilla, Chocolate, Coffee | 28 g | "Weight loss" formula (Svetol + ashwagandha + chromium) |
| SPORT Organic Plant-Based | Vanilla, Chocolate | 30 g | NSF Certified for Sport; recovery blend |
| Raw Organic Protein & Greens | Vanilla, Chocolate Cacao, Lightly Sweet | 20 g | Protein + greens |
| Organic Creamy Protein with Oatmilk | Vanilla Cookie, Chocolate Brownie | 20 g | Newer oat-milk "creamy" formula |

Adjacent dairy SKUs (SPORT Grass-Fed Whey, Organic Whey Protein) are noted only where they are the relevant comparison, because they are not organic *plant* protein.

Every flavor's panel, ingredients, sweeteners, and per-gram price: **[docs/02-product-inventory.md](docs/02-product-inventory.md)** and **[data/gol_products.csv](data/gol_products.csv)**.

---

## Repository map

```
README.md                         This file: scope, key findings, verdict summary
docs/
  01-methodology.md               How the investigation was done; evidence hierarchy; limits
  02-product-inventory.md         Every flavor: panel, ingredients, sweeteners, serving size
  03-ingredients-database.md      Additive-by-additive reference with function and evidence
  04-protein-quality.md           Amino acid scoring, PDCAAS/DIAAS, digestibility, bioavailability
  05-organic-certification.md     What USDA Organic does and does not guarantee
  06-contaminants.md              Heavy metals, pesticides, PFAS, phthalates, microbes
  07-sweeteners-and-digestion.md  Erythritol, stevia, gums, fiber, probiotics, enzymes
  08-evidence-review.md           Claims tested against the literature
  09-regulation-recalls-lawsuits.md  FDA framework, recalls, Prop 65, class actions
  10-price-analysis.md            Price per serving, per gram protein, per 25 g protein
  11-comparisons.md               Head-to-head vs organic and non-organic competitors
  12-verdict.md                   Advantages, disadvantages, risks, who should/shouldn't
  13-references.md                Full numbered reference list with DOIs and PMIDs
  14-source-verification.md       How every blocked citation was confirmed, corrected or removed
data/
  gol_products.csv                Product/flavor master table with panels and prices
  gol_amino_acids.csv             Labeled amino acid profiles (mg per serving)
  gol_contaminants.csv            Every published independent test result found
  gol_thresholds.csv              Regulatory and advisory limits used for comparison
scripts/
  analyze.py                      Recomputes all derived tables (stdlib only)
  check_links.py                  Checks every cited URL over HTTP
  verify_refs.py                  Re-checks blocked sources via Crossref, PubMed and the Wayback Machine
docs/generated/                   Output of analyze.py (do not edit by hand)
```

## Reproduce the numbers

```bash
python scripts/analyze.py          # writes docs/generated/*.md
python scripts/check_links.py      # checks every URL in the report
python scripts/verify_refs.py      # re-confirms sources that block automated clients
```

No third-party Python packages are required. All inputs are in `data/`.

---

## How to read this report

- **Established** = replicated human data or direct regulatory/lab measurement.
- **Probable** = consistent but limited evidence.
- **Uncertain** = single studies, modeling, or extrapolation.
- **Marketing** = assertion with no independent support.

Where a number is an estimate I say so and show the arithmetic. Where sources disagree (for example, CR's 564% versus the 552% implied by its rounded 2.76 µg figure) I show both.

## Source verification

Link checking only proves a URL answered. Every source that returned 401/403/429 to an automated request was re-checked against Crossref, PubMed, Semantic Scholar or an archived copy, and each claim was matched to the paper's abstract rather than its title. All 15 peer-reviewed articles were confirmed, three of them with corrected journal or DOI details; three web sources were replaced with loadable first-party equivalents and one unreadable news link was removed. The per-source record, including what could not be confirmed and why, is in [docs/14-source-verification.md](docs/14-source-verification.md).

## What this is not

Not medical advice. Not a lab test of a specific tub you own — contamination varies by lot, and the tests cited are samples bought in specific periods. Not affiliated with Garden of Life, Nestlé, Consumer Reports, Clean Label Project, Labdoor or Mamavation.

## A note on conflicts of interest

Garden of Life has been a **wholly owned subsidiary of Nestlé Health Science** since March 2018 (via the US$2.3 bn acquisition of Atrium Innovations). Nestlé Health Science also acquired a majority stake in **Orgain** in 2022, so two of the most-compared organic protein brands share an owner. This does not change the lab data, but it matters when reading brand-vs-brand marketing.

## License

Text and data: CC BY 4.0. Code: MIT.
