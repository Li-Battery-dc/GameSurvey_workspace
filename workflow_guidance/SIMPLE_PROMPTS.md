# Simple Prompts

Copy one of these prompts directly into Codex.
All prompts assume the repo rules in `AGENTS.md`.

## Prompt 1: Build Or Refresh Batches

```text
Use the repo skill `benchmark-triage`.

Read `AGENTS.md`, `benchmark.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, `template/registry_schema.md`, and `workflow_guidance/READING_WORKFLOW.md`.
Only use title, abstract, and introduction-level information for each paper.

Tasks:
1. Refresh the registry for Stage 1 triage.
2. Assign each paper a priority.
3. Group the papers into 3 to 5 batches under `corpus/batches/`.
4. Add or update brief triage notes and uncertainty flags.
5. Update `outline.md` only if the current outline cannot absorb the visible clusters.

Rules:
- Do not write paper cards yet.
- Do not draft prose.
- Keep uncertainty explicit.
- Leave each active row at `status = triaged`.
- Use `next_action = read-batch` for queued papers and `hold` only for intentional parking.
```

## Prompt 2: Choose The Next Reading Batch

```text
Use the current registry and outline to choose the next reading batch.

Read `AGENTS.md`, `benchmark.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, and `workflow_guidance/READING_WORKFLOW.md`.

Tasks:
1. Select the next batch of 6 to 12 papers that will stabilize the survey fastest.
2. Create or update `corpus/batches/batch_01.md` if no first batch exists, otherwise create the next batch file.
3. Explain why each selected paper belongs in the batch.
4. Mark whether each paper should be deep-read first or structured-skim first.

Rules:
- Prefer anchor and representative papers over edge cases.
- Cover multiple visible clusters when possible.
- If you touch the registry, keep queued papers at `status = triaged`.
```

## Prompt 3: Write One Paper Card

```text
Use the repo skill `paper-card-batch-reader`.

Read `AGENTS.md`, `benchmark.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, `template/paper_card_template.md`, `evals/quality_rubric.md`, and the paper for `{paper_id}`.

Tasks:
1. Create or update the card for `{paper_id}` using the registry path if present, otherwise `paper_cards/{paper_id}.md`.
2. Fill the template exactly.
3. Separate direct evidence, our synthesis, and uncertainty.
4. Update the matching registry row to `status = card-draft` unless you also run the review gate in the same pass.
5. Add exact outline anchors and nearby comparison papers.

Rules:
- Do not write polished section prose.
- If a field is unclear, mark it explicitly.
- If the card is still incomplete or uncertain, set `next_action = review-card`.
```

## Prompt 4: Process One Batch Into Cards

```text
Use the repo skill `paper-card-batch-reader`.

Read `AGENTS.md`, `benchmark.md`, `outline.md`, `corpus/batches/batch_01.md`, `corpus/registry/benchmark_registry.csv`, `template/paper_card_template.md`, `evals/quality_rubric.md`, and `evals/batch_review_checklist.md`.

Tasks:
1. Process every paper in `corpus/batches/batch_01.md`.
2. Create or update one paper card per paper.
3. Sync the registry after each card with `status = card-draft`.
4. Run the batch review gate and score each card as `strong`, `usable`, or `weak`.
5. Promote only the passing cards to `card-reviewed`.
6. Report which outline sections are now well supported.

Rules:
- Keep one paper per file.
- Keep facts separate from interpretation.
- Do not jump to survey drafting.
```

## Prompt 5: Review A Completed Batch Before Drafting

```text
Review the completed cards for one batch before any drafting.

Read `AGENTS.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, `evals/quality_rubric.md`, `evals/batch_review_checklist.md`, and all cards linked from `corpus/batches/batch_01.md`.

Tasks:
1. Score each card as strong, usable, or weak.
2. Explain the exact defect for weak cards.
3. Promote only strong or usable cards to `card-reviewed`; keep weak cards at `card-draft`.
4. Fix only the cards that can be corrected from the paper evidence already available.
5. Report which outline sections are ready to draft and which are still under-supported.

Rules:
- Prefer precise defects over generic feedback.
- Remove unsupported claims instead of smoothing them over.
```

## Prompt 6: Draft One Supported Section

```text
Draft one section of the survey using only `card-reviewed` paper cards.

Read `AGENTS.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, and the relevant reviewed cards in `paper_cards/`.

Tasks:
1. Choose one outline section with enough evidence.
2. Write a comparative draft to the path I specify.
3. Organize by benchmark evolution and comparison, not by isolated paper summaries.
4. End with limitations or open problems for that section.

Rules:
- Every paragraph must be traceable to reviewed paper cards.
- If the outline boundary needs to change, update `outline.md` and explain why.
```
