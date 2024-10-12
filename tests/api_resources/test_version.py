# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Reducto) -> None:
        version = client.version.retrieve()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Reducto) -> None:
        response = client.version.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Reducto) -> None:
        with client.version.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(object, version, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVersion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncReducto) -> None:
        version = await async_client.version.retrieve()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncReducto) -> None:
        response = await async_client.version.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(object, version, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncReducto) -> None:
        async with async_client.version.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(object, version, path=["response"])

        assert cast(Any, response.is_closed) is True
