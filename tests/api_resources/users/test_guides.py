# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types.users import (
    GuideGetChannelResponse,
    GuideMarkMessageAsSeenResponse,
    GuideMarkMessageAsArchivedResponse,
    GuideMarkMessageAsInteractedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGuides:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_channel(self, client: Knock) -> None:
        guide = client.users.guides.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_channel_with_all_params(self, client: Knock) -> None:
        guide = client.users.guides.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data="data",
            tenant="tenant",
            type="type",
        )
        assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_channel(self, client: Knock) -> None:
        response = client.users.guides.with_raw_response.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_channel(self, client: Knock) -> None:
        with client.users.guides.with_streaming_response.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_channel(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.guides.with_raw_response.get_channel(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.users.guides.with_raw_response.get_channel(
                user_id="user_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_message_as_archived(self, client: Knock) -> None:
        guide = client.users.guides.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )
        assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_message_as_archived_with_all_params(self, client: Knock) -> None:
        guide = client.users.guides.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
            content={
                "body": "bar",
                "title": "bar",
            },
            data={
                "next_time": "bar",
                "spots_left": "bar",
                "tour_id": "bar",
            },
            is_final=False,
            metadata={
                "cta": "bar",
                "theme": "bar",
                "type": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_message_as_archived(self, client: Knock) -> None:
        response = client.users.guides.with_raw_response.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_message_as_archived(self, client: Knock) -> None:
        with client.users.guides.with_streaming_response.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_message_as_archived(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.guides.with_raw_response.mark_message_as_archived(
                user_id="",
                message_id="message_id",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.users.guides.with_raw_response.mark_message_as_archived(
                user_id="user_id",
                message_id="",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_message_as_interacted(self, client: Knock) -> None:
        guide = client.users.guides.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )
        assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_message_as_interacted_with_all_params(self, client: Knock) -> None:
        guide = client.users.guides.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
            content={
                "body": "bar",
                "title": "bar",
            },
            data={
                "next_time": "bar",
                "spots_left": "bar",
                "tour_id": "bar",
            },
            is_final=False,
            metadata={
                "cta": "bar",
                "theme": "bar",
                "type": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_message_as_interacted(self, client: Knock) -> None:
        response = client.users.guides.with_raw_response.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_message_as_interacted(self, client: Knock) -> None:
        with client.users.guides.with_streaming_response.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_message_as_interacted(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.guides.with_raw_response.mark_message_as_interacted(
                user_id="",
                message_id="message_id",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.users.guides.with_raw_response.mark_message_as_interacted(
                user_id="user_id",
                message_id="",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_message_as_seen(self, client: Knock) -> None:
        guide = client.users.guides.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )
        assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_message_as_seen_with_all_params(self, client: Knock) -> None:
        guide = client.users.guides.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
            content={
                "body": "bar",
                "title": "bar",
            },
            data={
                "next_time": "bar",
                "spots_left": "bar",
                "tour_id": "bar",
            },
            is_final=False,
            metadata={
                "cta": "bar",
                "theme": "bar",
                "type": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_message_as_seen(self, client: Knock) -> None:
        response = client.users.guides.with_raw_response.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = response.parse()
        assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_message_as_seen(self, client: Knock) -> None:
        with client.users.guides.with_streaming_response.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = response.parse()
            assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_mark_message_as_seen(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.guides.with_raw_response.mark_message_as_seen(
                user_id="",
                message_id="message_id",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.users.guides.with_raw_response.mark_message_as_seen(
                user_id="user_id",
                message_id="",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )


class TestAsyncGuides:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_channel(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_channel_with_all_params(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data="data",
            tenant="tenant",
            type="type",
        )
        assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_channel(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.guides.with_raw_response.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_channel(self, async_client: AsyncKnock) -> None:
        async with async_client.users.guides.with_streaming_response.get_channel(
            user_id="user_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideGetChannelResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_channel(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.guides.with_raw_response.get_channel(
                user_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.users.guides.with_raw_response.get_channel(
                user_id="user_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_message_as_archived(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )
        assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_message_as_archived_with_all_params(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
            content={
                "body": "bar",
                "title": "bar",
            },
            data={
                "next_time": "bar",
                "spots_left": "bar",
                "tour_id": "bar",
            },
            is_final=False,
            metadata={
                "cta": "bar",
                "theme": "bar",
                "type": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_message_as_archived(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.guides.with_raw_response.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_message_as_archived(self, async_client: AsyncKnock) -> None:
        async with async_client.users.guides.with_streaming_response.mark_message_as_archived(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideMarkMessageAsArchivedResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_message_as_archived(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.guides.with_raw_response.mark_message_as_archived(
                user_id="",
                message_id="message_id",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.users.guides.with_raw_response.mark_message_as_archived(
                user_id="user_id",
                message_id="",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_message_as_interacted(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )
        assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_message_as_interacted_with_all_params(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
            content={
                "body": "bar",
                "title": "bar",
            },
            data={
                "next_time": "bar",
                "spots_left": "bar",
                "tour_id": "bar",
            },
            is_final=False,
            metadata={
                "cta": "bar",
                "theme": "bar",
                "type": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_message_as_interacted(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.guides.with_raw_response.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_message_as_interacted(self, async_client: AsyncKnock) -> None:
        async with async_client.users.guides.with_streaming_response.mark_message_as_interacted(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideMarkMessageAsInteractedResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_message_as_interacted(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.guides.with_raw_response.mark_message_as_interacted(
                user_id="",
                message_id="message_id",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.users.guides.with_raw_response.mark_message_as_interacted(
                user_id="user_id",
                message_id="",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_message_as_seen(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )
        assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_message_as_seen_with_all_params(self, async_client: AsyncKnock) -> None:
        guide = await async_client.users.guides.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
            content={
                "body": "bar",
                "title": "bar",
            },
            data={
                "next_time": "bar",
                "spots_left": "bar",
                "tour_id": "bar",
            },
            is_final=False,
            metadata={
                "cta": "bar",
                "theme": "bar",
                "type": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_message_as_seen(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.guides.with_raw_response.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guide = await response.parse()
        assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_message_as_seen(self, async_client: AsyncKnock) -> None:
        async with async_client.users.guides.with_streaming_response.mark_message_as_seen(
            user_id="user_id",
            message_id="message_id",
            channel_id="123e4567-e89b-12d3-a456-426614174000",
            guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
            guide_key="tour_notification",
            guide_step_ref="lab_tours",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guide = await response.parse()
            assert_matches_type(GuideMarkMessageAsSeenResponse, guide, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_mark_message_as_seen(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.guides.with_raw_response.mark_message_as_seen(
                user_id="",
                message_id="message_id",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.users.guides.with_raw_response.mark_message_as_seen(
                user_id="user_id",
                message_id="",
                channel_id="123e4567-e89b-12d3-a456-426614174000",
                guide_id="7e9dc78c-b3b1-4127-a54e-71f1899b831a",
                guide_key="tour_notification",
                guide_step_ref="lab_tours",
            )
