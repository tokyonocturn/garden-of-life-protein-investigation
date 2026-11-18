# Changelog

## 1.1, 18 November 2026

Verification pass on the published report. No analytical finding, score or verdict changed; the corrections are to citations, to the scope of one certification claim, and to the record of what has been verified.

### Citations corrected

- **Ref 55**, the field-pea scoring-pattern paper was attributed to *Food Research International*. It is in the *Journal of Food Composition and Analysis* (2024;128:105938). Journal name and DOI corrected.
- **Ref 69**, the ScienceDirect PII pointed at a different article. Replaced with the DOI (10.1093/advances/nmac094) and PMID 36041173.
- **Ref 70**, the JADA inulin paper's PII could not be confirmed. Replaced with the DOI (10.1016/j.jada.2010.03.025) and PMID 20497775.
- **Ref 12**, Nestlé Health Science's "About us" page returns 403 to every automated route and could not be verified. Replaced with Nestlé's own Orgain acquisition release (2 Feb 2022), its 3M-2018 results (Atrium completed at the beginning of March 2018) and its FY2022 results (Orgain completed 1 April 2022).
- **Ref 38**, the Informed Choice register (wetestyoutrust.com) is behind a CAPTCHA wall. Replaced with Garden of Life's Informed-Choice page and the SPORT line page, both of which state the certification.
- **Ref 81**, the Forbes round-up is behind a CAPTCHA wall and its $3.42/serving figure could not be re-read. Replaced with Vega's own US product page ($64.99 / 19 servings, 30 g protein = $3.42/serving, $0.114/g).
- **Ref 84**, the Reuters acquisition story was unreachable and duplicated Nestlé's primary release. Removed.

### Metadata added

- DOI and PMID added to 15 peer-reviewed references; DOI added to two more.

### Claims re-checked against abstracts

- Herreman 2020, Guillin 2022, Reid-McCann 2025, Santini 2025, Lim 2024, Morton 2018, Witkowski 2024, EFSA 2023, Abushamat 2025, Mysonhimer 2022, Bonnema 2010, Freedman 2021, Williams 2024, Rinde 2026 and Mendes 2026 were each confirmed to say what the report attributes to them. The Nutrition Reviews meta-analysis (plant protein −0.20 SMD for muscle mass) and the JAND 2026 MPS meta-analysis (advantage for animal protein concentrated in adults ≥65) both support the report's existing "mixed, converging on similar with adequate protein and leucine" framing; neither changed a conclusion.

### Scope correction

- **Informed Choice** is an LGC banned-substance certification held on the SPORT line, not across the whole range. Docs 08 and 12 previously listed it among the certifications of the products generally; both now scope it to SPORT.

### Added

- `docs/14-source-verification.md`, per-source record of how each of the 30 bot-blocked or rate-limited URLs was confirmed, corrected, replaced or removed.
- `scripts/verify_refs.py`, re-runs the Crossref, PubMed and Wayback checks.
- README section on source verification and a link to the new doc.

### Verification state

91 URLs checked: 61 return HTTP 200 directly, 30 are blocked to automated clients, 0 return 404. All 30 blocked URLs were resolved through an alternate route. Zero references remain as unverified assumptions.

---

## 1.0, 18 November 2026

Initial publication: 19 SKUs across 6 organic plant lines, contamination assessment, protein-quality analysis, evidence review, regulation and litigation history, price analysis, competitor comparisons and verdict. Grade C (5.1/10).
