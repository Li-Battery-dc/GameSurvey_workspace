# AGENTS.md

## Mission
This repository is the working control plane for an end-to-end survey on game benchmarks for LLM and VLM agents. The repo now covers intake, triage, paper cards, card review, section drafting, and manuscript stabilization. Batches and paper cards remain important intermediate assets, but they are no longer the end goal.

## Overleaf Paper Repository
The `overleaf_paper/` directory is a separately cloned Overleaf Git repository for the user's paper writing. Treat it as a read-only reference strictly. Do not modify, format, compile, pull, rebase, merge, commit, push, or generate files inside `overleaf_paper/`. When the user asks for changes to the paper, report the proposed edits in the conversation for human review first; apply them only after the user explicitly approves the exact scope.

## Important Files
Always open these files before planning work:
- `outline.md`
- `writing.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md`
  
the paper list in `benchmark.md` 
the final scripts in `script.md`

If the task touches batch card creation or batch review, also open:
- `template/paper_card_template.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`

If the task is a single-paper audit of an existing card, also open:
- `template/paper_card_template.md`
- the existing card for the target paper
- the target paper's registry row
- the full paper PDF or other authoritative full text

If the task touches drafting or revision, you can search:
- the relevant reviewed cards under `paper_cards/`
- the relevant file under `corpus/batches/` when section support depends on batch state

## Repo Skills
Repo-local skills live in `.codex/skills/`.
- `benchmark-triage`: initial screening, batching, priority setting, and first-pass outline anchoring.
- `paper-card-batch-reader`: deep-read selected papers, write paper cards, and sync the registry.
- `paper-card-auditor`: full-text audit of one existing paper card for hallucinations, card accuracy, and alignment to the current outline and writing plan.
- `survey-section-writer`: align section plans in `writing.md`, mine support from reviewed paper cards, and then draft or revise copy-ready prose in `script.md`. This skill is the default for section drafting, cross-section revision, and manuscript stabilization work.

## Evidence Rules
- Keep paper-supported facts separate from our synthesis.
- Record uncertainty explicitly instead of forcing labels.
- Prefer updating existing registry rows, card files, and writing surfaces over inventing parallel note systems.
- Treat paper cards as the evidence layer and `writing.md` as the active drafting layer.
- Draft or revise prose only from `card-reviewed` or `finalized` cards unless the text is explicitly marked as a placeholder or open question.
- When docs conflict, prefer `benchmark.md`, `outline.md`, `writing.md`, `template/registry_schema.md`, `template/paper_card_template.md`, `corpus/registry/benchmark_registry.csv`, `evals/*`, `workflow_guidance/WORKFLOW.md`, and this file.

## File Conventions
- Batch index: `corpus/batches/batch_index.md`
- Batch files: `corpus/batches/batch_XX.md`
- Default paper card path: `paper_cards/{batch_id}/{paper_id}.md`
- Active drafting workspace: `writing.md`
- Draft handoff file: `script.md`. When the user asks for copy-ready prose, write or revise `script.md` and keep it aligned with the latest `writing.md` and `outline.md` plan.
- Citation rule for draft prose: when writing `script.md` or other copy-ready survey text, place citations directly as `paper_id` from the registry, using the in inline parenthetical form, for example `(SmartPlay; GTBench)` 
- Registry status vocabulary: `triaged`, `card-draft`, `card-reviewed`, `finalized`
- Queue tiers: `now`, `next`, `later`, `hold`
- `paper_id` should be stable, title-aligned, and readable. Use PascalCase or acronym-preserving CamelCase such as `SmartPlay`, `CKArena`, `GameplayQA`, or `GTBench` instead of lowercase slugs.
- `last_updated` uses `YYYY-MM-DD`
- If a registry row already points to another card path, follow the registry unless asked to migrate.
- If `batch_id` changes, update `paper_card_path` to the matching batch subdirectory.
