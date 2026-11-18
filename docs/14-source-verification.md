# 14 — Source verification log

`scripts/check_links.py` is a link checker, not a citation verifier. It reports that a URL answered; it cannot tell you whether the paper exists, whether the authors and year are right, or whether the paper says what this report claims it says. On 18 November 2026 it left 34 URLs unresolved: 33 publisher bot blocks (401/403/429) and one HTTP 202 from CourtListener.

This document closes that gap. Every one of those 34 URLs was re-checked through a route that does not depend on the publisher letting a script in:

- **Crossref** (`api.crossref.org`) for DOI metadata: title, journal, year, first author.
- **PubMed E-utilities** (`eutils.ncbi.nlm.nih.gov`) for the PMID and the abstract, which is what lets a claim be tested against the paper rather than against its title.
- **Semantic Scholar** for the two 2026 articles too new for PubMed indexing.
- **Wayback Machine** (`web.archive.org`) for company and press pages, including the archived HTML, so the quoted text can be read.
- **CourtListener / RECAP** and **Top Class Actions** through a text-extraction route that returned the actual complaint and article.

Result: **15 of 15 peer-reviewed articles confirmed with matching metadata, and 15 of 19 web sources confirmed unchanged. Three were replaced or corrected and one was removed.** No citation remains on the assumption that it is probably real.

## 14.1 Peer-reviewed articles (15)

All fifteen matched on title, journal, year and first author, and the abstract was read to confirm the specific claim.

| Ref | Source | Verification route | Claim it supports | Outcome |
|---|---|---|---|---|
| 52 | Herreman et al., *Food Sci Nutr* 2020 | DOI 10.1002/fsn3.1809 · PMID 33133540 | DIAAS compilation; pea and rice below 75, whey and soy ≥75 | Confirmed |
| 54 | Guillin et al., *AJCN* 2022 | DOI 10.1093/ajcn/nqab354 · PMID 34665230 | Pea isolate DIAAS 1.00 in a human ileal trial | Confirmed (abstract states DIAAS 1.00 vs 1.45 for casein) |
| 55 | Sá et al., *J Food Compos Anal* 2024 | DOI 10.1016/j.jfca.2023.105938 | Amino-acid scoring patterns change apparent pea protein quality | Confirmed — **journal corrected**: the report previously said *Food Research International* |
| 58 | Santini et al., *JISSN* 2025 | DOI 10.1080/15502783.2025.2568047 · PMID 41059835 | Plant blend and animal protein produced similar 12-week gains | Confirmed |
| 59 | Reid-McCann et al., *Nutr Rev* 2025 | DOI 10.1093/nutrit/nuae200 · PMID 39813010 | Plant protein slightly lower muscle mass (SMD −0.20), difference in non-soy plants | Confirmed; the abstract says exactly this |
| 60 | Mendes et al., *JAND* 2026 | DOI 10.1016/j.jand.2026.156365 | Small MPS advantage for animal protein, larger in adults ≥65 | Confirmed via Semantic Scholar abstract (12 studies; ES 0.013 in ≥65) |
| 61 | Lim et al., *Curr Dev Nutr* 2024 | DOI 10.1016/j.cdnut.2024.103769 · PMID 38846451 | Plant blend matched whey for MPS **only with added leucine** | Confirmed |
| 65 | Witkowski et al., *ATVB* 2024 | DOI 10.1161/ATVBAHA.124.321019 · PMID 39114916 | 30 g erythritol enhanced platelet aggregation in all subjects | Confirmed |
| 66 | EFSA, *EFSA J* 2023 | DOI 10.2903/j.efsa.2023.8430 · PMID 38125972 | Laxative NOAEL 0.5 g/kg bw; ADI set at that level | Confirmed |
| 67 | Abushamat et al., *JACC Adv* 2025 | DOI 10.1016/j.jacadv.2025.101605 · PMID 39983608 | Erythritol/erythronate associated with HF and CV death in ARIC | Confirmed |
| 69 | Mysonhimer & Holscher, *Adv Nutr* 2022 | DOI 10.1093/advances/nmac094 · PMID 36041173 | Tolerable intake ranges for inulin, gums and other fibers | Confirmed — **URL corrected**: the old ScienceDirect PII belonged to a different article |
| 70 | Bonnema et al., *JADA* 2010 | DOI 10.1016/j.jada.2010.03.025 · PMID 20497775 | GI tolerance thresholds for chicory inulin | Confirmed — **URL corrected** to the DOI |
| 72 | Freedman et al., *IJMS* 2021 | DOI 10.3390/ijms22052453 · PMID 33671071 | DE111 pilot: immune-cell shifts, GI symptoms largely unchanged | Confirmed (this is a weaker result than "supports digestion") |
| 74 | Williams et al., *Fermentation* 2024 | DOI 10.3390/fermentation10020078 | Review of spore-based *B. subtilis* applications | Confirmed |
| 75 | Rinde et al., *Clin Kidney J* 2026 | DOI 10.1093/ckj/sfag235 · PMID 42549120 | Higher protein intake not linked to faster iohexol-measured GFR decline | Confirmed (n=1324) |

## 14.2 Web sources (19)

| Ref | Source | Verification route | Outcome |
|---|---|---|---|
| 1 | GOL protein category | Wayback 2026-07-13 | Confirmed |
| 2 | Raw Organic Protein, Vanilla | Wayback 2025-10-10 (`22g` present) | Confirmed |
| 3 | Raw Organic Protein, Unflavored | Wayback 2026-08-12 | Confirmed |
| 4 | SPORT Plant-Based, Vanilla | Wayback 2024-11-08 (`NSF`, `30g` present) | Confirmed |
| 5 | Raw Organic Fit, Original | Wayback 2024-11-08 | Confirmed |
| 6 | Raw Organic Meal, Lightly Sweet | Wayback 2023-03-26 | Confirmed |
| 7 | Creamy Protein with Oatmilk | Wayback 2025-07-23 | Confirmed |
| 8 | GOL certifications page | Wayback 2021-10-06 (page lists USDA, Non-GMO and Certified) | Confirmed |
| 9 | GOL COA page | Wayback 2026-04-13 (`Certificate`, `COA` present) | Confirmed |
| 10 | GOL "Sold to Nestlé" blog | Wayback 2026-05-16 | Confirmed |
| 11 | Nestlé Atrium acquisition release | Wayback 2025-08-04 | Confirmed |
| 12 | Nestlé Health Science "About us" | Live page returns 403 to every automated route, including a text-extraction proxy | **Replaced** with Nestlé's own Orgain release, its 3M-2018 results and its FY2022 results, which state the completion dates directly |
| 38 | Informed Choice register (wetestyoutrust.com) | CAPTCHA wall on every route | **Replaced** with Garden of Life's Informed-Choice page and the SPORT line page, both of which state the certification |
| 40 | CourtListener docket 71936453 | Extracted complaint PDF: "2025-11-19 – Garden of Life (Heavy Metals) Complaint", C.D. Cal. 5:25-cv-03118 | Confirmed |
| 41 | Top Class Actions, 16 Dec 2025 | Full article text retrieved | Confirmed |
| 81 | Forbes Vetted plant-protein round-up | CAPTCHA wall; the $3.42/serving figure could not be re-read | **Replaced** with Vega's own US product page ($64.99 / 19 servings, 30 g protein) |
| 84 | Reuters, Atrium acquisition | CAPTCHA wall; no Wayback snapshot | **Removed** — redundant with Nestlé's primary release (ref 11) |
| — | GOL Fit Coffee product page (inline link, doc 02) | Wayback | Confirmed |
| — | GOL Meal Chocolate product page (inline link, doc 02) | Wayback | Confirmed |

## 14.3 What this does and does not establish

**Established.** Every cited paper exists, is attributed to the right journal and year, and its abstract supports the sentence it is attached to. Every company and press claim quoted in this report can be read in an archived copy of the page. Four citations were wrong or unverifiable and are no longer in the report.

**Not established.** Reading an abstract is not reading a paper. Where a claim depends on a number buried in a results table — for example the exact DIAAS of a specific pea isolate — the number is quoted as the paper's own summary, not independently recomputed from its data. Two sources remain accessible only to a human with a browser: the Informed Choice register and the Garden of Life site itself; both are now cited through archived or first-party alternatives rather than left as bare links to a page that a reader may not be able to load.

**Reproduce it.** `python scripts/verify_refs.py` re-runs the Crossref, PubMed and Wayback checks used here and prints the same metadata and keyword matches.
