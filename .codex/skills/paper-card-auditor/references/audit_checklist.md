# Paper Card Audit Checklist

Use this file when a single-paper audit needs a tighter defect taxonomy or a stricter exit standard.

## 1. Hallucination And Accuracy Defects

Treat these as real defects, not style issues:

- fabricated fact: the paper card states something the paper does not support
- overclaim: the card says more than the paper actually establishes
- narrowed or distorted result: the card changes the scope, setup, metric, or conclusion
- wrong classification: the card assigns the wrong historical stage, narrative level, world type, interface type, or evaluation family
- unsupported survey-use claim: the card says the paper is central to a section that it only weakly or indirectly supports
- comparison drift: the card claims a relation to nearby papers that is not supported by the current corpus evidence
- missing caveat: the card omits a limitation that changes how the paper should be used in writing

## 2. Highest-Risk Card Areas

Audit these sections carefully even if the rest of the card looks fine:

- Section 2: survey position, historical stage, narrative level, outline sections, corpus role
- Section 4: capability claims
- Section 5: interface, scaffolds, privileged access, ecological-validity trade-off
- Section 6: metrics, baselines, calibration, comparability, contamination claims
- Section 8: empirical takeaway and failure modes
- Section 9: exact survey use
- Section 10: comparison targets and uniqueness claims
- Section 11: boundary between direct evidence, synthesis, and uncertainty

## 3. Full-Text Evidence Capture

Before editing, collect page, section, table, or figure anchors for:

- benchmark definition and intended task
- observation and action interface
- evaluation protocol and main metrics
- main findings
- limitations or threats to validity
- any card claim that looks especially strong or especially specific

When reporting major corrections to the user, prefer short page or section pointers when the PDF makes them stable.

## 4. Outline Alignment Questions

For each section below, decide whether the paper is direct support, contrast-only support, or not a meaningful fit:

- Section 0: why games matter as benchmarks
- Section 1: historical evolution
- Section 2: taxonomy and design space
- Section 3: capability target
- Section 4: interaction paradigm
- Section 5: evaluation protocol
- Section 6: recurring failure modes
- Section 7: open benchmark-design problems

Then ask:

- Which subsection, if any, is the real landing point?
- Is the paper an `anchor`, `representative`, `contrast`, or `peripheral` source for that landing point?
- Does the paper support a broad section claim, or only a narrower contrast or caveat?
- Is the current `outline_sections` field too broad?

## 5. Writing Alignment Questions

Cross-check against `writing.md`:

- Is the paper listed as an anchor for a section it only weakly supports?
- Does the paper provide direct evidence, a comparison case, or only a cautionary edge case?
- Does the full paper strengthen, weaken, or contradict an active synthesis note?
- Should this paper stay in the current evidence base for that section?
- What exact sentence or claim family should this paper support after the audit?

## 6. Downgrade Triggers

Downgrade a card back to `card-draft` when the audit still leaves one of these unresolved:

- the interface or evaluation protocol is still too unclear for safe survey use
- the main findings in the card cannot be supported from the paper
- the paper's section fit is materially wrong and not yet repaired
- the card still relies on abstract-level paraphrase instead of full-text evidence
- key Section 9 or Section 10 claims remain inflated or speculative

## 7. Exit Standard

A strong single-paper audit leaves behind:

- the full paper was actually read
- the highest-risk card sections were rechecked
- hallucinated or inflated claims were corrected or removed
- the evidence split in Section 11 is clean
- `outline_sections`, `survey_role`, and Section 9 reflect the current writing architecture
- the registry is synced if any of those changed
- the final user report says whether the card is `clean`, `fixed`, or `still-blocked`
