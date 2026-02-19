# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import Tenant
from knockapi.pagination import SyncEntriesCursor, AsyncEntriesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_list(self, client: Knock) -> None:
        tenant = client.tenants.list()
        assert_matches_type(SyncEntriesCursor[Tenant], tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_list_with_all_params(self, client: Knock) -> None:
        tenant = client.tenants.list(
            after="after",
            before="before",
            name="name",
            page_size=0,
            tenant_id="tenant_id",
        )
        assert_matches_type(SyncEntriesCursor[Tenant], tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_raw_response_list(self, client: Knock) -> None:
        response = client.tenants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(SyncEntriesCursor[Tenant], tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_list(self, client: Knock) -> None:
        with client.tenants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(SyncEntriesCursor[Tenant], tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_delete(self, client: Knock) -> None:
        tenant = client.tenants.delete(
            "id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_raw_response_delete(self, client: Knock) -> None:
        response = client.tenants.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_delete(self, client: Knock) -> None:
        with client.tenants.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_path_params_delete(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tenants.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_get(self, client: Knock) -> None:
        tenant = client.tenants.get(
            id="id",
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_get_with_all_params(self, client: Knock) -> None:
        tenant = client.tenants.get(
            id="id",
            resolve_full_preference_settings=True,
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_raw_response_get(self, client: Knock) -> None:
        response = client.tenants.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_get(self, client: Knock) -> None:
        with client.tenants.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(Tenant, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_path_params_get(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tenants.with_raw_response.get(
                id="",
            )

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_set(self, client: Knock) -> None:
        tenant = client.tenants.set(
            id="id",
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_method_set_with_all_params(self, client: Knock) -> None:
        tenant = client.tenants.set(
            id="id",
            resolve_full_preference_settings=True,
            channel_data={"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_xxx"]}},
            name="Jurassic Park",
            settings={
                "branding": {
                    "icon_url": "https://example.com/trex_silhouette_icon.png",
                    "logo_url": "https://example.com/amber_fossil_logo.png",
                    "primary_color": "#DF1A22",
                    "primary_color_contrast": "#FFDE00",
                },
                "preference_set": {
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
            },
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_raw_response_set(self, client: Knock) -> None:
        response = client.tenants.with_raw_response.set(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_set(self, client: Knock) -> None:
        with client.tenants.with_streaming_response.set(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(Tenant, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    def test_path_params_set(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tenants.with_raw_response.set(
                id="",
            )


class TestAsyncTenants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_list(self, async_client: AsyncKnock) -> None:
        tenant = await async_client.tenants.list()
        assert_matches_type(AsyncEntriesCursor[Tenant], tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnock) -> None:
        tenant = await async_client.tenants.list(
            after="after",
            before="before",
            name="name",
            page_size=0,
            tenant_id="tenant_id",
        )
        assert_matches_type(AsyncEntriesCursor[Tenant], tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnock) -> None:
        response = await async_client.tenants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Tenant], tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnock) -> None:
        async with async_client.tenants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Tenant], tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnock) -> None:
        tenant = await async_client.tenants.delete(
            "id",
        )
        assert tenant is None

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnock) -> None:
        response = await async_client.tenants.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert tenant is None

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnock) -> None:
        async with async_client.tenants.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert tenant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tenants.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_get(self, async_client: AsyncKnock) -> None:
        tenant = await async_client.tenants.get(
            id="id",
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncKnock) -> None:
        tenant = await async_client.tenants.get(
            id="id",
            resolve_full_preference_settings=True,
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKnock) -> None:
        response = await async_client.tenants.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKnock) -> None:
        async with async_client.tenants.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(Tenant, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tenants.with_raw_response.get(
                id="",
            )

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_set(self, async_client: AsyncKnock) -> None:
        tenant = await async_client.tenants.set(
            id="id",
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncKnock) -> None:
        tenant = await async_client.tenants.set(
            id="id",
            resolve_full_preference_settings=True,
            channel_data={"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_xxx"]}},
            name="Jurassic Park",
            settings={
                "branding": {
                    "icon_url": "https://example.com/trex_silhouette_icon.png",
                    "logo_url": "https://example.com/amber_fossil_logo.png",
                    "primary_color": "#DF1A22",
                    "primary_color_contrast": "#FFDE00",
                },
                "preference_set": {
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
            },
        )
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncKnock) -> None:
        response = await async_client.tenants.with_raw_response.set(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(Tenant, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncKnock) -> None:
        async with async_client.tenants.with_streaming_response.set(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(Tenant, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server doesn't support callbacks yet")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tenants.with_raw_response.set(
                id="",
            )
