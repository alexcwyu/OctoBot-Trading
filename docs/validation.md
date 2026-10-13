# OctoBot-Trading: final Python 3.15 verification

<!-- current-documentation-provenance -->
Documentation reviewed: 2026-10-13 · Git source base: `4a1eaa90ea2f0058e759fd84b26646d224f8c844` · [Current architecture and feature guide](ayu-develop.md).
Historical execution commands/results below retain their original dates and scope; this metadata update is not a new application test run.
<!-- /current-documentation-provenance -->


Selected runtime: **managed Python 3.15.0**, uv **0.13.0**; source commit `5af59c4cc7bb75249fa90de57ba9b66100eaceee`. Its own existing repository suite passed: **905 passed in 143.10s (0:02:23)**. This is the original standalone repository suite, separately executed from the newer host's package suites. Source distribution and wheel builds, frozen synchronization and strict source compilation passed. No test cases, golden values or formulas changed.

[Development and native prerequisites](development.md) · [Portable exact commands](maintenance/index.md) · [Machine-readable evidence](maintenance/verification.json). The locked adjacent licensed source and supported system-library configuration are explicit in the project metadata and development guide.

## Historical verification attempts


Recorded 2026-10-12T01:56:57.671387+08:00. Branch `feature/ayu_develop`; upstream default `upstream/master` is merged: **true**. Branch/tag synchronization records are retained in the workspace maintenance evidence. Feature branch publication is coordinated separately.

Historical runtime: **CPython 3.14.8**, uv **0.13.0**, build backend `hatchling.build`. The Python 3.15 dependency installation failed in native pycares. Python 3.14.8 was selected at this stage; the reviewed Python 3.15 migration above supersedes that fallback.

Existing suite: **905 passed in 149.65s (0:02:29)** (exit `0`). Current CCXT removed its private ECDSA package; the LGPL upstream trading-backend source is retained under vendor with a public ecdsa.der import. The shared compatible manager comes from ../OctoBot-Evaluators/vendor/tentacles-manager. Current TLS cleanup and counter composition are repaired; remaining final test failures, if any, are retained explicitly.

No test cases were added. Existing assertions and strict warning behavior remain active; repaired fixtures own their loops, sessions, files and configuration paths. Existing upstream platform skips and configured deselections are reported exactly.

## Historical build commands

| Check | Exact command | Exit | Seconds |
| --- | --- | ---: | ---: |
| lock | `uv lock --upgrade` | 0 | 0.23 |
| sync | `uv sync --all-extras --frozen --python 3.14.8` | 0 | 0.13 |
| build | `uv build --python 3.14.8` | 0 | 1.41 |
| compile | `.venv/bin/python -m compileall -q src vendor` | 0 | 0.18 |

## Existing test and compatibility evidence

| Check | Exact command | Exit | Result |
| --- | --- | ---: | --- |
| lock-3.15 | `uv lock --upgrade --python 3.15` | 0 | Check completed; see exact exit code. |
| sync-3.15 | `uv sync --all-extras --python 3.15` | 1 | 1 error generated. |
| tests | `/Users/alex/workspaces/trading/OctoBot-Trading/.venv/bin/python -m pytest tests` | 2 | 123 errors in 17.56s |
| tests-2 | `.venv/bin/python -m pytest tests` | 2 | 3 errors in 7.66s |
| tests-3 | `.venv/bin/python -m pytest tests` | 1 | 16 failed, 888 passed, 1 error in 111.06s (0:01:51) |
| tests-4 | `.venv/bin/python -m pytest tests` | 1 | 8 failed, 897 passed in 134.71s (0:02:14) |
| tests-5 | `.venv/bin/python -m pytest tests` | 2 | 122 errors in 21.77s |
| tests-6 | `.venv/bin/python -m pytest tests` | 2 | 121 errors in 18.82s |
| tests-7 | `.venv/bin/python -m pytest tests` | 2 | 121 errors in 10.86s |
| backend-compat-tests | `.venv/bin/python -m pytest tests` | 1 | 8 failed, 897 passed in 57.54s |
| ccxt-current-tests | `.venv/bin/python -m pytest tests` | 1 | 8 failed, 888 passed, 10 errors in 59.93s |
| transport-lazy-tests | `.venv/bin/python -m pytest tests` | 1 | 6 failed, 896 passed, 5 errors in 64.97s (0:01:04) |
| counter-focused-tests | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | 1 | 1 failed in 46.96s |
| counter-focused-tests-2 | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | 1 | 1 failed in 1.60s |
| counter-focused-tests-3 | `.venv/bin/python -m pytest tests/exchanges/connectors/ccxt/test_ccxt_client_util.py tests/exchanges/util/test_exchange_util.py tests/modes/test_abstract_mode_consumer.py -x` | 1 | 1 failed, 16 passed in 5.23s |
| full-current-tests | `.venv/bin/python -m pytest tests` | 1 | 2 failed, 900 passed, 3 errors in 66.94s (0:01:06) |
| final-existing-tests | `.venv/bin/python -m pytest tests` | 1 | 1 failed, 902 passed, 3 errors in 65.54s (0:01:05) |
| fixture-owned-tests | `.venv/bin/python -m pytest tests` | 4 | Check completed; see exact exit code. |
| fixture-owned-tests-2 | `.venv/bin/python -m pytest tests` | 1 | 3 failed, 902 passed in 291.25s (0:04:51) |
| transport-diagnosis-tests | `.venv/bin/python -X tracemalloc=10 -m pytest tests/exchanges/traders/test_trader.py` | 1 | 2 failed, 33 passed in 102.02s (0:01:42) |
| transport-owned-tests | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 1 | 3 failed, 32 passed in 14.67s |
| transport-abort-tests | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 1 | 3 failed, 32 passed in 13.74s |
| connection-diagnosis-tests | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` | 1 | 1 failed, 1 passed in 1.04s |
| allocation-diagnosis-tests | `.venv/bin/python -m pytest -s tests/exchanges/traders/test_trader.py::TestTrader::test_init_paused tests/exchanges/traders/test_trader.py::TestTrader::test_enabled` | 1 | 1 failed, 1 passed in 1.28s |
| stopped-paused-tests | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 1 | 2 failed, 33 passed in 13.86s |
| lazy-positional-tests | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 1 | 2 failed, 33 passed in 14.00s |
| scheduled-session-tests | `.venv/bin/python -m pytest tests/exchanges/traders/test_trader.py` | 0 | 35 passed in 14.46s |
| final-existing-tests-2 | `.venv/bin/python -m pytest tests` | 0 | 905 passed in 148.88s (0:02:28) |
| final-current-tests | `.venv/bin/python -m pytest tests` | 1 | 2 failed, 903 passed in 296.07s (0:04:56) |
| manager-owned-tests | `.venv/bin/python -m pytest tests` | 0 | 905 passed in 149.65s (0:02:29) |

Raw logs remain in the workspace maintenance evidence directory. The [portable verification record](maintenance/verification.json) retains exact command arrays, exits, timing, runtime inventory and log filenames. Earlier failed attempts remain recorded and are not treated as successful final validation.

## Historical installed dependency versions

This is the historical environment captured after its locked synchronization; isolated wheel build dependencies are resolved by the build backend and recorded in build output.

| Distribution | Version |
| --- | --- |
| aioboto3 | 15.5.0 |
| aiobotocore | 2.25.1 |
| aiofiles | 25.1.0 |
| aiohappyeyeballs | 2.7.1 |
| aiohttp | 3.14.5 |
| aiohttp-fast-zlib | 0.3.0 |
| aioitertools | 0.13.0 |
| aiosignal | 1.4.0 |
| aiosqlite | 0.22.1 |
| async_channel | 2.2.2 |
| attrs | 26.1.0 |
| boto3 | 1.40.61 |
| botocore | 1.40.61 |
| cachetools | 7.2.1 |
| ccxt | 4.5.85 |
| certifi | 2026.6.17 |
| cffi | 2.0.0 |
| charset-normalizer | 3.4.7 |
| coverage | 7.16.2 |
| cryptography | 50.0.2 |
| Cython | 3.3.0 |
| ecdsa | 0.19.2 |
| execnet | 2.1.2 |
| frozenlist | 1.8.0 |
| idna | 3.18 |
| iniconfig | 2.3.1 |
| Jinja2 | 3.1.6 |
| jmespath | 1.1.0 |
| jsonschema | 4.26.0 |
| jsonschema-specifications | 2025.9.1 |
| MarkupSafe | 3.0.4 |
| mock | 5.2.0 |
| multidict | 6.7.1 |
| numpy | 2.5.4 |
| octobot-backtesting | 1.10.0 |
| octobot-commons | 1.10.6 |
| octobot-tentacles-manager | 2.10.0+ayu.1 |
| octobot-trading | 2.5.13 |
| orjson | 3.11.9 |
| packaging | 26.3 |
| pluggy | 1.6.0 |
| propcache | 0.5.2 |
| psutil | 7.2.2 |
| pycparser | 3.0 |
| Pygments | 2.21.0 |
| pytest | 9.1.1 |
| pytest-asyncio | 1.4.0 |
| pytest-cov | 7.1.0 |
| pytest-timeout | 2.4.0 |
| pytest-xdist | 3.8.0 |
| python-dateutil | 2.9.0.post0 |
| PyYAML | 6.0.3 |
| referencing | 0.37.0 |
| requests | 2.34.2 |
| rpds-py | 2026.9.1 |
| ruff | 0.17.0 |
| s3transfer | 0.14.0 |
| six | 1.17.0 |
| sortedcontainers | 2.4.0 |
| tinydb | 4.9.0 |
| trading-backend | 1.2.43+ayu.1 |
| typing_extensions | 4.16.0 |
| urllib3 | 2.8.0 |
| uvloop | 0.22.1 |
| wrapt | 1.17.3 |
| yarl | 1.25.1 |
| zlib-ng | 1.0.0 |

See [architecture](ayu-develop.md) for source-linked component/sequence/workflow diagrams and [development](development.md) for reproducible uv commands.
