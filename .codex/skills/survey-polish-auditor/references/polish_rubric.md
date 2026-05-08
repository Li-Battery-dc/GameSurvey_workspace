# Polish Rubric

Use this reference when grading the strength of survey claims, `script.md` prose, and citation placement.

## Issue Severity

- `P0 factual contradiction`: the sentence contradicts an opened paper card or authoritative paper text, or attributes a result/design to the wrong paper.
- `P1 unsupported overclaim`: the claim may be directionally plausible but is broader, stronger, or more causal than the evidence allows.
- `P1 citation mismatch`: the cited paper does not support the claim's exact role, or a better direct paper is available.
- `P2 plan-prose drift`: `script.md` changes the order, scope, or emphasis of `writing.md` in a way that affects the argument.
- `P2 style/rigor`: wording is inflated, vague, repetitive, nonacademic, or insufficiently bounded.
- `P3 local polish`: grammar, naming consistency, citation punctuation, or minor concision issue.

## Support Grades

- `A direct`: the card or paper directly supports the sentence-level claim.
- `B synthesized`: the claim is a reasonable survey synthesis built from multiple direct facts; citations support the ingredients.
- `C weak`: the paper is adjacent but not the best evidence, or the card marks relevant uncertainty.
- `D mismatch`: the citation supports a different claim, level, modality, metric, or benchmark role.
- `E contradiction`: the claim conflicts with the card or paper.

## Claim Types And Citation Need

- Specific benchmark design: cite the paper(s) that implement the design.
- Empirical result, failure mode, or model behavior: cite the paper reporting it.
- Comparative claim across benchmarks: cite at least the compared papers, or cite an anchor plus a contrast if the comparison is asymmetric.
- Field-level trend: cite representative anchors; avoid long piles unless the sentence claims broad coverage.
- Survey taxonomy or terminology introduced by this project: no citation required unless the wording depends on external benchmark examples.
- Roadmap sentence or paragraph transition: usually no citation required.
- Original synthesis: cite the evidence ingredients, but phrase the sentence as the survey's interpretation.

## Stronger Evidence Selection

Prefer a replacement citation when it is:

- `finalized` over `card-reviewed`, and never `triaged`/`card-draft` for copy-ready claims unless marked as a placeholder;
- an anchor or representative paper for the relevant section rather than a peripheral mention;
- directly tied to the claim's capability, interface, metric, or empirical result;
- more precise about the benchmark mechanism than a broad suite paper;
- better aligned with the paragraph's level in the five-level narrative spine;
- able to supply contrast or boundary conditions rather than only another example.

Good citation sets usually use one or two direct anchors plus one contrast when needed. Avoid adding every paper named in `writing.md` if several do the same argumentative work.

## Writing And Style Checks

Flag or revise:

- absolute wording such as "prove", "guarantee", "fully", "true", or "unparalleled" unless the evidence really warrants it;
- ecological-validity claims that ignore interface privilege or entangled failure modes;
- "many games" language that conflates curated breadth, intra-world task variation, generated games, and first-contact novelty;
- capability claims that treat benchmark designer dimensions as validated cognitive factors;
- result-score claims that ignore calibration, opponent pool, randomness, or interface differences;
- citations attached to decorative name-dropping rather than argument support;
- inconsistent paper names or IDs, especially `BALROG`, `AI GameStore`, `LMGameBench`, `ARCAGI3`, and registry `paper_id` values;
- repeated sentences that restate `writing.md` planning language instead of producing copy-ready prose.

## Minimal Rewrite Pattern

When fixing a paragraph, preserve its role in the current section:

1. State the bounded synthesis claim.
2. Add the concrete mechanism or evidence type.
3. Attach the smallest useful citation set.
4. Add a boundary sentence only when the claim could otherwise be overread.

Example pattern:

`Rather than showing cross-game transfer, fixed curated suites mainly broaden capability coverage across known game forms. Generated or first-contact benchmarks make novelty more central because new rules, levels, or mechanics are part of the evaluation protocol (Orak; GameVerse; AIGameStore; ARCAGI3).`
