# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import UploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upload(self, client: Reducto) -> None:
        upload = client.upload.upload()
        assert_matches_type(UploadResponse, upload, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Reducto) -> None:
        upload = client.upload.upload(
            extension="extension",
            file=b"raw file contents",
        )
        assert_matches_type(UploadResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Reducto) -> None:
        response = client.upload.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Reducto) -> None:
        with client.upload.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUpload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_upload(self, async_client: AsyncReducto) -> None:
        upload = await async_client.upload.upload()
        assert_matches_type(UploadResponse, upload, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncReducto) -> None:
        upload = await async_client.upload.upload(
            extension="extension",
            file=b"raw file contents",
        )
        assert_matches_type(UploadResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncReducto) -> None:
        response = await async_client.upload.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncReducto) -> None:
        async with async_client.upload.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True
