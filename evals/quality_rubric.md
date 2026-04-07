# Quality Rubric

Use this rubric to judge whether the current reading outputs are strong enough to support section drafting, revision, and later survey writing.

## 1. Registry Quality

A strong registry row should:
- use the current CSV columns consistently
- keep `paper_id` stable, readable, and title-aligned
- include a usable `priority`
- include a usable `queue_tier`
- include a current `triage_round`
- include a usable `batch_id` or an explicit hold decision
- include a meaningful `outline_sections` value
- include a valid `paper_card_path` once `status` reaches `card-draft` or above
- include a valid `check_status`
- update `last_updated`

Warnings:
- lowercase slug-like `paper_id` values that no longer match the repo naming convention
- blank or invalid `check_status`
- blank `queue_tier` in a long-list corpus
- `queue_tier` does not match the actual reading queue anymore
- legacy statuses such as `unread` or `read-card`
- `paper_card_path` points to a file that does not exist when `status` is `card-draft` or above
- `paper_card_path` does not match the row's `batch_id`
- row still reflects Stage 1 assumptions after a deep read
- high-priority rows have no clear outline landing point

## 2. Paper Card Quality

A strong paper card should:
- follow `template/paper_card_template.md`
- identify the benchmark setup, interaction paradigm, and evaluation protocol correctly
- separate direct paper evidence, our synthesis, and unresolved uncertainty
- state why the paper matters for this survey rather than only summarizing the abstract
- list nearby comparison targets inside the corpus
- sync the registry status and path fields
- be grounded in the full paper PDF or another authoritative full-text source when one exists
- be scored explicitly as `strong`, `usable`, or `weak` during the batch review gate

Manual human review is tracked separately in `check_status`; a row may be `card-reviewed` for workflow purposes while still remaining `unchecked` until the team confirms it.

### Strong

The card is reliable enough to support comparative drafting and can normally be promoted to `status = card-reviewed`.

Signs:
- key benchmark facts are specific rather than generic
- Sections 3 to 6 are filled with benchmark-relevant detail
- Section 10 names concrete comparison papers
- Section 11 cleanly separates evidence and interpretation
- Section 13 reflects the current registry state

### Usable

The card can support planning and bounded synthesis. It may also be promoted to `status = card-reviewed` if its remaining uncertainty is explicit and does not undermine the section claim.

Typical issues:
- one or two fields remain vague
- comparison targets are weak
- evaluation details are partial
- some claims belong in `11.3` rather than `11.1`

### Weak

The card should not drive drafting yet and should remain at `status = card-draft` until corrected.

Typical issues:
- mostly abstract paraphrase
- benchmark interface or evaluation is unclear
- unsupported interpretation is mixed into direct evidence
- no meaningful outline anchoring
- no comparison targets

## 3. Batch Quality

A strong completed batch should:
- cover the intended comparison theme or outline need
- contain one card per paper in the batch
- keep registry rows in sync with those cards
- surface the remaining ambiguity instead of hiding it
- reveal which outline sections are now well supported
- leave a clear pass or fail decision for each card
- keep `corpus/batches/batch_index.md` aligned with the current queue state

Warnings:
- the batch mixes too many unrelated papers to compare cleanly
- half-finished cards are treated as ready evidence
- registry and card paths disagree
- no summary of what the batch clarified for the survey
- passing and failing cards are not separated in the registry
- the batch index still marks a finished batch as active

## 4. Draft Readiness

A section is ready to draft when:
- at least 3 reviewed cards rated `strong` or `usable` support it
- the cards can be compared on more than one axis
- the section claim is traceable to cards
- uncertainty is visible and bounded

A section is not ready when:
- one anchor paper is carrying the whole claim
- the available cards are only descriptive, not comparative
- visual, interface, or evaluation details are still missing
- the main disagreement between papers has not been identified

## 5. Red Flags

Stop and fix the underlying artifacts before drafting if you see any of these:
- registry says a card exists but the file is missing
- card and registry disagree on priority or path
- direct evidence contains claims that belong to synthesis
- outline anchors are missing or too vague
- draft prose introduces benchmark claims not present in cards
- weak cards are being used as if they had already passed review
- the agent is rereading the whole benchmark list instead of working from the registry and batch index
