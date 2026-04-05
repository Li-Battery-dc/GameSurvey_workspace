---
name: paper-card-batch-reader
description: "Use when deep-reading a selected batch of benchmark papers for this survey: create or revise paper cards, sync corpus/registry/benchmark_registry.csv, or anchor evidence into outline.md. Trigger on requests like 'read batch 01', 'complete cards for these papers', or 'write paper cards for this batch'."
---

# Paper Card Batch Reader

## Overview

Use this skill for Stage 2 work only. Turn selected papers into evidence-bearing paper cards that are ready for later survey writing.

## Open These Files First

- `benchmark.md`
- `outline.md`
- `corpus/registry/benchmark_registry.csv`
- the relevant batch file under `corpus/batches/` when one exists
- `template/paper_card_template.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`
- `references/card_rules.md`
- `assets/paper_card_template.md` only if the root template is missing

## Minimum Reading Scope

Read enough to fill the card reliably:
- abstract
- introduction
- benchmark or task or environment setup
- observation or action or interface details
- evaluation protocol and metrics
- main results, failure modes, and limitations
- appendix only when it resolves setup or metric ambiguity

## Workflow

1. Start from a selected batch file or an explicit paper list.
2. For each paper, follow the card path already stored in the registry. If none exists, default to `paper_cards/{paper_id}.md`.
3. Fill `template/paper_card_template.md` exactly. Preserve the section order so cards stay comparable.
4. Keep section `11.1` to direct paper-supported facts, section `11.2` to our synthesis, and section `11.3` to unresolved uncertainty.
5. Update the registry after each card:
   - `status`
   - `paper_card_path`
   - `priority` if the deep read changes importance
   - `next_action`
   - `last_updated`
6. After finishing the batch, run the checklist in `evals/batch_review_checklist.md` and judge card quality against `evals/quality_rubric.md`.
7. Promote only passing cards to `status = card-reviewed`. Keep weak cards at `status = card-draft` with `next_action = review-card`.
8. Strengthen `outline.md` only by adding clearer anchors or comparison targets. Do not draft long prose here.

## Status Rules

- `triaged`: only Stage 1 placement exists
- `card-draft`: first complete structured card exists
- `card-reviewed`: core fields checked against the paper and ready for synthesis
- `finalized`: stable enough to cite during writing

If you touch legacy rows that still use older status words, normalize them to the current repo vocabulary during the update.

## Evidence Rules

- Quote or paraphrase only what the paper actually supports.
- If a field is unclear, say why it is unclear and what section should be rechecked.
- Prefer concise, comparable statements over long paraphrase.
- Each card needs nearby comparison targets inside the corpus.

## Batch Exit Standard

A good batch leaves behind:
- one card per paper
- registry synced
- confidence and uncertainty explicit
- explicit `strong` / `usable` / `weak` review outcomes
- a short note on which outline sections are now well supported and which are still thin

## Do Not

- do not merge multiple papers into one card
- do not collapse facts and interpretation into the same bullet
- do not write polished survey prose instead of evidence notes
- do not invent taxonomy labels that are not supported by the paper or the current project vocabulary
