# Batch Review Checklist

Run this after finishing one reading batch and before moving into drafting.

## Scope Check

- [ ] The batch file clearly states which papers belong to this batch.
- [ ] Every paper in the batch has been processed or explicitly marked partial.
- [ ] The batch still makes thematic sense after deep reading.

## Registry Check

- [ ] Every processed paper has an updated row in `corpus/registry/benchmark_registry.csv`.
- [ ] `priority`, `status`, `paper_card_path`, `next_action`, and `last_updated` are current.
- [ ] No `paper_card_path` points to a missing file.
- [ ] Deep-read findings that changed importance or placement are reflected in the row.
- [ ] Weak cards remain `card-draft`; only passing cards move to `card-reviewed`.

## Paper Card Check

- [ ] Every processed paper has exactly one card.
- [ ] Every card follows `template/paper_card_template.md`.
- [ ] Direct evidence, our synthesis, and unresolved uncertainty are separated.
- [ ] Interaction paradigm and evaluation protocol are described concretely.
- [ ] Each card names nearby comparison targets.
- [ ] Each card has an explicit review label: `strong`, `usable`, or `weak`.

## Outline Check

- [ ] Each processed paper is anchored to at least one concrete part of `outline.md`.
- [ ] The batch clarifies at least one comparison theme or section boundary.
- [ ] Any needed outline change is explicit rather than implicit.

## Draft Readiness Check

- [ ] Strong cards and weak cards are distinguished clearly.
- [ ] Usable cards are distinguished from weak cards.
- [ ] Unsupported claims were removed or downgraded to uncertainty.
- [ ] It is clear which reviewed section or comparison theme can be drafted next.
- [ ] It is clear what still needs another reading pass.
