# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import (
    Schedule,
    ScheduleCreateResponse,
    ScheduleDeleteResponse,
    ScheduleUpdateResponse,
)
from knockapi._utils import parse_datetime
from knockapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create(self, client: Knock) -> None:
        schedule = client.schedules.create(
            recipients=["user_123"],
            workflow="comment-created",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create_with_all_params(self, client: Knock) -> None:
        schedule = client.schedules.create(
            recipients=["user_123"],
            workflow="comment-created",
            actor={
                "id": "user_1",
                "avatar": "avatar",
                "channel_data": {"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_xxx"]}},
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "email": "email",
                "locale": "locale",
                "name": "name",
                "phone_number": "phone_number",
                "preferences": {
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
                                        "argument": "frog_genome",
                                        "operator": "contains",
                                        "variable": "specimen.dna_sequence",
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
                            "welcome-sequence": True,
                        },
                    }
                },
                "timezone": "timezone",
            },
            data={"key": "bar"},
            ending_at=None,
            repeats=[
                {
                    "frequency": "daily",
                    "_typename": "ScheduleRepeat",
                    "day_of_month": None,
                    "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
                    "hours": None,
                    "interval": 1,
                    "minutes": None,
                }
            ],
            scheduled_at=None,
            tenant="acme_corp",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_create(self, client: Knock) -> None:
        response = client.schedules.with_raw_response.create(
            recipients=["user_123"],
            workflow="comment-created",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_create(self, client: Knock) -> None:
        with client.schedules.with_streaming_response.create(
            recipients=["user_123"],
            workflow="comment-created",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update(self, client: Knock) -> None:
        schedule = client.schedules.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update_with_all_params(self, client: Knock) -> None:
        schedule = client.schedules.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
            actor="string",
            data={"key": "bar"},
            ending_at=None,
            repeats=[
                {
                    "frequency": "daily",
                    "_typename": "ScheduleRepeat",
                    "day_of_month": None,
                    "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
                    "hours": None,
                    "interval": 1,
                    "minutes": None,
                }
            ],
            scheduled_at=None,
            tenant="acme_corp",
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_update(self, client: Knock) -> None:
        response = client.schedules.with_raw_response.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_update(self, client: Knock) -> None:
        with client.schedules.with_streaming_response.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list(self, client: Knock) -> None:
        schedule = client.schedules.list(
            workflow="workflow",
        )
        assert_matches_type(SyncEntriesCursor[Schedule], schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: Knock) -> None:
        schedule = client.schedules.list(
            workflow="workflow",
            after="after",
            before="before",
            page_size=0,
            recipients=["user_123"],
            tenant="tenant",
        )
        assert_matches_type(SyncEntriesCursor[Schedule], schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list(self, client: Knock) -> None:
        response = client.schedules.with_raw_response.list(
            workflow="workflow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(SyncEntriesCursor[Schedule], schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list(self, client: Knock) -> None:
        with client.schedules.with_streaming_response.list(
            workflow="workflow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(SyncEntriesCursor[Schedule], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_delete(self, client: Knock) -> None:
        schedule = client.schedules.delete(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_delete(self, client: Knock) -> None:
        response = client.schedules.with_raw_response.delete(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_delete(self, client: Knock) -> None:
        with client.schedules.with_streaming_response.delete(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncKnock) -> None:
        schedule = await async_client.schedules.create(
            recipients=["user_123"],
            workflow="comment-created",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKnock) -> None:
        schedule = await async_client.schedules.create(
            recipients=["user_123"],
            workflow="comment-created",
            actor={
                "id": "user_1",
                "avatar": "avatar",
                "channel_data": {"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_xxx"]}},
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "email": "email",
                "locale": "locale",
                "name": "name",
                "phone_number": "phone_number",
                "preferences": {
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
                                        "argument": "frog_genome",
                                        "operator": "contains",
                                        "variable": "specimen.dna_sequence",
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
                            "welcome-sequence": True,
                        },
                    }
                },
                "timezone": "timezone",
            },
            data={"key": "bar"},
            ending_at=None,
            repeats=[
                {
                    "frequency": "daily",
                    "_typename": "ScheduleRepeat",
                    "day_of_month": None,
                    "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
                    "hours": None,
                    "interval": 1,
                    "minutes": None,
                }
            ],
            scheduled_at=None,
            tenant="acme_corp",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKnock) -> None:
        response = await async_client.schedules.with_raw_response.create(
            recipients=["user_123"],
            workflow="comment-created",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKnock) -> None:
        async with async_client.schedules.with_streaming_response.create(
            recipients=["user_123"],
            workflow="comment-created",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update(self, async_client: AsyncKnock) -> None:
        schedule = await async_client.schedules.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncKnock) -> None:
        schedule = await async_client.schedules.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
            actor="string",
            data={"key": "bar"},
            ending_at=None,
            repeats=[
                {
                    "frequency": "daily",
                    "_typename": "ScheduleRepeat",
                    "day_of_month": None,
                    "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
                    "hours": None,
                    "interval": 1,
                    "minutes": None,
                }
            ],
            scheduled_at=None,
            tenant="acme_corp",
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncKnock) -> None:
        response = await async_client.schedules.with_raw_response.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncKnock) -> None:
        async with async_client.schedules.with_streaming_response.update(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncKnock) -> None:
        schedule = await async_client.schedules.list(
            workflow="workflow",
        )
        assert_matches_type(AsyncEntriesCursor[Schedule], schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnock) -> None:
        schedule = await async_client.schedules.list(
            workflow="workflow",
            after="after",
            before="before",
            page_size=0,
            recipients=["user_123"],
            tenant="tenant",
        )
        assert_matches_type(AsyncEntriesCursor[Schedule], schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnock) -> None:
        response = await async_client.schedules.with_raw_response.list(
            workflow="workflow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Schedule], schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnock) -> None:
        async with async_client.schedules.with_streaming_response.list(
            workflow="workflow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Schedule], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnock) -> None:
        schedule = await async_client.schedules.delete(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnock) -> None:
        response = await async_client.schedules.with_raw_response.delete(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnock) -> None:
        async with async_client.schedules.with_streaming_response.delete(
            schedule_ids=["123e4567-e89b-12d3-a456-426614174000"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True
