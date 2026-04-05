---
name: benchmark-triage
description: "Use when triaging a game benchmark literature list for this survey: assign batches, set reading priority or importance, update corpus/registry/benchmark_registry.csv, or decide what to read next from benchmark.md and outline.md. Trigger on requests like 'first-pass screening', 'assign batches', 'set priority', or 'choose the first reading batch'."
---

# Benchmark Triage

## Overview

Use this skill for Stage 1 work only. Start from `benchmark.md` and `outline.md`, then perform an abstract and introduction-level pass that turns the long paper list into a stable reading queue.

## Open These Files First

- `benchmark.md`
- `outline.md`
- `corpus/registry/benchmark_registry.csv` if it already exists
- `template/registry_schema.md`
- `assets/benchmark_registry_template.csv` if the registry needs to be initialized
- `assets/batch_template.md` when writing `corpus/batches/batch_XX.md`
- `references/triage_labels.md` for priority, stage, and uncertainty labels

## Scope

Read only enough to place the paper:
- title
- abstract
- introduction or benchmark overview
- code or project page only when it clarifies environment type or benchmark scope

Do not full-read methods or results unless placement is impossible without them.

## Workflow

1. Read `benchmark.md` and `outline.md` before touching the registry.
2. Preserve the existing registry schema when `corpus/registry/benchmark_registry.csv` already exists. Only initialize from the asset template if the file is missing.
3. For each paper, fill or revise the Stage 1 fields conservatively:
   - `priority`
   - `reading_depth`
   - `batch_id`
   - `batch_theme`
   - `batch_order`
   - `outline_sections`
   - `survey_role`
   - `triage_note`
   - `next_action`
   - `last_updated`
4. If the registry also carries the broader survey columns from `template/registry_schema.md`, fill them with first-pass labels only:
   - `historical_strand`
   - `narrative_level`
   - `single_or_diverse`
   - `game_type`
   - `purpose_primary`
   - `purpose_secondary`
   - `interface_type`
   - `perception_mode`
   - `action_mode`
   - `evaluation_type`
   - `cluster`
   - `uncertain_flags`
5. Group papers into 3 to 5 batches that help the survey converge, not just papers that look superficially similar.
6. Create or update `corpus/batches/batch_XX.md` files using the asset template.
7. Only adjust `outline.md` when the new batch structure reveals a missing cluster or a clearer narrative ordering.

## Priority Rules

- `P0`: anchor paper, milestone benchmark, or high-leverage bridge that stabilizes the outline
- `P1`: representative paper that strengthens a section or comparison cluster
- `P2`: useful but non-urgent, redundant, or mostly confirmatory
- `P3`: peripheral, weak fit, or worth keeping only as background

If the project is already using only `P0` or `P1` or `P2`, reserve `P3` for clear backlog cases and do not up-convert uncertain papers to `P0`.

## Batch Rules

- Prefer 6 to 12 papers per deep-reading batch.
- Make `batch_01` maximize outline stabilization:
  - include foundational or anchor papers
  - cover more than one narrative level
  - avoid filling the first batch with edge cases
- Reuse existing `batch_id` values when the grouping still makes sense.
- Use short, interpretable `batch_theme` slugs.

## Output Standard

A good Stage 1 pass leaves every paper with:
- a priority
- a tentative batch
- at least one outline landing point
- an explicit uncertainty marker when placement is fuzzy

## Do Not

- do not write full paper cards
- do not draft section prose
- do not hide ambiguity behind overconfident labels
- do not overwrite existing registry columns with a narrower schema

## Handoff

At the end of a triage pass, report:
- which batch should be read next
- which papers remain ambiguous
- whether `outline.md` needs structural change before Stage 2
