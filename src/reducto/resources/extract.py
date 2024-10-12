# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import extract_extract_params, extract_extract_async_params
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
from ..types.extract_response import ExtractResponse
from ..types.async_extract_response import AsyncExtractResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/reducto-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/reducto-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def extract(
        self,
        *,
        document_url: str,
        schema: object,
        advanced_options: extract_extract_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: extract_extract_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: extract_extract_params.Options | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """Extract

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          generate_citations: If citations should be generated for the extracted content.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "system_prompt": system_prompt,
                },
                extract_extract_params.ExtractExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def extract_async(
        self,
        *,
        document_url: str,
        schema: object,
        advanced_options: extract_extract_async_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: extract_extract_async_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: extract_extract_async_params.Options | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        webhook: extract_extract_async_params.Webhook | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncExtractResponse:
        """
        Extract Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          generate_citations: If citations should be generated for the extracted content.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "priority": priority,
                    "system_prompt": system_prompt,
                    "webhook": webhook,
                },
                extract_extract_async_params.ExtractExtractAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncExtractResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/reducto-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/reducto-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def extract(
        self,
        *,
        document_url: str,
        schema: object,
        advanced_options: extract_extract_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: extract_extract_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: extract_extract_params.Options | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """Extract

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          generate_citations: If citations should be generated for the extracted content.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "system_prompt": system_prompt,
                },
                extract_extract_params.ExtractExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def extract_async(
        self,
        *,
        document_url: str,
        schema: object,
        advanced_options: extract_extract_async_params.AdvancedOptions | NotGiven = NOT_GIVEN,
        experimental_options: extract_extract_async_params.ExperimentalOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: extract_extract_async_params.Options | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        webhook: extract_extract_async_params.Webhook | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncExtractResponse:
        """
        Extract Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          generate_citations: If citations should be generated for the extracted content.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "priority": priority,
                    "system_prompt": system_prompt,
                    "webhook": webhook,
                },
                extract_extract_async_params.ExtractExtractAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncExtractResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.extract = to_raw_response_wrapper(
            extract.extract,
        )
        self.extract_async = to_raw_response_wrapper(
            extract.extract_async,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.extract = async_to_raw_response_wrapper(
            extract.extract,
        )
        self.extract_async = async_to_raw_response_wrapper(
            extract.extract_async,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.extract = to_streamed_response_wrapper(
            extract.extract,
        )
        self.extract_async = to_streamed_response_wrapper(
            extract.extract_async,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.extract = async_to_streamed_response_wrapper(
            extract.extract,
        )
        self.extract_async = async_to_streamed_response_wrapper(
            extract.extract_async,
        )
