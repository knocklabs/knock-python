# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import (
    User,
    Message,
    Schedule,
    UserListPreferencesResponse,
)
from knockapi._utils import parse_datetime
from knockapi.pagination import SyncItemsCursor, AsyncItemsCursor, SyncEntriesCursor, AsyncEntriesCursor
from knockapi.types.recipients import (
    ChannelData,
    Subscription,
    PreferenceSet,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update(self, client: Knock) -> None:
        user = client.users.update(
            user_id="user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update_with_all_params(self, client: Knock) -> None:
        user = client.users.update(
            user_id="user_id",
            avatar="avatar",
            channel_data={"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_123"]}},
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="ian.malcolm@chaos.theory",
            locale="locale",
            name="Dr. Ian Malcolm",
            phone_number="phone_number",
            preferences={
                "default": {
                    "categories": {
                        "marketing": {
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
                                    "argument": "frog_genome",
                                    "operator": "contains",
                                    "variable": "specimen.dna_sequence",
                                }
                            ],
                        },
                        "transactional": True,
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
                                    "argument": "frog_genome",
                                    "operator": "contains",
                                    "variable": "specimen.dna_sequence",
                                }
                            ],
                        }
                    },
                }
            },
            timezone="America/New_York",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_update(self, client: Knock) -> None:
        response = client.users.with_raw_response.update(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_update(self, client: Knock) -> None:
        with client.users.with_streaming_response.update(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_update(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list(self, client: Knock) -> None:
        user = client.users.list()
        assert_matches_type(SyncEntriesCursor[User], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: Knock) -> None:
        user = client.users.list(
            after="after",
            before="before",
            include=["preferences"],
            page_size=0,
        )
        assert_matches_type(SyncEntriesCursor[User], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list(self, client: Knock) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncEntriesCursor[User], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list(self, client: Knock) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncEntriesCursor[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_delete(self, client: Knock) -> None:
        user = client.users.delete(
            "user_id",
        )
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_delete(self, client: Knock) -> None:
        response = client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_delete(self, client: Knock) -> None:
        with client.users.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_delete(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get(self, client: Knock) -> None:
        user = client.users.get(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get(self, client: Knock) -> None:
        response = client.users.with_raw_response.get(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get(self, client: Knock) -> None:
        with client.users.with_streaming_response.get(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_channel_data(self, client: Knock) -> None:
        user = client.users.get_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_channel_data(self, client: Knock) -> None:
        response = client.users.with_raw_response.get_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_channel_data(self, client: Knock) -> None:
        with client.users.with_streaming_response.get_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ChannelData, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.get_channel_data(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.users.with_raw_response.get_channel_data(
                user_id="user_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_preferences(self, client: Knock) -> None:
        user = client.users.get_preferences(
            user_id="user_id",
            id="default",
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_preferences_with_all_params(self, client: Knock) -> None:
        user = client.users.get_preferences(
            user_id="user_id",
            id="default",
            tenant="tenant",
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_preferences(self, client: Knock) -> None:
        response = client.users.with_raw_response.get_preferences(
            user_id="user_id",
            id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_preferences(self, client: Knock) -> None:
        with client.users.with_streaming_response.get_preferences(
            user_id="user_id",
            id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(PreferenceSet, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_preferences(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.get_preferences(
                user_id="",
                id="default",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.get_preferences(
                user_id="user_id",
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_messages(self, client: Knock) -> None:
        user = client.users.list_messages(
            user_id="user-123",
        )
        assert_matches_type(SyncItemsCursor[Message], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_messages_with_all_params(self, client: Knock) -> None:
        user = client.users.list_messages(
            user_id="user-123",
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
        assert_matches_type(SyncItemsCursor[Message], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_messages(self, client: Knock) -> None:
        response = client.users.with_raw_response.list_messages(
            user_id="user-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncItemsCursor[Message], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_messages(self, client: Knock) -> None:
        with client.users.with_streaming_response.list_messages(
            user_id="user-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncItemsCursor[Message], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_messages(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.list_messages(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_preferences(self, client: Knock) -> None:
        user = client.users.list_preferences(
            "user_id",
        )
        assert_matches_type(UserListPreferencesResponse, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_preferences(self, client: Knock) -> None:
        response = client.users.with_raw_response.list_preferences(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListPreferencesResponse, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_preferences(self, client: Knock) -> None:
        with client.users.with_streaming_response.list_preferences(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListPreferencesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_preferences(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.list_preferences(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_schedules(self, client: Knock) -> None:
        user = client.users.list_schedules(
            user_id="user_id",
        )
        assert_matches_type(SyncEntriesCursor[Schedule], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_schedules_with_all_params(self, client: Knock) -> None:
        user = client.users.list_schedules(
            user_id="user_id",
            after="after",
            before="before",
            page_size=0,
            tenant="tenant",
            workflow="workflow",
        )
        assert_matches_type(SyncEntriesCursor[Schedule], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_schedules(self, client: Knock) -> None:
        response = client.users.with_raw_response.list_schedules(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncEntriesCursor[Schedule], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_schedules(self, client: Knock) -> None:
        with client.users.with_streaming_response.list_schedules(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncEntriesCursor[Schedule], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_schedules(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.list_schedules(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_subscriptions(self, client: Knock) -> None:
        user = client.users.list_subscriptions(
            user_id="user_id",
        )
        assert_matches_type(SyncEntriesCursor[Subscription], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_subscriptions_with_all_params(self, client: Knock) -> None:
        user = client.users.list_subscriptions(
            user_id="user_id",
            after="after",
            before="before",
            include=["preferences"],
            objects=["user_123"],
            page_size=0,
        )
        assert_matches_type(SyncEntriesCursor[Subscription], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_subscriptions(self, client: Knock) -> None:
        response = client.users.with_raw_response.list_subscriptions(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncEntriesCursor[Subscription], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: Knock) -> None:
        with client.users.with_streaming_response.list_subscriptions(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncEntriesCursor[Subscription], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.list_subscriptions(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_merge(self, client: Knock) -> None:
        user = client.users.merge(
            user_id="user_id",
            from_user_id="user_1",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_merge(self, client: Knock) -> None:
        response = client.users.with_raw_response.merge(
            user_id="user_id",
            from_user_id="user_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_merge(self, client: Knock) -> None:
        with client.users.with_streaming_response.merge(
            user_id="user_id",
            from_user_id="user_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_merge(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.merge(
                user_id="",
                from_user_id="user_1",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_channel_data(self, client: Knock) -> None:
        user = client.users.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_channel_data_with_all_params(self, client: Knock) -> None:
        user = client.users.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set_channel_data(self, client: Knock) -> None:
        response = client.users.with_raw_response.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_set_channel_data(self, client: Knock) -> None:
        with client.users.with_streaming_response.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ChannelData, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_set_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.set_channel_data(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data={"tokens": ["push_token_1"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.users.with_raw_response.set_channel_data(
                user_id="user_id",
                channel_id="",
                data={"tokens": ["push_token_1"]},
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_preferences(self, client: Knock) -> None:
        user = client.users.set_preferences(
            user_id="user_id",
            id="default",
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_preferences_with_all_params(self, client: Knock) -> None:
        user = client.users.set_preferences(
            user_id="user_id",
            id="default",
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
                            "argument": "frog_genome",
                            "operator": "contains",
                            "variable": "specimen.dna_sequence",
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
                            "argument": "frog_genome",
                            "operator": "contains",
                            "variable": "specimen.dna_sequence",
                        }
                    ],
                }
            },
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set_preferences(self, client: Knock) -> None:
        response = client.users.with_raw_response.set_preferences(
            user_id="user_id",
            id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_set_preferences(self, client: Knock) -> None:
        with client.users.with_streaming_response.set_preferences(
            user_id="user_id",
            id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(PreferenceSet, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_set_preferences(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.set_preferences(
                user_id="",
                id="default",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.with_raw_response.set_preferences(
                user_id="user_id",
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_unset_channel_data(self, client: Knock) -> None:
        user = client.users.unset_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_unset_channel_data(self, client: Knock) -> None:
        response = client.users.with_raw_response.unset_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_unset_channel_data(self, client: Knock) -> None:
        with client.users.with_streaming_response.unset_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_unset_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.unset_channel_data(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.users.with_raw_response.unset_channel_data(
                user_id="user_id",
                channel_id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.update(
            user_id="user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.update(
            user_id="user_id",
            avatar="avatar",
            channel_data={"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_123"]}},
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="ian.malcolm@chaos.theory",
            locale="locale",
            name="Dr. Ian Malcolm",
            phone_number="phone_number",
            preferences={
                "default": {
                    "categories": {
                        "marketing": {
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
                                    "argument": "frog_genome",
                                    "operator": "contains",
                                    "variable": "specimen.dna_sequence",
                                }
                            ],
                        },
                        "transactional": True,
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
                                    "argument": "frog_genome",
                                    "operator": "contains",
                                    "variable": "specimen.dna_sequence",
                                }
                            ],
                        }
                    },
                }
            },
            timezone="America/New_York",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.update(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.update(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_update(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list()
        assert_matches_type(AsyncEntriesCursor[User], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list(
            after="after",
            before="before",
            include=["preferences"],
            page_size=0,
        )
        assert_matches_type(AsyncEntriesCursor[User], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncEntriesCursor[User], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncEntriesCursor[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.delete(
            "user_id",
        )
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.get(
            "user_id",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.get(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.get(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_channel_data(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.get_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.get_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.get_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ChannelData, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.get_channel_data(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.users.with_raw_response.get_channel_data(
                user_id="user_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_preferences(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.get_preferences(
            user_id="user_id",
            id="default",
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_preferences_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.get_preferences(
            user_id="user_id",
            id="default",
            tenant="tenant",
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_preferences(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.get_preferences(
            user_id="user_id",
            id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_preferences(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.get_preferences(
            user_id="user_id",
            id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(PreferenceSet, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_preferences(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.get_preferences(
                user_id="",
                id="default",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.get_preferences(
                user_id="user_id",
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_messages(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list_messages(
            user_id="user-123",
        )
        assert_matches_type(AsyncItemsCursor[Message], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list_messages(
            user_id="user-123",
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
        assert_matches_type(AsyncItemsCursor[Message], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.list_messages(
            user_id="user-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncItemsCursor[Message], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.list_messages(
            user_id="user-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncItemsCursor[Message], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.list_messages(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_preferences(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list_preferences(
            "user_id",
        )
        assert_matches_type(UserListPreferencesResponse, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_preferences(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.list_preferences(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListPreferencesResponse, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_preferences(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.list_preferences(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListPreferencesResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_preferences(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.list_preferences(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_schedules(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list_schedules(
            user_id="user_id",
        )
        assert_matches_type(AsyncEntriesCursor[Schedule], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_schedules_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list_schedules(
            user_id="user_id",
            after="after",
            before="before",
            page_size=0,
            tenant="tenant",
            workflow="workflow",
        )
        assert_matches_type(AsyncEntriesCursor[Schedule], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_schedules(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.list_schedules(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Schedule], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_schedules(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.list_schedules(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Schedule], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_schedules(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.list_schedules(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list_subscriptions(
            user_id="user_id",
        )
        assert_matches_type(AsyncEntriesCursor[Subscription], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_subscriptions_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.list_subscriptions(
            user_id="user_id",
            after="after",
            before="before",
            include=["preferences"],
            objects=["user_123"],
            page_size=0,
        )
        assert_matches_type(AsyncEntriesCursor[Subscription], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.list_subscriptions(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Subscription], user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.list_subscriptions(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Subscription], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.list_subscriptions(
                user_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_merge(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.merge(
            user_id="user_id",
            from_user_id="user_1",
        )
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.merge(
            user_id="user_id",
            from_user_id="user_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.merge(
            user_id="user_id",
            from_user_id="user_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_merge(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.merge(
                user_id="",
                from_user_id="user_1",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_channel_data(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_channel_data_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        )
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ChannelData, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_set_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.set_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={"tokens": ["push_token_1"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ChannelData, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_set_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.set_channel_data(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data={"tokens": ["push_token_1"]},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.users.with_raw_response.set_channel_data(
                user_id="user_id",
                channel_id="",
                data={"tokens": ["push_token_1"]},
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_preferences(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.set_preferences(
            user_id="user_id",
            id="default",
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_preferences_with_all_params(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.set_preferences(
            user_id="user_id",
            id="default",
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
                            "argument": "frog_genome",
                            "operator": "contains",
                            "variable": "specimen.dna_sequence",
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
                            "argument": "frog_genome",
                            "operator": "contains",
                            "variable": "specimen.dna_sequence",
                        }
                    ],
                }
            },
        )
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set_preferences(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.set_preferences(
            user_id="user_id",
            id="default",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(PreferenceSet, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_set_preferences(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.set_preferences(
            user_id="user_id",
            id="default",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(PreferenceSet, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_set_preferences(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.set_preferences(
                user_id="",
                id="default",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.with_raw_response.set_preferences(
                user_id="user_id",
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_unset_channel_data(self, async_client: AsyncKnock) -> None:
        user = await async_client.users.unset_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_unset_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.with_raw_response.unset_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(str, user, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_unset_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.users.with_streaming_response.unset_channel_data(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_unset_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.unset_channel_data(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.users.with_raw_response.unset_channel_data(
                user_id="user_id",
                channel_id="",
            )
