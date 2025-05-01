# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import (
    AudienceListMembersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_add_members(self, client: Knock) -> None:
        audience = client.audiences.add_members(
            key="key",
            members=[{"user": {}}],
        )
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_add_members(self, client: Knock) -> None:
        response = client.audiences.with_raw_response.add_members(
            key="key",
            members=[{"user": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_add_members(self, client: Knock) -> None:
        with client.audiences.with_streaming_response.add_members(
            key="key",
            members=[{"user": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(str, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_add_members(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.audiences.with_raw_response.add_members(
                key="",
                members=[{"user": {}}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_members(self, client: Knock) -> None:
        audience = client.audiences.list_members(
            "key",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_members(self, client: Knock) -> None:
        response = client.audiences.with_raw_response.list_members(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_members(self, client: Knock) -> None:
        with client.audiences.with_streaming_response.list_members(
            "key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_members(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.audiences.with_raw_response.list_members(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_remove_members(self, client: Knock) -> None:
        audience = client.audiences.remove_members(
            key="key",
            members=[{"user": {}}],
        )
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_remove_members(self, client: Knock) -> None:
        response = client.audiences.with_raw_response.remove_members(
            key="key",
            members=[{"user": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_remove_members(self, client: Knock) -> None:
        with client.audiences.with_streaming_response.remove_members(
            key="key",
            members=[{"user": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(str, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_remove_members(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.audiences.with_raw_response.remove_members(
                key="",
                members=[{"user": {}}],
            )


class TestAsyncAudiences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_add_members(self, async_client: AsyncKnock) -> None:
        audience = await async_client.audiences.add_members(
            key="key",
            members=[{"user": {}}],
        )
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_add_members(self, async_client: AsyncKnock) -> None:
        response = await async_client.audiences.with_raw_response.add_members(
            key="key",
            members=[{"user": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_add_members(self, async_client: AsyncKnock) -> None:
        async with async_client.audiences.with_streaming_response.add_members(
            key="key",
            members=[{"user": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(str, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_add_members(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.audiences.with_raw_response.add_members(
                key="",
                members=[{"user": {}}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_members(self, async_client: AsyncKnock) -> None:
        audience = await async_client.audiences.list_members(
            "key",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncKnock) -> None:
        response = await async_client.audiences.with_raw_response.list_members(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncKnock) -> None:
        async with async_client.audiences.with_streaming_response.list_members(
            "key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.audiences.with_raw_response.list_members(
                "",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_remove_members(self, async_client: AsyncKnock) -> None:
        audience = await async_client.audiences.remove_members(
            key="key",
            members=[{"user": {}}],
        )
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_remove_members(self, async_client: AsyncKnock) -> None:
        response = await async_client.audiences.with_raw_response.remove_members(
            key="key",
            members=[{"user": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(str, audience, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_remove_members(self, async_client: AsyncKnock) -> None:
        async with async_client.audiences.with_streaming_response.remove_members(
            key="key",
            members=[{"user": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(str, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_remove_members(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.audiences.with_raw_response.remove_members(
                key="",
                members=[{"user": {}}],
            )
