# Paper Card Audit Checklist

Use this reference when a final audit needs a tighter defect taxonomy, a batch-sweep checklist, or a clearer exit standard.

## 1. Defects To Treat As Real Problems

- fabricated fact: the card states something the paper does not support
- overclaim: the card says more than the paper establishes
- distorted result: the card changes setup, metric, scope, baseline, or conclusion
- stale taxonomy: the card uses old stages, old outline sections, or broad labels that conflict with the current L1-L5 framework
- wrong design-space code: Form, Construction, Scope, observation modality, or action modality is unsupported
- writing-support gap: Section 9 does not say what claim the paper can support in the new `writing.md`/`script.md` framework
- unsupported citation target: the paper is cited or positioned for a claim it only weakly supports
- comparison drift: Section 10 claims a relationship to nearby papers that current cards do not justify
- missing caveat: the card omits a limitation that changes how the paper should be used

## 2. Highest-Risk Card Areas

Audit these sections even when the rest of the card looks plausible:

- Section 2: historical stage, L1-L5 level(s), outline sections, corpus role
- Section 3: Form, Construction, Scope, modality, benchmark unit
- Section 4: capability target and game-specific measurement rationale
- Section 5: interface, scaffolds, privileged access, ecological-validity trade-off
- Section 6: metrics, baselines, calibration, robustness, contamination claims
- Section 8: empirical takeaways and failure modes
- Section 9: exact survey use under Sections 0-4
- Section 10: comparison targets and uniqueness claims
- Section 11: boundary between direct evidence, synthesis, and uncertainty
- Section 13: registry sync fields

## 3. Current Taxonomy Validation

Confirm that the card's labels match the current `outline.md` and `writing.md`:

- Level 1: rule understanding and legal action in formal containers
- Level 2: strategic, game-theoretic, spatial, or adaptive interactive reasoning
- Level 3: social intelligence, deception, negotiation, or coordination under interdependence
- Level 4: visual agency, UI grounding, native or near-native control, long-horizon doing
- Level 5: cross-game generalization, expandable/living game spaces, first-contact adaptation, or open-ended task generalization

Then validate secondary axes:

- Form: Match / Puzzle / Dialogue / Encounter / Arc / World / Mixed
- Construction: Embedded / Wrapped / Adapted / Authored / Generated
- Scope: single game / game family / curated suite / expandable suite / open-ended tasks
- Observation: text or symbolic / visual image / mixed
- Action: semantic / native control / mixed

If a paper spans levels or axes, record the dominant role for the table and keep nuance in Sections 2, 9, and 11.

## 4. Writing-Support Capture

For each finalized card, Section 9 should answer:

- What exact Section 0 claim can this paper support, if any?
- What exact Section 1 taxonomy or historical-development claim can it support?
- What exact Section 2 Purpose claim can it support?
- What exact Section 3 interaction/evaluation paradigm claim can it support?
- What exact Section 4 bottleneck or future-design claim can it support?
- Is the paper direct support, a representative example, a contrast case, or only a caveat?
- Does current `script.md` already cite or imply this paper in a way the audit supports or weakens?

Prefer claim families over generic praise. Example shape: "Supports the Level 4 knowing-doing gap by showing that raw visual/native-control play entangles perception, UI grounding, and recovery failures."

## 5. Evidence Capture

Before editing, collect stable anchors for:

- benchmark definition and intended task
- observation and action interface
- scaffold or privilege assumptions
- evaluation protocol and main metrics
- baselines, human/AI anchors, or calibration method
- main empirical finding and failure modes
- limitations, robustness, or contamination discussion
- any strong or surprising card claim

Use page, section, table, or figure references when they are stable. Use appendix material only for specific unresolved questions.

## 6. Appendix Use Rule

Do not read appendices wholesale at the start of an audit. Query them only when needed for:

- full task/game lists or data construction details
- prompt templates, action schemas, or interface contracts
- metric definitions and scoring formulas
- additional ablations or baseline details needed to verify a card claim
- limitations or robustness details absent from the main body

If an appendix is too large, inaccessible, or only partially checked, record the residual uncertainty in Section 11.3.

## 7. Batch Audit Checklist

For whole-batch audits:

- confirm every target row has exactly one existing card
- process cards in batch order
- finalize only cards that pass full-paper and writing-framework verification
- keep blocked cards at `card-reviewed` or `card-draft` with explicit reasons
- keep `check_status` unchanged unless the user explicitly requests human-check marking
- avoid loading all cards, PDFs, and appendices together
- after the batch, report finalized/fixed-not-final/blocked counts and recurring taxonomy corrections

## 8. Downgrade Or Block Triggers

Do not finalize a card when:

- interface or evaluation protocol remains unclear
- main findings in the card cannot be supported from the paper
- taxonomy or Section 9 support is materially wrong and not repaired
- the card still relies on abstract-level paraphrase
- key claims need appendix evidence that has not been checked
- `script.md` relies on a claim the audit weakens and the mismatch remains unresolved

## 9. Exit Standard

A successful audit leaves:

- the main paper body read and targeted appendix checks performed only as needed
- hallucinated or inflated claims corrected or removed
- taxonomy/design-space labels aligned to the current framework
- Section 9 populated with concrete supportable survey claims
- Section 11 split cleanly between paper facts, synthesis, and uncertainty
- registry and card Section 13 synced
- passing cards marked `finalized`
- final report clear about remaining uncertainty and writing impact
