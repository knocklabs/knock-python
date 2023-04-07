from unittest.mock import Mock

from knockapi.resources.workflows import Workflows

# Tests


def test_trigger():
    mocked_client = Mock()
    workflows = Workflows(mocked_client)
    workflows.trigger(
        "workflow-key",
        ["user-123"],
        {"foo": "bar"},
        actor="actor-123",
        cancellation_key="cancel-key",
        tenant="tenant-123",
        options={"idempotency_key": "123"})
    mocked_client.request.assert_called_with("post", "/workflows/workflow-key/trigger", payload={
        "actor": "actor-123",
        "recipients": ["user-123"],
        "data": {"foo": "bar"},
        "cancellation_key": "cancel-key",
        "tenant": "tenant-123"},
        options={'idempotency_key': '123'})
