# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import AudienceListMembersResponse
from knockapi._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_members(self, client: Knock) -> None:
        audience = client.audiences.add_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )
        assert audience is None

    @parametrize
    def test_method_add_members_with_all_params(self, client: Knock) -> None:
        audience = client.audiences.add_members(
            key="key",
            members=[
                {
                    "user": {
                        "id": "dr_sattler",
                        "avatar": "avatar",
                        "channel_data": {"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_123"]}},
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "email": "ellie@ingen.net",
                        "locale": "locale",
                        "name": "Dr. Ellie Sattler",
                        "phone_number": "phone_number",
                        "preferences": {
                            "default": {
                                "_persistence_strategy": "merge",
                                "categories": {
                                    "marketing": False,
                                    "transactional": {
                                        "channel_types": {
                                            "chat": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "email": False,
                                            "http": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "in_app_feed": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "push": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
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
                                    "chat": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
                                    "email": True,
                                    "http": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
                                    "in_app_feed": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
                                    "push": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
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
                                            "chat": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "email": True,
                                            "http": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "in_app_feed": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "push": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
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
                            }
                        },
                        "timezone": "America/New_York",
                    },
                    "tenant": "ingen_isla_nublar",
                }
            ],
            create_audience=True,
        )
        assert audience is None

    @parametrize
    def test_raw_response_add_members(self, client: Knock) -> None:
        response = client.audiences.with_raw_response.add_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert audience is None

    @parametrize
    def test_streaming_response_add_members(self, client: Knock) -> None:
        with client.audiences.with_streaming_response.add_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert audience is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_members(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.audiences.with_raw_response.add_members(
                key="",
                members=[{"user": {"id": "dr_sattler"}}],
            )

    @parametrize
    def test_method_list_members(self, client: Knock) -> None:
        audience = client.audiences.list_members(
            "key",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @parametrize
    def test_raw_response_list_members(self, client: Knock) -> None:
        response = client.audiences.with_raw_response.list_members(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

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

    @parametrize
    def test_path_params_list_members(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.audiences.with_raw_response.list_members(
                "",
            )

    @parametrize
    def test_method_remove_members(self, client: Knock) -> None:
        audience = client.audiences.remove_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )
        assert audience is None

    @parametrize
    def test_raw_response_remove_members(self, client: Knock) -> None:
        response = client.audiences.with_raw_response.remove_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert audience is None

    @parametrize
    def test_streaming_response_remove_members(self, client: Knock) -> None:
        with client.audiences.with_streaming_response.remove_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert audience is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_members(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.audiences.with_raw_response.remove_members(
                key="",
                members=[{"user": {"id": "dr_sattler"}}],
            )


class TestAsyncAudiences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_members(self, async_client: AsyncKnock) -> None:
        audience = await async_client.audiences.add_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )
        assert audience is None

    @parametrize
    async def test_method_add_members_with_all_params(self, async_client: AsyncKnock) -> None:
        audience = await async_client.audiences.add_members(
            key="key",
            members=[
                {
                    "user": {
                        "id": "dr_sattler",
                        "avatar": "avatar",
                        "channel_data": {"97c5837d-c65c-4d54-aa39-080eeb81c69d": {"tokens": ["push_token_123"]}},
                        "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "email": "ellie@ingen.net",
                        "locale": "locale",
                        "name": "Dr. Ellie Sattler",
                        "phone_number": "phone_number",
                        "preferences": {
                            "default": {
                                "_persistence_strategy": "merge",
                                "categories": {
                                    "marketing": False,
                                    "transactional": {
                                        "channel_types": {
                                            "chat": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "email": False,
                                            "http": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "in_app_feed": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "push": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
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
                                    "chat": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
                                    "email": True,
                                    "http": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
                                    "in_app_feed": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
                                    "push": {
                                        "conditions": [
                                            {
                                                "argument": "US",
                                                "operator": "equal_to",
                                                "variable": "recipient.country_code",
                                            }
                                        ]
                                    },
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
                                            "chat": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "email": True,
                                            "http": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "in_app_feed": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
                                            "push": {
                                                "conditions": [
                                                    {
                                                        "argument": "US",
                                                        "operator": "equal_to",
                                                        "variable": "recipient.country_code",
                                                    }
                                                ]
                                            },
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
                            }
                        },
                        "timezone": "America/New_York",
                    },
                    "tenant": "ingen_isla_nublar",
                }
            ],
            create_audience=True,
        )
        assert audience is None

    @parametrize
    async def test_raw_response_add_members(self, async_client: AsyncKnock) -> None:
        response = await async_client.audiences.with_raw_response.add_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert audience is None

    @parametrize
    async def test_streaming_response_add_members(self, async_client: AsyncKnock) -> None:
        async with async_client.audiences.with_streaming_response.add_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert audience is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_members(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.audiences.with_raw_response.add_members(
                key="",
                members=[{"user": {"id": "dr_sattler"}}],
            )

    @parametrize
    async def test_method_list_members(self, async_client: AsyncKnock) -> None:
        audience = await async_client.audiences.list_members(
            "key",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncKnock) -> None:
        response = await async_client.audiences.with_raw_response.list_members(
            "key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

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

    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.audiences.with_raw_response.list_members(
                "",
            )

    @parametrize
    async def test_method_remove_members(self, async_client: AsyncKnock) -> None:
        audience = await async_client.audiences.remove_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )
        assert audience is None

    @parametrize
    async def test_raw_response_remove_members(self, async_client: AsyncKnock) -> None:
        response = await async_client.audiences.with_raw_response.remove_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert audience is None

    @parametrize
    async def test_streaming_response_remove_members(self, async_client: AsyncKnock) -> None:
        async with async_client.audiences.with_streaming_response.remove_members(
            key="key",
            members=[{"user": {"id": "dr_sattler"}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert audience is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_members(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.audiences.with_raw_response.remove_members(
                key="",
                members=[{"user": {"id": "dr_sattler"}}],
            )
