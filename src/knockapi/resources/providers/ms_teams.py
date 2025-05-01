# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncMsTeamsPagination, AsyncMsTeamsPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.providers import (
    ms_team_check_auth_params,
    ms_team_list_teams_params,
    ms_team_list_channels_params,
    ms_team_revoke_access_params,
)
from ...types.providers.ms_team_check_auth_response import MsTeamCheckAuthResponse
from ...types.providers.ms_team_list_teams_response import MsTeamListTeamsResponse
from ...types.providers.ms_team_list_channels_response import MsTeamListChannelsResponse
from ...types.providers.ms_team_revoke_access_response import MsTeamRevokeAccessResponse

__all__ = ["MsTeamsResource", "AsyncMsTeamsResource"]


class MsTeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MsTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return MsTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MsTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return MsTeamsResourceWithStreamingResponse(self)

    def check_auth(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MsTeamCheckAuthResponse:
        """
        Check if a connection to Microsoft Teams has been authorized for a given
        Microsoft Teams tenant object.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/v1/providers/ms-teams/{channel_id}/auth_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"ms_teams_tenant_object": ms_teams_tenant_object}, ms_team_check_auth_params.MsTeamCheckAuthParams
                ),
            ),
            cast_to=MsTeamCheckAuthResponse,
        )

    def list_channels(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        team_id: str,
        query_options: ms_team_list_channels_params.QueryOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MsTeamListChannelsResponse:
        """List the Microsoft Teams channels within a team.

        By default, archived and
        private channels are excluded from the results.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          team_id: Microsoft Teams team ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/v1/providers/ms-teams/{channel_id}/channels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ms_teams_tenant_object": ms_teams_tenant_object,
                        "team_id": team_id,
                        "query_options": query_options,
                    },
                    ms_team_list_channels_params.MsTeamListChannelsParams,
                ),
            ),
            cast_to=MsTeamListChannelsResponse,
        )

    def list_teams(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        query_options: ms_team_list_teams_params.QueryOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncMsTeamsPagination[MsTeamListTeamsResponse]:
        """Get a list of teams belonging to the Microsoft Entra tenant.

        By default,
        archived and private channels are excluded from the results.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            f"/v1/providers/ms-teams/{channel_id}/teams",
            page=SyncMsTeamsPagination[MsTeamListTeamsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ms_teams_tenant_object": ms_teams_tenant_object,
                        "query_options": query_options,
                    },
                    ms_team_list_teams_params.MsTeamListTeamsParams,
                ),
            ),
            model=MsTeamListTeamsResponse,
        )

    def revoke_access(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MsTeamRevokeAccessResponse:
        """
        Remove a Microsoft Entra tenant ID from a Microsoft Teams tenant object.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._put(
            f"/v1/providers/ms-teams/{channel_id}/revoke_access",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"ms_teams_tenant_object": ms_teams_tenant_object},
                    ms_team_revoke_access_params.MsTeamRevokeAccessParams,
                ),
            ),
            cast_to=MsTeamRevokeAccessResponse,
        )


class AsyncMsTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMsTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMsTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMsTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncMsTeamsResourceWithStreamingResponse(self)

    async def check_auth(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MsTeamCheckAuthResponse:
        """
        Check if a connection to Microsoft Teams has been authorized for a given
        Microsoft Teams tenant object.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/v1/providers/ms-teams/{channel_id}/auth_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ms_teams_tenant_object": ms_teams_tenant_object}, ms_team_check_auth_params.MsTeamCheckAuthParams
                ),
            ),
            cast_to=MsTeamCheckAuthResponse,
        )

    async def list_channels(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        team_id: str,
        query_options: ms_team_list_channels_params.QueryOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MsTeamListChannelsResponse:
        """List the Microsoft Teams channels within a team.

        By default, archived and
        private channels are excluded from the results.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          team_id: Microsoft Teams team ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/v1/providers/ms-teams/{channel_id}/channels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ms_teams_tenant_object": ms_teams_tenant_object,
                        "team_id": team_id,
                        "query_options": query_options,
                    },
                    ms_team_list_channels_params.MsTeamListChannelsParams,
                ),
            ),
            cast_to=MsTeamListChannelsResponse,
        )

    def list_teams(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        query_options: ms_team_list_teams_params.QueryOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MsTeamListTeamsResponse, AsyncMsTeamsPagination[MsTeamListTeamsResponse]]:
        """Get a list of teams belonging to the Microsoft Entra tenant.

        By default,
        archived and private channels are excluded from the results.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            f"/v1/providers/ms-teams/{channel_id}/teams",
            page=AsyncMsTeamsPagination[MsTeamListTeamsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ms_teams_tenant_object": ms_teams_tenant_object,
                        "query_options": query_options,
                    },
                    ms_team_list_teams_params.MsTeamListTeamsParams,
                ),
            ),
            model=MsTeamListTeamsResponse,
        )

    async def revoke_access(
        self,
        channel_id: str,
        *,
        ms_teams_tenant_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MsTeamRevokeAccessResponse:
        """
        Remove a Microsoft Entra tenant ID from a Microsoft Teams tenant object.

        Args:
          ms_teams_tenant_object: A JSON encoded string containing the Microsoft Teams tenant object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._put(
            f"/v1/providers/ms-teams/{channel_id}/revoke_access",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"ms_teams_tenant_object": ms_teams_tenant_object},
                    ms_team_revoke_access_params.MsTeamRevokeAccessParams,
                ),
            ),
            cast_to=MsTeamRevokeAccessResponse,
        )


class MsTeamsResourceWithRawResponse:
    def __init__(self, ms_teams: MsTeamsResource) -> None:
        self._ms_teams = ms_teams

        self.check_auth = to_raw_response_wrapper(
            ms_teams.check_auth,
        )
        self.list_channels = to_raw_response_wrapper(
            ms_teams.list_channels,
        )
        self.list_teams = to_raw_response_wrapper(
            ms_teams.list_teams,
        )
        self.revoke_access = to_raw_response_wrapper(
            ms_teams.revoke_access,
        )


class AsyncMsTeamsResourceWithRawResponse:
    def __init__(self, ms_teams: AsyncMsTeamsResource) -> None:
        self._ms_teams = ms_teams

        self.check_auth = async_to_raw_response_wrapper(
            ms_teams.check_auth,
        )
        self.list_channels = async_to_raw_response_wrapper(
            ms_teams.list_channels,
        )
        self.list_teams = async_to_raw_response_wrapper(
            ms_teams.list_teams,
        )
        self.revoke_access = async_to_raw_response_wrapper(
            ms_teams.revoke_access,
        )


class MsTeamsResourceWithStreamingResponse:
    def __init__(self, ms_teams: MsTeamsResource) -> None:
        self._ms_teams = ms_teams

        self.check_auth = to_streamed_response_wrapper(
            ms_teams.check_auth,
        )
        self.list_channels = to_streamed_response_wrapper(
            ms_teams.list_channels,
        )
        self.list_teams = to_streamed_response_wrapper(
            ms_teams.list_teams,
        )
        self.revoke_access = to_streamed_response_wrapper(
            ms_teams.revoke_access,
        )


class AsyncMsTeamsResourceWithStreamingResponse:
    def __init__(self, ms_teams: AsyncMsTeamsResource) -> None:
        self._ms_teams = ms_teams

        self.check_auth = async_to_streamed_response_wrapper(
            ms_teams.check_auth,
        )
        self.list_channels = async_to_streamed_response_wrapper(
            ms_teams.list_channels,
        )
        self.list_teams = async_to_streamed_response_wrapper(
            ms_teams.list_teams,
        )
        self.revoke_access = async_to_streamed_response_wrapper(
            ms_teams.revoke_access,
        )
