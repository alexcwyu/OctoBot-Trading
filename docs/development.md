# Development

## uv maintenance workflow (2026-10-12)

Selected complete environment: Python 3.14.8; build backend `hatchling.build`. The workspace uses uv 0.13.0. Python 3.15 was attempted before any fallback; the actual failure and selected runtime are recorded in [validation](validation.md).

```sh
export UV_PYTHON_PREFERENCE=only-managed
uv python install 3.14.8
uv lock --upgrade
uv sync --all-extras --python 3.14.8
uv build --python 3.14.8
uv run --frozen --all-extras python -m compileall -q src/octobot_trading
uv run --frozen --all-extras python -m pytest tests
```

Keep source resources inside their package and preserve the repository's existing src layout. Rebuild after source/native/asset changes. Use the locked environment for final verification. Commands above are the standard workflow, not a promise that every existing suite currently passes; consult validation for exact outcomes and unresolved compatibility issues.

## Compatible dependency sources

The [LGPL trading backend source](../vendor/trading-backend/PROVENANCE.md) preserves upstream 1.2.43 behavior while importing `ecdsa.der` through its public package instead of CCXT's removed private copy. The uv sources also share the compatible manager maintained in `../OctoBot-Evaluators/vendor/tentacles-manager`; its provenance records the exact upstream revision and runtime repairs. Keep these sibling repositories together for locked synchronization. Exchange HTTP clients own and close their aiohttp sessions; tests release sessions they allocate and allow TLS transport shutdown to complete.
