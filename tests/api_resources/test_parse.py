# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import AsyncParseResponse, ParseParseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_parse(self, client: Reducto) -> None:
        parse = client.parse.parse(
            document_url="document_url",
        )
        assert_matches_type(ParseParseResponse, parse, path=["response"])

    @parametrize
    def test_method_parse_with_all_params(self, client: Reducto) -> None:
        parse = client.parse.parse(
            document_url="document_url",
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
        )
        assert_matches_type(ParseParseResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_parse(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.parse(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseParseResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_parse(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.parse(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_parse_async(self, client: Reducto) -> None:
        parse = client.parse.parse_async(
            document_url="document_url",
        )
        assert_matches_type(AsyncParseResponse, parse, path=["response"])

    @parametrize
    def test_method_parse_async_with_all_params(self, client: Reducto) -> None:
        parse = client.parse.parse_async(
            document_url="document_url",
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
            webhook={
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(AsyncParseResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_parse_async(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.parse_async(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(AsyncParseResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_parse_async(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.parse_async(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(AsyncParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParse:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_parse(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.parse(
            document_url="document_url",
        )
        assert_matches_type(ParseParseResponse, parse, path=["response"])

    @parametrize
    async def test_method_parse_with_all_params(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.parse(
            document_url="document_url",
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
        )
        assert_matches_type(ParseParseResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_parse(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.parse(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseParseResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_parse(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.parse(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_parse_async(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.parse_async(
            document_url="document_url",
        )
        assert_matches_type(AsyncParseResponse, parse, path=["response"])

    @parametrize
    async def test_method_parse_async_with_all_params(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.parse_async(
            document_url="document_url",
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
            webhook={
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(AsyncParseResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_parse_async(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.parse_async(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(AsyncParseResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_parse_async(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.parse_async(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(AsyncParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True
