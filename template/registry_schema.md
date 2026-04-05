# Registry Schema

This file is the canonical schema for `corpus/registry/benchmark_registry.csv`.
Keep the column order stable. Do not add legacy taxonomy columns, `notes_path`, reviewer-assignment fields, or other leftovers from older schema drafts unless the whole repo is intentionally migrated.

## Active columns

| Column | Meaning | Typical values |
| :--- | :--- | :--- |
| `paper_id` | Stable, title-aligned paper identifier used across the repo | `SmartPlay`, `GameplayQA`, `GTBench` |
| `date` | Publication date or arXiv month | `2024/11`, `2025` |
| `title` | Short paper title | `BALROG` |
| `venue` | Venue or source | `ICLR 2025`, `arXiv` |
| `paper_link` | Primary paper URL | arXiv or publisher URL |
| `code_link` | Code or project page URL | GitHub URL or blank |
| `status` | Current workflow state | `triaged`, `card-draft`, `card-reviewed`, `finalized` |
| `priority` | Reading priority | `P0`, `P1`, `P2`, `P3` |
| `queue_tier` | Queue position for long-list triage | `now`, `next`, `later`, `hold` |
| `triage_round` | Which triage pass last touched the row | `1`, `2`, `3` |
| `reading_depth` | Intended reading depth for the next pass | `structured-skim`, `deep` |
| `batch_id` | Reading batch identifier | `B01`, `B02` |
| `batch_theme` | Short batch theme slug | `formal-foundations` |
| `batch_order` | Order inside the batch | `1`, `2`, `3` |
| `outline_sections` | Comma-separated landing points in `outline.md` | `0,2,3` |
| `survey_role` | Why this paper is in the corpus | `anchor`, `representative`, `contrast`, `peripheral` |
| `paper_card_path` | Relative path to the paper card | `paper_cards/B03/Balrog.md` |
| `triage_note` | Short reason for placement, with inline uncertainty when needed | `Anchor for social evaluation. [uncertain: outline-fit]` |
| `next_action` | Immediate next step for this paper | `read-batch`, `deep-read`, `review-card`, `draft-section`, `hold` |
| `last_updated` | Last registry edit date | `2026-04-05` |

## Field rules

- `paper_id`: keep it stable, title-aligned, and readable. Use PascalCase or acronym-preserving CamelCase such as `SmartPlay`, `CKArena`, `GameplayQA`, or `GTBench` instead of lowercase slugs.
- `status`: use the repo vocabulary exactly: `triaged`, `card-draft`, `card-reviewed`, `finalized`.
- `priority`: `P0` is anchor or outline-stabilizing; `P3` is backlog or peripheral.
- `queue_tier`: use `now` for the next `1-3` batches, `next` for the near queue after that, `later` for backlog that should remain visible, and `hold` for intentionally parked papers.
- `triage_round`: start at `1` for the first triage pass and increment when a later pass materially revises placement or urgency.
- `reading_depth`: use `structured-skim` for lighter Stage 2 passes and `deep` for full benchmark reading.
- `batch_id`: leave blank only for papers intentionally parked with `next_action = hold`.
- `outline_sections`: keep values short and traceable to the current `outline.md`.
- `paper_card_path`: default to `paper_cards/{batch_id}/{paper_id}.md`. If `batch_id` changes, update the path to the matching batch subdirectory. Once `status` reaches `card-draft` or above, this path must exist.
- `triage_note`: keep it to one or two sentences. Put uncertainty inside the note, for example `[uncertain: evaluation|outline-fit]`.
- `next_action`: keep it concrete and workflow-facing rather than descriptive prose.
- `last_updated`: use ISO date format `YYYY-MM-DD`.
