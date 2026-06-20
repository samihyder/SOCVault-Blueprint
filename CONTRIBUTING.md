# Contributing to SOCVault Blueprint

This repository holds product documentation, wireframes, and planning artefacts — not application source code.

## Making changes

1. **User stories** — Edit `userstories-wireframes/SOCVault-User-Stories.xlsx`. Keep IDs sequential (`US-001`–`US-185`).
2. **Requirements** — Update `docs/03_REQUIREMENTS.md` and add a row to `docs/16_TRACEABILITY_MATRIX.md`.
3. **Wireframes** — Edit HTML in `userstories-wireframes/`. Include `story-ref` tags for linked user stories.
4. **Architecture** — Update `docs/02_TECHNICAL_STACK.md` and add an ADR in `docs/adr/` for significant decisions.
5. **Tracker (mandatory)** — Log every action in [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md): add an Action Log row and update the matching INF/DEV/API checklist status.

## Conventions

- Functional requirements: `FR-###`
- Non-functional requirements: `NFR-###`
- User stories: `US-###`
- Brand colours: `#1B3D35` (forest green), `#4CC844` (lime green)
- AI provider: Anthropic Claude only

## Review checklist

- [ ] No contradictory rate limits or financial figures across docs
- [ ] Traceability matrix updated for new FR/US pairs
- [ ] Wireframe index (`00-index.html`) reflects new pages
- [ ] `docs/README.md` index updated
- [ ] [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md) updated (action log + status tables)
