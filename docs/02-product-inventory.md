# 02 — Product inventory: every organic plant SKU, flavor by flavor

Garden of Life's US protein category listed **43 items** on 18 November 2026. Nineteen are organic plant-based powder SKUs in six lines. This document gives each one's panel, protein source, sweetener system, and price per serving. Machine-readable versions: [`data/gol_products.csv`](../data/gol_products.csv).

> **Label drift warning.** These products are reformulated and re-scooped without changing the product name. Raw Organic Protein Vanilla has appeared as a **29 g scoop / 110 kcal / 1 g fiber / 180 mg sodium** product and as a **33 g scoop / 130 kcal / 5 g fiber / 300 mg sodium** product. Reviews and databases that mix label vintages are comparing different powders. `panel_confidence` in the dataset records how well each panel is corroborated.

## 2.1 Summary table

| Line / flavor | Serving | kcal | Protein | Carb | Fiber | Sugar | Sodium | Sweetener | $/serving |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| **Raw Organic Protein** | | | | | | | | | |
| Unflavored | 30 g | 120 | 22 g | 4 g | 2 g | 0 g | 320 mg | none (stevia-free) | $2.04 |
| Vanilla | 33 g | 130 | 22 g | 6 g | 5 g | 0 g | 300 mg | erythritol + stevia | $2.04 |
| Chocolate | 35 g | 140 | 22 g | 7 g | 5 g | 0 g | 350 mg | erythritol + stevia | $2.04 |
| Vanilla Chai | 34 g | 140 | 22 g | 7 g | 3 g | 0 g | 300 mg | erythritol + stevia | $2.04 |
| **Raw Organic Meal** | | | | | | | | | |
| Vanilla | 38 g | 150 | 20 g | 13 g | 7 g | 0 g | 190 mg | stevia | $1.06 |
| Chocolate | 38 g | 150 | 20 g | 13 g | 7 g | 0 g | 190 mg | stevia | $1.06 |
| Lightly Sweet | 38 g | 150 | 20 g | 12 g | 6 g | 0 g | 310 mg | stevia-free | $1.06 |
| Vanilla Spiced Chai | 38 g | 150 | 20 g | 13 g | 7 g | 0 g | 190 mg | stevia | $1.06 |
| **Raw Organic Fit** | | | | | | | | | |
| Original | 45.5 g | 170 | 28 g | 12 g | 9 g | <1 g | 150 mg | stevia | $2.08 |
| Vanilla | 46 g | 170 | 28 g | 12 g | 9 g | <1 g | 150 mg | stevia | $2.08 |
| Chocolate | 45.5 g | 170 | 28 g | 12 g | 9 g | <1 g | 200 mg | stevia | $2.08 |
| Coffee | 46.5 g | 170 | 28 g | 12 g | 9 g | <1 g | 150 mg | stevia | $4.16* |
| **SPORT Organic Plant-Based** | | | | | | | | | |
| Vanilla | 45 g (2 scoops) | 170 | 30 g | 7 g | 3 g | <1 g | 460 mg | stevia | $2.53 |
| Chocolate | 48 g (2 scoops) | 180 | 30 g | 8 g | 4 g | 2 g | 460 mg | stevia | $2.53 |
| **Raw Organic Protein & Greens** | | | | | | | | | |
| Vanilla | 27.5 g | 110 | 20 g | 3 g | 1 g | 0 g | 170 mg | stevia | $2.04 |
| Chocolate Cacao | 30.5 g | 120 | 20 g | 4 g | 3 g | 1 g | 150 mg | stevia | $2.04 |
| Lightly Sweet | 30 g | 130 | 20 g | 10 g | 6 g | 6 g | 170 mg | stevia-free | $2.04 |
| **Organic Creamy Protein with Oatmilk** | | | | | | | | | |
| Vanilla Cookie | 43 g | 160 | 20 g | 14 g | 5 g | <1 g | 340 mg | erythritol + stevia | $1.80 |
| Chocolate Brownie | 46 g | 170 | 20 g | 16 g | 6 g | <1 g | 350 mg | erythritol + stevia | $1.80 |

\* Fit Coffee is sold in a 465 g / 10-serving tub at the same $41.59 price, which doubles its cost per serving. That looks like a packaging/pricing anomaly rather than a different formula, but it is what the listing says.

All prices: Garden of Life US list, 18 Nov 2026. Servings per container: 20 for all Raw Organic Protein, Protein & Greens and Creamy Oatmilk; 28 for Raw Organic Meal; 20 for Fit (10 for Coffee); 19 for SPORT.

## 2.2 Raw Organic Protein — the flagship

**Protein blend (identical across flavors):** organic pea protein, organic sprouted brown rice protein, then twelve sprouted "supporting" ingredients at unspecified amounts: amaranth, buckwheat, millet, cracked-wall chlorella, quinoa, chia, garbanzo, lentil, adzuki, flax, sunflower, pumpkin and sesame sprouts.

Because pea and rice are the only two ingredients with meaningful protein density, and they are listed first, the blend is effectively **pea + rice protein**, with the sprout powders contributing flavor, fiber, trace minerals and a "14 sprouts" marketing number rather than grams of protein. Garden of Life does not disclose the pea:rice ratio.

**Flavor systems differ:**

- **Vanilla:** organic vanilla flavors with other natural flavors, organic erythritol, organic guar gum, organic stevia leaf extract, sea salt.
- **Chocolate:** organic chocolate flavor with other natural flavors, organic cocoa, organic erythritol, organic guar gum, sea salt, organic stevia.
- **Vanilla Chai:** organic vanilla and chai flavors, organic erythritol, organic guar gum, organic stevia, sea salt.
- **Unflavored:** no flavor blend, no erythritol, no stevia — the only SKU in the line with no sweetener at all.

**Probiotic/enzyme blend (all flavors):** lipase, protease, aspergillopepsin, beta-glucanase, cellulase, bromelain, phytase, lactase, papain, peptidase, pectinase, hemicellulase, xylanase, plus *Bacillus subtilis* DE111 at **250 million CFU at expiry**. Note the discrepancy with the SPORT line, which carries **2 billion CFU** — the flagship dose is roughly one-eighth of the dose used in the published DE111 trials (1–2.5 billion CFU/day).

**Declared allergens:** sesame. "Contains no dairy or soy ingredients, tree nuts, added sugars or filler ingredient." A separate facility statement on the newer Creamy line discloses that the plant also handles egg, milk, soy, wheat, fish, tree nuts and sesame.

**Vitamins:** the panel claims 10 µg (400 IU) vitamin D, 50 µg vitamin A, 3 mg vitamin E, 5 µg vitamin K and 6 mg iron per serving, with no vitamin premix in the ingredient list. The label presents these as naturally occurring. 400 IU of vitamin D from sprouted seeds and chlorella is not plausible at these inclusion rates; the source is undisclosed. Treat the vitamin numbers as label claims awaiting an explanation, not as established whole-food nutrition.

## 2.3 Raw Organic Meal — meal replacement

20 g protein from the same pea/rice base plus **44 "superfoods"**: a fiber blend (tapioca fiber, chia, flax meal), a fruit-and-vegetable blend (spinach, baobab, apple, beet, broccoli, carrot, tomato, green pepper, Brussels sprout, ginger, garlic, onion, strawberry, cherry, parsley, cauliflower, blackberry and more), and a probiotic/enzyme blend.

Adds **18–21 vitamins and minerals** at meaningful percentages: vitamin D 25%, E 70%, K 15%, B12 380%, biotin 140%, pantothenic acid 90%, chromium 100%, zinc 20%, iron 20%. These are added nutrients, not just whole-food trace amounts — the panel is closer to a multivitamin than the protein line is.

**Sodium is low (190 mg)** compared with the protein line (300–350 mg), which is unusual for a flavored powder and suggests a different salt/flavor strategy.

**Lightly Sweet** is the stevia-free option. Its panel is the least well corroborated in this dataset (`panel_confidence: medium`) and appears to use a different carbohydrate base (12 g carb, 6 g fiber, 310 mg sodium).

## 2.4 Raw Organic Fit — the "weight loss" line

28 g protein from a 41–42 g blend of pea, rice, tapioca fiber, pea fiber, chia, flax, chlorella and the sprout blend. Adds **700 mg of a "weight loss & stress management blend"**: organic Svetol (decaffeinated green coffee bean extract) and organic ashwagandha. Chromium is listed as 120 µg in older panels and 35 µg in newer ones.

The claims — "burns fat, satisfies hunger, helps fight cravings" — are structure/function claims, not approved health claims, and the evidence for green coffee extract and chromium for meaningful weight loss is weak and inconsistent (see [08 — evidence review](08-evidence-review.md)).

Fit has the **highest fiber (9 g)** and **highest protein (28 g)** of the non-SPORT lines, and the second-lowest cost per gram of protein ($0.074/g). It is, functionally, the most "protein per dollar" product in the range after Meal.

## 2.5 SPORT Organic Plant-Based — the athlete line

Different formula from the flagship: pea protein plus **sprouted navy bean, lentil and garbanzo**, and **cranberry seed protein** — no rice protein. 30 g protein per two-scoop, 45 g serving, with a labeled amino acid profile that meets the FAO pattern for every essential amino acid (see [04](04-protein-quality.md)).

Adds an "organic muscle recovery blend" of apple, tart cherry, turmeric, blueberry and goji — all at unspecified, probably small, amounts. Probiotic is 2 billion CFU *Bacillus subtilis* DE111 (older labels say *Bifidobacterium lactis* Bl-04, another sign of reformulation).

**Certifications:** USDA Organic, Non-GMO Project, NSF Certified for Sport, Informed Choice, NSF gluten-free, Kosher, vegan. This is the only line with NSF Certified for Sport, which matters for drug-tested athletes.

**Sodium is 460 mg per serving** — 20% of the Daily Value, and higher than a serving of many canned soups. If you use two servings a day, that is 920 mg before any food.

SPORT is also the product with the **worst independent lead result in the range**: 2.76 µg per serving, 564% of Consumer Reports' level of concern ([06](06-contaminants.md)).

## 2.6 Raw Organic Protein & Greens

20 g protein from pea, rice, chia, navy bean, lentil and garbanzo, plus six greens/vegetables (alfalfa grass juice, spinach, kale, broccoli, carrot, beet). 110–130 kcal, very low carb (3–4 g), low fiber (1–3 g), and the **highest cost per gram of protein in the range ($0.102/g)**.

The vanilla and chocolate versions are essentially protein plus a small greens blend; the "6 organic greens and veggies" are not quantified and contribute negligible micronutrients at the amounts used. The Lightly Sweet version has 6 g sugar and 10 g carb, which is a different product nutritionally.

## 2.7 Organic Creamy Protein with Oatmilk — newest line

20 g protein from **sprouted and fermented** pea and brown rice, plus amaranth, quinoa, buckwheat, millet and chia. The "creamy" system is coconut MCT oil powder, coconut water powder, oatmilk powder and coconut milk powder; the prebiotic/probiotic blend is inulin, acacia gum, xanthan gum, guar gum and *B. subtilis* DE111 (250 million CFU).

160–170 kcal, 4–4.5 g fat (2.5 g saturated, from coconut), 14–16 g carb, 5–6 g fiber, 340–350 mg sodium. Contains **tree nut (coconut)**. This is the cheapest per serving ($1.80) and the most "food-like" of the range, but it also has the most added ingredients and the highest cadmium result in the independent record (6.55 µg/serving, 160% of Prop 65's oral MADL — [06](06-contaminants.md)).

## 2.8 What is *not* in the range

- **No certified organic plant protein with no sweetener except Unflavored** — every flavored SKU uses stevia, erythritol, or both.
- **No unsweetened unflavored SPORT or Meal.**
- **No published PDCAAS/DIAAS** on any label or product page.
- **No lot-level certificate of analysis** published for any protein powder (Garden of Life publishes COAs only for its CBD softgels).
- **No "heavy metal tested" number** anywhere on pack or site — only the assertion that products are tested.

## 2.9 Adjacent dairy SKUs (not organic plant protein)

For completeness: **SPORT Certified Grass-Fed Whey** (chocolate/vanilla) and **Organic Whey Protein** are separate dairy lines. The SPORT whey vanilla was one of Clean Label Project's "Clean Sixteen" — non-detect for lead, cadmium, arsenic and mercury — which is a useful internal contrast: the same company's dairy SKU tested clean while its plant SKUs did not. That pattern is consistent with the wider literature on plant vs whey protein and heavy metals, and it undercuts any claim that contamination is simply a brand-wide inevitability.
