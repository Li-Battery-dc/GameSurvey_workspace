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
- `workflow_guidance/START_HERE.md`
- `workflow_guidance/READING_WORKFLOW.md`
- `workflow_guidance/SIMPLE_PROMPTS.md`
- `workflow_guidance/QA_CHECKLIST.md`
- `corpus/batches/batch_index.md` if it exists

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
1. Stage 1: intake, triage, and queue management. Use `benchmark-triage`. Read only title, abstract, and introduction-level material. For long corpora, read `benchmark.md` once to seed context, then work in rolling windows from the registry. Update the registry strictly against `template/registry_schema.md`, maintain `corpus/batches/batch_index.md` plus `corpus/batches/batch_XX.md`, and leave each active row with `status = triaged`, a `queue_tier`, a `triage_round`, a batch or hold decision, `check_status = unchecked`, and updated `last_updated`.
2. Stage 2: deep read and write paper cards. Use `paper-card-batch-reader`. Read benchmark setup, interface, evaluation, results, and limitations. Work from one batch at a time, resolve a PDF when `paper_link` is only an abstract or landing page, create or update one card per paper under `paper_cards/{batch_id}/`, and sync the registry fields defined in `template/registry_schema.md`.
3. Stage 3: review and promote evidence. Run the eval gate before section drafting. Only strong or usable cards that pass `evals/quality_rubric.md` and `evals/batch_review_checklist.md` should be promoted to `card-reviewed`. For a targeted single-paper recheck of an existing card, use `paper-card-auditor`; that workflow is separate from the batch eval gate and should work directly against the full paper plus the current `outline.md` and `writing.md`.
4. Stage 4: section drafting and synthesis. Work from `outline.md`, `writing.md`, `corpus/registry/benchmark_registry.csv`, relevant reviewed cards, and batch state. Draft only from `card-reviewed` or `finalized` evidence unless the text is explicitly marked as a gap or open question. Keep section claims comparative and traceable back to cards.
5. Stage 5: manuscript revision and stabilization. Use `writing.md` plus reviewed evidence to tighten terminology, rebalance sections, identify missing support, and prepare citation-ready synthesis. When drafting exposes evidence gaps, send them back to the registry and paper-card workflow instead of guessing.

## Evidence Rules
- Keep paper-supported facts separate from our synthesis.
- Record uncertainty explicitly instead of forcing labels.
- Prefer updating existing registry rows, card files, and writing surfaces over inventing parallel note systems.
- Treat paper cards as the evidence layer and `writing.md` as the active drafting layer.
- Draft or revise prose only from `card-reviewed` or `finalized` cards unless the text is explicitly marked as a placeholder or open question.
- When docs conflict, prefer `benchmark.md`, `outline.md`, `writing.md`, `template/registry_schema.md`, `template/paper_card_template.md`, `corpus/registry/benchmark_registry.csv`, `evals/*`, `workflow_guidance/*`, and this file.

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
