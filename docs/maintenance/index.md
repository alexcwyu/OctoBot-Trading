# OctoBot-Trading: portable verification records

These records retain exact commands, outcomes, original-log hashes and available source snapshots. Failed, interrupted and earlier exploratory commands remain visible. A later focused pass proves only its own scope.

[Machine-readable records](verification.json) · [Validation](../validation.md) · [Engineering guide](../ayu-develop.md)

Original logs remain in the workspace maintenance evidence. Tracked source hashes exclude untracked additions and later edits, as stated in each captured snapshot.

| Check | Exit | Duration | Command |
| --- | ---: | ---: | --- |
| allocation-diagnosis-tests | 1 | 2.69s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` |
| backend-compat-sync | 0 | 0.78s | `uv sync --all-extras --python 3.14.8` |
| backend-compat-tests | 1 | 58.41s | `.venv/bin/python -m pytest tests` |
| build | 0 | 2.28s | `uv build --python 3.14` |
| ccxt-current-tests | 1 | 60.83s | `.venv/bin/python -m pytest tests` |
| compile | 0 | 1.03s | `<workspace>/OctoBot-Trading/.venv/bin/python -m compileall -q src` |
| connection-diagnosis-tests | 1 | 1.97s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` |
| counter-focused-tests-2 | 1 | 2.54s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` |
| counter-focused-tests-3 | 1 | 6.07s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` |
| counter-focused-tests | 1 | 49.62s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` |
| current-sync-2 | 1 | 0.05s | `uv sync --all-extras --python 3.14` |
| current-sync-3 | 1 | 0.09s | `uv sync --all-extras --python 3.14` |
| current-sync-4 | 1 | 0.08s | `uv sync --all-extras --python 3.14` |
| current-sync-5 | 0 | 0.88s | `uv sync --all-extras --python 3.14` |
| current-sync-6 | 0 | 0.78s | `uv sync --all-extras --python 3.14` |
| current-sync | 0 | 32.8s | `uv sync --all-extras --python 3.14` |
| deadlock-diagnostic | 1 | 18.05s | `.venv/bin/python -m pytest tests/modes/test_abstract_mode_consumer.py::test_create_order_if_possible_ensure_no_deadlock_when_canceling_orders` |
| directory-resource-sync | 0 | 1.15s | `uv sync --all-extras --python 3.14.8` |
| final-build-2 | 0 | 1.55s | `uv build --python 3.14.8` |
| final-build-current | 0 | 1.41s | `uv build --python 3.14.8` |
| final-build | 0 | 2.99s | `uv build --python 3.14.8` |
| final-compile-2 | 0 | 0.12s | `.venv/bin/python -m compileall -q src` |
| final-compile-current | 0 | 0.18s | `.venv/bin/python -m compileall -q src vendor` |
| final-compile | 0 | 0.19s | `.venv/bin/python -m compileall -q src` |
| final-current-tests | 1 | 297.63s | `.venv/bin/python -m pytest tests` |
| final-existing-tests-2 | 0 | 150.7s | `.venv/bin/python -m pytest tests` |
| final-existing-tests | 1 | 66.7s | `.venv/bin/python -m pytest tests` |
| final-lock-2 | 0 | 0.23s | `uv lock --upgrade` |
| final-lock | 0 | 0.24s | `uv lock --upgrade` |
| final-sync-2 | 0 | 0.13s | `uv sync --all-extras --frozen --python 3.14.8` |
| final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.14.8` |
| fixture-owned-tests-2 | 1 | 292.57s | `.venv/bin/python -m pytest tests` |
| fixture-owned-tests | 4 | 0.61s | `.venv/bin/python -m pytest tests` |
| full-current-tests | 1 | 68.65s | `.venv/bin/python -m pytest tests` |
| lazy-positional-tests | 1 | 15.56s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| lock-3.14 | 0 | 0.46s | `uv lock --upgrade --python 3.14` |
| lock-3.15 | 0 | 6.15s | `uv lock --upgrade --python 3.15` |
| manager-owned-tests | 0 | 151.0s | `.venv/bin/python -m pytest tests` |
| public-manager-sync | 0 | 1.6s | `uv sync --all-extras --python 3.14` |
| scheduled-session-tests | 0 | 16.38s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| compile | 0 | 0.06s | `.venv/bin/python -Werror -m compileall -q src` |
| sync | 0 | 0.91s | `uv sync --all-extras --frozen --python 3.15.0` |
| build | 0 | 1.57s | `uv build --python 3.15.0` |
| compile | 0 | 0.45s | `/tmp/octobot-trading-final315-control/bin/python -Werror -m compileall -q src` |
| lock | 0 | 0.02s | `uv lock` |
| sync | 0 | 0.29s | `uv sync --all-extras --frozen --python 3.15.0` |
| tests | 0 | 149.92s | `/tmp/octobot-trading-final315-control/bin/python -m pytest tests --tb=short` |
| stopped-paused-tests | 1 | 15.08s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| sync-3.14 | 0 | 0.3s | `uv sync --all-extras --python 3.14` |
| sync-3.15 | 1 | 63.71s | `uv sync --all-extras --python 3.15` |
| tests-2 | 2 | 8.94s | `.venv/bin/python -m pytest tests` |
| tests-3 | 1 | 113.46s | `.venv/bin/python -m pytest tests` |
| tests-4 | 1 | 137.25s | `.venv/bin/python -m pytest tests` |
| tests-5 | 2 | 23.83s | `.venv/bin/python -m pytest tests` |
| tests-6 | 2 | 20.81s | `.venv/bin/python -m pytest tests` |
| tests-7 | 2 | 11.76s | `.venv/bin/python -m pytest tests` |
| tests | 2 | 18.96s | `<workspace>/OctoBot-Trading/.venv/bin/python -m pytest tests` |
| transport-abort-tests | 1 | 14.89s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| transport-diagnosis-tests | 1 | 117.64s | `.venv/bin/python -X tracemalloc=10 -m pytest tests/exchanges/traders/test_trader.py` |
| transport-lazy-tests | 1 | 66.04s | `.venv/bin/python -m pytest tests` |
| transport-owned-tests | 1 | 16.23s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` |
| updated-manager-sync | 0 | 1.32s | `uv sync --all-extras --python 3.14` |
