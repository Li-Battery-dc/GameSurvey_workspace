# Reading Workflow

This repository uses a three-stage reading and review pipeline.

## Stage 1: Triage And Batch

Goal:
- turn the benchmark list into a reading queue
- assign priority
- create 3 to 5 comparison-friendly batches
- stabilize the outline before deep reading

Use:
- `benchmark.md`
- `outline.md`
- `corpus/registry/benchmark_registry.csv`
- `template/registry_schema.md`
- `.codex/skills/benchmark-triage`

Read only:
- title
- abstract
- introduction-level framing
- project page or code page only when needed to clarify benchmark scope

Expected outputs:
- updated `corpus/registry/benchmark_registry.csv`
- batch files under `corpus/batches/`
- small `outline.md` adjustments only if the current structure cannot absorb the paper clusters
- active rows left at `status = triaged`
- `next_action` set concretely, usually `read-batch` or `hold`
- `last_updated` refreshed on touched rows

Do not:
- write paper cards
- write draft prose
- force uncertain labels

## Stage 2: Deep Read And Write Paper Cards

Goal:
- convert selected papers into evidence-bearing cards
- map each card to the survey outline
- identify comparison targets and unresolved ambiguity

Use:
- `benchmark.md`
- `outline.md`
- the relevant file under `corpus/batches/`
- `corpus/registry/benchmark_registry.csv`
- `template/paper_card_template.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`
- `.codex/skills/paper-card-batch-reader`

Read at least:
- abstract
- introduction
- benchmark or environment setup
- interface and interaction design
- evaluation protocol
- main results
- limitations

Expected outputs:
- one card per paper under `paper_cards/` unless the registry points elsewhere
- synced registry rows
- stronger outline anchors in `outline.md`
- touched rows moved to `status = card-draft`
- `next_action` updated to `review-card` unless the card already passes the review gate in the same run

Do not:
- merge multiple papers into one note
- blur direct evidence and interpretation
- draft polished survey prose yet
- mark cards `card-reviewed` before the eval gate is actually run

## Stage 3: Review Gate And Draft

Goal:
- review card quality against the active eval documents
- compare cards inside a cluster
- draft only the sections that already have enough support

Use:
- `paper_cards/`
- `outline.md`
- `corpus/registry/benchmark_registry.csv`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`

Expected outputs:
- each touched card rated `strong`, `usable`, or `weak`
- only `strong` or `usable` cards promoted to `status = card-reviewed`
- weak cards left at `status = card-draft` with `next_action = review-card`
- comparative drafting notes or section drafts built only from reviewed cards
- explicit outline updates when structure changes

Do not:
- write unsupported synthesis
- generalize from one weak card
- hide uncertainty
- treat `finalized` as the default post-review status; use it only for cards that are stable enough to cite repeatedly during writing

## Recommended Rhythm

1. Run Stage 1 on the full benchmark list or on newly added papers.
2. Choose one batch, usually `batch_01`, for Stage 2.
3. Finish cards for that batch before moving on.
4. Run the batch review gate using `evals/quality_rubric.md` and `evals/batch_review_checklist.md`.
5. Promote passing cards to `card-reviewed` and leave weak cards at `card-draft`.
6. Draft only the outline sections that now have enough reviewed support.
