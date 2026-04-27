---
name: paper-card-auditor
description: "Use when final-auditing existing paper cards against the authoritative paper and the current survey framework: verify facts, fix hallucinations, validate taxonomy/design-space labels, add writing-support claims for outline.md/writing.md/script.md, and sync the registry to finalized. Supports one-card audits and whole-batch finalization sweeps. Trigger on requests like 'audit this card', 'finalize batch B04', 'check whether this card supports Purpose', or 'verify this paper under the new taxonomy'. Do not use for first-pass card creation, unread-paper triage, or section drafting."
---

# Paper Card Auditor

## Overview

Use this skill for final verification of cards that already exist. The purpose is to make each card safe for repeated citation in the current survey narrative, not to create first-pass cards or draft prose.

Audits may target one paper or an entire batch. In batch mode, process one card at a time and keep only a compact cross-batch summary.

## Boundaries

- Use `paper-card-batch-reader` when cards do not exist yet or the user asks to deep-read a fresh batch into first-pass cards.
- Use `survey-section-writer` when the user asks to draft or rewrite manuscript prose from reviewed/finalized cards.
- Do not edit `writing.md`; report suggested changes or evidence gaps instead. Edit `script.md` only when the user explicitly asks for manuscript edits.

## Open These Files First

- `outline.md`
- `writing.md`
- `script.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md`
- `benchmark.md` as backstop context only
- `template/paper_card_template.md`
- the existing card(s) for the target paper(s)
- the target paper's registry row(s)
- `.codex/skills/paper-card-auditor/references/audit_checklist.md`

For batch audits, also open:

- the relevant `corpus/batches/batch_XX.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`

## Paper Reading Standard

Read the main paper body closely enough to verify the card's factual and survey claims:

- abstract and introduction
- benchmark, task, or environment setup
- observation, action, interface, scaffold, and privilege details
- evaluation protocol, metrics, baselines, calibration, and robustness claims
- main experiments, headline tables or figures, and key failure modes
- limitations, discussion, and threat-to-validity material

Do not default to loading all appendix material. Query appendices selectively only when they resolve a specific ambiguity in setup, metrics, prompts, task lists, baselines, implementation details, or a card claim that depends on appendix evidence. If appendix evidence is needed but too large or inaccessible, record the exact unresolved gap in Section 11.3.

## PDF Resolution Rule

If `paper_link` is not direct full text, resolve the authoritative PDF with bounded steps:

- arXiv `abs` -> matching `pdf` URL
- ACL Anthology landing page -> corresponding `.pdf` URL
- OpenReview `forum?id=...` -> matching `pdf?id=...` URL when accessible
- DOI, publisher, or project page -> one official hop to a direct PDF if the page exposes one

Prefer verified official PDFs over landing pages. Do not use search-engine detours or unofficial mirrors. If a better verified PDF is found, update the registry `paper_link`.

## Audit Priorities

Check in this order:

1. factual accuracy and unsupported or inflated claims
2. current taxonomy and design-space classification
3. writing-framework role under `outline.md`, `writing.md`, and existing `script.md`
4. missing claim-support details needed for Section 0-4 drafting
5. interface, metric, calibration, robustness, and evidence-boundary caveats
6. comparison claims about nearby papers
7. registry/card synchronization and finalization readiness

## Current Framework Checks

Validate the card against the current survey architecture:

- Section 2 survey position: historical stage, L1-L5 benchmark level(s), outline sections, corpus role
- Section 3 design-space coding: Form, Construction, Scope, observation modality, action modality
- Section 4 capability target: rule understanding, strategic reasoning, social intelligence, visual agency, or cross-game/open-ended generalization
- Section 5 interaction paradigm: observation/action channel, scaffold, privileged access, ecological-validity trade-off
- Section 6 evaluation protocol: result metric, process diagnostics, adversarial setup, calibration, robustness, contamination controls
- Section 9 survey use: exact claims this paper can support in Sections 0-4, especially Purpose claims that still need evidence
- Section 11 evidence split: direct paper-supported facts in 11.1, survey synthesis in 11.2, unresolved uncertainty in 11.3

Add or tighten supportable claim information when the card is too generic. Each Section 9 bullet should name the paper's concrete argumentative use, not merely say it is "useful" or "important."

## Workflow

1. Identify target paper(s), card path(s), registry row(s), and batch context if applicable.
2. Read each current card before editing. Mark risky, vague, generic, or suspiciously broad claims.
3. Resolve the authoritative PDF if needed.
4. Read the main paper body and targeted appendix material only when necessary.
5. Re-audit the card sections listed in Current Framework Checks.
6. Fix the card directly when evidence settles the issue. Move unsupported direct claims out of 11.1, downgrade them to 11.2 or 11.3, or delete them.
7. Tighten taxonomy placement and writing support:
   - historical stage
   - L1-L5 benchmark level(s)
   - Form, Construction, Scope, observation modality, action modality
   - Section 9 best-use bullets
   - Section 10 comparison targets
8. Sync the registry row:
   - `paper_link` when a better official PDF is verified
   - `status`
   - `priority` only if the paper's real survey leverage changed
   - `outline_sections`
   - `survey_role`
   - `paper_card_path` if needed
   - `triage_note` when role, caveat, or uncertainty changed
   - `last_updated`
9. Sync the card metadata and Section 13 with the registry row.
10. Report unsafe existing `script.md` claims if the audit affects already-drafted prose. Do not rewrite prose unless explicitly asked.

## Batch Audit Mode

When the target is a whole batch:

- Use the batch file and registry `batch_order` as the processing order.
- Do not load every paper PDF, appendix, and card into context at once.
- Audit and finalize one paper at a time, then keep a compact running table of `finalized`, `fixed`, and `blocked` cards.
- Open nearby cards only for concrete comparison questions, normally `1-3` at a time.
- After the batch, summarize common taxonomy corrections, writing-support gains, remaining blockers, and any registry rows not promoted.
- Update `corpus/batches/batch_index.md` only if the batch's next step or status text becomes stale.

## Status Rules

- Set `status = finalized` in both the registry and card when the audit verifies the card against the paper and the current writing framework.
- Keep `status = card-reviewed` only when the card is mostly reliable but still needs a bounded recheck before repeated citation.
- Downgrade or keep `status = card-draft` when material unresolved problems block safe drafting.
- Keep `check_status` unchanged unless the user explicitly says a human completed the manual check.
- Use the current date in `YYYY-MM-DD` for `last_updated`.

## Card Correction Rules

- Preserve the repo card structure and section order.
- Preserve useful extra fields such as `Review gate label` when still accurate.
- Prefer narrow, defensible `outline_sections` over broad coverage claims.
- Treat a paper as `contrast` when it mainly sharpens a boundary or caveat, even if it is technically interesting.
- Put cross-paper interpretation in 11.2, not 11.1.
- Put unverified or appendix-dependent uncertainty in 11.3.
- Remove stale placeholders and vague praise unless the sentence states exactly what claim the paper supports.

## Output Standard

After an audit, report:

- verdict: `finalized`, `fixed-not-final`, or `blocked`
- major factual, taxonomy, or writing-support corrections
- registry/status changes
- impact on `outline.md`, `writing.md`, and `script.md`
- residual uncertainty or appendix recheck targets
- files updated

For batch audits, include counts and paper IDs for finalized, fixed-not-final, and blocked cards.

## Do Not

- do not create first-pass paper cards
- do not treat abstract-level confidence as enough for finalization
- do not preserve unsupported survey-relevance claims
- do not read all appendices by default
- do not silently edit `writing.md`
- do not mark `check_status = checked` unless the user explicitly asks
- do not draft polished section prose unless the user explicitly asks for writing work
