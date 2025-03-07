# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knock import Knock, AsyncKnock
from knock.types import (
    ObjectListMessagesResponse,
    ObjectListPreferencesResponse,
    ObjectAddSubscriptionsResponse,
    ObjectDeleteSubscriptionsResponse,
)
from tests.utils import assert_matches_type
from knock.pagination import SyncEntriesCursor, AsyncEntriesCursor
from knock.types.shared import Object, Schedule, ChannelData, Subscription, PreferenceSet

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list(self, client: Knock) -> None:
        object_ = client.objects.list(
            collection="collection",
        )
        assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.list(
            collection="collection",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list(self, client: Knock) -> None:
        response = client.objects.with_raw_response.list(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list(self, client: Knock) -> None:
        with client.objects.with_streaming_response.list(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.list(
                collection="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_delete(self, client: Knock) -> None:
        object_ = client.objects.delete(
            id="id",
            collection="collection",
        )
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_delete(self, client: Knock) -> None:
        response = client.objects.with_raw_response.delete(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_delete(self, client: Knock) -> None:
        with client.objects.with_streaming_response.delete(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(str, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_delete(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.delete(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objects.with_raw_response.delete(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_add_subscriptions(self, client: Knock) -> None:
        object_ = client.objects.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_add_subscriptions_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
            properties={"key": "bar"},
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_add_subscriptions(self, client: Knock) -> None:
        response = client.objects.with_raw_response.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_add_subscriptions(self, client: Knock) -> None:
        with client.objects.with_streaming_response.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_add_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.add_subscriptions(
                object_id="object_id",
                collection="",
                recipients=["user_1", "user_2"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.add_subscriptions(
                object_id="",
                collection="collection",
                recipients=["user_1", "user_2"],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_delete_subscriptions(self, client: Knock) -> None:
        object_ = client.objects.delete_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=[{"id": "user_1"}],
        )
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_delete_subscriptions(self, client: Knock) -> None:
        response = client.objects.with_raw_response.delete_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=[{"id": "user_1"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_delete_subscriptions(self, client: Knock) -> None:
        with client.objects.with_streaming_response.delete_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=[{"id": "user_1"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_delete_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.delete_subscriptions(
                object_id="object_id",
                collection="",
                recipients=[{"id": "user_1"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.delete_subscriptions(
                object_id="",
                collection="collection",
                recipients=[{"id": "user_1"}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get(self, client: Knock) -> None:
        object_ = client.objects.get(
            id="id",
            collection="collection",
        )
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get(self, client: Knock) -> None:
        response = client.objects.with_raw_response.get(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get(self, client: Knock) -> None:
        with client.objects.with_streaming_response.get(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(Object, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.get(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objects.with_raw_response.get(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_channel_data(self, client: Knock) -> None:
        object_ = client.objects.get_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_channel_data(self, client: Knock) -> None:
        response = client.objects.with_raw_response.get_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_channel_data(self, client: Knock) -> None:
        with client.objects.with_streaming_response.get_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.get_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.get_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.objects.with_raw_response.get_channel_data(
                channel_id="",
                collection="collection",
                object_id="object_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_preferences(self, client: Knock) -> None:
        object_ = client.objects.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_preferences_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
            tenant="tenant",
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_preferences(self, client: Knock) -> None:
        response = client.objects.with_raw_response.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_preferences(self, client: Knock) -> None:
        with client.objects.with_streaming_response.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(PreferenceSet, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_preferences(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.get_preferences(
                id="id",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.get_preferences(
                id="id",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objects.with_raw_response.get_preferences(
                id="",
                collection="collection",
                object_id="object_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_messages(self, client: Knock) -> None:
        object_ = client.objects.list_messages(
            id="project-123",
            collection="projects",
        )
        assert_matches_type(SyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_messages_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.list_messages(
            id="project-123",
            collection="projects",
            after="after",
            before="before",
            channel_id="channel_id",
            engagement_status=["seen"],
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
        assert_matches_type(SyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_messages(self, client: Knock) -> None:
        response = client.objects.with_raw_response.list_messages(
            id="project-123",
            collection="projects",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_messages(self, client: Knock) -> None:
        with client.objects.with_streaming_response.list_messages(
            id="project-123",
            collection="projects",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_messages(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.list_messages(
                id="project-123",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objects.with_raw_response.list_messages(
                id="",
                collection="projects",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_preferences(self, client: Knock) -> None:
        object_ = client.objects.list_preferences(
            object_id="object_id",
            collection="collection",
        )
        assert_matches_type(ObjectListPreferencesResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_preferences(self, client: Knock) -> None:
        response = client.objects.with_raw_response.list_preferences(
            object_id="object_id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectListPreferencesResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_preferences(self, client: Knock) -> None:
        with client.objects.with_streaming_response.list_preferences(
            object_id="object_id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectListPreferencesResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_preferences(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.list_preferences(
                object_id="object_id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.list_preferences(
                object_id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_schedules(self, client: Knock) -> None:
        object_ = client.objects.list_schedules(
            id="id",
            collection="collection",
        )
        assert_matches_type(SyncEntriesCursor[Schedule], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_schedules_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.list_schedules(
            id="id",
            collection="collection",
            after="after",
            before="before",
            page_size=0,
            tenant="tenant",
            workflow="workflow",
        )
        assert_matches_type(SyncEntriesCursor[Schedule], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_schedules(self, client: Knock) -> None:
        response = client.objects.with_raw_response.list_schedules(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncEntriesCursor[Schedule], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_schedules(self, client: Knock) -> None:
        with client.objects.with_streaming_response.list_schedules(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncEntriesCursor[Schedule], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_schedules(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.list_schedules(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objects.with_raw_response.list_schedules(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_subscriptions(self, client: Knock) -> None:
        object_ = client.objects.list_subscriptions(
            object_id="object_id",
            collection="collection",
        )
        assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_subscriptions_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.list_subscriptions(
            object_id="object_id",
            collection="collection",
            after="after",
            before="before",
            mode="recipient",
            page_size=0,
            recipients=["user_123"],
        )
        assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_subscriptions(self, client: Knock) -> None:
        response = client.objects.with_raw_response.list_subscriptions(
            object_id="object_id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: Knock) -> None:
        with client.objects.with_streaming_response.list_subscriptions(
            object_id="object_id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.list_subscriptions(
                object_id="object_id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.list_subscriptions(
                object_id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set(self, client: Knock) -> None:
        object_ = client.objects.set(
            id="id",
            collection="collection",
        )
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.set(
            id="id",
            collection="collection",
            channel_data={"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"data": {"tokens": ["push_token_xxx"]}}},
            preferences={
                "default": {
                    "categories": {
                        "transactional": {
                            "channel_types": {
                                "chat": True,
                                "email": False,
                                "http": True,
                                "in_app_feed": True,
                                "push": True,
                                "sms": True,
                            },
                            "conditions": [
                                {
                                    "argument": "some_property",
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                }
                            ],
                        }
                    },
                    "channel_types": {
                        "chat": True,
                        "email": True,
                        "http": True,
                        "in_app_feed": True,
                        "push": True,
                        "sms": True,
                    },
                    "workflows": {
                        "dinosaurs-loose": {
                            "channel_types": {
                                "chat": True,
                                "email": True,
                                "http": True,
                                "in_app_feed": True,
                                "push": True,
                                "sms": True,
                            },
                            "conditions": [
                                {
                                    "argument": "some_property",
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                }
                            ],
                        }
                    },
                }
            },
        )
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set(self, client: Knock) -> None:
        response = client.objects.with_raw_response.set(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_set(self, client: Knock) -> None:
        with client.objects.with_streaming_response.set(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(Object, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_set(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.set(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objects.with_raw_response.set(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_channel_data(self, client: Knock) -> None:
        object_ = client.objects.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_channel_data_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set_channel_data(self, client: Knock) -> None:
        response = client.objects.with_raw_response.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_set_channel_data(self, client: Knock) -> None:
        with client.objects.with_streaming_response.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_set_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.set_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="",
                object_id="object_id",
                data={"tokens": ["push_token_1"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.set_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="collection",
                object_id="",
                data={"tokens": ["push_token_1"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.objects.with_raw_response.set_channel_data(
                channel_id="",
                collection="collection",
                object_id="object_id",
                data={"tokens": ["push_token_1"]},
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_preferences(self, client: Knock) -> None:
        object_ = client.objects.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_preferences_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
            categories={
                "marketing": False,
                "transactional": {
                    "channel_types": {
                        "chat": True,
                        "email": False,
                        "http": True,
                        "in_app_feed": True,
                        "push": True,
                        "sms": True,
                    },
                    "conditions": [
                        {
                            "argument": "some_property",
                            "operator": "equal_to",
                            "variable": "recipient.property",
                        }
                    ],
                },
            },
            channel_types={
                "chat": True,
                "email": True,
                "http": True,
                "in_app_feed": True,
                "push": True,
                "sms": True,
            },
            workflows={
                "dinosaurs-loose": {
                    "channel_types": {
                        "chat": True,
                        "email": False,
                        "http": True,
                        "in_app_feed": True,
                        "push": True,
                        "sms": True,
                    },
                    "conditions": [
                        {
                            "argument": "some_property",
                            "operator": "equal_to",
                            "variable": "recipient.property",
                        }
                    ],
                }
            },
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set_preferences(self, client: Knock) -> None:
        response = client.objects.with_raw_response.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_set_preferences(self, client: Knock) -> None:
        with client.objects.with_streaming_response.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(PreferenceSet, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_set_preferences(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.set_preferences(
                id="id",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.set_preferences(
                id="id",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objects.with_raw_response.set_preferences(
                id="",
                collection="collection",
                object_id="object_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_unset_channel_data(self, client: Knock) -> None:
        object_ = client.objects.unset_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_unset_channel_data(self, client: Knock) -> None:
        response = client.objects.with_raw_response.unset_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_unset_channel_data(self, client: Knock) -> None:
        with client.objects.with_streaming_response.unset_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(str, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_unset_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.unset_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.unset_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.objects.with_raw_response.unset_channel_data(
                channel_id="",
                collection="collection",
                object_id="object_id",
            )


class TestAsyncObjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list(
            collection="collection",
        )
        assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list(
            collection="collection",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.list(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.list(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.list(
                collection="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.delete(
            id="id",
            collection="collection",
        )
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.delete(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.delete(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(str, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.delete(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objects.with_raw_response.delete(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_add_subscriptions(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_add_subscriptions_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
            properties={"key": "bar"},
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_add_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_add_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.add_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_add_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.add_subscriptions(
                object_id="object_id",
                collection="",
                recipients=["user_1", "user_2"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.add_subscriptions(
                object_id="",
                collection="collection",
                recipients=["user_1", "user_2"],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.delete_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=[{"id": "user_1"}],
        )
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.delete_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=[{"id": "user_1"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.delete_subscriptions(
            object_id="object_id",
            collection="collection",
            recipients=[{"id": "user_1"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.delete_subscriptions(
                object_id="object_id",
                collection="",
                recipients=[{"id": "user_1"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.delete_subscriptions(
                object_id="",
                collection="collection",
                recipients=[{"id": "user_1"}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.get(
            id="id",
            collection="collection",
        )
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.get(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.get(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(Object, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.get(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objects.with_raw_response.get(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_channel_data(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.get_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.get_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.get_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.get_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.get_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.objects.with_raw_response.get_channel_data(
                channel_id="",
                collection="collection",
                object_id="object_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_preferences(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_preferences_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
            tenant="tenant",
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_preferences(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_preferences(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.get_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(PreferenceSet, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_preferences(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.get_preferences(
                id="id",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.get_preferences(
                id="id",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objects.with_raw_response.get_preferences(
                id="",
                collection="collection",
                object_id="object_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_messages(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_messages(
            id="project-123",
            collection="projects",
        )
        assert_matches_type(AsyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_messages(
            id="project-123",
            collection="projects",
            after="after",
            before="before",
            channel_id="channel_id",
            engagement_status=["seen"],
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
        assert_matches_type(AsyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.list_messages(
            id="project-123",
            collection="projects",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.list_messages(
            id="project-123",
            collection="projects",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncEntriesCursor[ObjectListMessagesResponse], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.list_messages(
                id="project-123",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objects.with_raw_response.list_messages(
                id="",
                collection="projects",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_preferences(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_preferences(
            object_id="object_id",
            collection="collection",
        )
        assert_matches_type(ObjectListPreferencesResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_preferences(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.list_preferences(
            object_id="object_id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectListPreferencesResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_preferences(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.list_preferences(
            object_id="object_id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectListPreferencesResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_preferences(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.list_preferences(
                object_id="object_id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.list_preferences(
                object_id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_schedules(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_schedules(
            id="id",
            collection="collection",
        )
        assert_matches_type(AsyncEntriesCursor[Schedule], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_schedules_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_schedules(
            id="id",
            collection="collection",
            after="after",
            before="before",
            page_size=0,
            tenant="tenant",
            workflow="workflow",
        )
        assert_matches_type(AsyncEntriesCursor[Schedule], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_schedules(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.list_schedules(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Schedule], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_schedules(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.list_schedules(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Schedule], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_schedules(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.list_schedules(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objects.with_raw_response.list_schedules(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_subscriptions(
            object_id="object_id",
            collection="collection",
        )
        assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_subscriptions_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_subscriptions(
            object_id="object_id",
            collection="collection",
            after="after",
            before="before",
            mode="recipient",
            page_size=0,
            recipients=["user_123"],
        )
        assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.list_subscriptions(
            object_id="object_id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.list_subscriptions(
            object_id="object_id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.list_subscriptions(
                object_id="object_id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.list_subscriptions(
                object_id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.set(
            id="id",
            collection="collection",
        )
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.set(
            id="id",
            collection="collection",
            channel_data={"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"data": {"tokens": ["push_token_xxx"]}}},
            preferences={
                "default": {
                    "categories": {
                        "transactional": {
                            "channel_types": {
                                "chat": True,
                                "email": False,
                                "http": True,
                                "in_app_feed": True,
                                "push": True,
                                "sms": True,
                            },
                            "conditions": [
                                {
                                    "argument": "some_property",
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                }
                            ],
                        }
                    },
                    "channel_types": {
                        "chat": True,
                        "email": True,
                        "http": True,
                        "in_app_feed": True,
                        "push": True,
                        "sms": True,
                    },
                    "workflows": {
                        "dinosaurs-loose": {
                            "channel_types": {
                                "chat": True,
                                "email": True,
                                "http": True,
                                "in_app_feed": True,
                                "push": True,
                                "sms": True,
                            },
                            "conditions": [
                                {
                                    "argument": "some_property",
                                    "operator": "equal_to",
                                    "variable": "recipient.property",
                                }
                            ],
                        }
                    },
                }
            },
        )
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.set(
            id="id",
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(Object, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.set(
            id="id",
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(Object, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_set(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.set(
                id="id",
                collection="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objects.with_raw_response.set(
                id="",
                collection="collection",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_channel_data(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_channel_data_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_set_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.set_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
            data={"tokens": ["push_token_1"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_set_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.set_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="",
                object_id="object_id",
                data={"tokens": ["push_token_1"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.set_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="collection",
                object_id="",
                data={"tokens": ["push_token_1"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.objects.with_raw_response.set_channel_data(
                channel_id="",
                collection="collection",
                object_id="object_id",
                data={"tokens": ["push_token_1"]},
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_preferences(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_preferences_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
            categories={
                "marketing": False,
                "transactional": {
                    "channel_types": {
                        "chat": True,
                        "email": False,
                        "http": True,
                        "in_app_feed": True,
                        "push": True,
                        "sms": True,
                    },
                    "conditions": [
                        {
                            "argument": "some_property",
                            "operator": "equal_to",
                            "variable": "recipient.property",
                        }
                    ],
                },
            },
            channel_types={
                "chat": True,
                "email": True,
                "http": True,
                "in_app_feed": True,
                "push": True,
                "sms": True,
            },
            workflows={
                "dinosaurs-loose": {
                    "channel_types": {
                        "chat": True,
                        "email": False,
                        "http": True,
                        "in_app_feed": True,
                        "push": True,
                        "sms": True,
                    },
                    "conditions": [
                        {
                            "argument": "some_property",
                            "operator": "equal_to",
                            "variable": "recipient.property",
                        }
                    ],
                }
            },
        )
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set_preferences(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(PreferenceSet, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_set_preferences(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.set_preferences(
            id="id",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(PreferenceSet, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_set_preferences(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.set_preferences(
                id="id",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.set_preferences(
                id="id",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objects.with_raw_response.set_preferences(
                id="",
                collection="collection",
                object_id="object_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_unset_channel_data(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.unset_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_unset_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.unset_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_unset_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.unset_channel_data(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(str, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_unset_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.unset_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.unset_channel_data(
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                collection="collection",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.objects.with_raw_response.unset_channel_data(
                channel_id="",
                collection="collection",
                object_id="object_id",
            )
