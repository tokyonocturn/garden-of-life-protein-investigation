#!/usr/bin/env python3
"""Resolve references that return 401/403/429 to an automated client.

Three routes, all public and key-free:

1. Wayback Machine  -- for publisher pages and company statements. Returns the
   archived snapshot's timestamp plus whether expected strings appear in it.
2. Crossref         -- DOI metadata (title, journal, year, first author).
3. PubMed E-utilities -- PMID and abstract, used to confirm that a paper says
   what the report attributes to it.

Run:  python scripts/verify_refs.py            (all routes)
      python scripts/verify_refs.py --route wb (one route)

Nothing here writes to the repository; it prints a report to stdout.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Reference number, short label, URL that the bot-blocked check could not read,
# and strings that must appear on the page for the citation to be supported.
WAYBACK = [
    (1, "GOL protein category", "https://www.gardenoflife.com/products/our-protein", ["Protein"]),
    (2, "Raw Organic Protein Vanilla", "https://www.gardenoflife.com/products/our-vitamins/raw-organic-protein/raw-organic-protein-powder-vanilla", ["22g", "Raw Organic Protein"]),
    (3, "Raw Organic Protein Unflavored", "https://www.gardenoflife.com/products/our-protein/raw-organic-protein-powder-unflavored-no-stevia", ["Unflavored"]),
    (4, "SPORT Plant-Based Vanilla", "https://www.gardenoflife.com/products/our-protein/sport-organic-plant-based-protein-vanilla", ["NSF", "30g"]),
    (5, "Raw Organic Fit Original", "https://www.gardenoflife.com/products/our-protein/raw-organic-fit-protein-original-powder", ["Fit"]),
    (6, "Raw Organic Meal Lightly Sweet", "https://www.gardenoflife.com/products/raw-organic-meal-lightly-sweet-powder", ["Lightly Sweet"]),
    (7, "Creamy Protein Oatmilk", "https://www.gardenoflife.com/products/organic-creamy-protein-oatmilk-vanilla-cookie", ["Oatmilk"]),
    (8, "GOL certifications", "https://www.gardenoflife.com/our-certifications", ["Non-GMO", "Certified"]),
    (9, "GOL COA page", "https://www.gardenoflife.com/cbd-coas", ["Certificate of Analysis"]),
    (10, "GOL Nestle blog", "https://www.gardenoflife.com/blog/nestle", ["Nestl"]),
    (11, "Nestle Atrium release", "https://www.nestle.com/media/pressreleases/allpressreleases/nestle-acquires-atrium-innovations", ["Atrium"]),
    (12, "Nestle Health Science about", "https://www.nestlehealthscience.us/about-us", ["Orgain", "Atrium"]),
    (38, "Informed Choice listing", "https://choice.wetestyoutrust.com/supplement-search/garden-life/raw-organic-protein", ["Garden of Life"]),
    (40, "CourtListener docket", "https://www.courtlistener.com/docket/71936453/1/anne-marie-deherrera-v-garden-of-life-llc", ["DeHerrera"]),
    (41, "Top Class Actions", "https://topclassactions.com/lawsuit-settlements/lawsuit-news/garden-of-life-faces-lawsuit-over-dangerous-lead-levels-in-organic-plant-based-protein/", ["Garden of Life"]),
    (81, "Forbes Vetted", "https://www.forbes.com/sites/forbes-personal-shopper/article/best-plant-based-protein-powders", ["Vega"]),
    (84, "Reuters Atrium", "https://www.reuters.com/article/business/nestle-to-buy-vitamin-maker-atrium-innovations-for-23-billion-idUSKBN1DZ2EK", ["Atrium"]),
]

# Reference number, DOI, PubMed ID (or None when not indexed), short label.
JOURNALS = [
    (52, "10.1002/fsn3.1809", "33133540", "Herreman 2020 DIAAS compilation"),
    (54, "10.1093/ajcn/nqab354", "34665230", "Guillin 2022 pea ileal digestibility"),
    (55, "10.1016/j.jfca.2023.105938", None, "Field pea scoring patterns 2024"),
    (58, "10.1080/15502783.2025.2568047", "41059835", "Plant vs animal blend RCT 2025"),
    (59, "10.1093/nutrit/nuae200", "39813010", "Plant vs animal muscle meta-analysis 2025"),
    (60, "10.1016/j.jand.2026.156365", None, "Plant vs animal MPS meta-analysis 2026"),
    (61, "10.1016/j.cdnut.2024.103769", "38846451", "Plant blend + leucine vs whey 2024"),
    (62, "10.1136/bjsports-2017-097608", "28698222", "Morton 2018 protein meta-analysis"),
    (65, "10.1161/ATVBAHA.124.321019", "39114916", "Erythritol platelet reactivity 2024"),
    (66, "10.2903/j.efsa.2023.8430", "38125972", "EFSA erythritol re-evaluation 2023"),
    (67, "10.1016/j.jacadv.2025.101605", "39983608", "Erythritol ARIC 2025"),
    (69, "10.1093/advances/nmac094", "36041173", "Nondigestible carbohydrate tolerance 2022"),
    (70, "10.1016/j.jada.2010.03.025", "20497775", "Chicory inulin tolerance 2010"),
    (72, "10.3390/ijms22052453", "33671071", "B. subtilis DE111 pilot 2021"),
    (74, "10.3390/fermentation10020078", None, "B. subtilis review 2024"),
    (75, "10.1093/ckj/sfag235", None, "Protein intake and iohexol GFR 2026"),
]


def get(url: str, tries: int = 4, timeout: int = 45) -> str:
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001 - reported, not swallowed
            last = exc
            time.sleep(2 + 2 * attempt)
    raise last  # type: ignore[misc]


def plain(html: str) -> str:
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))


def check_wayback() -> None:
    print("== Wayback Machine ==")
    for num, label, url, keys in WAYBACK:
        try:
            api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
            snap = json.loads(get(api)).get("archived_snapshots", {}).get("closest", {})
            if not snap.get("url"):
                print(f"[{num}] {label}: NO SNAPSHOT")
                continue
            raw = snap["url"].replace("/http", "id_/http", 1) if "id_/" not in snap["url"] else snap["url"]
            text = plain(get(raw))
            hits = {k: (k.lower() in text.lower()) for k in keys}
            verdict = "CONFIRMED" if all(hits.values()) else "PARTIAL"
            print(f"[{num}] {label}: {verdict} archived={snap['timestamp']} len={len(text)} {hits}")
        except Exception as exc:  # noqa: BLE001
            print(f"[{num}] {label}: ERROR {type(exc).__name__} {str(exc)[:90]}")
        time.sleep(1)


def check_journals() -> None:
    print("== Crossref + PubMed ==")
    for num, doi, pmid, label in JOURNALS:
        try:
            meta = json.loads(get("https://api.crossref.org/works/" + doi))["message"]
            title = (meta.get("title") or [""])[0]
            journal = (meta.get("container-title") or [""])[0]
            year = meta.get("issued", {}).get("date-parts", [[None]])[0][0]
            authors = meta.get("author") or [{}]
            first = authors[0].get("family", "?")
            print(f"[{num}] {label}\n     DOI {doi} -> {title[:95]} | {journal[:50]} | {year} | {first}")
        except Exception as exc:  # noqa: BLE001
            print(f"[{num}] {label}: CROSSREF ERROR {type(exc).__name__} {str(exc)[:80]}")
        if pmid:
            try:
                xml = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
                          f"?db=pubmed&retmode=xml&id={pmid}")
                abstract = re.findall(r"<AbstractText[^>]*>(.*?)</AbstractText>", xml, re.S)
                text = re.sub(r"<[^>]+>", "", " ".join(abstract))
                print(f"     PMID {pmid} abstract {len(text)} chars: {text[:220]}...")
            except Exception as exc:  # noqa: BLE001
                print(f"     PMID {pmid} ERROR {type(exc).__name__}")
            time.sleep(0.5)
        time.sleep(1.5)


def main() -> int:
    # Windows consoles default to cp1252; metadata contains accented surnames.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    parser = argparse.ArgumentParser()
    parser.add_argument("--route", choices=["wb", "doi", "all"], default="all")
    args = parser.parse_args()
    if args.route in ("wb", "all"):
        check_wayback()
    if args.route in ("doi", "all"):
        check_journals()
    return 0


if __name__ == "__main__":
    sys.exit(main())
