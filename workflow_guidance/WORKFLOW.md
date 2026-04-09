# Workflow

This folder intentionally keeps one workflow file only.

Use this repo in four steps:

## 1. List -> Queue

Goal:
- turn `benchmark.md` into the next reading queue

Read:
- `benchmark.md`
- `outline.md`
- `writing.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md` if it exists

Use:
- `.codex/skills/benchmark-triage`

Do:
- read only title, abstract, and intro-level framing
- update the registry and batch files
- leave touched rows at `status = triaged`
- keep `check_status = unchecked`

## 2. Queue -> Paper Card

Goal:
- turn one selected paper or batch into evidence-bearing paper cards

Read:
- `outline.md`
- `writing.md`
- `template/paper_card_template.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md` and the active batch file when needed
- the full paper PDF

Use:
- `.codex/skills/paper-card-batch-reader`

Do:
- resolve the authoritative PDF if the stored link is only a landing page
- read the paper closely enough to capture setup, interface, evaluation, results, and limitations
- create or update one card per paper
- sync the registry
- leave new or revised cards at `status = card-draft` unless the check step is also completed

## 3. Paper Card -> Check

Goal:
- verify the card is accurate enough to support drafting

Read:
- the paper card
- the full paper PDF
- `outline.md`
- `writing.md`
- `corpus/registry/benchmark_registry.csv`

Use:
- `.codex/skills/paper-card-auditor` for a single-paper full-text audit
- batch review only when the user explicitly wants batch-level checking

Do:
- remove or rewrite hallucinated or unsupported claims
- fix wrong taxonomy labels, section anchors, and survey-role claims
- keep direct evidence separate from synthesis
- promote only reliable cards to `status = card-reviewed`
- keep `check_status = unchecked` unless a human explicitly says the paper is checked

## 4. Checked Card -> Draft

Goal:
- write or revise survey sections from reliable evidence only

Read:
- `outline.md`
- `writing.md`
- the relevant `card-reviewed` or `finalized` cards
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md` when section readiness depends on queue state

Do:
- draft in `writing.md`
- keep claims comparative and traceable to cards
- if evidence is thin or conflicting, push the work back to the earlier steps instead of guessing

## Hard Rules

- Keep paper-supported facts separate from our synthesis.
- Update the existing registry row, card file, and `writing.md` instead of creating parallel notes.
- Use `paper_cards/` as the evidence layer and `writing.md` as the drafting layer.
- Do not draft from `card-draft` evidence unless the text is explicitly marked as a gap or open question.
- If docs conflict, prefer `benchmark.md`, `outline.md`, `writing.md`, `template/registry_schema.md`, `template/paper_card_template.md`, `corpus/registry/benchmark_registry.csv`, `evals/*`, this file, and `AGENTS.md`.
