# Citation Policy For Benchmark Chapter Audits

## Scholarly Judgment

Audit citations at the claim level. A useful citation either:

- anchors a historical or design-space classification
- supports a capability claim with a concrete benchmark mechanism or result
- supplies a boundary caveat about interface privilege, metric semantics, calibration, robustness, contamination, or generalization
- gives a representative contrast that prevents overgeneralization

Do not recommend a paper only because its topic keyword appears in the sentence.

## Preferred Evidence Sources

Use paper cards before full papers for routine chapter support:

- Section 5: interaction model, observation/action channel, scaffold, privilege
- Section 6: evaluation protocol, metrics, baselines, calibration, robustness
- Section 8: empirical findings and failure modes
- Section 9: survey-use claims
- Section 10: comparison targets
- Section 11.1: direct paper-supported facts
- Section 11.2: project synthesis
- Section 11.3: unresolved uncertainty

Open the full paper only when the card is ambiguous, the citation would support a high-stakes factual claim, or the card itself marks the point as uncertain.

## Citation Density

- One or two strong citations are usually better than a long list.
- Use three or more citations when the paragraph claims broad field coverage, compares families, or names multiple benchmark paradigms.
- Separate support roles: one citation may support an interface mechanism, another may support a metric caveat.

## Common Problems In `Benchmarks.tex`

- raw paper-ID parentheticals copied from `script.md`, e.g. `(SmartPlay; GTBench)`
- BibTeX citation keys that differ from registry IDs, e.g. registry `AIGameStore` but bib key `aigamescore57`
- missing BibTeX keys caused by using registry IDs directly when `references.bib` still uses legacy keys
- citations attached to preceding words without a tie or space
- claims about "games" or "benchmarks" as a broad field supported by only one narrow paper
- Level 5 generalization claims that mix curated breadth, single-world open-ended tasks, generated environments, and first-contact evaluation without distinguishing their evidence types
