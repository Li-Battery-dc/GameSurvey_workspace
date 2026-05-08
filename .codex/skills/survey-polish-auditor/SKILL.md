---
name: survey-polish-auditor
description: "Use when auditing or polishing this game-benchmark survey across the full argument chain: verify `writing.md` claims against reviewed/finalized paper cards and, when needed, authoritative paper text; check whether evidence supports the planned thesis or should be replaced by stronger papers; compare `script.md` prose against `writing.md` for drift, flow, concision, academic rigor, and citation placement; audit whether script citations match the claim type and the evidence used in `writing.md`. Trigger on requests to polish, refine, review, or check survey sections, validate argument-evidence alignment, audit `writing.md` to `script.md` consistency, or improve script citations. Also trigger on Chinese requests such as 润色, 论点论据检查, 引用合理性检查, or 写作思路与正文一致性检查. Do not use for first-pass paper card creation, standalone single-card finalization, or Overleaf/BibTeX citation normalization unless explicitly requested."
---

# Survey Polish Auditor

## Overview

Use this skill to audit the survey as an argument chain: paper evidence -> `writing.md` plan -> `script.md` prose -> `script.md` citations. The goal is to catch factual errors, weak support, plan-prose drift, citation mismatch, and inflated or uneven academic wording before manuscript handoff.

This skill is primarily an audit and polishing workflow. It may revise `script.md` only when the user asks for file edits or copy-ready polishing. It must not edit `writing.md`; propose targeted `writing.md` changes in the conversation.

## Open These Files First

- `outline.md`
- `writing.md`
- `script.md`
- `template/registry_schema.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md`
- `benchmark.md` as backstop context only
- relevant reviewed or finalized cards under `paper_cards/`
- relevant batch files under `corpus/batches/` when section support depends on a cluster
- `template/paper_card_template.md` when interpreting card fields or evidence sections
- `.codex/skills/survey-polish-auditor/references/polish_rubric.md`

If a factual claim is high-impact, suspicious, or only weakly resolved by a card, open the authoritative paper text or PDF linked by the registry. Prefer official PDFs and do not use search-engine detours unless the registry link is broken.

## Evidence Rules

- Treat paper cards as the first evidence layer, and authoritative paper text as the tie-breaker for risky or disputed claims.
- Prefer `status = finalized`; use `card-reviewed` when the uncertainty does not affect the claim.
- Do not rely on `benchmark.md`, registry rows, or batch summaries as the only evidence for paper-specific claims.
- Keep paper-supported facts separate from survey synthesis. A synthesis claim may cite papers that support its components, but do not imply the cited papers directly state the synthesis.
- Do not recommend `triaged` or `card-draft` papers for copy-ready citation unless the sentence is explicitly marked as a placeholder or evidence gap.

## Workflow

1. Scope the audit target.
   - Identify the section, subsection, paragraph range, or claim cluster in `outline.md`, `writing.md`, and `script.md`.
   - If the user does not specify a narrow target, start with the section that appears most recently edited or most explicitly named.

2. Build the planned argument map from `writing.md`.
   - Extract the intended thesis, paragraph sequence, key claims, named paper IDs, and any stated boundaries.
   - Mark which claims are factual, comparative, evaluative, methodological, or pure survey framing.

3. Build the actual prose map from `script.md`.
   - Match script paragraphs to the `writing.md` plan.
   - Note additions, omissions, reordered logic, overclaims, repeated ideas, terminology drift, and citation differences.

4. Route and mine evidence.
   - Use the registry to confirm paper status, section fit, card path, and survey role.
   - Open anchor cards first, then representative or contrast cards needed for the paragraph.
   - Use card Sections 5, 6, 8, 9, 10, and 11 for interaction design, evaluation design, empirical findings, survey-use claims, comparisons, and uncertainty.
   - Open full paper text only when the card is ambiguous, the claim is central, or the script/writing wording appears stronger than the card support.

5. Audit `writing.md` claims.
   - Check factual accuracy against the card and, when needed, the paper.
   - Decide whether each cited or named paper actually supports the intended role.
   - Recommend stronger evidence only when it is more direct, higher-status, more section-aligned, or better at supporting the exact claim.
   - Preserve the user's narrative when it is supportable; do not replace it with a paper-by-paper catalog.

6. Audit `script.md` prose.
   - Check whether the script follows the `writing.md` claim order and boundaries.
   - Tighten inflated, vague, repetitive, or overly absolute language.
   - Keep the prose synthetic and academic: claims should be precise, bounded, and linked to benchmark design, interface, metrics, or empirical behavior.
   - Avoid adding long paper summaries unless the paragraph's argument needs a concrete example.

7. Audit `script.md` citations.
   - Use inline paper IDs in script prose, for example `(SmartPlay; GTBench)`.
   - Add citations for specific paper facts, benchmark-design claims, empirical claims, comparative claims, and field-pattern claims.
   - Do not force citations onto roadmap sentences, local definitions, or clearly original survey framing unless they depend on particular papers.
   - Prefer a small number of high-fit citations over long citation piles.
   - Ensure each citation also appears in, or is consistent with, the paper support named in `writing.md`; if not, flag the divergence.

8. Produce findings before rewrites.
   - Start with the highest-risk factual or evidence-mismatch issues.
   - Then report plan-prose drift, citation issues, and style polish opportunities.
   - Provide exact replacement wording for important script sentences or paragraphs.
   - Edit `script.md` only if the user asked for direct polishing edits; otherwise keep changes as proposed replacements.

## Output Standard

Use this order:

1. Findings: severity, location, issue, evidence checked, and recommended action.
2. Evidence map: claim -> current support -> support grade -> stronger support if any.
3. Script alignment: whether the prose follows `writing.md`, with concrete drift points.
4. Citation audit: add/replace/remove/keep recommendations and why.
5. Proposed revisions or applied edits.
6. Residual uncertainty: missing cards, full-paper checks, or claims needing user decision.

For direct file edits, end with a concise file summary and verification performed.

## Do Not

- Do not edit `writing.md` directly.
- Do not treat a polished sentence as valid until its substantive claim is evidence-checked.
- Do not cite papers merely because their names are nearby in `writing.md`.
- Do not smooth over uncertainty by weakening the citation audit; mark unsupported claims clearly.
- Do not turn the survey into a list of paper summaries when the user's plan is synthetic.
- Do not alter `overleaf_paper/` unless the user explicitly approves an exact Overleaf edit scope.
