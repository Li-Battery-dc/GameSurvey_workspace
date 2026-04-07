---
name: benchmark-triage
description: "Use when triaging a game benchmark literature list for this survey: assign batches, set reading priority or importance, update corpus/registry/benchmark_registry.csv, or decide what to read next from benchmark.md, outline.md, and the current writing needs in writing.md. Trigger on requests like 'first-pass screening', 'assign batches', 'set priority', or 'choose the first reading batch'."
---

# Benchmark Triage

## Overview

Use this skill for Stage 1 work only. Start from `benchmark.md`, `outline.md`, and `writing.md`, then perform an abstract and introduction-level pass that turns the long paper list into a stable reading queue for later review and drafting.

## Open These Files First

- `benchmark.md`
- `outline.md`
- `writing.md`
- `corpus/registry/benchmark_registry.csv` if it already exists
- `corpus/batches/batch_index.md` if it already exists
- `template/registry_schema.md`
- `assets/benchmark_registry_template.csv` if the registry needs to be initialized
- `assets/batch_template.md` when writing `corpus/batches/batch_XX.md`
- `assets/batch_index_template.md` when writing `corpus/batches/batch_index.md`
- `references/triage_labels.md` for priority, queue, role, and check-status labels

## Scope

Read only enough to place the paper:
- title
- abstract
- introduction or benchmark overview
- code or project page only when it clarifies environment type or benchmark scope

Do not full-read methods or results unless placement is impossible without them.

## Identifier Rule

- `paper_id` must stay readable and title-aligned.
- Use PascalCase or acronym-preserving CamelCase such as `SmartPlay`, `GameplayQA`, `CKArena`, `GTBench`, or `PokeAgentChallenge`.
- Do not introduce new lowercase slug-style IDs.

## Long-List Mode

Use long-list mode whenever `benchmark.md` is around `50+` papers.

- Read the full benchmark list when initializing the registry or importing genuinely new papers.
- Once the registry exists, default to a working window of `20-30` papers per triage pass.
- Use the registry and `corpus/batches/batch_index.md` as the active queue; do not reread the full benchmark list for routine reshuffling.
- Maintain many small reading batches instead of a few large ones. For a corpus around `60+` papers, expect roughly `8-15` reading batches overall.
- Keep deep-reading batches small: normally `4-6` papers, at most `8` if the cluster is unusually tight.

## Workflow

1. Read `benchmark.md` and `outline.md` before touching the registry.
2. Preserve the existing registry schema when `corpus/registry/benchmark_registry.csv` already exists. Only initialize from the asset template if the file is missing.
3. For each paper in the active window, fill or revise the Stage 1 fields conservatively:
   - `paper_id`
   - `status`
   - `priority`
   - `queue_tier`
   - `triage_round`
   - `reading_depth`
   - `batch_id`
   - `batch_theme`
   - `batch_order`
   - `outline_sections`
   - `survey_role`
   - `paper_card_path`
   - `triage_note`
   - `check_status`
   - `last_updated`
4. Keep Stage 1 rows at `status = triaged`.
5. Use `queue_tier` to control scale:
   - `now`: next `1-3` batches to read soon
   - `next`: the near queue after `now`
   - `later`: backlog that should stay visible but not active yet
   - `hold`: intentionally parked rows
6. Set `triage_round = 1` on first placement and increment it when a later pass materially changes urgency, batching, or outline placement.
7. Set `check_status = unchecked` for newly touched rows. Use `queue_tier`, `batch_id`, and explicit hold decisions to express what should happen next.
8. When a paper has a `batch_id`, reserve `paper_card_path` as `paper_cards/{batch_id}/{paper_id}.md`.
9. Create or update `corpus/batches/batch_index.md` plus any touched `corpus/batches/batch_XX.md` files.
10. Only adjust `outline.md` when the new batch structure reveals a missing cluster or a clearer narrative ordering.

## Priority Rules

- `P0`: anchor paper, milestone benchmark, or high-leverage bridge that stabilizes the outline
- `P1`: representative paper that strengthens a section or comparison theme
- `P2`: useful but non-urgent, redundant, or mostly confirmatory
- `P3`: peripheral, weak fit, or worth keeping only as background

If the project is already using only `P0` or `P1` or `P2`, reserve `P3` for clear backlog cases and do not up-convert uncertain papers to `P0`.

## Batch Rules

- Prefer `4-6` papers per deep-reading batch.
- Keep only `2-3` batches at `queue_tier = now`.
- Make the first `now` batch maximize outline stabilization:
  - include foundational or anchor papers
  - cover more than one narrative level when useful
  - avoid filling the first batch with edge cases
- Reuse existing `batch_id` values when the grouping still makes sense.
- Use short, interpretable `batch_theme` slugs.
- Keep `corpus/batches/batch_index.md` short enough to inspect at a glance.

## Output Standard

A good Stage 1 pass leaves every touched paper with:
- a stable, readable `paper_id`
- `status = triaged`
- a priority
- a `queue_tier`
- a `triage_round`
- a tentative batch or an explicit hold decision
- `check_status = unchecked`
- at least one outline landing point
- an explicit uncertainty marker when placement is fuzzy
- a default future card path of `paper_cards/{batch_id}/{paper_id}.md` once batching is known

## Do Not

- do not write full paper cards
- do not draft section prose
- do not hide ambiguity behind overconfident labels
- do not reintroduce legacy taxonomy columns from older schema drafts
- do not keep rereading the full benchmark list when the registry already captures the active queue

## Handoff

At the end of a triage pass, report:
- how many papers were processed in this window
- which batch should be read next
- which papers remain ambiguous
- whether `outline.md` needs structural change before Stage 2
