#!/usr/bin/env python3
"""Read-only citation scanner for overleaf_paper/Chapters/Benchmarks.tex."""

from __future__ import annotations

import argparse
import csv
import difflib
import re
from pathlib import Path


CITE_RE = re.compile(r"\\(cite\w*|citeyearpar)(?:\[[^\]]*\])*\{([^{}]+)\}")
BIB_ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
BIB_BLOCK_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,(?P<body>.*?)(?=\n@\w+\s*\{|\Z)", re.DOTALL)
TITLE_RE = re.compile(r"\btitle\s*=\s*[{\"\'](?P<title>.*?)[}\"']\s*,", re.IGNORECASE | re.DOTALL)
PAREN_RE = re.compile(r"\(([^()\n]{2,180})\)")


def normalize_title(value: str) -> str:
    value = re.sub(r"[{}\\]", "", value)
    value = re.sub(r"\s+", " ", value).strip().lower()
    return re.sub(r"[^a-z0-9]+", "", value)


def read_registry(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["paper_id"]: row for row in csv.DictReader(handle)}


def read_bib(path: Path) -> tuple[set[str], dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    keys = set(BIB_ENTRY_RE.findall(text))
    titles: dict[str, str] = {}
    for match in BIB_BLOCK_RE.finditer(text):
        key = match.group(1)
        title_match = TITLE_RE.search(match.group("body"))
        if title_match:
            titles[key] = normalize_title(title_match.group("title"))
    return keys, titles


def best_registry_title_match(bib_title: str, registry: dict[str, dict[str, str]]) -> tuple[str, float] | None:
    if not bib_title:
        return None
    best: tuple[str, float] | None = None
    for paper_id, row in registry.items():
        reg_title = normalize_title(row.get("title", ""))
        if not reg_title:
            continue
        score = difflib.SequenceMatcher(None, bib_title, reg_title).ratio()
        if best is None or score > best[1]:
            best = (paper_id, score)
    if best and best[1] >= 0.72:
        return best
    return None


def split_keys(raw: str) -> list[str]:
    return [part.strip() for part in raw.split(",") if part.strip()]


def detect_parenthetical_ids(line: str, registry_ids: set[str]) -> list[str]:
    hits: list[str] = []
    for match in PAREN_RE.finditer(line):
        text = match.group(1)
        if "\\" in text:
            continue
        parts = [p.strip() for p in re.split(r"[;,]", text)]
        parts = [re.sub(r"^[Ee]\.?g\.?\s*", "", p).strip() for p in parts]
        ids = [p for p in parts if p in registry_ids]
        if len(ids) >= 2 or (len(ids) == 1 and (";" in text or "," in text)):
            hits.append(match.group(0))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex", default="overleaf_paper/Chapters/Benchmarks.tex")
    parser.add_argument("--bib", default="overleaf_paper/references.bib")
    parser.add_argument("--registry", default="corpus/registry/benchmark_registry.csv")
    args = parser.parse_args()

    tex_path = Path(args.tex)
    bib_path = Path(args.bib)
    registry_path = Path(args.registry)

    registry = read_registry(registry_path)
    registry_ids = set(registry)
    bib_keys, bib_titles = read_bib(bib_path)
    lines = tex_path.read_text(encoding="utf-8").splitlines()

    cite_occurrences: list[tuple[int, str, list[str]]] = []
    missing_bib: list[tuple[int, str, str]] = []
    nonregistry_keys: list[tuple[int, str, str, str]] = []
    parenthetical_ids: list[tuple[int, str]] = []
    attached_cites: list[tuple[int, str]] = []

    for line_no, line in enumerate(lines, start=1):
        if re.search(r"[A-Za-z0-9}]\\cite", line):
            attached_cites.append((line_no, line.strip()))

        for command, raw_keys in CITE_RE.findall(line):
            keys = split_keys(raw_keys)
            cite_occurrences.append((line_no, command, keys))
            for key in keys:
                if key not in bib_keys:
                    missing_bib.append((line_no, command, key))
                if registry_ids and key not in registry_ids:
                    inferred = ""
                    match = best_registry_title_match(bib_titles.get(key, ""), registry)
                    if match:
                        inferred = f"possible registry paper_id: {match[0]} ({match[1]:.2f} title match)"
                    nonregistry_keys.append((line_no, command, key, inferred))

        for hit in detect_parenthetical_ids(line, registry_ids):
            parenthetical_ids.append((line_no, hit))

    print(f"Scanned: {tex_path}")
    print(f"Bibliography: {bib_path} ({len(bib_keys)} keys)")
    print(f"Registry: {registry_path} ({len(registry_ids)} paper_ids)")
    print()
    print(f"Citation commands: {len(cite_occurrences)}")
    print(f"Missing BibTeX keys: {len(missing_bib)}")
    for line_no, command, key in missing_bib:
        print(f"  line {line_no}: \\{command}{{{key}}} missing from bib")
    print()
    print(f"Raw registry-id parentheticals: {len(parenthetical_ids)}")
    for line_no, hit in parenthetical_ids:
        print(f"  line {line_no}: {hit}")
    print()
    print(f"Citation keys not matching registry paper_id: {len(nonregistry_keys)}")
    for line_no, command, key, inferred in nonregistry_keys:
        suffix = f" [{inferred}]" if inferred else ""
        print(f"  line {line_no}: \\{command} key `{key}`{suffix}")
    print()
    print(f"Attached citations needing style check: {len(attached_cites)}")
    for line_no, text in attached_cites:
        print(f"  line {line_no}: {text}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
