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

If you find any other workflow document outside this folder later, treat it as legacy unless it is explicitly referenced here or in `AGENTS.md`.
