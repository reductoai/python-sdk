# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..types import parse_parse_params, parse_parse_async_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.async_parse_response import AsyncParseResponse
from ..types.parse_parse_response import ParseParseResponse

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/python-sdk#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)

    def parse(
        self,
        *,
        document_url: str,
        advanced_options: parse_parse_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: parse_parse_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        options: parse_parse_params.Options | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseParseResponse:
        """Parse

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ParseParseResponse,
            self._post(
                "/parse",
                body=maybe_transform(
                    {
                        "document_url": document_url,
                        "advanced_options": advanced_options,
                        "experimental_options": experimental_options,
                        "options": options,
                    },
                    parse_parse_params.ParseParseParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseParseResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def parse_async(
        self,
        *,
        document_url: str,
        advanced_options: parse_parse_async_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: parse_parse_async_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        options: parse_parse_async_params.Options | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: parse_parse_async_params.Webhook | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncParseResponse:
        """
        Async Parse

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/parse_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "webhook": webhook,
                },
                parse_parse_async_params.ParseParseAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncParseResponse,
        )


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/python-sdk#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)

    async def parse(
        self,
        *,
        document_url: str,
        advanced_options: parse_parse_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: parse_parse_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        options: parse_parse_params.Options | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseParseResponse:
        """Parse

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ParseParseResponse,
            await self._post(
                "/parse",
                body=await async_maybe_transform(
                    {
                        "document_url": document_url,
                        "advanced_options": advanced_options,
                        "experimental_options": experimental_options,
                        "options": options,
                    },
                    parse_parse_params.ParseParseParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseParseResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def parse_async(
        self,
        *,
        document_url: str,
        advanced_options: parse_parse_async_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: parse_parse_async_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        options: parse_parse_async_params.Options | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: parse_parse_async_params.Webhook | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncParseResponse:
        """
        Async Parse

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/parse_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "webhook": webhook,
                },
                parse_parse_async_params.ParseParseAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncParseResponse,
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.parse = to_raw_response_wrapper(
            parse.parse,
        )
        self.parse_async = to_raw_response_wrapper(
            parse.parse_async,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.parse = async_to_raw_response_wrapper(
            parse.parse,
        )
        self.parse_async = async_to_raw_response_wrapper(
            parse.parse_async,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.parse = to_streamed_response_wrapper(
            parse.parse,
        )
        self.parse_async = to_streamed_response_wrapper(
            parse.parse_async,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.parse = async_to_streamed_response_wrapper(
            parse.parse,
        )
        self.parse_async = async_to_streamed_response_wrapper(
            parse.parse_async,
        )
