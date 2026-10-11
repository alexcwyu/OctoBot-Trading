"""Release HTTP sessions allocated by mocked exchange test setups."""
import asyncio

import aiohttp
import pytest_asyncio

from octobot_trading.exchanges.exchange_manager import ExchangeManager
from octobot_trading.exchanges.types.rest_exchange import RestExchange


@pytest_asyncio.fixture(autouse=True)
async def close_test_http_sessions(monkeypatch):
    sessions = []
    managers = []
    manager_init = ExchangeManager.__init__
    manager_stop = ExchangeManager.stop

    def tracked_manager_init(self, *args, **kwargs):
        manager_init(self, *args, **kwargs)
        managers.append(self)

    monkeypatch.setattr(ExchangeManager, "__init__", tracked_manager_init)
    original_init = aiohttp.ClientSession.__init__

    def tracked_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        sessions.append(self)

    monkeypatch.setattr(aiohttp.ClientSession, "__init__", tracked_init)
    yield
    for manager in managers:
        if isinstance(manager.exchange, RestExchange):
            await manager_stop(manager)
    await asyncio.sleep(0)
    for session in sessions:
        await session.close()
    # TLS transports finish asynchronously after ClientSession.close().
    if sessions:
        await asyncio.sleep(0.25)
