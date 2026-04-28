---
name: survey-section-writer
description: "Use when drafting or revising survey sections from the current outline and writing plan: follow the existing `writing.md` structure, mine evidence from reviewed or finalized paper cards, and produce copy-ready `script.md` prose or targeted revision suggestions. Trigger on requests like 'draft Section 3.1', 'revise this subsection', 'turn this writing.md subsection into script prose', or 'rewrite the lead-in with stronger paper-card evidence'."
---

# Survey Section Writer

## Overview

Use this skill for Stages 3 to 5 work: section drafting, cross-section revision, and manuscript stabilization.

This repo treats `writing.md` as the active section plan and `script.md` as the copy-ready handoff. Do not reopen a `writing.md` update discussion by default. First follow the current `writing.md` structure, paragraph order, section boundaries, and intended claims. Then mine paper-card evidence and draft or revise prose.

Do not directly edit `writing.md`. Suggest `writing.md` changes only when the user asks for planning help, the current plan is missing a necessary structure, or the card evidence contradicts the plan. Keep those suggestions targeted and separate from copy-ready prose.

## Open These Files First

- `outline.md`
- `writing.md`
- `script.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md`
- `benchmark.md` as backstop context only
- the relevant batch file under `corpus/batches/` when section support depends on a specific evidence cluster
- the relevant reviewed or finalized cards under `paper_cards/`
- `template/paper_card_template.md` only if a card field needs interpretation

## Use This Skill When

- the user wants to draft or revise one section or subsection of the survey
- the user wants to turn an existing `writing.md` plan into copy-ready prose
- the user wants to improve existing `script.md` prose while preserving the current section structure
- the user wants cross-paper synthesis from existing cards rather than new card creation
- the user wants tighter citations, comparisons, or paper-supported evidence in drafted prose

## Do Not Use This Skill When

- triaging unread papers
- creating first-pass paper cards for a batch
- auditing a single card against the full paper
- drafting claims mainly from papers that are still `triaged` or `card-draft`

Use `.codex/skills/benchmark-triage` for Stage 1 queue building.
Use `.codex/skills/paper-card-batch-reader` for Stage 2 card creation.
Use `.codex/skills/paper-card-auditor` for one-paper verification.

## Core Rule: Follow The Writing Structure

Treat the current `writing.md` section as the governing scaffold for drafting.

Before drafting, identify:

- the target section or subsection in `outline.md`
- the matching heading and paragraph plan in `writing.md`
- the section goal and intended claim sequence
- the anchor papers, comparison papers, and open gaps already named there
- the boundary of the requested edit in `script.md`

Preserve that scaffold unless there is a clear reason not to. Do not invent a parallel organization, change the section's purpose, or expand beyond the requested boundary just because the cards contain interesting extra material.

If the plan is thin but usable, draft within it and state the assumption briefly. If the plan is internally inconsistent, conflicts with `outline.md`, or cannot be supported by reviewed cards, stop and propose the smallest necessary `writing.md` adjustment before drafting.

## Evidence Eligibility

- Prefer cards with `status = card-reviewed` or `finalized`.
- Treat `corpus/registry/benchmark_registry.csv` as the routing layer for section fit, status, and card paths.
- Use `paper_cards/` as the evidence layer for substantive claims.
- Do not use `benchmark.md`, registry rows, or batch summaries as sole evidence for paper-specific claims; use them to find cards.
- Use `writing.md` for narrative decisions and `script.md` for reader-facing prose.
- If a useful paper is only `triaged` or `card-draft`, either keep it out of copy-ready prose or mark the sentence as a placeholder/open question.

Every nontrivial factual or comparative claim in drafted prose should be traceable to at least one opened paper card. Keep paper-supported facts separate in your reasoning from survey synthesis:

- use card Section 11.1 for direct paper-supported facts
- use card Section 11.2 for our synthesis
- use card Section 11.3 for unresolved uncertainty
- use card Sections 5, 6, 8, 9, and 10 for interaction details, evaluation details, findings, best section use, and comparison targets

## Paper Material Limits

- Let `writing.md` set the argumentative line. Use specific papers to support that line, not to redirect the section into paper-by-paper summaries.
- Include only the paper methods, settings, results, or failure modes needed to support the current claim.
- Avoid extended paper-specific narration unless the section explicitly analyzes that design choice.

## Card Mining Order

Start narrow, but always read cards before making substantive claims.

1. Identify the target section in `outline.md` and the current story in `writing.md`.
2. Use the registry to shortlist papers whose `outline_sections`, `status`, `survey_role`, and `paper_card_path` match the target section.
3. Use `corpus/batches/batch_index.md` to find the batch clusters most likely to support the section.
4. Open the highest-leverage cards first: anchors, direct representatives, and `2-5` comparison cards.
5. Extract an evidence map before drafting: claim, supporting paper IDs, card sections used, and uncertainty.
6. Open more cards only when a paragraph needs contrast, coverage, or a missing citation.

## Workflow

1. Locate the requested section in `outline.md`, `writing.md`, and `script.md`.
2. Treat the current `writing.md` structure as binding: section goal, paragraph order, terminology, and scope.
3. Build a compact evidence set from the registry and reviewed or finalized paper cards. Prefer breadth of contrast over redundant citation piles.
4. Draft or revise prose according to the existing `writing.md` plan, using inline paper IDs as citations.
5. Suggest `writing.md` changes only when needed:
   - the user explicitly asks for plan revision
   - the plan is missing a necessary section structure
   - the requested prose would conflict with `outline.md`
   - opened paper cards show the planned claim is unsupported or uncertain
6. If `writing.md` changes are needed, present a concise proposed delta in the dialogue and keep it separate from copy-ready prose.
7. If evidence is not strong enough for copy-ready prose, stop at an evidence-gap report and state which cards or card audits are missing.

## Drafting Rules For `script.md`

- Write from the current `outline.md` and `writing.md`, not from memory.
- When the user asks for copy-ready prose or a file edit, write or revise `script.md`; otherwise provide candidate prose in the dialogue.
- Use inline paper IDs as citations, for example `(SmartPlay; GTBench)`.
- Confirm every citation is doing argumentative work and is supported by an opened card.
- Favor a small number of well-chosen citations over long citation piles with no argumentative role.
- Preserve the user's intended story and framing when `writing.md` already makes a deliberate choice.
- Revise existing prose when possible instead of appending parallel versions of the same paragraph.
- Mark unsupported claims as open questions rather than smoothing over missing evidence.

## Good `writing.md` Suggestions

Only suggest `writing.md` changes when they are necessary or requested. A strong suggestion is short and usually adds or sharpens:

- a section goal sentence
- the intended progression of paragraphs
- which papers anchor each paragraph
- what comparison or tension each paragraph should surface
- which claims are settled versus still open

## Good `script.md` Prose

Strong script prose is:

- traceable to the current `writing.md`
- supported by reviewed or finalized cards
- specific about benchmark design, interface, metrics, or empirical failure modes
- synthetic rather than paper-by-paper
- already in copy-ready survey prose rather than card-style notes

## Do Not

- do not turn every drafting request into a `writing.md` revision discussion
- do not edit `writing.md` directly
- do not treat `script.md` as independent from the current `writing.md` structure
- do not write polished prose from unread, weakly supported, or draft-only cards
- do not use registry rows or `benchmark.md` as evidence substitutes for paper cards
- do not collapse direct evidence and our interpretation into one unsupported claim
- do not cite a paper for a role its card explicitly marks as uncertain
- do not search the entire corpus when the registry and batch structure already narrow the section

## Handoff

At the end of a drafting pass, report:

- which section or subsection was addressed
- how the draft followed the current `writing.md` structure, or what minimal plan change was needed
- which cards supplied the main support
- what `script.md` prose was produced or revised, or why the section still has evidence gaps
