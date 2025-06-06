# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from .feeds import (
    FeedsResource,
    AsyncFeedsResource,
    FeedsResourceWithRawResponse,
    AsyncFeedsResourceWithRawResponse,
    FeedsResourceWithStreamingResponse,
    AsyncFeedsResourceWithStreamingResponse,
)
from .guides import (
    GuidesResource,
    AsyncGuidesResource,
    GuidesResourceWithRawResponse,
    AsyncGuidesResourceWithRawResponse,
    GuidesResourceWithStreamingResponse,
    AsyncGuidesResourceWithStreamingResponse,
)
from ...types import (
    user_list_params,
    user_merge_params,
    user_update_params,
    user_list_messages_params,
    user_list_schedules_params,
    user_get_preferences_params,
    user_set_preferences_params,
    user_set_channel_data_params,
    user_list_subscriptions_params,
)
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
from ...pagination import SyncItemsCursor, AsyncItemsCursor, SyncEntriesCursor, AsyncEntriesCursor
from ...types.user import User
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message import Message
from ...types.schedule import Schedule
from ...types.recipients.channel_data import ChannelData
from ...types.recipients.subscription import Subscription
from ...types.recipient_reference_param import RecipientReferenceParam
from ...types.recipients.preference_set import PreferenceSet
from ...types.user_list_preferences_response import UserListPreferencesResponse
from ...types.recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from ...types.recipients.preference_set_channel_types_param import PreferenceSetChannelTypesParam
from ...types.recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def feeds(self) -> FeedsResource:
        return FeedsResource(self._client)

    @cached_property
    def guides(self) -> GuidesResource:
        return GuidesResource(self._client)

    @cached_property
    def bulk(self) -> BulkResource:
        return BulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        channel_data: Optional[InlineChannelDataRequestParam] | NotGiven = NOT_GIVEN,
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        locale: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        preferences: Optional[InlinePreferenceSetRequestParam] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Create or update a user with the provided identification data.

        When you identify
        an existing user, the system merges the properties you specific with what is
        currently set on the user, updating only the fields included in your requests.

        Args:
          avatar: URL to the user's avatar image.

          channel_data: A request to set channel data for a type of channel inline.

          created_at: The creation date of the user from your system.

          email: The primary email address for the user.

          locale: The locale of the user. Used for [message localization](/concepts/translations).

          name: Display name of the user.

          phone_number: The [E.164](https://www.twilio.com/docs/glossary/what-e164) phone number of the
              user (required for SMS channels).

          preferences: Inline set preferences for a recipient, where the key is the preference set id.

          timezone: The timezone of the user. Must be a
              valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
              Used
              for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/v1/users/{user_id}",
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "channel_data": channel_data,
                    "created_at": created_at,
                    "email": email,
                    "locale": locale,
                    "name": name,
                    "phone_number": phone_number,
                    "preferences": preferences,
                    "timezone": timezone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[User]:
        """Retrieve a paginated list of users in the environment.

        Defaults to 50 users per
        page.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Associated resources to include in the response.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/users",
            page=SyncEntriesCursor[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "page_size": page_size,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Permanently delete a user and all associated data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            f"/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def get(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Retrieve a specific user by their ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def get_channel_data(
        self,
        user_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Retrieves the channel data for a specific user and channel ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/v1/users/{user_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    def get_preferences(
        self,
        user_id: str,
        id: str,
        *,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """
        Retrieves a specific preference set for a user identified by the preference set
        ID.

        Args:
          tenant: The unique identifier for the tenant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/users/{user_id}/preferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tenant": tenant}, user_get_preferences_params.UserGetPreferencesParams),
            ),
            cast_to=PreferenceSet,
        )

    def list_messages(
        self,
        user_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        channel_id: str | NotGiven = NOT_GIVEN,
        engagement_status: List[
            Literal["seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"]
        ]
        | NotGiven = NOT_GIVEN,
        inserted_at: user_list_messages_params.InsertedAt | NotGiven = NOT_GIVEN,
        message_ids: List[str] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
        | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        workflow_categories: List[str] | NotGiven = NOT_GIVEN,
        workflow_recipient_run_id: str | NotGiven = NOT_GIVEN,
        workflow_run_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncItemsCursor[Message]:
        """Returns a paginated list of messages for a specific user.

        Allows filtering by
        message status and provides various sorting options. Messages outside the
        account's retention window will not be included in the results.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          channel_id: Limits the results to items with the corresponding channel ID.

          engagement_status: Limits the results to messages with the given engagement status.

          message_ids: Limits the results to only the message IDs given (max 50). Note: when using this
              option, the results will be subject to any other filters applied to the query.

          page_size: The number of items per page.

          source: Limits the results to messages triggered by the given workflow key.

          status: Limits the results to messages with the given delivery status.

          tenant: Limits the results to items with the corresponding tenant.

          trigger_data: Limits the results to only messages that were generated with the given data. See
              [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
              more information.

          workflow_categories: Limits the results to messages related to any of the provided categories.

          workflow_recipient_run_id: Limits the results to messages for a specific recipient's workflow run.

          workflow_run_id: Limits the results to messages associated with the top-level workflow run ID
              returned by the workflow trigger request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/messages",
            page=SyncItemsCursor[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "channel_id": channel_id,
                        "engagement_status": engagement_status,
                        "inserted_at": inserted_at,
                        "message_ids": message_ids,
                        "page_size": page_size,
                        "source": source,
                        "status": status,
                        "tenant": tenant,
                        "trigger_data": trigger_data,
                        "workflow_categories": workflow_categories,
                        "workflow_recipient_run_id": workflow_recipient_run_id,
                        "workflow_run_id": workflow_run_id,
                    },
                    user_list_messages_params.UserListMessagesParams,
                ),
            ),
            model=Message,
        )

    def list_preferences(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPreferencesResponse:
        """
        Retrieves a list of all preference sets for a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/v1/users/{user_id}/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListPreferencesResponse,
        )

    def list_schedules(
        self,
        user_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        workflow: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Schedule]:
        """
        Returns a paginated list of schedules for a specific user, in descending order.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          tenant: The tenant ID to filter schedules for.

          workflow: The workflow key to filter schedules for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/schedules",
            page=SyncEntriesCursor[Schedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "page_size": page_size,
                        "tenant": tenant,
                        "workflow": workflow,
                    },
                    user_list_schedules_params.UserListSchedulesParams,
                ),
            ),
            model=Schedule,
        )

    def list_subscriptions(
        self,
        user_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        objects: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Subscription]:
        """
        Retrieves a paginated list of subscriptions for a specific user, in descending
        order.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Associated resources to include in the response.

          objects: Only returns subscriptions for the specified object references.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/subscriptions",
            page=SyncEntriesCursor[Subscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "objects": objects,
                        "page_size": page_size,
                    },
                    user_list_subscriptions_params.UserListSubscriptionsParams,
                ),
            ),
            model=Subscription,
        )

    def merge(
        self,
        user_id: str,
        *,
        from_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Merge two users together, where the user specified with the `from_user_id` param
        will be merged into the user specified by `user_id`.

        Args:
          from_user_id: The user ID to merge from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/v1/users/{user_id}/merge",
            body=maybe_transform({"from_user_id": from_user_id}, user_merge_params.UserMergeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def set_channel_data(
        self,
        user_id: str,
        channel_id: str,
        *,
        data: user_set_channel_data_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """Updates or creates channel data for a specific user and channel ID.

        If no user
        exists in the current environment for the given `user_id`, Knock will create the
        user entry as part of this request.

        Args:
          data: Channel data for a given channel type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._put(
            f"/v1/users/{user_id}/channel_data/{channel_id}",
            body=maybe_transform({"data": data}, user_set_channel_data_params.UserSetChannelDataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    def set_preferences(
        self,
        user_id: str,
        id: str,
        *,
        categories: Optional[Dict[str, user_set_preferences_params.Categories]] | NotGiven = NOT_GIVEN,
        channel_types: Optional[PreferenceSetChannelTypesParam] | NotGiven = NOT_GIVEN,
        workflows: Optional[Dict[str, user_set_preferences_params.Workflows]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """Updates a complete preference set for a user.

        This is a destructive operation
        that will replace the existing preference set for the user.

        Args:
          categories: An object where the key is the category and the values are the preference
              settings for that category.

          channel_types: Channel type preferences.

          workflows: An object where the key is the workflow key and the values are the preference
              settings for that workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/users/{user_id}/preferences/{id}",
            body=maybe_transform(
                {
                    "categories": categories,
                    "channel_types": channel_types,
                    "workflows": workflows,
                },
                user_set_preferences_params.UserSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSet,
        )

    def unset_channel_data(
        self,
        user_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Deletes channel data for a specific user and channel ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._delete(
            f"/v1/users/{user_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def feeds(self) -> AsyncFeedsResource:
        return AsyncFeedsResource(self._client)

    @cached_property
    def guides(self) -> AsyncGuidesResource:
        return AsyncGuidesResource(self._client)

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        return AsyncBulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        channel_data: Optional[InlineChannelDataRequestParam] | NotGiven = NOT_GIVEN,
        created_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        locale: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_number: Optional[str] | NotGiven = NOT_GIVEN,
        preferences: Optional[InlinePreferenceSetRequestParam] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Create or update a user with the provided identification data.

        When you identify
        an existing user, the system merges the properties you specific with what is
        currently set on the user, updating only the fields included in your requests.

        Args:
          avatar: URL to the user's avatar image.

          channel_data: A request to set channel data for a type of channel inline.

          created_at: The creation date of the user from your system.

          email: The primary email address for the user.

          locale: The locale of the user. Used for [message localization](/concepts/translations).

          name: Display name of the user.

          phone_number: The [E.164](https://www.twilio.com/docs/glossary/what-e164) phone number of the
              user (required for SMS channels).

          preferences: Inline set preferences for a recipient, where the key is the preference set id.

          timezone: The timezone of the user. Must be a
              valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
              Used
              for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/v1/users/{user_id}",
            body=await async_maybe_transform(
                {
                    "avatar": avatar,
                    "channel_data": channel_data,
                    "created_at": created_at,
                    "email": email,
                    "locale": locale,
                    "name": name,
                    "phone_number": phone_number,
                    "preferences": preferences,
                    "timezone": timezone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[User, AsyncEntriesCursor[User]]:
        """Retrieve a paginated list of users in the environment.

        Defaults to 50 users per
        page.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Associated resources to include in the response.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/users",
            page=AsyncEntriesCursor[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "page_size": page_size,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=User,
        )

    async def delete(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Permanently delete a user and all associated data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            f"/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def get(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Retrieve a specific user by their ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/v1/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def get_channel_data(
        self,
        user_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Retrieves the channel data for a specific user and channel ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/v1/users/{user_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    async def get_preferences(
        self,
        user_id: str,
        id: str,
        *,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """
        Retrieves a specific preference set for a user identified by the preference set
        ID.

        Args:
          tenant: The unique identifier for the tenant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/users/{user_id}/preferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant": tenant}, user_get_preferences_params.UserGetPreferencesParams
                ),
            ),
            cast_to=PreferenceSet,
        )

    def list_messages(
        self,
        user_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        channel_id: str | NotGiven = NOT_GIVEN,
        engagement_status: List[
            Literal["seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"]
        ]
        | NotGiven = NOT_GIVEN,
        inserted_at: user_list_messages_params.InsertedAt | NotGiven = NOT_GIVEN,
        message_ids: List[str] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
        | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        workflow_categories: List[str] | NotGiven = NOT_GIVEN,
        workflow_recipient_run_id: str | NotGiven = NOT_GIVEN,
        workflow_run_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Message, AsyncItemsCursor[Message]]:
        """Returns a paginated list of messages for a specific user.

        Allows filtering by
        message status and provides various sorting options. Messages outside the
        account's retention window will not be included in the results.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          channel_id: Limits the results to items with the corresponding channel ID.

          engagement_status: Limits the results to messages with the given engagement status.

          message_ids: Limits the results to only the message IDs given (max 50). Note: when using this
              option, the results will be subject to any other filters applied to the query.

          page_size: The number of items per page.

          source: Limits the results to messages triggered by the given workflow key.

          status: Limits the results to messages with the given delivery status.

          tenant: Limits the results to items with the corresponding tenant.

          trigger_data: Limits the results to only messages that were generated with the given data. See
              [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
              more information.

          workflow_categories: Limits the results to messages related to any of the provided categories.

          workflow_recipient_run_id: Limits the results to messages for a specific recipient's workflow run.

          workflow_run_id: Limits the results to messages associated with the top-level workflow run ID
              returned by the workflow trigger request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/messages",
            page=AsyncItemsCursor[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "channel_id": channel_id,
                        "engagement_status": engagement_status,
                        "inserted_at": inserted_at,
                        "message_ids": message_ids,
                        "page_size": page_size,
                        "source": source,
                        "status": status,
                        "tenant": tenant,
                        "trigger_data": trigger_data,
                        "workflow_categories": workflow_categories,
                        "workflow_recipient_run_id": workflow_recipient_run_id,
                        "workflow_run_id": workflow_run_id,
                    },
                    user_list_messages_params.UserListMessagesParams,
                ),
            ),
            model=Message,
        )

    async def list_preferences(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPreferencesResponse:
        """
        Retrieves a list of all preference sets for a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/v1/users/{user_id}/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListPreferencesResponse,
        )

    def list_schedules(
        self,
        user_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        workflow: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Schedule, AsyncEntriesCursor[Schedule]]:
        """
        Returns a paginated list of schedules for a specific user, in descending order.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          tenant: The tenant ID to filter schedules for.

          workflow: The workflow key to filter schedules for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/schedules",
            page=AsyncEntriesCursor[Schedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "page_size": page_size,
                        "tenant": tenant,
                        "workflow": workflow,
                    },
                    user_list_schedules_params.UserListSchedulesParams,
                ),
            ),
            model=Schedule,
        )

    def list_subscriptions(
        self,
        user_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        objects: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Subscription, AsyncEntriesCursor[Subscription]]:
        """
        Retrieves a paginated list of subscriptions for a specific user, in descending
        order.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Associated resources to include in the response.

          objects: Only returns subscriptions for the specified object references.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/subscriptions",
            page=AsyncEntriesCursor[Subscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "objects": objects,
                        "page_size": page_size,
                    },
                    user_list_subscriptions_params.UserListSubscriptionsParams,
                ),
            ),
            model=Subscription,
        )

    async def merge(
        self,
        user_id: str,
        *,
        from_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Merge two users together, where the user specified with the `from_user_id` param
        will be merged into the user specified by `user_id`.

        Args:
          from_user_id: The user ID to merge from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/v1/users/{user_id}/merge",
            body=await async_maybe_transform({"from_user_id": from_user_id}, user_merge_params.UserMergeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def set_channel_data(
        self,
        user_id: str,
        channel_id: str,
        *,
        data: user_set_channel_data_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """Updates or creates channel data for a specific user and channel ID.

        If no user
        exists in the current environment for the given `user_id`, Knock will create the
        user entry as part of this request.

        Args:
          data: Channel data for a given channel type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._put(
            f"/v1/users/{user_id}/channel_data/{channel_id}",
            body=await async_maybe_transform({"data": data}, user_set_channel_data_params.UserSetChannelDataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    async def set_preferences(
        self,
        user_id: str,
        id: str,
        *,
        categories: Optional[Dict[str, user_set_preferences_params.Categories]] | NotGiven = NOT_GIVEN,
        channel_types: Optional[PreferenceSetChannelTypesParam] | NotGiven = NOT_GIVEN,
        workflows: Optional[Dict[str, user_set_preferences_params.Workflows]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """Updates a complete preference set for a user.

        This is a destructive operation
        that will replace the existing preference set for the user.

        Args:
          categories: An object where the key is the category and the values are the preference
              settings for that category.

          channel_types: Channel type preferences.

          workflows: An object where the key is the workflow key and the values are the preference
              settings for that workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/users/{user_id}/preferences/{id}",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "channel_types": channel_types,
                    "workflows": workflows,
                },
                user_set_preferences_params.UserSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSet,
        )

    async def unset_channel_data(
        self,
        user_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Deletes channel data for a specific user and channel ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._delete(
            f"/v1/users/{user_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.get = to_raw_response_wrapper(
            users.get,
        )
        self.get_channel_data = to_raw_response_wrapper(
            users.get_channel_data,
        )
        self.get_preferences = to_raw_response_wrapper(
            users.get_preferences,
        )
        self.list_messages = to_raw_response_wrapper(
            users.list_messages,
        )
        self.list_preferences = to_raw_response_wrapper(
            users.list_preferences,
        )
        self.list_schedules = to_raw_response_wrapper(
            users.list_schedules,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            users.list_subscriptions,
        )
        self.merge = to_raw_response_wrapper(
            users.merge,
        )
        self.set_channel_data = to_raw_response_wrapper(
            users.set_channel_data,
        )
        self.set_preferences = to_raw_response_wrapper(
            users.set_preferences,
        )
        self.unset_channel_data = to_raw_response_wrapper(
            users.unset_channel_data,
        )

    @cached_property
    def feeds(self) -> FeedsResourceWithRawResponse:
        return FeedsResourceWithRawResponse(self._users.feeds)

    @cached_property
    def guides(self) -> GuidesResourceWithRawResponse:
        return GuidesResourceWithRawResponse(self._users.guides)

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        return BulkResourceWithRawResponse(self._users.bulk)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.get = async_to_raw_response_wrapper(
            users.get,
        )
        self.get_channel_data = async_to_raw_response_wrapper(
            users.get_channel_data,
        )
        self.get_preferences = async_to_raw_response_wrapper(
            users.get_preferences,
        )
        self.list_messages = async_to_raw_response_wrapper(
            users.list_messages,
        )
        self.list_preferences = async_to_raw_response_wrapper(
            users.list_preferences,
        )
        self.list_schedules = async_to_raw_response_wrapper(
            users.list_schedules,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            users.list_subscriptions,
        )
        self.merge = async_to_raw_response_wrapper(
            users.merge,
        )
        self.set_channel_data = async_to_raw_response_wrapper(
            users.set_channel_data,
        )
        self.set_preferences = async_to_raw_response_wrapper(
            users.set_preferences,
        )
        self.unset_channel_data = async_to_raw_response_wrapper(
            users.unset_channel_data,
        )

    @cached_property
    def feeds(self) -> AsyncFeedsResourceWithRawResponse:
        return AsyncFeedsResourceWithRawResponse(self._users.feeds)

    @cached_property
    def guides(self) -> AsyncGuidesResourceWithRawResponse:
        return AsyncGuidesResourceWithRawResponse(self._users.guides)

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        return AsyncBulkResourceWithRawResponse(self._users.bulk)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.get = to_streamed_response_wrapper(
            users.get,
        )
        self.get_channel_data = to_streamed_response_wrapper(
            users.get_channel_data,
        )
        self.get_preferences = to_streamed_response_wrapper(
            users.get_preferences,
        )
        self.list_messages = to_streamed_response_wrapper(
            users.list_messages,
        )
        self.list_preferences = to_streamed_response_wrapper(
            users.list_preferences,
        )
        self.list_schedules = to_streamed_response_wrapper(
            users.list_schedules,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            users.list_subscriptions,
        )
        self.merge = to_streamed_response_wrapper(
            users.merge,
        )
        self.set_channel_data = to_streamed_response_wrapper(
            users.set_channel_data,
        )
        self.set_preferences = to_streamed_response_wrapper(
            users.set_preferences,
        )
        self.unset_channel_data = to_streamed_response_wrapper(
            users.unset_channel_data,
        )

    @cached_property
    def feeds(self) -> FeedsResourceWithStreamingResponse:
        return FeedsResourceWithStreamingResponse(self._users.feeds)

    @cached_property
    def guides(self) -> GuidesResourceWithStreamingResponse:
        return GuidesResourceWithStreamingResponse(self._users.guides)

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        return BulkResourceWithStreamingResponse(self._users.bulk)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            users.get,
        )
        self.get_channel_data = async_to_streamed_response_wrapper(
            users.get_channel_data,
        )
        self.get_preferences = async_to_streamed_response_wrapper(
            users.get_preferences,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            users.list_messages,
        )
        self.list_preferences = async_to_streamed_response_wrapper(
            users.list_preferences,
        )
        self.list_schedules = async_to_streamed_response_wrapper(
            users.list_schedules,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            users.list_subscriptions,
        )
        self.merge = async_to_streamed_response_wrapper(
            users.merge,
        )
        self.set_channel_data = async_to_streamed_response_wrapper(
            users.set_channel_data,
        )
        self.set_preferences = async_to_streamed_response_wrapper(
            users.set_preferences,
        )
        self.unset_channel_data = async_to_streamed_response_wrapper(
            users.unset_channel_data,
        )

    @cached_property
    def feeds(self) -> AsyncFeedsResourceWithStreamingResponse:
        return AsyncFeedsResourceWithStreamingResponse(self._users.feeds)

    @cached_property
    def guides(self) -> AsyncGuidesResourceWithStreamingResponse:
        return AsyncGuidesResourceWithStreamingResponse(self._users.guides)

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._users.bulk)
