# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import BulkOperation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_delete(self, client: Knock) -> None:
        bulk = client.users.bulk.delete(
            user_ids=["user_1", "user_2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_delete(self, client: Knock) -> None:
        response = client.users.bulk.with_raw_response.delete(
            user_ids=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_delete(self, client: Knock) -> None:
        with client.users.bulk.with_streaming_response.delete(
            user_ids=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_identify(self, client: Knock) -> None:
        bulk = client.users.bulk.identify(
            users=[{"id": "user_1"}],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_identify(self, client: Knock) -> None:
        response = client.users.bulk.with_raw_response.identify(
            users=[{"id": "user_1"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_identify(self, client: Knock) -> None:
        with client.users.bulk.with_streaming_response.identify(
            users=[{"id": "user_1"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_set_preferences(self, client: Knock) -> None:
        bulk = client.users.bulk.set_preferences(
            preferences={},
            user_ids=["user_1", "user_2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_set_preferences_with_all_params(self, client: Knock) -> None:
        bulk = client.users.bulk.set_preferences(
            preferences={
                "_persistence_strategy": "merge",
                "categories": {
                    "marketing": False,
                    "transactional": {
                        "channel_types": {
                            "chat": True,
                            "email": False,
                            "http": True,
                            "in_app_feed": True,
                            "push": True,
                            "sms": {
                                "conditions": [
                                    {
                                        "argument": "US",
                                        "operator": "equal_to",
                                        "variable": "recipient.country_code",
                                    }
                                ]
                            },
                        },
                        "channels": {"aef6e715-df82-4ab6-b61e-b743e249f7b6": True},
                        "conditions": [
                            {
                                "argument": "frog_genome",
                                "operator": "contains",
                                "variable": "specimen.dna_sequence",
                            }
                        ],
                    },
                },
                "channel_types": {
                    "chat": True,
                    "email": True,
                    "http": True,
                    "in_app_feed": True,
                    "push": True,
                    "sms": {
                        "conditions": [
                            {
                                "argument": "US",
                                "operator": "equal_to",
                                "variable": "recipient.country_code",
                            }
                        ]
                    },
                },
                "channels": {
                    "2f641633-95d3-4555-9222-9f1eb7888a80": {
                        "conditions": [
                            {
                                "argument": "US",
                                "operator": "equal_to",
                                "variable": "recipient.country_code",
                            }
                        ]
                    },
                    "aef6e715-df82-4ab6-b61e-b743e249f7b6": True,
                },
                "commercial_subscribed": True,
                "workflows": {
                    "dinosaurs-loose": {
                        "channel_types": {
                            "chat": True,
                            "email": False,
                            "http": True,
                            "in_app_feed": True,
                            "push": True,
                            "sms": {
                                "conditions": [
                                    {
                                        "argument": "US",
                                        "operator": "equal_to",
                                        "variable": "recipient.country_code",
                                    }
                                ]
                            },
                        },
                        "channels": {"aef6e715-df82-4ab6-b61e-b743e249f7b6": True},
                        "conditions": [
                            {
                                "argument": "frog_genome",
                                "operator": "contains",
                                "variable": "specimen.dna_sequence",
                            }
                        ],
                    }
                },
            },
            user_ids=["user_1", "user_2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_set_preferences(self, client: Knock) -> None:
        response = client.users.bulk.with_raw_response.set_preferences(
            preferences={},
            user_ids=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_set_preferences(self, client: Knock) -> None:
        with client.users.bulk.with_streaming_response.set_preferences(
            preferences={},
            user_ids=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.users.bulk.delete(
            user_ids=["user_1", "user_2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.bulk.with_raw_response.delete(
            user_ids=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnock) -> None:
        async with async_client.users.bulk.with_streaming_response.delete(
            user_ids=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_identify(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.users.bulk.identify(
            users=[{"id": "user_1"}],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_identify(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.bulk.with_raw_response.identify(
            users=[{"id": "user_1"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_identify(self, async_client: AsyncKnock) -> None:
        async with async_client.users.bulk.with_streaming_response.identify(
            users=[{"id": "user_1"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_set_preferences(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.users.bulk.set_preferences(
            preferences={},
            user_ids=["user_1", "user_2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_set_preferences_with_all_params(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.users.bulk.set_preferences(
            preferences={
                "_persistence_strategy": "merge",
                "categories": {
                    "marketing": False,
                    "transactional": {
                        "channel_types": {
                            "chat": True,
                            "email": False,
                            "http": True,
                            "in_app_feed": True,
                            "push": True,
                            "sms": {
                                "conditions": [
                                    {
                                        "argument": "US",
                                        "operator": "equal_to",
                                        "variable": "recipient.country_code",
                                    }
                                ]
                            },
                        },
                        "channels": {"aef6e715-df82-4ab6-b61e-b743e249f7b6": True},
                        "conditions": [
                            {
                                "argument": "frog_genome",
                                "operator": "contains",
                                "variable": "specimen.dna_sequence",
                            }
                        ],
                    },
                },
                "channel_types": {
                    "chat": True,
                    "email": True,
                    "http": True,
                    "in_app_feed": True,
                    "push": True,
                    "sms": {
                        "conditions": [
                            {
                                "argument": "US",
                                "operator": "equal_to",
                                "variable": "recipient.country_code",
                            }
                        ]
                    },
                },
                "channels": {
                    "2f641633-95d3-4555-9222-9f1eb7888a80": {
                        "conditions": [
                            {
                                "argument": "US",
                                "operator": "equal_to",
                                "variable": "recipient.country_code",
                            }
                        ]
                    },
                    "aef6e715-df82-4ab6-b61e-b743e249f7b6": True,
                },
                "commercial_subscribed": True,
                "workflows": {
                    "dinosaurs-loose": {
                        "channel_types": {
                            "chat": True,
                            "email": False,
                            "http": True,
                            "in_app_feed": True,
                            "push": True,
                            "sms": {
                                "conditions": [
                                    {
                                        "argument": "US",
                                        "operator": "equal_to",
                                        "variable": "recipient.country_code",
                                    }
                                ]
                            },
                        },
                        "channels": {"aef6e715-df82-4ab6-b61e-b743e249f7b6": True},
                        "conditions": [
                            {
                                "argument": "frog_genome",
                                "operator": "contains",
                                "variable": "specimen.dna_sequence",
                            }
                        ],
                    }
                },
            },
            user_ids=["user_1", "user_2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_set_preferences(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.bulk.with_raw_response.set_preferences(
            preferences={},
            user_ids=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_set_preferences(self, async_client: AsyncKnock) -> None:
        async with async_client.users.bulk.with_streaming_response.set_preferences(
            preferences={},
            user_ids=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
