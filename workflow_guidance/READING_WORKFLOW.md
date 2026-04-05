# Reading Workflow

This repository uses a three-stage reading and review pipeline. Because `benchmark.md` now holds a long paper list, the default operating mode is incremental: keep the registry and batch index as the active control plane, and treat the raw benchmark list as intake material.

## Stage 1: Triage And Batch

Goal:
- turn the benchmark list into a durable rolling reading queue
- assign priority and queue position
- create many small comparison-friendly reading batches
- stabilize the outline before deep reading

Use:
- `benchmark.md`
- `outline.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md` if it exists
- `template/registry_schema.md`
- `.codex/skills/benchmark-triage`

Read only:
- title
- abstract
- introduction-level framing
- project page or code page only when needed to clarify benchmark scope

Long-list mode:
- On the first import pass, you may scan the full `benchmark.md`.
- After the registry exists, do not reread the full benchmark list for routine triage. Work from a registry window plus only the new or stale entries you need to refresh.
- Process `20-30` papers per triage pass by default. Go above `30` only when importing a fresh block of new papers.
- For a corpus around `60+` papers, expect roughly `8-15` reading batches overall rather than `3-5` large batches.
- Keep deep-reading batches small: normally `4-6` papers, at most `8` if they are tightly coupled.
- Maintain a short `corpus/batches/batch_index.md` so the agent can see the queue without opening every batch file.

Expected outputs:
- updated `corpus/registry/benchmark_registry.csv`
- updated `corpus/batches/batch_index.md`
- batch files under `corpus/batches/`
- small `outline.md` adjustments only if the current structure cannot absorb the paper clusters
- active rows left at `status = triaged`
- readable title-aligned `paper_id` values in PascalCase or acronym-preserving CamelCase
- `queue_tier` set to `now`, `next`, `later`, or `hold`
- `triage_round` incremented when a paper is reconsidered in a later pass
- `paper_card_path` reserved as `paper_cards/{batch_id}/{paper_id}.md` once a batch is assigned
- `next_action` set concretely, usually `read-batch`, `deep-read`, or `hold`
- `last_updated` refreshed on touched rows

Do not:
- write paper cards
- write draft prose
- force uncertain labels
- try to classify all `60+` papers in one context window when the registry already exists

## Stage 2: Deep Read And Write Paper Cards

Goal:
- convert selected papers into evidence-bearing cards
- map each card to the survey outline
- identify comparison targets and unresolved ambiguity

Use:
- `benchmark.md` as backstop context only
- `outline.md`
- `corpus/batches/batch_index.md` if it exists
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

Long-list mode:
- Never load the full benchmark list plus multiple reading batches into one pass.
- Process one batch at a time, normally `4-6` papers.
- Keep comparison spillover small: at most `1-2` nearby cards beyond the active batch unless the user asks for a broader synthesis.
- If `paper_link` is an abstract page or landing page rather than a PDF, resolve the official PDF URL before reading. For arXiv, prefer the matching `/pdf/...pdf` target.

Expected outputs:
- one card per paper under `paper_cards/{batch_id}/` unless the registry points elsewhere
- synced registry rows
- stronger outline anchors in `outline.md`
- touched rows moved to `status = card-draft`
- `next_action` updated to `review-card` unless the card already passes the review gate in the same run
- `queue_tier` revised only when the deep read materially changes urgency
- `paper_card_path` aligned with the row's `batch_id` and readable `paper_id`

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
- `corpus/batches/batch_index.md` when drafting decisions depend on queue state
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

1. Import or refresh the registry from `benchmark.md`.
2. Triage only the next `20-30` papers that are new, stale, or still ambiguous.
3. Keep `2-3` `queue_tier = now` batches and a larger `next` queue in `corpus/batches/batch_index.md`.
4. Choose one batch, usually the first `now` batch, for Stage 2.
5. Finish cards for that batch before moving on.
6. Run the batch review gate using `evals/quality_rubric.md` and `evals/batch_review_checklist.md`.
7. Promote passing cards to `card-reviewed` and leave weak cards at `card-draft`.
8. Draft only the outline sections that now have enough reviewed support.
