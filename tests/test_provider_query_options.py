from typing import Any, Dict, List, Optional

import httpx
import pytest

from knockapi import Knock, AsyncKnock


@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.parametrize("provider", ["slack", "ms_teams"])
@pytest.mark.parametrize("start_cursor", [None, "start"])
@pytest.mark.asyncio
async def test_provider_options_and_pagination(
    async_client: bool, provider: str, start_cursor: Optional[str]
) -> None:
    requests: List[httpx.Request] = []
    cursor_key = (
        "query_options.cursor" if provider == "slack" else "query_options.$skiptoken"
    )
    option_key = "query_options.limit" if provider == "slack" else "query_options.$top"
    kwargs: Dict[str, Any]
    if provider == "slack":
        options: Dict[str, Any] = {"limit": 2, "exclude_archived": False}
        if start_cursor:
            options["cursor"] = start_cursor
        kwargs = {"access_token_object": "{}", "query_options": options}
        result_key, response_cursor = "slack_channels", "next_cursor"
    else:
        options = {"top": 2, "filter": "displayName eq 'Example'"}
        if start_cursor:
            options["skiptoken"] = start_cursor
        kwargs = {"ms_teams_tenant_object": "{}", "query_options": options}
        result_key, response_cursor = "ms_teams_teams", "skip_token"

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                result_key: [{"id": str(len(requests))}],
                response_cursor: "next" if len(requests) == 1 else None,
            },
        )

    transport = httpx.MockTransport(handle)
    if async_client:
        async with AsyncKnock(
            api_key="test", http_client=httpx.AsyncClient(transport=transport)
        ) as client:
            resource = getattr(client.providers, provider)
            method = (
                resource.list_channels if provider == "slack" else resource.list_teams
            )
            page = await method("channel", **kwargs)
            await page.get_next_page()
    else:
        with Knock(
            api_key="test", http_client=httpx.Client(transport=transport)
        ) as sync_client:
            resource = getattr(sync_client.providers, provider)
            method = (
                resource.list_channels if provider == "slack" else resource.list_teams
            )
            page = method("channel", **kwargs)
            page.get_next_page()

    assert len(requests) == 2
    for request in requests:
        assert request.url.params[option_key] == "2"
        assert not any(key.startswith("query_options[") for key in request.url.params)
        if provider == "slack":
            assert request.url.params["query_options.exclude_archived"] == "false"
        else:
            assert (
                request.url.params["query_options.$filter"]
                == "displayName eq 'Example'"
            )
    assert requests[0].url.params.get_list(cursor_key) == (
        [start_cursor] if start_cursor else []
    )
    assert requests[1].url.params.get_list(cursor_key) == ["next"]
    assert options.get("cursor" if provider == "slack" else "skiptoken") == start_cursor


@pytest.mark.parametrize("async_client", [False, True])
@pytest.mark.asyncio
async def test_unrelated_nested_query_format_is_unchanged(async_client: bool) -> None:
    if async_client:
        async with AsyncKnock(api_key="test") as client:
            params = httpx.QueryParams(
                client.qs.stringify({"other": {"name": "value"}, "ids": [1, 2]})
            )
    else:
        with Knock(api_key="test") as sync_client:
            params = httpx.QueryParams(
                sync_client.qs.stringify({"other": {"name": "value"}, "ids": [1, 2]})
            )
    assert params["other[name]"] == "value"
    assert params.get_list("ids[]") == ["1", "2"]
