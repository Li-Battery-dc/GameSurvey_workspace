# Simple Prompts

Copy one of these prompts directly into Codex.
All prompts assume the repo rules in `AGENTS.md`.

## Prompt 1: Triage The Next Window In A Long List

```text
Use the repo skill `benchmark-triage`.

Read `AGENTS.md`, `benchmark.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, `corpus/batches/batch_index.md` if it exists, `template/registry_schema.md`, and `workflow_guidance/READING_WORKFLOW.md`.

Tasks:
1. Process only the next `20-30` papers that are new, stale, or still ambiguous.
2. Refresh Stage 1 fields for those papers only.
3. Use readable title-aligned `paper_id` values in PascalCase or acronym-preserving CamelCase.
4. Set `queue_tier` and `triage_round` for each touched row.
5. Split high-value papers into small reading batches of `4-6` deep-read papers.
6. Reserve `paper_card_path` as `paper_cards/{batch_id}/{paper_id}.md` once a batch is assigned.
7. Update `corpus/batches/batch_index.md` and any touched `corpus/batches/batch_XX.md` files.
8. Update `outline.md` only if the current structure cannot absorb the visible clusters.

Rules:
- Do not write paper cards yet.
- Do not draft prose.
- Keep uncertainty explicit.
- Leave each active row at `status = triaged`.
- Use `next_action = read-batch` for queued papers and `hold` only for intentional parking.
- Do not reread the entire benchmark list if the registry already contains the papers you need.
```

## Prompt 2: Expand Or Rebalance The Batch Map

```text
Use the repo skill `benchmark-triage`.

Read `AGENTS.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, `corpus/batches/batch_index.md`, and `workflow_guidance/READING_WORKFLOW.md`.

Tasks:
1. Use only the registry and current batch files to rebalance the reading queue.
2. Keep `2-3` batches at `queue_tier = now`, enough batches at `queue_tier = next`, and move the rest to `later` or `hold`.
3. Resize deep-reading batches to `4-6` papers unless a tighter comparison cluster justifies more.
4. Ensure each touched row keeps a readable title-aligned `paper_id` and a matching `paper_cards/{batch_id}/{paper_id}.md` path.
5. Update `corpus/batches/batch_index.md` so it is enough to understand the queue without opening every batch file.
6. Report which batch should be read next and why.

Rules:
- Prefer anchor and representative papers over edge cases.
- Do not reread `benchmark.md` unless the registry is clearly missing information.
```

## Prompt 3: Resolve PDF Links From Abs Or Landing Pages

```text
Given these paper links, resolve the authoritative PDF URL for each paper before reading.

Read only the provided links and the linked official paper pages.

Tasks:
1. If a link is an arXiv `abs` page, resolve the matching PDF URL.
2. If a link is OpenReview, a publisher landing page, or a project page, locate the official PDF from that page.
3. Return a table with `paper_id`, original link, resolved PDF link, and any uncertainty.
4. Flag any link that still needs manual checking.

Rules:
- Prefer the official paper PDF over mirrors.
- Do not hallucinate a PDF URL if the landing page is unclear.
- If you cannot verify the PDF, return `needs-manual-check`.
```

## Prompt 4: Write One Paper Card

```text
Use the repo skill `paper-card-batch-reader`.

Read `AGENTS.md`, `benchmark.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, `corpus/batches/batch_index.md` if it exists, `template/paper_card_template.md`, `evals/quality_rubric.md`, and the paper for `{paper_id}`.

Tasks:
1. If `paper_link` is an abstract or landing page, resolve the authoritative PDF URL first.
2. Create or update the card for `{paper_id}` using the registry path if present, otherwise `paper_cards/{batch_id}/{paper_id}.md`.
3. Fill the template exactly.
4. Separate direct evidence, our synthesis, and uncertainty.
5. Update the matching registry row to `status = card-draft` unless you also run the review gate in the same pass.
6. Add exact outline anchors and nearby comparison papers.

Rules:
- Do not write polished section prose.
- If a field is unclear, mark it explicitly.
- If the card is still incomplete or uncertain, set `next_action = review-card`.
```

## Prompt 5: Process One Batch Into Cards

```text
Use the repo skill `paper-card-batch-reader`.

Read `AGENTS.md`, `benchmark.md`, `outline.md`, `corpus/batches/batch_index.md` if it exists, `corpus/batches/batch_01.md`, `corpus/registry/benchmark_registry.csv`, `template/paper_card_template.md`, `evals/quality_rubric.md`, and `evals/batch_review_checklist.md`.

Tasks:
1. Process every paper in `corpus/batches/batch_01.md`.
2. Resolve the authoritative PDF URL for each paper when `paper_link` is only an abstract or landing page.
3. Create or update one paper card per paper at the registry path, normally `paper_cards/{batch_id}/{paper_id}.md`.
4. Sync the registry after each card with `status = card-draft`.
5. Run the batch review gate and score each card as `strong`, `usable`, or `weak`.
6. Promote only the passing cards to `card-reviewed`.
7. Update `corpus/batches/batch_index.md` if the batch state changed.
8. Report which outline sections are now well supported.

Rules:
- Keep one paper per file.
- Keep facts separate from interpretation.
- Do not jump to survey drafting.
- Do not open unrelated batches unless a direct comparison is necessary.
```

## Prompt 6: Review A Completed Batch Before Drafting

```text
Review the completed cards for one batch before any drafting.

Read `AGENTS.md`, `outline.md`, `corpus/batches/batch_index.md` if it exists, `corpus/registry/benchmark_registry.csv`, `evals/quality_rubric.md`, `evals/batch_review_checklist.md`, and all cards linked from `corpus/batches/batch_01.md`.

Tasks:
1. Score each card as strong, usable, or weak.
2. Explain the exact defect for weak cards.
3. Promote only strong or usable cards to `card-reviewed`; keep weak cards at `card-draft`.
4. Fix only the cards that can be corrected from the paper evidence already available.
5. Update `corpus/batches/batch_index.md` if the batch state changed.
6. Report which outline sections are ready to draft and which are still under-supported.

Rules:
- Prefer precise defects over generic feedback.
- Remove unsupported claims instead of smoothing them over.
```

## Prompt 7: Draft One Supported Section

```text
Draft one section of the survey using only `card-reviewed` paper cards.

Read `AGENTS.md`, `outline.md`, `corpus/registry/benchmark_registry.csv`, `corpus/batches/batch_index.md` if it exists, and the relevant reviewed cards in `paper_cards/`.

Tasks:
1. Choose one outline section with enough evidence.
2. Write a comparative draft to the path I specify.
3. Organize by benchmark evolution and comparison, not by isolated paper summaries.
4. End with limitations or open problems for that section.

Rules:
- Every paragraph must be traceable to reviewed paper cards.
- If the outline boundary needs to change, update `outline.md` and explain why.
```
