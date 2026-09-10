# Shiplet beta deployment fixtures

This repository contains two independent deployment fixtures used for beta
acceptance testing:

- `static-site/` — dependency-free HTML/CSS/JS; must be classified as Static HTML.
- `node-site/` — a minimal Node HTTP server; must be classified as Node.js.

Each project is intentionally tiny so failures represent platform behavior,
not application complexity.
