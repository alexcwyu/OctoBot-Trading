# OctoBot-Trading: portable verification records

Full raw logs are retained in the workspace maintenance evidence, not distributed here. Hashes identify those original logs. A successful build or selected test subset does not imply a full test-suite pass. Commands containing <workspace> describe the original execution environment.

[Machine-readable records](verification.json) · [Repository validation summary](../validation.md)

## Executed commands

| Check | Exit | Duration | Command | Outcomes |
| --- | ---: | ---: | --- | --- |
| allocation-diagnosis-tests | 1 | 2.69s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` | 1 failed, 1 passed in 1.28s |
| backend-compat-sync | 0 | 0.78s | `uv sync --all-extras --python 3.14.8` | See exit status; no test-count assertion. |
| backend-compat-tests | 1 | 58.41s | `.venv/bin/python -m pytest tests` | 8 failed, 897 passed in 57.54s |
| build | 0 | 2.28s | `uv build --python 3.14` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| ccxt-current-tests | 1 | 60.83s | `.venv/bin/python -m pytest tests` | 8 failed, 888 passed, 10 errors in 59.93s |
| compile | 0 | 1.03s | `<workspace>/OctoBot-Trading/.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| connection-diagnosis-tests | 1 | 1.97s | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` | 1 failed, 1 passed in 1.04s |
| counter-focused-tests | 1 | 49.62s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | See exit status; no test-count assertion. |
| counter-focused-tests-2 | 1 | 2.54s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | See exit status; no test-count assertion. |
| counter-focused-tests-3 | 1 | 6.07s | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | 1 failed, 16 passed in 5.23s |
| current-sync | 0 | 32.8s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-2 | 1 | 0.05s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-3 | 1 | 0.09s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-4 | 1 | 0.08s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-5 | 0 | 0.88s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| current-sync-6 | 0 | 0.78s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| deadlock-diagnostic | 1 | 18.05s | `.venv/bin/python -m pytest tests/modes/test_abstract_mode_consumer.py::test_create_order_if_possible_ensure_no_deadlock_when_canceling_orders` | See exit status; no test-count assertion. |
| directory-resource-sync | 0 | 1.15s | `uv sync --all-extras --python 3.14.8` | See exit status; no test-count assertion. |
| final-build | 0 | 2.99s | `uv build --python 3.14.8` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| final-build-2 | 0 | 1.55s | `uv build --python 3.14.8` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| final-build-current | 0 | 1.41s | `uv build --python 3.14.8` | Successfully built dist/octobot_trading-2.5.13.tar.gz<br>Successfully built dist/octobot_trading-2.5.13-py3-none-any.whl |
| final-compile | 0 | 0.19s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-compile-2 | 0 | 0.12s | `.venv/bin/python -m compileall -q src` | See exit status; no test-count assertion. |
| final-compile-current | 0 | 0.18s | `.venv/bin/python -m compileall -q src vendor` | See exit status; no test-count assertion. |
| final-current-tests | 1 | 297.63s | `.venv/bin/python -m pytest tests` | 2 failed, 903 passed in 296.07s (0:04:56) |
| final-existing-tests | 1 | 66.7s | `.venv/bin/python -m pytest tests` | 1 failed, 902 passed, 3 errors in 65.54s (0:01:05) |
| final-existing-tests-2 | 0 | 150.7s | `.venv/bin/python -m pytest tests` | 905 passed in 148.88s (0:02:28) |
| final-lock | 0 | 0.24s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-lock-2 | 0 | 0.23s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| final-sync | 0 | 0.05s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| final-sync-2 | 0 | 0.13s | `uv sync --all-extras --frozen --python 3.14.8` | See exit status; no test-count assertion. |
| fixture-owned-tests | 4 | 0.61s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| fixture-owned-tests-2 | 1 | 292.57s | `.venv/bin/python -m pytest tests` | 3 failed, 902 passed in 291.25s (0:04:51) |
| full-current-tests | 1 | 68.65s | `.venv/bin/python -m pytest tests` | 2 failed, 900 passed, 3 errors in 66.94s (0:01:06) |
| lazy-positional-tests | 1 | 15.56s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 2 failed, 33 passed in 14.00s |
| lock-3.14 | 0 | 0.46s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| lock-3.15 | 0 | 6.15s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| manager-owned-tests | 0 | 151.0s | `.venv/bin/python -m pytest tests` | 905 passed in 149.65s (0:02:29) |
| public-manager-sync | 0 | 1.6s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| scheduled-session-tests | 0 | 16.38s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 35 passed in 14.46s |
| stopped-paused-tests | 1 | 15.08s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 2 failed, 33 passed in 13.86s |
| sync-3.14 | 0 | 0.3s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
| sync-3.15 | 1 | 63.71s | `uv sync --all-extras --python 3.15` | See exit status; no test-count assertion. |
| tests | 2 | 18.96s | `<workspace>/OctoBot-Trading/.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-2 | 2 | 8.94s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-3 | 1 | 113.46s | `.venv/bin/python -m pytest tests` | 16 failed, 888 passed, 1 error in 111.06s (0:01:51) |
| tests-4 | 1 | 137.25s | `.venv/bin/python -m pytest tests` | 8 failed, 897 passed in 134.71s (0:02:14) |
| tests-5 | 2 | 23.83s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-6 | 2 | 20.81s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| tests-7 | 2 | 11.76s | `.venv/bin/python -m pytest tests` | See exit status; no test-count assertion. |
| transport-abort-tests | 1 | 14.89s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 3 failed, 32 passed in 13.74s |
| transport-diagnosis-tests | 1 | 117.64s | `.venv/bin/python -X tracemalloc=10 -m pytest tests/exchanges/traders/test_trader.py` | 2 failed, 33 passed in 102.02s (0:01:42) |
| transport-lazy-tests | 1 | 66.04s | `.venv/bin/python -m pytest tests` | 6 failed, 896 passed, 5 errors in 64.97s (0:01:04) |
| transport-owned-tests | 1 | 16.23s | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 3 failed, 32 passed in 14.67s |
| updated-manager-sync | 0 | 1.32s | `uv sync --all-extras --python 3.14` | See exit status; no test-count assertion. |
