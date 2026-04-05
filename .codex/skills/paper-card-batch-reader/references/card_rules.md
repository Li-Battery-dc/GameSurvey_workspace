# Paper Card Rules

## Minimum Evidence Split

- `11.1 Direct paper-supported facts`: only claims that the paper directly states or clearly implies through reported setup, metrics, or results
- `11.2 Our synthesis / interpretation`: cross-paper framing, survey positioning, and narrative interpretation
- `11.3 Uncertain or needs re-check`: unresolved labels, ambiguous setup details, missing metrics, or claims that require another pass

## Recommended Status Progression

- `triaged`
- `card-draft`
- `card-reviewed`
- `finalized`

A card file normally starts at `card-draft`. `triaged` is only for registry rows before a card exists.

## Registry Sync Fields

After each completed card, update at least:
- `status`
- `priority` if the deep read changes importance
- `paper_card_path`
- `next_action`
- `last_updated`

## Good Stage 2 Behavior

- keep one paper per file
- keep the template section order stable
- anchor the card to concrete outline sections
- name nearby comparison targets inside the corpus
- leave uncertainty visible instead of forcing completeness
