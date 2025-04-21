# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.pagination import SyncSlackChannelsCursor, AsyncSlackChannelsCursor
from knockapi.types.providers import (
    SlackCheckAuthResponse,
    SlackListChannelsResponse,
    SlackRevokeAccessResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSlack:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_check_auth(self, client: Knock) -> None:
        slack = client.providers.slack.check_auth(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )
        assert_matches_type(SlackCheckAuthResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_check_auth(self, client: Knock) -> None:
        response = client.providers.slack.with_raw_response.check_auth(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackCheckAuthResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_check_auth(self, client: Knock) -> None:
        with client.providers.slack.with_streaming_response.check_auth(
            channel_id="channel_id",
            access_token_object="access_token_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackCheckAuthResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_check_auth(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.providers.slack.with_raw_response.check_auth(
                channel_id="",
                access_token_object="access_token_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_channels(self, client: Knock) -> None:
        slack = client.providers.slack.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )
        assert_matches_type(SyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_channels_with_all_params(self, client: Knock) -> None:
        slack = client.providers.slack.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
            query_options={
                "cursor": "cursor",
                "exclude_archived": True,
                "limit": 0,
                "team_id": "team_id",
                "types": "types",
            },
        )
        assert_matches_type(SyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_channels(self, client: Knock) -> None:
        response = client.providers.slack.with_raw_response.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_channels(self, client: Knock) -> None:
        with client.providers.slack.with_streaming_response.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_channels(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.providers.slack.with_raw_response.list_channels(
                channel_id="",
                access_token_object="access_token_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_revoke_access(self, client: Knock) -> None:
        slack = client.providers.slack.revoke_access(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )
        assert_matches_type(SlackRevokeAccessResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_revoke_access(self, client: Knock) -> None:
        response = client.providers.slack.with_raw_response.revoke_access(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = response.parse()
        assert_matches_type(SlackRevokeAccessResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_revoke_access(self, client: Knock) -> None:
        with client.providers.slack.with_streaming_response.revoke_access(
            channel_id="channel_id",
            access_token_object="access_token_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = response.parse()
            assert_matches_type(SlackRevokeAccessResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_revoke_access(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.providers.slack.with_raw_response.revoke_access(
                channel_id="",
                access_token_object="access_token_object",
            )


class TestAsyncSlack:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_check_auth(self, async_client: AsyncKnock) -> None:
        slack = await async_client.providers.slack.check_auth(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )
        assert_matches_type(SlackCheckAuthResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_check_auth(self, async_client: AsyncKnock) -> None:
        response = await async_client.providers.slack.with_raw_response.check_auth(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackCheckAuthResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_check_auth(self, async_client: AsyncKnock) -> None:
        async with async_client.providers.slack.with_streaming_response.check_auth(
            channel_id="channel_id",
            access_token_object="access_token_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackCheckAuthResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_check_auth(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.providers.slack.with_raw_response.check_auth(
                channel_id="",
                access_token_object="access_token_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_channels(self, async_client: AsyncKnock) -> None:
        slack = await async_client.providers.slack.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )
        assert_matches_type(AsyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_channels_with_all_params(self, async_client: AsyncKnock) -> None:
        slack = await async_client.providers.slack.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
            query_options={
                "cursor": "cursor",
                "exclude_archived": True,
                "limit": 0,
                "team_id": "team_id",
                "types": "types",
            },
        )
        assert_matches_type(AsyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_channels(self, async_client: AsyncKnock) -> None:
        response = await async_client.providers.slack.with_raw_response.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(AsyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_channels(self, async_client: AsyncKnock) -> None:
        async with async_client.providers.slack.with_streaming_response.list_channels(
            channel_id="channel_id",
            access_token_object="access_token_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(AsyncSlackChannelsCursor[SlackListChannelsResponse], slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_channels(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.providers.slack.with_raw_response.list_channels(
                channel_id="",
                access_token_object="access_token_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_revoke_access(self, async_client: AsyncKnock) -> None:
        slack = await async_client.providers.slack.revoke_access(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )
        assert_matches_type(SlackRevokeAccessResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_revoke_access(self, async_client: AsyncKnock) -> None:
        response = await async_client.providers.slack.with_raw_response.revoke_access(
            channel_id="channel_id",
            access_token_object="access_token_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        slack = await response.parse()
        assert_matches_type(SlackRevokeAccessResponse, slack, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_revoke_access(self, async_client: AsyncKnock) -> None:
        async with async_client.providers.slack.with_streaming_response.revoke_access(
            channel_id="channel_id",
            access_token_object="access_token_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            slack = await response.parse()
            assert_matches_type(SlackRevokeAccessResponse, slack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_revoke_access(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.providers.slack.with_raw_response.revoke_access(
                channel_id="",
                access_token_object="access_token_object",
            )
