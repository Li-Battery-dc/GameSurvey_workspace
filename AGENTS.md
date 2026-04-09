# AGENTS.md

## Mission
This repository is the working control plane for an end-to-end survey on game benchmarks for LLM and VLM agents. The repo now covers intake, triage, paper cards, card review, section drafting, and manuscript stabilization. Batches and paper cards remain important intermediate assets, but they are no longer the end goal.

## Read First
Always open these files before planning work:
- `benchmark.md`
- `outline.md`
- `writing.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `workflow_guidance/WORKFLOW.md`
- `corpus/batches/batch_index.md`

If the task touches batch card creation or batch review, also open:
- `template/paper_card_template.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`

If the task is a single-paper audit of an existing card, also open:
- `template/paper_card_template.md`
- the existing card for the target paper
- the target paper's registry row
- the full paper PDF or other authoritative full text

If the task touches drafting or revision, also open:
- the relevant reviewed cards under `paper_cards/`
- the relevant file under `corpus/batches/` when section support depends on batch state

## Repo Skills
Repo-local skills live in `.codex/skills/`.
- `benchmark-triage`: initial screening, batching, priority setting, and first-pass outline anchoring.
- `paper-card-batch-reader`: deep-read selected papers, write paper cards, and sync the registry.
- `paper-card-auditor`: full-text audit of one existing paper card for hallucinations, card accuracy, and alignment to the current outline and writing plan.
- No dedicated repo-local skill exists yet for section drafting or cross-section revision. For Stages 3 to 5, work directly from the workflow docs, reviewed cards, `outline.md`, and `writing.md`.

## Default Workflow
1. List -> queue. Use `benchmark-triage` to turn `benchmark.md` into the next reading queue and keep touched registry rows at `status = triaged`.
2. Queue -> paper card. Use `paper-card-batch-reader` to read the paper, create or update the card, and sync the registry at `status = card-draft`.
3. Paper card -> check. Verify the card against the full paper before drafting. Use `paper-card-auditor` for a single-paper full-text audit, or run batch review only when the user explicitly wants batch-level checking. Promote only reliable cards to `card-reviewed`.
4. Checked card -> draft. Draft or revise `writing.md` only from `card-reviewed` or `finalized` evidence. If support is thin or conflicting, push the work back to the earlier steps instead of guessing.

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
- Registry status vocabulary: `triaged`, `card-draft`, `card-reviewed`, `finalized`
- Queue tiers: `now`, `next`, `later`, `hold`
- `paper_id` should be stable, title-aligned, and readable. Use PascalCase or acronym-preserving CamelCase such as `SmartPlay`, `CKArena`, `GameplayQA`, or `GTBench` instead of lowercase slugs.
- `last_updated` uses `YYYY-MM-DD`
- If a registry row already points to another card path, follow the registry unless asked to migrate.
- If `batch_id` changes, update `paper_card_path` to the matching batch subdirectory.
