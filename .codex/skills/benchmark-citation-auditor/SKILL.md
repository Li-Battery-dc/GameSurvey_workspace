---
name: benchmark-citation-auditor
description: "Use when auditing, organizing, or standardizing argument-level citations in the Overleaf paper's Benchmark chapter for this game-benchmark survey. Trigger on requests to check `overleaf_paper/Chapters/Benchmarks.tex` or the user's `Benchmark.tex` chapter for missing paper support, weak or mismatched evidence, nonstandard citation formats, raw paper-id parentheticals, BibTeX-key inconsistencies, or proposed citation edits. Always provide scholarly evidence recommendations first; edit the Overleaf repository only after explicit approval of the exact citation-normalization scope."
---

# Benchmark Citation Auditor

## Overview

Use this skill to audit the Benchmark chapter as an academic argument, not as a mechanical citation counter. The goal is to understand the survey's current narrative, map each substantive claim to suitable reviewed or finalized paper-card evidence, and propose citation additions or citation-format fixes without silently changing the Overleaf paper.

## Hard Boundary

Treat `overleaf_paper/` as read-only by default.

- Do not modify, format, compile, pull, merge, commit, or generate files inside `overleaf_paper/` during the audit phase.
- When citation formatting should be standardized, report the exact affected lines and proposed replacements first.
- Edit `overleaf_paper/Chapters/Benchmarks.tex` only after the user explicitly approves the exact scope of replacements.
- Do not modify `overleaf_paper/references.bib` unless the user separately approves bibliography edits.

## Open These Files First

- `outline.md`
- `writing.md`
- `script.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md`
- `benchmark.md` as backstop context
- `overleaf_paper/Chapters/Benchmarks.tex`
- `overleaf_paper/references.bib`
- relevant reviewed or finalized cards under `paper_cards/`
- `references/citation_policy.md`

If the user says `overleaf_paper/Chapter/Benchmark.tex`, resolve the actual file with:

```bash
rg --files overleaf_paper | rg 'Benchmarks?\.tex$'
```

The current repository path is `overleaf_paper/Chapters/Benchmarks.tex`.

## Evidence Eligibility

- Use `writing.md` and `outline.md` to understand the intended argument sequence.
- Use `script.md` and `Benchmarks.tex` to identify the actual written claims.
- Use `corpus/registry/benchmark_registry.csv` to route paper IDs, status, outline fit, and card paths.
- Use paper cards as the evidence layer for substantive citation recommendations.
- Prefer `status = finalized`; use `card-reviewed` only when the card's uncertainty does not affect the claim.
- Do not recommend `triaged` or `card-draft` papers for copy-ready citation unless the suggestion is explicitly labeled as a placeholder or evidence gap.
- Keep direct paper facts separate from survey synthesis. If a claim is the survey's synthesis, cite papers that support the ingredients and say what each citation contributes.

## Quick Scan

Run the read-only scanner before the scholarly audit:

```bash
.codex/skills/benchmark-citation-auditor/scripts/scan_benchmark_citations.py \
  --tex overleaf_paper/Chapters/Benchmarks.tex \
  --bib overleaf_paper/references.bib \
  --registry corpus/registry/benchmark_registry.csv
```

Use the script output to find:

- raw paper-ID parentheticals such as `(SmartPlay; GTBench)` that should become LaTeX citations
- citation commands whose keys are missing from `references.bib`
- citation keys that do not match registry `paper_id` values
- attached citations such as `AI GameStore\citep{...}` that may need spacing/style normalization

The script is diagnostic only. It must not be treated as proof that a citation is substantively appropriate.

## Audit Workflow

1. Build the narrative map:
   - identify which part of the Benchmark chapter is being audited: lead-in, taxonomy, purpose, interaction, evaluation, or synthesis
   - summarize the paragraph-level claim sequence in one compact list
   - note where the Overleaf text diverges from `writing.md` or `script.md`

2. Build a citation inventory:
   - run the scanner
   - list nonstandard citation formats and missing BibTeX keys
   - separate table citations from prose citations because `\citeyearpar{...}` in the taxonomy table can be legitimate

3. Mine evidence:
   - shortlist paper cards from registry `outline_sections`, `survey_role`, `status`, and `paper_card_path`
   - open the highest-leverage anchor and representative cards first
   - use card Sections 5, 6, 8, 9, 10, and 11 for interface, metrics, findings, survey-use claims, comparisons, and uncertainty
   - open additional cards only when a paragraph needs a missing contrast, calibration example, or boundary caveat

4. Evaluate each paragraph:
   - identify claims that are uncited, under-cited, over-cited, or cited with mismatched papers
   - state whether the paragraph needs an added citation, a citation replacement, a wording caveat, or no action
   - recommend a small number of citations that each do visible argumentative work
   - avoid citation piles unless the paragraph explicitly claims field-level breadth

5. Produce two separate outputs:
   - Evidence recommendations: paragraph or line reference, claim needing support, proposed paper IDs or BibTeX keys, and the reason each paper supports the claim
   - Citation-format fixes: exact current text and proposed replacement for nonstandard citation formatting

6. Ask for approval before any Overleaf edit:
   - include the exact lines or replacement categories to be changed
   - do not edit until the user approves that exact scope

## Citation Standard

Use the Overleaf paper's LaTeX citation style in `Benchmarks.tex`:

- prose support: `\citep{KeyA, KeyB}`
- textual author/year mention when grammatically needed: `\citet{Key}` or `Name~\citep{Key}` depending on local style
- taxonomy table year-only references: `Name~\citeyearpar{Key}` may be kept if already used consistently
- no raw copy-ready parenthetical paper IDs such as `(SmartPlay; GTBench)` in Overleaf text
- no Markdown-style citations in Overleaf text
- no invented BibTeX keys; verify every proposed key exists in `overleaf_paper/references.bib`

If registry `paper_id` and BibTeX key differ, use the actual BibTeX key in the replacement, but mention the registry `paper_id` in the audit explanation.

## Output Format

Start with findings, not a general summary.

For each evidence recommendation, include:

- location: line or paragraph identifier
- claim: the sentence-level assertion needing support
- recommendation: add, replace, remove, or keep citation
- proposed citation: BibTeX key(s), with registry paper IDs when different
- rationale: one sentence explaining the paper-card support
- uncertainty: any card caveat or need for full-paper recheck

For citation-format fixes, include exact replacement snippets. Keep them ready for user approval, but do not apply them unless explicitly authorized.

End with:

- cards opened
- scanner result summary
- remaining evidence gaps
- whether Overleaf edits are awaiting approval or were applied under approved scope

## Do Not

- do not rewrite the chapter unless explicitly asked
- do not edit `writing.md`
- do not treat `benchmark.md` or registry rows as evidence substitutes for cards
- do not cite papers only because their names appear in the paragraph
- do not use unreviewed cards for copy-ready claims without marking uncertainty
- do not normalize every BibTeX key to registry `paper_id` unless the bibliography already supports it or the user approves bib edits
