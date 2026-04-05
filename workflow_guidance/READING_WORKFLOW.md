# Reading Workflow

This repository uses a two-skill reading pipeline plus a light drafting phase.

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

Do not:
- merge multiple papers into one note
- blur direct evidence and interpretation
- draft polished survey prose yet

## Stage 3: Review And Draft

Goal:
- review card quality
- compare cards inside a cluster
- draft only the sections that already have enough support

Use:
- `paper_cards/`
- `outline.md`
- `corpus/registry/benchmark_registry.csv`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`

Expected outputs:
- corrected weak cards
- comparative drafting notes or section drafts
- explicit outline updates when structure changes

Do not:
- write unsupported synthesis
- generalize from one weak card
- hide uncertainty

## Recommended Rhythm

1. Run Stage 1 on the full benchmark list or on newly added papers.
2. Choose one batch, usually `batch_01`, for Stage 2.
3. Finish cards for that batch before moving on.
4. Review the batch using the QA checklist.
5. Draft only the outline sections that now have enough support.
