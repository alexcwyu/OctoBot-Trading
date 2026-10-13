# Development

<!-- current-documentation-provenance -->
Documentation reviewed: 2026-10-13 · Git source base: `4a1eaa90ea2f0058e759fd84b26646d224f8c844` · [Current architecture and feature guide](ayu-develop.md).
Historical execution commands/results below retain their original dates and scope; this metadata update is not a new application test run.
<!-- /current-documentation-provenance -->


## uv maintenance workflow (2026-10-12)

Selected complete environment: Python 3.15.0; build backend `hatchling.build`. The workspace uses uv 0.13.0. An isolated complete native build and all 905 original standalone cases pass on Python 3.15; exact results are recorded in [validation](validation.md).

```sh
export UV_PYTHON_PREFERENCE=only-managed
export PYCARES_USE_SYSTEM_LIB=1
export CFLAGS='-I/opt/homebrew/opt/c-ares/include'
export LDFLAGS='-L/opt/homebrew/opt/c-ares/lib'
uv python install 3.15.0
uv lock --upgrade
uv sync --all-extras --python 3.15.0
uv build --python 3.15.0
uv run --frozen --all-extras python -m compileall -q src/octobot_trading
uv run --frozen --all-extras python -m pytest tests
```

Keep source resources inside their package and preserve the repository's existing src layout. Rebuild after source/native/asset changes. Use the locked environment for final verification. Commands above are the standard workflow, not a promise that every existing suite currently passes; consult validation for exact outcomes and unresolved compatibility issues.

## Compatible dependency sources

The [LGPL trading backend source](../vendor/trading-backend/PROVENANCE.md) preserves upstream 1.2.43 behavior while importing `ecdsa.der` through its public package instead of CCXT's removed private copy. The uv sources also share the compatible manager maintained in `../OctoBot-Evaluators/vendor/tentacles-manager`; its provenance records the exact upstream revision and runtime repairs. Keep these sibling repositories together for locked synchronization. Exchange HTTP clients own and close their aiohttp sessions; tests release sessions they allocate and allow TLS transport shutdown to complete.

## Native Python 3.15 dependency build

The earlier pycares fallback is resolved using its supported `PYCARES_USE_SYSTEM_LIB=1` build against the actual installed Homebrew c-ares library. Include and library paths are supplied above; the OS deployment target is unchanged. The repository’s own 905 original cases pass on Python 3.15, alongside its source distribution, wheel and strict source compilation. Its sibling Commons, Backtesting and licensed compatibility sources remain the original standalone API stack; host-package tests are not substituted.
