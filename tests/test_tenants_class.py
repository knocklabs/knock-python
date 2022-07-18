from unittest.mock import Mock

from knockapi.resources.tenants import Tenants

# Tests


def test_list():
    mocked_client = Mock()
    tenants = Tenants(mocked_client)
    tenants.list()
    mocked_client.request.assert_called_with("get", "/tenants")


def test_get():
    mocked_client = Mock()
    tenants = Tenants(mocked_client)
    tenants.get("tenant-123")
    mocked_client.request.assert_called_with("get", "/tenants/tenant-123")


def test_delete():
    mocked_client = Mock()
    tenants = Tenants(mocked_client)
    tenants.delete("tenant-123")
    mocked_client.request.assert_called_with("delete", "/tenants/tenant-123")


def test_set():
    mocked_client = Mock()
    tenants = Tenants(mocked_client)
    tenants.set_tenant("tenant-123", {"name": "Tenant 1"})
    mocked_client.request.assert_called_with(
        "put", "/tenants/tenant-123", payload={'name': 'Tenant 1'})
