# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import (
    WorkflowRecipientRun,
    WorkflowRecipientRunDetail,
)
from knockapi._utils import parse_datetime
from knockapi.pagination import SyncItemsCursor, AsyncItemsCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflowRecipientRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Knock) -> None:
        workflow_recipient_run = client.workflow_recipient_runs.list()
        assert_matches_type(SyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Knock) -> None:
        workflow_recipient_run = client.workflow_recipient_runs.list(
            after="after",
            before="before",
            ending_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            has_errors=True,
            page_size=0,
            recipient="user_123",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["queued"],
            tenant="tenant",
            workflow="workflow",
        )
        assert_matches_type(SyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Knock) -> None:
        response = client.workflow_recipient_runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_recipient_run = response.parse()
        assert_matches_type(SyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Knock) -> None:
        with client.workflow_recipient_runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_recipient_run = response.parse()
            assert_matches_type(SyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Knock) -> None:
        workflow_recipient_run = client.workflow_recipient_runs.get(
            "id",
        )
        assert_matches_type(WorkflowRecipientRunDetail, workflow_recipient_run, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Knock) -> None:
        response = client.workflow_recipient_runs.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_recipient_run = response.parse()
        assert_matches_type(WorkflowRecipientRunDetail, workflow_recipient_run, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Knock) -> None:
        with client.workflow_recipient_runs.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_recipient_run = response.parse()
            assert_matches_type(WorkflowRecipientRunDetail, workflow_recipient_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workflow_recipient_runs.with_raw_response.get(
                "",
            )


class TestAsyncWorkflowRecipientRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncKnock) -> None:
        workflow_recipient_run = await async_client.workflow_recipient_runs.list()
        assert_matches_type(AsyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnock) -> None:
        workflow_recipient_run = await async_client.workflow_recipient_runs.list(
            after="after",
            before="before",
            ending_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            has_errors=True,
            page_size=0,
            recipient="user_123",
            starting_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["queued"],
            tenant="tenant",
            workflow="workflow",
        )
        assert_matches_type(AsyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnock) -> None:
        response = await async_client.workflow_recipient_runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_recipient_run = await response.parse()
        assert_matches_type(AsyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnock) -> None:
        async with async_client.workflow_recipient_runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_recipient_run = await response.parse()
            assert_matches_type(AsyncItemsCursor[WorkflowRecipientRun], workflow_recipient_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncKnock) -> None:
        workflow_recipient_run = await async_client.workflow_recipient_runs.get(
            "id",
        )
        assert_matches_type(WorkflowRecipientRunDetail, workflow_recipient_run, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncKnock) -> None:
        response = await async_client.workflow_recipient_runs.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow_recipient_run = await response.parse()
        assert_matches_type(WorkflowRecipientRunDetail, workflow_recipient_run, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncKnock) -> None:
        async with async_client.workflow_recipient_runs.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow_recipient_run = await response.parse()
            assert_matches_type(WorkflowRecipientRunDetail, workflow_recipient_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workflow_recipient_runs.with_raw_response.get(
                "",
            )
