#!/usr/bin/env python3
"""Recompute every derived table in the Garden of Life investigation.

Inputs : data/products.csv, data/amino_acids.csv, data/thresholds.csv, data/contaminants.csv
Outputs: docs/generated/price-table.md, docs/generated/amino-acid-scores.md,
         docs/generated/contaminant-ratios.md

Stdlib only. Run from the repository root:  python scripts/analyze.py
"""

from __future__ import annotations

import csv
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "generated"

# FAO/WHO 2013 adult indispensable amino acid scoring pattern, mg per g protein.
FAO_2013 = {
    "his": 15.0,
    "ile": 30.0,
    "leu": 59.0,
    "lys": 45.0,
    "saa": 22.0,   # methionine + cysteine
    "aaa": 38.0,   # phenylalanine + tyrosine
    "thr": 23.0,
    "trp": 6.0,
    "val": 39.0,
}

# Fecal true digestibility and true ileal digestibility assumptions for
# isolated plant proteins (literature range), used for estimates only.
FECAL_DIG = (0.90, 0.97)
ILEAL_DIG = (0.85, 0.92)


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def money(value: float) -> str:
    return f"${value:,.2f}"


def write(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote docs/generated/{name}")


def price_tables() -> None:
    rows = read_csv("gol_products.csv")
    lines = [
        "# Generated: price per serving and per gram of protein",
        "",
        "Source: `data/products.csv`. Garden of Life US list prices, 18 Nov 2026.",
        "Subscription price is 15% below list where Garden of Life publishes it.",
        "",
        "| Product | Flavor | Serving (g) | Protein (g) | Servings | List price | $/serving | $/g protein | $/25 g protein |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        serving_g = float(r["serving_g"])
        protein = float(r["protein_g"])
        servings = float(r["servings_per_container"])
        price = float(r["price_usd_us_list"])
        per_serving = price / servings
        per_gram = per_serving / protein
        per_25 = per_gram * 25
        lines.append(
            f"| {r['product_line']} | {r['flavor']} | {serving_g:g} | {protein:g} | "
            f"{servings:g} | {money(price)} | {money(per_serving)} | "
            f"${per_gram:0.4f} | {money(per_25)} |"
        )

    # Cheapest and most expensive per gram of protein.
    scored = []
    for r in rows:
        per_gram = (
            float(r["price_usd_us_list"])
            / float(r["servings_per_container"])
            / float(r["protein_g"])
        )
        scored.append((per_gram, r["product_line"], r["flavor"]))
    scored.sort()
    lines += [
        "",
        "## Ranking by cost per gram of protein",
        "",
        f"- **Cheapest:** {scored[0][1]} {scored[0][2]} at ${scored[0][0]:0.4f}/g",
        f"- **Most expensive:** {scored[-1][1]} {scored[-1][2]} at ${scored[-1][0]:0.4f}/g",
        "",
        "Note: a serving of Raw Organic Meal delivers 20 g protein but also 13 g carbohydrate "
        "and 7 g fiber, so it is not a like-for-like protein-only purchase.",
    ]
    write("price-table.md", lines)


def amino_acid_tables() -> None:
    rows = read_csv("gol_amino_acids.csv")
    lines = [
        "# Generated: amino acid scores from manufacturer-labeled profiles",
        "",
        "Method: labeled mg of each amino acid per serving divided by labeled protein per "
        "serving, compared with the FAO/WHO 2013 adult pattern (mg/g protein). "
        "PDCAAS and DIAAS are **estimates** using assumed digestibility ranges, not measurements.",
        "",
        "| Product | His | Ile | Leu | Lys | Met+Cys | Phe+Tyr | Thr | Trp | Val | AAS (limiting) | Est. PDCAAS | Est. DIAAS |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|",
    ]
    for r in rows:
        protein = float(r["protein_g"])
        aa = {
            "his": float(r["his_mg"]),
            "ile": float(r["ile_mg"]),
            "leu": float(r["leu_mg"]),
            "lys": float(r["lys_mg"]),
            "saa": float(r["met_mg"]) + float(r["cys_mg"]),
            "aaa": float(r["phe_mg"]) + float(r["tyr_mg"]),
            "thr": float(r["thr_mg"]),
            "trp": float(r["trp_mg"]),
            "val": float(r["val_mg"]),
        }
        per_g = {k: v / protein for k, v in aa.items()}
        ratios = {k: per_g[k] / FAO_2013[k] for k in FAO_2013}
        limiting = min(ratios, key=ratios.get)
        aas = min(ratios[limiting], 1.0)
        all_aa_total = sum(
            float(r[k])
            for k in (
                "ala_mg", "arg_mg", "asp_mg", "cys_mg", "glu_mg", "gly_mg",
                "his_mg", "ile_mg", "leu_mg", "lys_mg", "met_mg", "phe_mg",
                "pro_mg", "ser_mg", "thr_mg", "trp_mg", "tyr_mg", "val_mg",
            )
        )
        pdcaas_lo = aas * FECAL_DIG[0]
        pdcaas_hi = min(aas * FECAL_DIG[1], 1.0)
        diaas_lo = aas * ILEAL_DIG[0]
        diaas_hi = min(aas * ILEAL_DIG[1], 1.0)
        label = {"saa": "Met+Cys", "aaa": "Phe+Tyr"}.get(limiting, limiting.capitalize())
        if ratios[limiting] >= 1.0:
            label = "none (all >=1.00)"
        lines.append(
            f"| {r['product']} | {ratios['his']:0.2f} | {ratios['ile']:0.2f} | "
            f"{ratios['leu']:0.2f} | {ratios['lys']:0.2f} | {ratios['saa']:0.2f} | "
            f"{ratios['aaa']:0.2f} | {ratios['thr']:0.2f} | {ratios['trp']:0.2f} | "
            f"{ratios['val']:0.2f} | {label}{"" if label.startswith("none") else f" ({aas:0.2f})"} | "
            f"{pdcaas_lo:0.2f}-{pdcaas_hi:0.2f} | {diaas_lo:0.2f}-{diaas_hi:0.2f} |"
        )
        lines.append(
            f"|  |  |  |  |  |  |  |  |  |  | *Total AA {all_aa_total/1000:0.2f} g vs {protein:g} g protein* | | |"
        )

    lines += [
        "",
        "Values in the amino acid columns are **ratios to the FAO pattern**; 1.00 means the "
        "pattern is exactly met. A ratio below 1.00 is the first limiting amino acid.",
        "",
        "Reference values for context: whey isolate PDCAAS 1.00 / DIAAS 1.09-1.18; "
        "pea protein concentrate PDCAAS 0.89 / DIAAS 0.82; rice protein concentrate "
        "PDCAAS 0.42 / DIAAS 0.37.",
    ]
    write("amino-acid-scores.md", lines)


def contaminant_tables() -> None:
    rows = read_csv("gol_contaminants.csv")
    thresholds = read_csv("gol_thresholds.csv")

    def limit(metal: str, authority_fragment: str) -> float | None:
        for t in thresholds:
            if t["metal"] == metal and authority_fragment.lower() in t["authority"].lower():
                return float(t["value_ug_per_day"])
        return None

    prop65 = {
        "lead": limit("lead", "OEHHA"),
        "cadmium": limit("cadmium", "OEHHA"),
        "arsenic_inorganic": limit("arsenic_inorganic", "OEHHA"),
    }

    lines = [
        "# Generated: contaminant concentration and ratio to benchmarks",
        "",
        "Conversion: ppb = ug per serving / serving_g * 1000. "
        "Percent of benchmark = ug per serving / benchmark * 100.",
        "",
        "| Study | Product | Flavor | Serving (g) | Lead ug | Lead ppb | % of 0.5 ug/day | Servings/week at 0.5 ug/day | Cadmium ug | % of 4.1 ug/day |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        if not r["serving_g"] or not r["lead_ug"]:
            continue
        serving = float(r["serving_g"])
        lead = float(r["lead_ug"])
        cadmium = float(r["cadmium_ug"]) if r["cadmium_ug"] else None
        lead_ppb = lead / serving * 1000
        pct = lead / 0.5 * 100
        per_week = 0.5 * 7 / lead
        cad_cell = f"{cadmium:0.2f}" if cadmium is not None else ""
        cad_pct = f"{cadmium / 4.1 * 100:0.0f}%" if cadmium is not None else ""
        lines.append(
            f"| {r['study']} | {r['product']} | {r['flavor']} | {serving:g} | "
            f"{lead:0.2f} | {lead_ppb:0.1f} | {pct:0.0f}% | {per_week:0.2f} | "
            f"{cad_cell} | {cad_pct} |"
        )

    lines += [
        "",
        "## Benchmark spread for lead",
        "",
    ]
    for t in thresholds:
        if t["metal"] == "lead":
            lines.append(
                f"- {t['value_ug_per_day']} ug/day, {t['authority']} ({t['benchmark']})"
            )
    lines += [
        "",
        "The same 2.76 ug lead result is **564%** of the 0.5 ug/day Prop 65-linked level, "
        "**125%** of the 2.2 ug/day FDA children's benchmark, and **28%** of the 10 ug/day "
        "NSF/USP adult limit. All three statements are true at once.",
    ]
    write("contaminant-ratios.md", lines)


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    price_tables()
    amino_acid_tables()
    contaminant_tables()
    print("done")


if __name__ == "__main__":
    main()
