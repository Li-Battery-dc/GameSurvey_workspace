#!/usr/bin/env python3
"""Audit two BibTeX files for duplicate and inconsistent paper records.

The script treats the first file as the reference source and the second file as
the target to audit. It compares papers by DOI, arXiv id, normalized title, and
high-confidence fuzzy title matches, then reports risky target entries.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable


@dataclass
class BibEntry:
    source: str
    entry_type: str
    key: str
    start_line: int
    raw: str
    fields: dict[str, str]

    def field(self, name: str) -> str:
        return self.fields.get(name.lower(), "")

    @property
    def title_norm(self) -> str:
        return normalize_title(self.field("title"))

    @property
    def doi_norm(self) -> str:
        return normalize_doi(self.field("doi") or self.field("DOI") or self.field("url"))

    @property
    def arxiv_id(self) -> str:
        values = [
            self.field("eprint"),
            self.field("url"),
            self.field("journal"),
            self.field("note"),
        ]
        return extract_arxiv_id(" ".join(v for v in values if v))


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def parse_entries(path: Path) -> tuple[list[BibEntry], list[dict[str, str]]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    starts = list(re.finditer(r"(?m)^@([A-Za-z]+)\s*\{", text))
    entries: list[BibEntry] = []
    parse_warnings: list[dict[str, str]] = []

    for index, match in enumerate(starts):
        start = match.start()
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        raw = text[start:end].rstrip()
        entry_type = match.group(1)
        start_line = line_number(text, start)

        if entry_type.lower() == "string":
            continue

        key_start = match.end()
        comma = find_top_level_comma(text, key_start)
        if comma is None or comma >= end:
            key = ""
            parse_warnings.append(
                {
                    "kind": "malformed_entry",
                    "file": str(path),
                    "line": str(start_line),
                    "message": "entry has no top-level comma after key",
                }
            )
            fields_text = raw
        else:
            key = text[key_start:comma].strip()
            fields_text = text[comma + 1 : end]

        if not key:
            parse_warnings.append(
                {
                    "kind": "empty_key",
                    "file": str(path),
                    "line": str(start_line),
                    "message": "entry key is empty",
                }
            )

        fields = parse_fields(fields_text)
        entries.append(
            BibEntry(
                source=str(path),
                entry_type=entry_type,
                key=key,
                start_line=start_line,
                raw=raw,
                fields=fields,
            )
        )

    return entries, parse_warnings


def find_top_level_comma(text: str, start: int) -> int | None:
    depth = 0
    quote = False
    escape = False
    for pos in range(start, len(text)):
        char = text[pos]
        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if quote:
            if char == '"':
                quote = False
            continue
        if char == '"':
            quote = True
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            if depth == 0:
                return None
            depth -= 1
        elif char == "," and depth == 0:
            return pos
    return None


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    index = 0
    length = len(text)
    while index < length:
        match = re.search(r"([A-Za-z][A-Za-z0-9_\-]*)\s*=", text[index:])
        if not match:
            break
        name = match.group(1).lower()
        value_start = index + match.end()
        while value_start < length and text[value_start].isspace():
            value_start += 1
        value, value_end = read_bib_value(text, value_start)
        fields[name] = clean_value(value)
        index = value_end + 1
    return fields


def read_bib_value(text: str, start: int) -> tuple[str, int]:
    if start >= len(text):
        return "", start

    if text[start] == "{":
        depth = 0
        pos = start
        while pos < len(text):
            char = text[pos]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return text[start + 1 : pos], pos + 1
            pos += 1
        return text[start + 1 :], len(text)

    if text[start] == '"':
        pos = start + 1
        escape = False
        while pos < len(text):
            char = text[pos]
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                return text[start + 1 : pos], pos + 1
            pos += 1
        return text[start + 1 :], len(text)

    pos = start
    while pos < len(text) and text[pos] not in ",\n}":
        pos += 1
    return text[start:pos], pos


def clean_value(value: str) -> str:
    value = value.strip().rstrip(",").strip()
    value = re.sub(r"\s+", " ", value)
    return value


def strip_latex(value: str) -> str:
    value = value.replace("\\&", "&")
    value = value.replace("ł", "l").replace("Ł", "L")
    latex_letter_map = {
        "l": "l",
        "L": "L",
        "o": "o",
        "O": "O",
        "ae": "ae",
        "AE": "AE",
        "aa": "aa",
        "AA": "AA",
    }
    for command, replacement in latex_letter_map.items():
        value = re.sub(r"\{?\\" + command + r"\}?", replacement, value)
    value = re.sub(r"\{?\\[\"'`^~=.]\{?([A-Za-z])\}?", r"\1", value)
    value = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\[a-zA-Z]+\*?", " ", value)
    value = value.replace("{", "").replace("}", "")
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return value


def normalize_title(value: str) -> str:
    value = strip_latex(value).lower()
    value = value.replace("language", "language")
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_people(value: str) -> list[str]:
    value = strip_latex(value).lower()
    parts = [p.strip() for p in re.split(r"\s+and\s+", value) if p.strip()]
    normalized = []
    for part in parts:
        if "," in part:
            pieces = [piece.strip() for piece in part.split(",", 1)]
            if len(pieces) == 2 and pieces[0] and pieces[1]:
                part = f"{pieces[1]} {pieces[0]}"
        words = [w for w in re.split(r"[^a-z0-9]+", part) if w]
        if not words:
            continue
        if words == ["others"] or words[-1] in {"others", "etc", "al"}:
            continue
        normalized.append(" ".join(words))
    return normalized


def normalize_doi(value: str) -> str:
    if not value:
        return ""
    value = strip_latex(value).lower()
    match = re.search(r"(10\.\d{4,9}/[^\s,;{}]+)", value)
    if not match:
        return ""
    return match.group(1).rstrip(".")


def extract_arxiv_id(value: str) -> str:
    if not value:
        return ""
    value = strip_latex(value)
    patterns = [
        r"arxiv[:/\s]+([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"abs/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"pdf/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"\b([0-9]{4}\.[0-9]{4,5})(?:v\d+)?\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, value, flags=re.I)
        if match:
            return match.group(1)
    return ""


def stable_id(entry: BibEntry) -> str:
    if entry.doi_norm:
        return f"doi:{entry.doi_norm}"
    if entry.arxiv_id:
        return f"arxiv:{entry.arxiv_id}"
    if entry.title_norm:
        return f"title:{entry.title_norm}"
    return f"key:{entry.key}"


def title_similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def build_reference_matches(
    ref_entries: list[BibEntry], target_entries: list[BibEntry], fuzzy_threshold: float
) -> list[dict[str, object]]:
    ref_by_key = {entry.key: entry for entry in ref_entries if entry.key}
    ref_by_doi = defaultdict(list)
    ref_by_arxiv = defaultdict(list)
    ref_by_title = defaultdict(list)
    for entry in ref_entries:
        if entry.doi_norm:
            ref_by_doi[entry.doi_norm].append(entry)
        if entry.arxiv_id:
            ref_by_arxiv[entry.arxiv_id].append(entry)
        if entry.title_norm:
            ref_by_title[entry.title_norm].append(entry)

    matches = []
    for target in target_entries:
        candidates: list[tuple[BibEntry, str, float]] = []
        if target.key in ref_by_key:
            candidates.append((ref_by_key[target.key], "same_key", 1.0))
        if target.doi_norm:
            candidates.extend((entry, "same_doi", 1.0) for entry in ref_by_doi[target.doi_norm])
        if target.arxiv_id:
            candidates.extend((entry, "same_arxiv", 1.0) for entry in ref_by_arxiv[target.arxiv_id])
        if target.title_norm:
            candidates.extend((entry, "same_title", 1.0) for entry in ref_by_title[target.title_norm])
            for entry in ref_entries:
                score = title_similarity(target.title_norm, entry.title_norm)
                if score >= fuzzy_threshold:
                    candidates.append((entry, "fuzzy_title", score))

        unique: dict[str, tuple[BibEntry, str, float]] = {}
        for entry, reason, score in candidates:
            slot = unique.get(entry.key)
            if slot is None or score > slot[2]:
                unique[entry.key] = (entry, reason, score)

        if not unique:
            continue

        best = sorted(unique.values(), key=lambda item: (item[2], item[1] == "same_key"), reverse=True)[0]
        matches.append(compare_entries(best[0], target, best[1], best[2]))
    return matches


def compare_entries(ref: BibEntry, target: BibEntry, match_reason: str, score: float) -> dict[str, object]:
    issues: list[dict[str, str]] = []

    if ref.key != target.key:
        issues.append({"field": "key", "reference": ref.key, "target": target.key})

    for field in ["title", "year", "doi", "eprint", "url"]:
        ref_value = canonical_field(ref, field)
        target_value = canonical_field(target, field)
        if not ref_value or not target_value:
            if ref_value != target_value:
                issues.append({"field": f"{field}_missing", "reference": ref_value, "target": target_value})
            continue
        if field == "title":
            if normalize_title(ref_value) != normalize_title(target_value):
                issues.append({"field": field, "reference": ref_value, "target": target_value})
        elif field == "doi":
            if normalize_doi(ref_value) != normalize_doi(target_value):
                issues.append({"field": field, "reference": ref_value, "target": target_value})
        elif field == "eprint":
            if extract_arxiv_id(ref_value) != extract_arxiv_id(target_value):
                issues.append({"field": field, "reference": ref_value, "target": target_value})
        else:
            if strip_latex(ref_value).lower() != strip_latex(target_value).lower():
                issues.append({"field": field, "reference": ref_value, "target": target_value})

    ref_authors = normalize_people(ref.field("author"))
    target_authors = normalize_people(target.field("author"))
    if ref_authors and target_authors:
        if ref_authors[:3] != target_authors[:3]:
            issues.append(
                {
                    "field": "author_first3",
                    "reference": " | ".join(ref_authors[:3]),
                    "target": " | ".join(target_authors[:3]),
                }
            )
        elif abs(len(ref_authors) - len(target_authors)) >= 5 and "etc" not in target.field("author").lower():
            issues.append(
                {
                    "field": "author_count",
                    "reference": str(len(ref_authors)),
                    "target": str(len(target_authors)),
                }
            )
    elif ref.field("author") != target.field("author"):
        issues.append({"field": "author_missing", "reference": ref.field("author"), "target": target.field("author")})

    severity = severity_for_issues(issues)
    return {
        "reference_key": ref.key,
        "target_key": target.key,
        "target_line": target.start_line,
        "match_reason": match_reason,
        "match_score": round(score, 3),
        "stable_id": stable_id(target),
        "target_title": target.field("title"),
        "severity": severity,
        "issues": issues,
    }


def canonical_field(entry: BibEntry, field: str) -> str:
    if field == "doi":
        return entry.field("doi") or entry.field("DOI")
    if field == "eprint":
        return entry.arxiv_id
    return entry.field(field)


def severity_for_issues(issues: list[dict[str, str]]) -> str:
    fields = {issue["field"] for issue in issues}
    if {"title", "doi", "eprint", "year", "author_first3"} & fields:
        return "high"
    if any(field.endswith("_missing") for field in fields):
        return "medium"
    if {"key", "url", "author_count"} & fields:
        return "low"
    return "ok"


def target_duplicates(entries: list[BibEntry]) -> list[dict[str, object]]:
    groups = defaultdict(list)
    for entry in entries:
        sid = stable_id(entry)
        if sid and not sid.startswith("key:"):
            groups[sid].append(entry)

    duplicates = []
    for sid, group in sorted(groups.items()):
        keys = [entry.key for entry in group]
        if len(set(keys)) <= 1 and len(group) <= 1:
            continue
        if len(group) > 1:
            duplicates.append(
                {
                    "stable_id": sid,
                    "keys": keys,
                    "lines": [entry.start_line for entry in group],
                    "titles": [entry.field("title") for entry in group],
                }
            )
    return duplicates


def duplicate_keys(entries: list[BibEntry]) -> list[dict[str, object]]:
    groups = defaultdict(list)
    for entry in entries:
        if entry.key:
            groups[entry.key].append(entry)
    return [
        {"key": key, "lines": [entry.start_line for entry in group], "titles": [entry.field("title") for entry in group]}
        for key, group in sorted(groups.items())
        if len(group) > 1
    ]


def format_markdown(report: dict[str, object]) -> str:
    lines: list[str] = []
    summary = report["summary"]
    lines.append("# Bib Consistency Audit")
    lines.append("")
    lines.append(
        f"- Reference entries: {summary['reference_entries']}; target entries: {summary['target_entries']}"
    )
    lines.append(
        f"- Matched target entries: {summary['matched_target_entries']}; high-risk matched inconsistencies: {summary['high_risk_matches']}"
    )
    lines.append(
        f"- Target duplicate paper groups: {summary['target_duplicate_paper_groups']}; duplicate target keys: {summary['target_duplicate_key_groups']}"
    )
    lines.append("")

    if report["parse_warnings"]:
        lines.append("## Parse Warnings")
        for warning in report["parse_warnings"]:
            lines.append(f"- {warning['file']}:{warning['line']} {warning['kind']}: {warning['message']}")
        lines.append("")

    if report["target_duplicate_keys"]:
        lines.append("## Duplicate Target Keys")
        for item in report["target_duplicate_keys"]:
            lines.append(f"- `{item['key']}` at lines {item['lines']}")
        lines.append("")

    if report["target_duplicate_papers"]:
        lines.append("## Duplicate Target Papers")
        for item in report["target_duplicate_papers"]:
            keys = ", ".join(f"`{key}`" for key in item["keys"])
            lines.append(f"- {item['stable_id']} at lines {item['lines']}: {keys}")
        lines.append("")

    risky_matches = [item for item in report["matches"] if item["severity"] in {"high", "medium"}]
    if risky_matches:
        lines.append("## Risky Matched Inconsistencies")
        for item in risky_matches:
            lines.append(
                f"- target `{item['target_key']}` line {item['target_line']} matches reference `{item['reference_key']}` "
                f"by {item['match_reason']} ({item['severity']})"
            )
            for issue in item["issues"]:
                if issue["field"] == "key":
                    continue
                lines.append(f"  - {issue['field']}: ref=`{issue['reference']}` target=`{issue['target']}`")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", default="reference.bib", help="canonical/reference BibTeX file")
    parser.add_argument("--target", default="overleaf_paper/references.bib", help="target BibTeX file to audit")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--fuzzy-threshold", type=float, default=0.94)
    args = parser.parse_args()

    ref_entries, ref_warnings = parse_entries(Path(args.reference))
    target_entries, target_warnings = parse_entries(Path(args.target))

    matches = build_reference_matches(ref_entries, target_entries, args.fuzzy_threshold)
    dup_papers = target_duplicates(target_entries)
    dup_keys = duplicate_keys(target_entries)

    report = {
        "summary": {
            "reference_entries": len(ref_entries),
            "target_entries": len(target_entries),
            "matched_target_entries": len(matches),
            "high_risk_matches": sum(1 for item in matches if item["severity"] == "high"),
            "medium_risk_matches": sum(1 for item in matches if item["severity"] == "medium"),
            "target_duplicate_paper_groups": len(dup_papers),
            "target_duplicate_key_groups": len(dup_keys),
        },
        "parse_warnings": ref_warnings + target_warnings,
        "target_duplicate_keys": dup_keys,
        "target_duplicate_papers": dup_papers,
        "matches": matches,
    }

    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(format_markdown(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
