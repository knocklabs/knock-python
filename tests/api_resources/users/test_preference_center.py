# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types.users import PreferenceCenterGetConfigResponse, PreferenceCenterGenerateSignedURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferenceCenter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate_signed_url(self, client: Knock) -> None:
        preference_center = client.users.preference_center.generate_signed_url(
            "user_id",
        )
        assert_matches_type(PreferenceCenterGenerateSignedURLResponse, preference_center, path=["response"])

    @parametrize
    def test_raw_response_generate_signed_url(self, client: Knock) -> None:
        response = client.users.preference_center.with_raw_response.generate_signed_url(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = response.parse()
        assert_matches_type(PreferenceCenterGenerateSignedURLResponse, preference_center, path=["response"])

    @parametrize
    def test_streaming_response_generate_signed_url(self, client: Knock) -> None:
        with client.users.preference_center.with_streaming_response.generate_signed_url(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = response.parse()
            assert_matches_type(PreferenceCenterGenerateSignedURLResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_generate_signed_url(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.preference_center.with_raw_response.generate_signed_url(
                "",
            )

    @parametrize
    def test_method_get_config(self, client: Knock) -> None:
        preference_center = client.users.preference_center.get_config(
            "user_id",
        )
        assert_matches_type(PreferenceCenterGetConfigResponse, preference_center, path=["response"])

    @parametrize
    def test_raw_response_get_config(self, client: Knock) -> None:
        response = client.users.preference_center.with_raw_response.get_config(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = response.parse()
        assert_matches_type(PreferenceCenterGetConfigResponse, preference_center, path=["response"])

    @parametrize
    def test_streaming_response_get_config(self, client: Knock) -> None:
        with client.users.preference_center.with_streaming_response.get_config(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = response.parse()
            assert_matches_type(PreferenceCenterGetConfigResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_config(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.preference_center.with_raw_response.get_config(
                "",
            )


class TestAsyncPreferenceCenter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_generate_signed_url(self, async_client: AsyncKnock) -> None:
        preference_center = await async_client.users.preference_center.generate_signed_url(
            "user_id",
        )
        assert_matches_type(PreferenceCenterGenerateSignedURLResponse, preference_center, path=["response"])

    @parametrize
    async def test_raw_response_generate_signed_url(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.preference_center.with_raw_response.generate_signed_url(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = await response.parse()
        assert_matches_type(PreferenceCenterGenerateSignedURLResponse, preference_center, path=["response"])

    @parametrize
    async def test_streaming_response_generate_signed_url(self, async_client: AsyncKnock) -> None:
        async with async_client.users.preference_center.with_streaming_response.generate_signed_url(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = await response.parse()
            assert_matches_type(PreferenceCenterGenerateSignedURLResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_generate_signed_url(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.preference_center.with_raw_response.generate_signed_url(
                "",
            )

    @parametrize
    async def test_method_get_config(self, async_client: AsyncKnock) -> None:
        preference_center = await async_client.users.preference_center.get_config(
            "user_id",
        )
        assert_matches_type(PreferenceCenterGetConfigResponse, preference_center, path=["response"])

    @parametrize
    async def test_raw_response_get_config(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.preference_center.with_raw_response.get_config(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_center = await response.parse()
        assert_matches_type(PreferenceCenterGetConfigResponse, preference_center, path=["response"])

    @parametrize
    async def test_streaming_response_get_config(self, async_client: AsyncKnock) -> None:
        async with async_client.users.preference_center.with_streaming_response.get_config(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_center = await response.parse()
            assert_matches_type(PreferenceCenterGetConfigResponse, preference_center, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_config(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.preference_center.with_raw_response.get_config(
                "",
            )
