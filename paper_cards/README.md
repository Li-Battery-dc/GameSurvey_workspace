# Paper Cards

File name convention:
- default: `paper_cards/{batch_id}/{paper_id}.md`
- create the batch subdirectory before writing cards for that batch
- if the registry already points to another relative path, follow the registry entry

Every processed paper must have one card based on `template/paper_card_template.md`.
Keep direct paper facts, synthesis, and unresolved uncertainty in separate sections.
Treat paper cards as intermediate evidence units for review and drafting, not as the final survey sections.
Section prose and drafting decisions should live in `writing.md` and remain traceable back to these cards.
Use the repo workflow status vocabulary consistently: `card-draft`, `card-reviewed`, `finalized`.
Use readable title-aligned `paper_id` values such as `SmartPlay`, `GameplayQA`, `CKArena`, or `GTBench`.
