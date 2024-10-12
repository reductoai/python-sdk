# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_configure(self, client: Reducto) -> None:
        webhook = client.webhooks.configure()
        assert_matches_type(str, webhook, path=["response"])

    @parametrize
    def test_raw_response_configure(self, client: Reducto) -> None:
        response = client.webhooks.with_raw_response.configure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(str, webhook, path=["response"])

    @parametrize
    def test_streaming_response_configure(self, client: Reducto) -> None:
        with client.webhooks.with_streaming_response.configure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(str, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_configure(self, async_client: AsyncReducto) -> None:
        webhook = await async_client.webhooks.configure()
        assert_matches_type(str, webhook, path=["response"])

    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncReducto) -> None:
        response = await async_client.webhooks.with_raw_response.configure()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(str, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncReducto) -> None:
        async with async_client.webhooks.with_streaming_response.configure() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(str, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
