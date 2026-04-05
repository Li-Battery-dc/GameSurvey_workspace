# QA Checklist

Use this before moving from one stage to the next.

## Stage 1 QA

- Does every paper in the active scope have a priority?
- Does every paper in the active scope have a `queue_tier`?
- Does every touched paper have a `triage_round`?
- Does every touched paper use a readable title-aligned `paper_id`?
- Does every paper have a tentative batch or an explicit hold decision?
- Does every batched paper reserve `paper_card_path` as `paper_cards/{batch_id}/{paper_id}.md`?
- Is ambiguity recorded instead of hidden?
- Is `corpus/batches/batch_index.md` current for the active queue?
- Can the current outline explain the main visible paper clusters?
- Is the next reading batch justified by survey value rather than convenience?

## Stage 2 QA

- Does every processed paper have exactly one card?
- Does each card follow `template/paper_card_template.md`?
- Are direct facts, our synthesis, and unresolved uncertainty separated?
- Does each card name nearby comparison targets?
- Was the authoritative PDF resolved when `paper_link` was only an abstract or landing page?
- Is the registry synced after each card with `status = card-draft`, `paper_card_path`, `next_action`, and `last_updated`?
- Does each `paper_card_path` match the row's `batch_id` and `paper_id`?
- Is the paper anchored to a concrete part of `outline.md`?

## Stage 3 QA

- Did you run both `evals/quality_rubric.md` and `evals/batch_review_checklist.md`?
- Has each touched card been judged `strong`, `usable`, or `weak`?
- Were only `strong` or `usable` cards promoted to `card-reviewed`?
- Do weak cards remain `card-draft` with `next_action = review-card`?
- Are drafted sections comparative rather than serial summaries?
- Can each major paragraph be traced back to reviewed cards?
- Are unsupported claims removed or softened?
- Are outline changes explicit?
- Is `finalized` reserved for cards that are already stable enough to cite repeatedly during writing?
