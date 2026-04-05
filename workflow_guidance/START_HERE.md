# Start Here

This is the active workflow for the repository.

Read these files first:
- `benchmark.md`
- `outline.md`
- `AGENTS.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `workflow_guidance/READING_WORKFLOW.md`
- `workflow_guidance/SIMPLE_PROMPTS.md`
- `workflow_guidance/QA_CHECKLIST.md`
- `corpus/batches/batch_index.md` if it exists

If you are doing Stage 2 or Stage 3 work, also read:
- `template/paper_card_template.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`

Use the repo skills directly:
- `.codex/skills/benchmark-triage`
- `.codex/skills/paper-card-batch-reader`

Rule of thumb:
- Stage 1 decides what to read next and leaves active rows at `status = triaged`.
- Stage 2 turns papers into structured evidence and leaves new cards at `status = card-draft`.
- Stage 3 runs the eval gate, promotes only strong or usable cards to `card-reviewed`, and drafts only from reviewed evidence.
- Reserve `finalized` for cards that have already been checked enough to cite repeatedly during writing.

Long-list mode for this repo:
- When `benchmark.md` holds roughly 50 or more papers, treat it as the intake source, not the daily working context.
- Read the full `benchmark.md` when initializing the registry or importing newly added papers, then switch to `corpus/registry/benchmark_registry.csv` plus `corpus/batches/batch_index.md` for daily work.
- Default working windows are: Stage 1 triage `20-30` papers per pass, batch planning `10-20` queued rows per pass, and Stage 2 deep reading `4-6` papers per batch.
- Before deep reading, if a `paper_link` is only an arXiv `abs` page or another landing page, resolve the authoritative PDF URL first.

If you find any other workflow document outside this folder later, treat it as legacy unless it is explicitly referenced here or in `AGENTS.md`.
