# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import (
    WorkflowTriggerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_cancel(self, client: Knock) -> None:
        workflow = client.workflows.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
        )
        assert_matches_type(str, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_cancel_with_all_params(self, client: Knock) -> None:
        workflow = client.workflows.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
            recipients=["jhammond"],
        )
        assert_matches_type(str, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_cancel(self, client: Knock) -> None:
        response = client.workflows.with_raw_response.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(str, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_cancel(self, client: Knock) -> None:
        with client.workflows.with_streaming_response.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(str, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_cancel(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.workflows.with_raw_response.cancel(
                key="",
                cancellation_key="cancel-workflow-123",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_trigger(self, client: Knock) -> None:
        workflow = client.workflows.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
        )
        assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_trigger_with_all_params(self, client: Knock) -> None:
        workflow = client.workflows.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
            actor="mr_dna",
            cancellation_key="isla_nublar_incident_1993",
            data={
                "affected_areas": "bar",
                "attraction_id": "bar",
                "evacuation_protocol": "bar",
                "message": "bar",
                "severity": "bar",
                "system_status": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_trigger(self, client: Knock) -> None:
        response = client.workflows.with_raw_response.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_trigger(self, client: Knock) -> None:
        with client.workflows.with_streaming_response.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_trigger(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.workflows.with_raw_response.trigger(
                key="",
                recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_cancel(self, async_client: AsyncKnock) -> None:
        workflow = await async_client.workflows.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
        )
        assert_matches_type(str, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncKnock) -> None:
        workflow = await async_client.workflows.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
            recipients=["jhammond"],
        )
        assert_matches_type(str, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncKnock) -> None:
        response = await async_client.workflows.with_raw_response.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(str, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncKnock) -> None:
        async with async_client.workflows.with_streaming_response.cancel(
            key="key",
            cancellation_key="cancel-workflow-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(str, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.workflows.with_raw_response.cancel(
                key="",
                cancellation_key="cancel-workflow-123",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_trigger(self, async_client: AsyncKnock) -> None:
        workflow = await async_client.workflows.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
        )
        assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncKnock) -> None:
        workflow = await async_client.workflows.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
            actor="mr_dna",
            cancellation_key="isla_nublar_incident_1993",
            data={
                "affected_areas": "bar",
                "attraction_id": "bar",
                "evacuation_protocol": "bar",
                "message": "bar",
                "severity": "bar",
                "system_status": "bar",
            },
            tenant="ingen_isla_nublar",
        )
        assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncKnock) -> None:
        response = await async_client.workflows.with_raw_response.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncKnock) -> None:
        async with async_client.workflows.with_streaming_response.trigger(
            key="key",
            recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowTriggerResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.workflows.with_raw_response.trigger(
                key="",
                recipients=["dr_grant", "dr_sattler", "dr_malcolm"],
            )
