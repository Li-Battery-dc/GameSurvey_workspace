---
name: paper-card-auditor
description: "Use when verifying one existing paper card against the full paper and the current survey writing structure: detect hallucinations or unsupported claims, correct the card, tighten outline and writing anchors, and sync the registry for that single paper. Trigger on requests like 'audit this card', 're-read this paper and fix hallucinations', or 'does this paper really support Section 4?'. Do not use for batch review, multi-paper card writing, or section drafting."
---

# Paper Card Auditor

## Overview

Use this skill for single-paper deep verification. The goal is not to score a batch. The goal is to decide whether one paper card is actually trustworthy for the survey's current `outline.md` and `writing.md`, then fix it.

## Use This Skill When

- one existing paper card may contain hallucinations, drift, or unsupported claims
- a card looks too abstract, overconfident, or weakly tied to the full paper
- you need to decide whether one paper really supports a specific survey section or subsection
- you need to correct one paper's `outline_sections`, `survey_role`, or Section 9 survey-use mapping after a deeper read

## Do Not Use This Skill When

- triaging unread papers
- reading a full batch into first-pass cards
- running the batch-level review gate across several papers
- drafting survey prose from multiple reviewed cards

Use `.codex/skills/paper-card-batch-reader` for Stage 2 card creation.
Use the batch review docs only when the user explicitly wants the batch gate.
This skill does not treat `evals/quality_rubric.md` or `evals/batch_review_checklist.md` as the primary standard.

If the target paper has no card yet, prefer `.codex/skills/paper-card-batch-reader` unless the user explicitly wants a one-off single-paper audit pass.

## Open These Files First

- `benchmark.md` as backstop context only
- `outline.md`
- `writing.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `template/paper_card_template.md`
- the existing card for the target paper
- the target paper's registry row
- the relevant batch file only if section support depends on current batch context
- `.codex/skills/paper-card-auditor/references/audit_checklist.md`

## Full-Text Standard

Read the whole paper, not just the abstract and introduction. Minimum full-text coverage:

- abstract and introduction
- benchmark or task or environment setup
- observation, action, and interface details
- evaluation protocol, metrics, baselines, and calibration
- main experiments and headline tables or figures
- discussion, limitations, and threat-to-validity material
- appendices when they resolve interface, metric, or result ambiguity

If the current `paper_link` is only an arXiv `abs` page or another landing page, resolve the authoritative PDF first. Keep this bounded:

- If the link is arXiv `abs`, rewrite it to the matching `pdf` URL.
- If it is an ACL Anthology landing page, prefer the page's `.pdf` URL.
- If it is an OpenReview `forum?id=...` page, try the matching `pdf?id=...` URL. If OpenReview blocks retrieval in the current environment, keep the landing page and record that blocker instead of guessing.
- If it is a DOI, publisher landing page, or project page, look for `citation_pdf_url` or a direct official PDF link on that page. If the page only links onward to an official paper page such as arXiv or proceedings, follow that one hop and resolve the PDF there.
- Prefer a verified official PDF over a landing page, but do not use search-engine detours or unofficial mirrors.
- If the resolved PDF is clearly better, update the registry `paper_link`.

## Audit Priorities

Check the current card in this order:

1. factual accuracy and unsupported claims
2. incorrect or inflated benchmark classification
3. wrong placement in the survey outline or writing plan
4. missing details that make the card unsafe for drafting
5. misleading comparison claims about nearby papers
6. whether the paper is being overused or underused in `writing.md`

## Workflow

1. Identify the target paper, card path, and registry row.
2. Read the current card once before editing. Note which bullets are risky, vague, or suspiciously generic.
3. Read the full paper and capture evidence for the benchmark definition, interface, evaluation, main findings, limitations, and the claims that the current card relies on.
4. Re-audit the card section by section, especially Sections 2 to 11.
5. Fix the card directly when the paper settles the issue. Do not stop at critique if a correction is possible.
6. Move unsupported "facts" out of `11.1` into `11.2` or `11.3`, or delete them if they are not defensible.
7. Tighten survey placement:
   - `Historical stage`
   - `Narrative level(s)`
   - `Most relevant outline section(s)`
   - Section 9 "best use" bullets
   - Section 10 comparison targets
8. Sync the registry row when the audit changes:
   - `paper_link`
   - `status`
   - `priority` only if the paper's actual survey leverage changed
   - `outline_sections`
   - `survey_role`
   - `paper_card_path` if needed
   - `triage_note` if the paper's role or uncertainty changed
   - `last_updated`
9. Update `writing.md` only when the audit materially changes an active section claim, active evidence list, or logged evidence gap.
10. Report the audit outcome clearly: what was wrong, what was fixed, what is still uncertain, and what section use changed.

## Card Correction Rules

- Keep the paper card structure comparable and preserve the current section order.
- Preserve useful extra fields already present in repo cards, such as `Review gate label`, only if they still remain accurate after the audit.
- Prefer narrower and defensible `outline_sections` over broad coverage claims.
- A paper can be a good comparison target without being an anchor.
- If a claim is only cross-paper interpretation, it belongs in `11.2`, not `11.1`.
- If you cannot verify a detail from the full paper, record the gap explicitly in `11.3`.
- Do not let Section 9 turn into generic praise; make each "best use" bullet correspond to a real survey section need.
- Do not keep stale placeholders or vague phrases like `strong case`, `useful benchmark`, or `important for the survey` unless the surrounding sentence says exactly why.

## Status Rules

- Keep `check_status` unchanged unless the user explicitly says a human finished checking the paper.
- If the audit fully repairs the card and the card is reliable for drafting, it may remain `card-reviewed`.
- If the audit reveals material unresolved problems that still block safe use in drafting, downgrade the registry row and the card to `card-draft`.
- Reserve `finalized` for cards that are already stable enough to support repeated citation during writing.

## Output Standard

When responding to the user after an audit, include:

- audit verdict: `clean`, `fixed`, or `still-blocked`
- major corrections, especially removed or rewritten hallucinated claims
- outline and writing impact
- residual uncertainty or recheck targets
- files updated

## Do Not

- do not use batch-level eval labels as the main decision framework
- do not treat abstract-level confidence as enough for a pass
- do not preserve flattering but unsupported survey-relevance claims
- do not draft polished section prose unless the user explicitly asked for writing work
- do not mark the paper human-checked
