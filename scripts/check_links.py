#!/usr/bin/env python3
"""Check every cited URL resolves.

Reads URLs from docs/*.md and data/*.csv, requests each one with a browser
User-Agent, and prints a status table. Concurrent (8 workers) so the whole
list finishes in about a minute.

Some publishers (Consumer Reports, Labdoor, Forbes) block automated
requests and return 403/429 even though the page is live. Those are
reported separately and must be verified by hand.

Stdlib only. Run: python scripts/check_links.py
"""

from __future__ import annotations

import csv
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = ROOT / "data"
URL_RE = re.compile(r"https?://[^\s\)\]\"<>]+")
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
TIMEOUT = 15


def collect() -> list[str]:
    urls: set[str] = set()
    for path in sorted(DOCS.rglob("*.md")):
        urls.update(URL_RE.findall(path.read_text(encoding="utf-8")))
    for path in sorted(DATA.glob("*.csv")):
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                for value in row.values():
                    if isinstance(value, str) and value.strip().startswith("http"):
                        urls.add(value.strip())
    cleaned = {u.rstrip(".,;") for u in urls}
    return sorted(cleaned)


def check(url: str) -> tuple[str, int | str, str]:
    ctx = ssl.create_default_context()
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "text/html,*/*"}
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT, context=ctx) as response:
            return url, response.status, response.geturl()
    except urllib.error.HTTPError as exc:
        return url, exc.code, str(exc.reason)
    except Exception as exc:  # noqa: BLE001 - network errors are the output
        return url, type(exc).__name__, str(exc)[:80]


def main() -> int:
    urls = collect()
    print(f"checking {len(urls)} urls with {TIMEOUT}s timeout, 8 workers\n")
    results = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for result in pool.map(check, urls):
            results.append(result)

    ok = [r for r in results if r[1] == 200]
    blocked = [r for r in results if r[1] in (401, 403, 429)]
    broken = [r for r in results if r not in ok and r not in blocked]

    for url, status, _detail in results:
        flag = "OK " if status == 200 else ("BLK" if status in (401, 403, 429) else "!! ")
        print(f"{flag} {status!s:>4} {url}")

    print(f"\n{len(ok)}/{len(urls)} returned 200")
    if blocked:
        print(f"\n{len(blocked)} bot-blocked (401/403/429) — page may still be live:")
        for url, status, detail in blocked:
            print(f"  {status} {url} ({detail})")
    if broken:
        print(f"\n{len(broken)} other non-200 results — verify before citing:")
        for url, status, detail in broken:
            print(f"  {status} {url} ({detail})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
