---
name: survey-section-writer
description: "Use when drafting or revising survey sections from the current outline and writing plan: discuss and refine `writing.md` without editing it directly, mine support from reviewed paper cards, and provide candidate survey prose in the dialogue for human review. Trigger on requests like 'draft Section 3.1', 'revise the taxonomy writing plan', 'turn this subsection into script prose', or 'rewrite the lead-in with stronger evidence'."
---

# Survey Section Writer

## Overview

Use this skill for Stages 3 to 5 work: section drafting, cross-section revision, and manuscript stabilization.

This repo treats `writing.md` as the active thinking surface and `script.md` as the copy-ready handoff. Do not jump straight to polished prose. First align the section plan in `writing.md`, then pull evidence from reviewed cards, and only then propose draft or revised prose.

Do not directly edit `writing.md`. Always present suggested `writing.md` changes and candidate section prose in the dialogue so the user can review them manually first.

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
- the user wants to improve the narrative logic in `writing.md` before writing prose
- the user wants to turn notes in `writing.md` into copy-ready paragraphs in `script.md`
- the user wants cross-paper synthesis from existing cards rather than new card creation
- the user wants to tighten citations, comparisons, or evidence support in drafted prose

## Do Not Use This Skill When

- triaging unread papers
- creating first-pass paper cards for a batch
- auditing a single card against the full paper
- drafting claims mainly from papers that are still `triaged` or `card-draft`

Use `.codex/skills/benchmark-triage` for Stage 1 queue building.
Use `.codex/skills/paper-card-batch-reader` for Stage 2 card creation.
Use `.codex/skills/paper-card-auditor` for one-paper verification.

## Core Rule: Writing Surface First

Default to a discussion-first move centered on `writing.md`.

Never modify `writing.md` directly. The job is to inspect the current plan, identify what should change, and present a suggested revision in the dialogue.

Before touching `script.md`, make sure `writing.md` captures:

- the target section or subsection
- the section goal in the language of `outline.md`
- the claim ladder or paragraph order
- the anchor papers and comparison papers
- the evidence type each paragraph needs
- open gaps, uncertainty, or placeholder claims

If the current plan is underspecified or internally inconsistent, explain the problem and propose a better `writing.md` version in the dialogue first. Do not let `script.md` outrun the planning surface.

## Evidence Eligibility

- Prefer cards with `status = card-reviewed` or `finalized`.
- Treat `corpus/registry/benchmark_registry.csv` as the routing layer for section fit, status, and card paths.
- Use `paper_cards/` as the evidence layer.
- Use `writing.md` for narrative decisions and `script.md` for reader-facing prose.
- If a useful paper is only `triaged` or `card-draft`, either keep it out of copy-ready prose or mark the script sentence as a placeholder/open question.

## Paper Material Limits

- Let `writing.md` set the argumentative line. Use specific papers to supply evidence for that line, not to redirect the section into paper-by-paper summaries.
- Include only the paper methods, settings, or result details needed to support the current claim. Avoid extended paper-specific narration unless the section explicitly analyzes that design choice.

## Card Mining Order

Start narrow. Do not open large swaths of the corpus without a section reason.

1. Identify the target section in `outline.md` and the current story in `writing.md`.
2. Use the registry to shortlist papers whose `outline_sections` and `status` match the target section.
3. Use `corpus/batches/batch_index.md` to find the batch clusters most likely to support the section.
4. Open only the highest-leverage cards first, usually anchors plus `2-5` comparison cards.
5. Inside each card, look first at:
   - Section 2 for survey positioning
   - Section 5 for interaction details
   - Section 6 for evaluation details
   - Section 8 for findings and failure modes
   - Section 9 for section-specific best use
   - Section 10 for comparison targets
   - Section 11.1 for direct paper-supported facts
   - Section 11.2 for our synthesis
   - Section 11.3 for unresolved uncertainty

## Workflow

1. Restate the target section in terms of `outline.md` and identify the live drafting problem in `writing.md`.
2. Discuss and refine `writing.md` first in the dialogue:
   - clarify the section objective
   - choose the paragraph sequence
   - assign anchor and comparison papers
   - record thin spots or claims that still need evidence
3. Build a compact evidence set from the registry and reviewed cards. Prefer breadth of contrast over dumping many redundant citations.
4. Provide a recommended `writing.md` revision in the response, with usable structure, evidence hooks, and explicit open questions, but do not edit the file.
5. Only after the plan is stable, provide candidate `script.md` prose in the dialogue.
6. Keep the proposed prose aligned to the latest `writing.md` wording, structure, and section boundaries.
7. If the evidence is not yet strong enough for copy-ready prose, stop at the `writing.md` suggestion layer and say what is still missing.

## Drafting Rules For `script.md`

- Write from the current `outline.md` and the updated `writing.md`, not from memory.
- Use inline paper IDs as citations, for example `(SmartPlay; GTBench)`.
- Keep direct paper-supported facts separate in your own reasoning from cross-paper synthesis, even if both appear in the final prose.
- Favor a small number of well-chosen citations over long citation piles with no argumentative role.
- Preserve the user's intended story and framing when `writing.md` already makes a deliberate choice.
- Present candidate prose in the dialogue for review instead of directly editing `script.md`, unless the user explicitly asks for a file edit later.
- Revise existing prose when possible instead of appending parallel versions of the same paragraph.

## Good `writing.md` Suggestions

A strong writing-plan suggestion usually adds or sharpens:

- a section goal sentence
- the intended progression of paragraphs
- which papers anchor each paragraph
- what comparison or tension each paragraph should surface
- which claims are settled versus still open

## Good `script.md` Suggestions

A strong script suggestion is:

- traceable to the current `writing.md`
- supported by reviewed evidence
- specific about benchmark design, interface, or empirical failure modes
- already in copy-ready survey prose rather than card-style notes

## Do Not

- do not treat `script.md` as the first drafting surface
- do not edit `writing.md` directly
- do not write polished prose from unread or weakly supported cards
- do not collapse direct evidence and our interpretation into one unsupported claim
- do not cite a paper for a role its card explicitly marks as uncertain
- do not search the entire corpus when the registry and batch structure already narrow the section
- do not silently apply wording changes to `writing.md`; always show them in the dialogue for review first

## Handoff

At the end of a drafting pass, report:

- which section or subsection was addressed
- what `writing.md` revision you recommend, and how the plan becomes clearer
- which cards supplied the main support
- what candidate prose you recommend for `script.md`, or why the section still has evidence gaps
