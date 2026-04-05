# AGENTS.md

## Mission
This repository supports a survey on game benchmarks for LLM and VLM agents. The working goal is to turn the long benchmark list into a stable reading queue, then into evidence-bearing paper cards for later survey writing.

## Read First
Always open these files before planning work:
- `benchmark.md`
- `outline.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `workflow_guidance/START_HERE.md`
- `workflow_guidance/READING_WORKFLOW.md`
- `workflow_guidance/SIMPLE_PROMPTS.md`
- `workflow_guidance/QA_CHECKLIST.md`

If the task is Stage 2 or Stage 3 work, also open:
- `template/paper_card_template.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`

## Repo Skills
Repo-local skills live in `.codex/skills/`.
- `benchmark-triage`: initial screening, batching, priority setting, and first-pass outline anchoring.
- `paper-card-batch-reader`: deep-read selected papers, write paper cards, and sync the registry.

## Default Workflow
1. Stage 1: use `benchmark-triage`. Read only title, abstract, and introduction-level material. Update the registry strictly against `template/registry_schema.md`, create or refresh `corpus/batches/`, and leave each active row with `status = triaged`, a batch or hold decision, a concrete `next_action`, and updated `last_updated`.
2. Stage 2: use `paper-card-batch-reader`. Read benchmark setup, interface, evaluation, results, and limitations. Create or update one card per paper under `paper_cards/` and sync the registry fields defined in `template/registry_schema.md`.
3. Stage 3: run the eval gate before drafting. Only strong or usable cards that pass `evals/quality_rubric.md` and `evals/batch_review_checklist.md` should be promoted to `card-reviewed` and used for section drafting.

## Evidence Rules
- Keep paper-supported facts separate from our synthesis.
- Record uncertainty explicitly instead of forcing labels.
- Prefer updating existing registry rows and card files over inventing parallel note systems.
- When docs conflict, prefer `benchmark.md`, `outline.md`, `template/registry_schema.md`, `template/paper_card_template.md`, `corpus/registry/benchmark_registry.csv`, `evals/*`, `workflow_guidance/*`, and this file.

## File Conventions
- Batch files: `corpus/batches/batch_XX.md`
- Default paper card path: `paper_cards/{paper_id}.md`
- Registry status vocabulary: `triaged`, `card-draft`, `card-reviewed`, `finalized`
- `last_updated` uses `YYYY-MM-DD`
- If a registry row already points to another card path, follow the registry unless asked to migrate.
- Keep `paper_id` stable and lowercase.
