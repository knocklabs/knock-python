import pytest

from unittest.mock import AsyncMock
from knockapi.async_client.services.tenants import Tenants


@pytest.mark.asyncio
async def test_list():
    mocked_client = AsyncMock()
    tenants = Tenants(mocked_client)
    await tenants.list()
    mocked_client.connection.request.assert_awaited_with("get", "/tenants")


@pytest.mark.asyncio
async def test_get():
    mocked_client = AsyncMock()
    tenants = Tenants(mocked_client)
    await tenants.get("tenant-123")
    mocked_client.connection.request.assert_awaited_with("get", "/tenants/tenant-123")


@pytest.mark.asyncio
async def test_delete():
    mocked_client = AsyncMock()
    tenants = Tenants(mocked_client)
    await tenants.delete("tenant-123")
    mocked_client.connection.request.assert_awaited_with("delete", "/tenants/tenant-123")


@pytest.mark.asyncio
async def test_set():
    mocked_client = AsyncMock()
    tenants = Tenants(mocked_client)
    await tenants.set_tenant("tenant-123", {"name": "Tenant 1"})
    mocked_client.connection.request.assert_awaited_with(
        "put", "/tenants/tenant-123", payload={'name': 'Tenant 1'})
