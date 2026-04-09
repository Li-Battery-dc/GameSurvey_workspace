---
name: paper-card-batch-reader
description: "Use when deep-reading a selected batch of benchmark papers for this survey: create or revise paper cards, sync corpus/registry/benchmark_registry.csv, or anchor evidence into outline.md and writing.md. Trigger on requests like 'read batch 01', 'complete cards for these papers', or 'write paper cards for this batch'."
---

# Paper Card Batch Reader

## Overview

Use this skill for Stage 2 work only. Turn selected papers into evidence-bearing paper cards that are ready for current drafting, later survey writing, and revision.

## Open These Files First

- `benchmark.md`
- `outline.md`
- `writing.md`
- `corpus/registry/benchmark_registry.csv`
- `corpus/batches/batch_index.md` when it exists
- the relevant batch file under `corpus/batches/` when one exists
- `template/paper_card_template.md`
- `evals/quality_rubric.md`
- `evals/batch_review_checklist.md`
- `.codex/skills/paper-card-batch-reader/references/card_rules.md`
- `.codex/skills/paper-card-batch-reader/assets/paper_card_template.md` only if the root template is missing

## Minimum Reading Scope

Read enough to fill the card reliably:
- abstract
- introduction
- benchmark or task or environment setup
- observation or action or interface details
- evaluation protocol and metrics
- main results, failure modes, and limitations
- appendix only when it resolves setup or metric ambiguity

## Identifier And Path Rule

- Keep `paper_id` exactly as the readable title-aligned ID stored in the registry.
- Default card location is `paper_cards/{batch_id}/{paper_id}.md`.
- If `batch_id` is blank, do not drop the card into the root `paper_cards/` folder; assign or confirm the batch first unless the registry already points to a deliberate override path.

## Long-List Mode

- Work from one batch at a time.
- Do not load the full benchmark list plus multiple batches into one pass.
- Keep comparison spillover small: at most `1-2` nearby cards unless the user asks for broader synthesis.
- Treat the registry row and active batch file as the primary context; use `benchmark.md` only as backstop context.

## PDF Resolution Rule

Before deep reading, check whether `paper_link` already points to full text.

- Keep the workflow simple and bounded. Only use deterministic rewrites plus one landing-page hop.
- If `paper_link` is an arXiv `abs` page, rewrite it to `https://arxiv.org/pdf/<id>.pdf`.
- If `paper_link` is an ACL Anthology landing page, prefer the corresponding `.pdf` URL on that page.
- If `paper_link` is an OpenReview `forum?id=...` page, try the matching `pdf?id=...` URL. If the site blocks retrieval in the current environment, keep the landing page and record the blocker.
- If `paper_link` is a DOI, publisher landing page, or project page, inspect that page for `citation_pdf_url` or a direct official PDF link. If the page only links onward to an official paper page such as arXiv or proceedings, follow that one hop and resolve the PDF there.
- If you find a clearly better verified PDF URL, update the registry `paper_link` to that PDF URL before finishing the card.
- Verify hard cases with a temporary download plus `file` or `pdfinfo`. Do not create or commit a repo-wide PDF cache unless the user explicitly asks for one.
- Prefer the authoritative paper PDF over mirrors or informal summaries.
- If the PDF cannot be verified or the site blocks automated retrieval, keep the landing page, mark the blocker explicitly, and avoid inventing a URL.

## Workflow

1. Start from a selected batch file or an explicit paper list.
2. For each paper, follow the card path already stored in the registry. If none exists, default to `paper_cards/{batch_id}/{paper_id}.md`.
3. Resolve the PDF URL when `paper_link` is only an abstract or landing page, using the bounded rules above.
4. Fill `template/paper_card_template.md` exactly. Preserve the section order so cards stay comparable.
5. Keep section `11.1` to direct paper-supported facts, section `11.2` to our synthesis, and section `11.3` to unresolved uncertainty.
6. Update the registry after each card:
   - `status`
   - `paper_card_path`
   - `priority` if the deep read changes importance
   - `queue_tier` if the deep read materially changes urgency
   - `check_status`
   - `last_updated`
7. After finishing the batch, run the checklist in `evals/batch_review_checklist.md` and judge card quality against `evals/quality_rubric.md`.
8. Promote only passing cards to `status = card-reviewed`. Keep weak cards at `status = card-draft`. Leave `check_status = unchecked` unless the user explicitly confirms a human check is complete.
9. Update `corpus/batches/batch_index.md` when the batch state changes.
10. Strengthen `outline.md` only by adding clearer anchors or comparison targets. Do not draft long prose here.

## Status Rules

- `triaged`: only Stage 1 placement exists
- `card-draft`: first complete structured card exists
- `card-reviewed`: passed the repo review gate and is ready for synthesis; this does not by itself imply `check_status = checked`
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
- an updated batch state in `corpus/batches/batch_index.md`
- a short note on which outline sections are now well supported and which are still thin

## Do Not

- do not merge multiple papers into one card
- do not collapse facts and interpretation into the same bullet
- do not write polished survey prose instead of evidence notes
- do not invent taxonomy labels that are not supported by the paper or the current project vocabulary
