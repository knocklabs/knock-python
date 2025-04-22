# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.pagination import SyncMsTeamsPagination, AsyncMsTeamsPagination
from knockapi.types.providers import (
    MsTeamCheckAuthResponse,
    MsTeamListTeamsResponse,
    MsTeamListChannelsResponse,
    MsTeamRevokeAccessResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMsTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_check_auth(self, client: Knock) -> None:
        ms_team = client.providers.ms_teams.check_auth(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )
        assert_matches_type(MsTeamCheckAuthResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_check_auth(self, client: Knock) -> None:
        response = client.providers.ms_teams.with_raw_response.check_auth(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = response.parse()
        assert_matches_type(MsTeamCheckAuthResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_check_auth(self, client: Knock) -> None:
        with client.providers.ms_teams.with_streaming_response.check_auth(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = response.parse()
            assert_matches_type(MsTeamCheckAuthResponse, ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_check_auth(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.providers.ms_teams.with_raw_response.check_auth(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_channels(self, client: Knock) -> None:
        ms_team = client.providers.ms_teams.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
        )
        assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_channels_with_all_params(self, client: Knock) -> None:
        ms_team = client.providers.ms_teams.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
            query_options={
                "filter": "$filter",
                "select": "$select",
            },
        )
        assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_channels(self, client: Knock) -> None:
        response = client.providers.ms_teams.with_raw_response.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = response.parse()
        assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_channels(self, client: Knock) -> None:
        with client.providers.ms_teams.with_streaming_response.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = response.parse()
            assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_channels(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.providers.ms_teams.with_raw_response.list_channels(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
                team_id="team_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_teams(self, client: Knock) -> None:
        ms_team = client.providers.ms_teams.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )
        assert_matches_type(SyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_teams_with_all_params(self, client: Knock) -> None:
        ms_team = client.providers.ms_teams.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            query_options={
                "filter": "$filter",
                "select": "$select",
                "skiptoken": "$skiptoken",
                "top": 0,
            },
        )
        assert_matches_type(SyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_teams(self, client: Knock) -> None:
        response = client.providers.ms_teams.with_raw_response.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = response.parse()
        assert_matches_type(SyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_teams(self, client: Knock) -> None:
        with client.providers.ms_teams.with_streaming_response.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = response.parse()
            assert_matches_type(SyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_teams(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.providers.ms_teams.with_raw_response.list_teams(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_revoke_access(self, client: Knock) -> None:
        ms_team = client.providers.ms_teams.revoke_access(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )
        assert_matches_type(MsTeamRevokeAccessResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_revoke_access(self, client: Knock) -> None:
        response = client.providers.ms_teams.with_raw_response.revoke_access(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = response.parse()
        assert_matches_type(MsTeamRevokeAccessResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_revoke_access(self, client: Knock) -> None:
        with client.providers.ms_teams.with_streaming_response.revoke_access(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = response.parse()
            assert_matches_type(MsTeamRevokeAccessResponse, ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_revoke_access(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.providers.ms_teams.with_raw_response.revoke_access(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
            )


class TestAsyncMsTeams:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_check_auth(self, async_client: AsyncKnock) -> None:
        ms_team = await async_client.providers.ms_teams.check_auth(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )
        assert_matches_type(MsTeamCheckAuthResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_check_auth(self, async_client: AsyncKnock) -> None:
        response = await async_client.providers.ms_teams.with_raw_response.check_auth(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = await response.parse()
        assert_matches_type(MsTeamCheckAuthResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_check_auth(self, async_client: AsyncKnock) -> None:
        async with async_client.providers.ms_teams.with_streaming_response.check_auth(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = await response.parse()
            assert_matches_type(MsTeamCheckAuthResponse, ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_check_auth(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.providers.ms_teams.with_raw_response.check_auth(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_channels(self, async_client: AsyncKnock) -> None:
        ms_team = await async_client.providers.ms_teams.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
        )
        assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_channels_with_all_params(self, async_client: AsyncKnock) -> None:
        ms_team = await async_client.providers.ms_teams.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
            query_options={
                "filter": "$filter",
                "select": "$select",
            },
        )
        assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_channels(self, async_client: AsyncKnock) -> None:
        response = await async_client.providers.ms_teams.with_raw_response.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = await response.parse()
        assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_channels(self, async_client: AsyncKnock) -> None:
        async with async_client.providers.ms_teams.with_streaming_response.list_channels(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            team_id="team_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = await response.parse()
            assert_matches_type(MsTeamListChannelsResponse, ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_channels(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.providers.ms_teams.with_raw_response.list_channels(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
                team_id="team_id",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_teams(self, async_client: AsyncKnock) -> None:
        ms_team = await async_client.providers.ms_teams.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )
        assert_matches_type(AsyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_teams_with_all_params(self, async_client: AsyncKnock) -> None:
        ms_team = await async_client.providers.ms_teams.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
            query_options={
                "filter": "$filter",
                "select": "$select",
                "skiptoken": "$skiptoken",
                "top": 0,
            },
        )
        assert_matches_type(AsyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_teams(self, async_client: AsyncKnock) -> None:
        response = await async_client.providers.ms_teams.with_raw_response.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = await response.parse()
        assert_matches_type(AsyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_teams(self, async_client: AsyncKnock) -> None:
        async with async_client.providers.ms_teams.with_streaming_response.list_teams(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = await response.parse()
            assert_matches_type(AsyncMsTeamsPagination[MsTeamListTeamsResponse], ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_teams(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.providers.ms_teams.with_raw_response.list_teams(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_revoke_access(self, async_client: AsyncKnock) -> None:
        ms_team = await async_client.providers.ms_teams.revoke_access(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )
        assert_matches_type(MsTeamRevokeAccessResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_revoke_access(self, async_client: AsyncKnock) -> None:
        response = await async_client.providers.ms_teams.with_raw_response.revoke_access(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ms_team = await response.parse()
        assert_matches_type(MsTeamRevokeAccessResponse, ms_team, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_revoke_access(self, async_client: AsyncKnock) -> None:
        async with async_client.providers.ms_teams.with_streaming_response.revoke_access(
            channel_id="channel_id",
            ms_teams_tenant_object="ms_teams_tenant_object",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ms_team = await response.parse()
            assert_matches_type(MsTeamRevokeAccessResponse, ms_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_revoke_access(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.providers.ms_teams.with_raw_response.revoke_access(
                channel_id="",
                ms_teams_tenant_object="ms_teams_tenant_object",
            )
