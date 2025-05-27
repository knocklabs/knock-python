# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import (
    Message,
    Activity,
    MessageEvent,
    MessageDeliveryLog,
    MessageGetContentResponse,
)
from knockapi.pagination import SyncItemsCursor, AsyncItemsCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list(self, client: Knock) -> None:
        message = client.messages.list()
        assert_matches_type(SyncItemsCursor[Message], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: Knock) -> None:
        message = client.messages.list(
            after="after",
            before="before",
            channel_id="channel_id",
            engagement_status=["seen"],
            inserted_at={
                "gt": "gt",
                "gte": "gte",
                "lt": "lt",
                "lte": "lte",
            },
            message_ids=["string"],
            page_size=0,
            source="source",
            status=["queued"],
            tenant="tenant",
            trigger_data="trigger_data",
            workflow_categories=["string"],
            workflow_recipient_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            workflow_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncItemsCursor[Message], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list(self, client: Knock) -> None:
        response = client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncItemsCursor[Message], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list(self, client: Knock) -> None:
        with client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncItemsCursor[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_archive(self, client: Knock) -> None:
        message = client.messages.archive(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_archive(self, client: Knock) -> None:
        response = client.messages.with_raw_response.archive(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_archive(self, client: Knock) -> None:
        with client.messages.with_streaming_response.archive(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_archive(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get(self, client: Knock) -> None:
        message = client.messages.get(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get(self, client: Knock) -> None:
        response = client.messages.with_raw_response.get(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get(self, client: Knock) -> None:
        with client.messages.with_streaming_response.get(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_content(self, client: Knock) -> None:
        message = client.messages.get_content(
            "message_id",
        )
        assert_matches_type(MessageGetContentResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_content(self, client: Knock) -> None:
        response = client.messages.with_raw_response.get_content(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetContentResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_content(self, client: Knock) -> None:
        with client.messages.with_streaming_response.get_content(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetContentResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_content(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.get_content(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_activities(self, client: Knock) -> None:
        message = client.messages.list_activities(
            message_id="message_id",
        )
        assert_matches_type(SyncItemsCursor[Activity], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_activities_with_all_params(self, client: Knock) -> None:
        message = client.messages.list_activities(
            message_id="message_id",
            after="after",
            before="before",
            page_size=0,
            trigger_data="trigger_data",
        )
        assert_matches_type(SyncItemsCursor[Activity], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_activities(self, client: Knock) -> None:
        response = client.messages.with_raw_response.list_activities(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncItemsCursor[Activity], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_activities(self, client: Knock) -> None:
        with client.messages.with_streaming_response.list_activities(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncItemsCursor[Activity], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_activities(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.list_activities(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_delivery_logs(self, client: Knock) -> None:
        message = client.messages.list_delivery_logs(
            message_id="message_id",
        )
        assert_matches_type(SyncItemsCursor[MessageDeliveryLog], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_delivery_logs_with_all_params(self, client: Knock) -> None:
        message = client.messages.list_delivery_logs(
            message_id="message_id",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(SyncItemsCursor[MessageDeliveryLog], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_delivery_logs(self, client: Knock) -> None:
        response = client.messages.with_raw_response.list_delivery_logs(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncItemsCursor[MessageDeliveryLog], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_delivery_logs(self, client: Knock) -> None:
        with client.messages.with_streaming_response.list_delivery_logs(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncItemsCursor[MessageDeliveryLog], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_delivery_logs(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.list_delivery_logs(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_events(self, client: Knock) -> None:
        message = client.messages.list_events(
            message_id="message_id",
        )
        assert_matches_type(SyncItemsCursor[MessageEvent], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_events_with_all_params(self, client: Knock) -> None:
        message = client.messages.list_events(
            message_id="message_id",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(SyncItemsCursor[MessageEvent], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_events(self, client: Knock) -> None:
        response = client.messages.with_raw_response.list_events(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncItemsCursor[MessageEvent], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_events(self, client: Knock) -> None:
        with client.messages.with_streaming_response.list_events(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncItemsCursor[MessageEvent], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_events(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.list_events(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_interacted(self, client: Knock) -> None:
        message = client.messages.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_interacted_with_all_params(self, client: Knock) -> None:
        message = client.messages.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
            metadata={"key": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_interacted(self, client: Knock) -> None:
        response = client.messages.with_raw_response.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_interacted(self, client: Knock) -> None:
        with client.messages.with_streaming_response.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_as_interacted(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.mark_as_interacted(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_read(self, client: Knock) -> None:
        message = client.messages.mark_as_read(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_read(self, client: Knock) -> None:
        response = client.messages.with_raw_response.mark_as_read(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_read(self, client: Knock) -> None:
        with client.messages.with_streaming_response.mark_as_read(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_as_read(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.mark_as_read(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_seen(self, client: Knock) -> None:
        message = client.messages.mark_as_seen(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_seen(self, client: Knock) -> None:
        response = client.messages.with_raw_response.mark_as_seen(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_seen(self, client: Knock) -> None:
        with client.messages.with_streaming_response.mark_as_seen(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_as_seen(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.mark_as_seen(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_unread(self, client: Knock) -> None:
        message = client.messages.mark_as_unread(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_unread(self, client: Knock) -> None:
        response = client.messages.with_raw_response.mark_as_unread(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_unread(self, client: Knock) -> None:
        with client.messages.with_streaming_response.mark_as_unread(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_as_unread(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.mark_as_unread(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_unseen(self, client: Knock) -> None:
        message = client.messages.mark_as_unseen(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_unseen(self, client: Knock) -> None:
        response = client.messages.with_raw_response.mark_as_unseen(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_unseen(self, client: Knock) -> None:
        with client.messages.with_streaming_response.mark_as_unseen(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_as_unseen(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.mark_as_unseen(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_unarchive(self, client: Knock) -> None:
        message = client.messages.unarchive(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_unarchive(self, client: Knock) -> None:
        response = client.messages.with_raw_response.unarchive(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_unarchive(self, client: Knock) -> None:
        with client.messages.with_streaming_response.unarchive(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_unarchive(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.unarchive(
                "",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list()
        assert_matches_type(AsyncItemsCursor[Message], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list(
            after="after",
            before="before",
            channel_id="channel_id",
            engagement_status=["seen"],
            inserted_at={
                "gt": "gt",
                "gte": "gte",
                "lt": "lt",
                "lte": "lte",
            },
            message_ids=["string"],
            page_size=0,
            source="source",
            status=["queued"],
            tenant="tenant",
            trigger_data="trigger_data",
            workflow_categories=["string"],
            workflow_recipient_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            workflow_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncItemsCursor[Message], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncItemsCursor[Message], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncItemsCursor[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_archive(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.archive(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.archive(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.archive(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.get(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.get(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.get(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_content(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.get_content(
            "message_id",
        )
        assert_matches_type(MessageGetContentResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_content(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.get_content(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetContentResponse, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_content(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.get_content(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetContentResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_content(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.get_content(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_activities(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list_activities(
            message_id="message_id",
        )
        assert_matches_type(AsyncItemsCursor[Activity], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_activities_with_all_params(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list_activities(
            message_id="message_id",
            after="after",
            before="before",
            page_size=0,
            trigger_data="trigger_data",
        )
        assert_matches_type(AsyncItemsCursor[Activity], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_activities(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.list_activities(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncItemsCursor[Activity], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_activities(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.list_activities(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncItemsCursor[Activity], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_activities(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.list_activities(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_delivery_logs(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list_delivery_logs(
            message_id="message_id",
        )
        assert_matches_type(AsyncItemsCursor[MessageDeliveryLog], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_delivery_logs_with_all_params(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list_delivery_logs(
            message_id="message_id",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(AsyncItemsCursor[MessageDeliveryLog], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_delivery_logs(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.list_delivery_logs(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncItemsCursor[MessageDeliveryLog], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_delivery_logs(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.list_delivery_logs(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncItemsCursor[MessageDeliveryLog], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_delivery_logs(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.list_delivery_logs(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_events(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list_events(
            message_id="message_id",
        )
        assert_matches_type(AsyncItemsCursor[MessageEvent], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.list_events(
            message_id="message_id",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(AsyncItemsCursor[MessageEvent], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.list_events(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncItemsCursor[MessageEvent], message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.list_events(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncItemsCursor[MessageEvent], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.list_events(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_interacted(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_interacted_with_all_params(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
            metadata={"key": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_interacted(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_interacted(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.mark_as_interacted(
            message_id="1jNaXzB2RZX3LY8wVQnfCKyPnv7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_as_interacted(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.mark_as_interacted(
                message_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_read(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.mark_as_read(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_read(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.mark_as_read(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_read(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.mark_as_read(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_as_read(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.mark_as_read(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_seen(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.mark_as_seen(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_seen(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.mark_as_seen(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_seen(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.mark_as_seen(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_as_seen(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.mark_as_seen(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_unread(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.mark_as_unread(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_unread(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.mark_as_unread(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_unread(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.mark_as_unread(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_as_unread(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.mark_as_unread(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_unseen(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.mark_as_unseen(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_unseen(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.mark_as_unseen(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_unseen(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.mark_as_unseen(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_as_unseen(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.mark_as_unseen(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncKnock) -> None:
        message = await async_client.messages.unarchive(
            "message_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.with_raw_response.unarchive(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.with_streaming_response.unarchive(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.unarchive(
                "",
            )
