# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import ExtractResponse, AsyncExtractResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_extract(self, client: Reducto) -> None:
        extract = client.extract.extract(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @parametrize
    def test_method_extract_with_all_params(self, client: Reducto) -> None:
        extract = client.extract.extract(
            document_url="document_url",
            schema={},
            advanced_options={
                "continue_hierarchy": True,
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "table_output_format": "html",
            },
            experimental_options={
                "enable_checkboxes": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "rotate_pages": True,
            },
            generate_citations=True,
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header", "Footer", "Title"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            system_prompt="system_prompt",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_extract(self, client: Reducto) -> None:
        response = client.extract.with_raw_response.extract(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_extract(self, client: Reducto) -> None:
        with client.extract.with_streaming_response.extract(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_extract_async(self, client: Reducto) -> None:
        extract = client.extract.extract_async(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(AsyncExtractResponse, extract, path=["response"])

    @parametrize
    def test_method_extract_async_with_all_params(self, client: Reducto) -> None:
        extract = client.extract.extract_async(
            document_url="document_url",
            schema={},
            advanced_options={
                "continue_hierarchy": True,
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "table_output_format": "html",
            },
            experimental_options={
                "enable_checkboxes": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "rotate_pages": True,
            },
            generate_citations=True,
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header", "Footer", "Title"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            webhook={
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(AsyncExtractResponse, extract, path=["response"])

    @parametrize
    def test_raw_response_extract_async(self, client: Reducto) -> None:
        response = client.extract.with_raw_response.extract_async(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(AsyncExtractResponse, extract, path=["response"])

    @parametrize
    def test_streaming_response_extract_async(self, client: Reducto) -> None:
        with client.extract.with_streaming_response.extract_async(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(AsyncExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_extract(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.extract(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.extract(
            document_url="document_url",
            schema={},
            advanced_options={
                "continue_hierarchy": True,
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "table_output_format": "html",
            },
            experimental_options={
                "enable_checkboxes": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "rotate_pages": True,
            },
            generate_citations=True,
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header", "Footer", "Title"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            system_prompt="system_prompt",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncReducto) -> None:
        response = await async_client.extract.with_raw_response.extract(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncReducto) -> None:
        async with async_client.extract.with_streaming_response.extract(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_extract_async(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.extract_async(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(AsyncExtractResponse, extract, path=["response"])

    @parametrize
    async def test_method_extract_async_with_all_params(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.extract_async(
            document_url="document_url",
            schema={},
            advanced_options={
                "continue_hierarchy": True,
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "table_output_format": "html",
            },
            experimental_options={
                "enable_checkboxes": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "rotate_pages": True,
            },
            generate_citations=True,
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header", "Footer", "Title"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            webhook={
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(AsyncExtractResponse, extract, path=["response"])

    @parametrize
    async def test_raw_response_extract_async(self, async_client: AsyncReducto) -> None:
        response = await async_client.extract.with_raw_response.extract_async(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(AsyncExtractResponse, extract, path=["response"])

    @parametrize
    async def test_streaming_response_extract_async(self, async_client: AsyncReducto) -> None:
        async with async_client.extract.with_streaming_response.extract_async(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(AsyncExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
