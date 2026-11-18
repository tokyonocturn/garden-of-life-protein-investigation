#!/usr/bin/env python3
"""Check every cited URL resolves.

Reads URLs from docs/13-references.md and data/*.csv, issues a HEAD request
(falling back to GET), and prints a table of status codes.

Stdlib only. Run: python scripts/check_links.py
Some publishers (Consumer Reports, Labdoor) block automated requests and will
return 403 even though the page is live; those are reported, not treated as dead.
"""

from __future__ import annotations

import csv
import re
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = ROOT / "data"
URL_RE = re.compile(r"https?://[^\s\)\]\"<>]+")
UA = "Mozilla/5.0 (compatible; research-link-checker/1.0)"


def collect() -> list[str]:
    urls: set[str] = set()
    for path in sorted(DOCS.glob("*.md")):
        urls.update(URL_RE.findall(path.read_text(encoding="utf-8")))
    for path in sorted(DATA.glob("*.csv")):
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                for value in row.values():
                    if value and value.startswith("http"):
                        urls.add(value.strip())
    return sorted(u.rstrip(".,;") for u in urls)


def check(url: str) -> tuple[int | str, str]:
    ctx = ssl.create_default_context()
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(request, timeout=20, context=ctx) as response:
                return response.status, response.geturl()
        except urllib.error.HTTPError as exc:
            if method == "GET":
                return exc.code, str(exc.reason)
        except Exception as exc:  # noqa: BLE001 - network errors are the output
            if method == "GET":
                return type(exc).__name__, str(exc)[:80]
    return "error", "no response"


def main() -> int:
    urls = collect()
    print(f"checking {len(urls)} urls\n")
    ok = 0
    problems = []
    for url in urls:
        status, detail = check(url)
        flag = "OK " if status == 200 else "!! "
        if status == 200:
            ok += 1
        else:
            problems.append((url, status, detail))
        print(f"{flag}{status} {url}")
    print(f"\n{ok}/{len(urls)} returned 200")
    if problems:
        print("\nNon-200 results (verify manually before citing):")
        for url, status, detail in problems:
            print(f"  {status} {url} -> {detail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
