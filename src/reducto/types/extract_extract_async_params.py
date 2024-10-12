# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ExtractExtractAsyncParams",
    "AdvancedOptions",
    "AdvancedOptionsLargeTableChunking",
    "AdvancedOptionsPageRange",
    "ExperimentalOptions",
    "ExperimentalOptionsEnrich",
    "Options",
    "OptionsChunking",
    "OptionsFigureSummary",
    "OptionsTableSummary",
    "Webhook",
]


class ExtractExtractAsyncParams(TypedDict, total=False):
    document_url: Required[str]
    """The URL of the document to be processed. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
    """

    schema: Required[object]
    """The JSON schema to use for extraction."""

    advanced_options: AdvancedOptions

    experimental_options: ExperimentalOptions

    generate_citations: bool
    """If citations should be generated for the extracted content."""

    options: Options

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    system_prompt: str
    """A system prompt to use for the extraction.

    This is a general prompt that is applied to the entire document before any other
    prompts.
    """

    webhook: Webhook


class AdvancedOptionsLargeTableChunking(TypedDict, total=False):
    enabled: bool
    """
    If large tables should be chunked into smaller tables, currently only supported
    on spreadsheet and CSV files.
    """

    size: int
    """The max row/column size for a table to be chunked.

    Defaults to 50. Header rows/columns are persisted based on heuristics.
    """


class AdvancedOptionsPageRange(TypedDict, total=False):
    end: Optional[int]
    """The page number to stop processing at."""

    start: Optional[int]
    """The page number to start processing from."""


class AdvancedOptions(TypedDict, total=False):
    continue_hierarchy: bool
    """
    A flag to indicate if the hierarchy of the document should be continued from
    chunk to chunk.
    """

    force_file_extension: str
    """Force the URL to be downloaded as a specific file extension (e.g. .png)."""

    keep_line_breaks: bool
    """If line breaks should be preserved in the text."""

    large_table_chunking: AdvancedOptionsLargeTableChunking
    """
    The configuration options for large table chunking (currently only supported on
    spreadsheet and CSV files).
    """

    merge_tables: bool
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged.
    """

    ocr_system: Literal["highres", "multilingual"]
    """The OCR system to use.

    Highres is recommended for documents with English characters.
    """

    page_range: AdvancedOptionsPageRange
    """The page range to process. By default, the entire document is processed."""

    table_output_format: Literal["html", "json", "md", "jsonbbox"]
    """The mode to use for table output."""


class ExperimentalOptionsEnrich(TypedDict, total=False):
    enabled: bool
    """
    If enabled, a large language/vision model will be used to postprocess the
    extracted content. Defaults to False.
    """

    prompt: str
    """Add information to the prompt for enrichment."""


class ExperimentalOptions(TypedDict, total=False):
    enable_checkboxes: bool
    """
    Use an experimental checkbox detection model to add checkboxes to the output,
    defaults to False
    """

    enable_underlines: bool
    """
    Add <u> tag around text that's underlined and surround strikethroughs and
    underlines with <change> tags, defaults to False
    """

    enrich: ExperimentalOptionsEnrich
    """The configuration options for enrichment."""

    native_office_conversion: bool
    """
    Instead of using LibreOffice, when enabled, this flag uses a Windows VM to
    convert files. This is slower but more accurate.
    """

    rotate_pages: bool
    """
    Use an orientation model to detect and rotate pages as needed, defaults to False
    """


class OptionsChunking(TypedDict, total=False):
    chunk_mode: Literal["variable", "section", "page", "block", "disabled"]
    """The mode to use for chunking.

    Section chunks according to sections in the doucment. Page chunks accordcing to
    pages. Disabled returns a single chunk.
    """

    chunk_size: int
    """
    The approximate size of chunks (in characters) that the document will be split
    into. Defaults to None, in which case the chunk size is variable between 250 -
    1500 characters.
    """


class OptionsFigureSummary(TypedDict, total=False):
    enabled: bool
    """If figure summarization should be performed."""

    prompt: str
    """Add information to the prompt for figure summarization."""


class OptionsTableSummary(TypedDict, total=False):
    enabled: bool
    """If table summarization should be performed."""

    prompt: str
    """Add information to the prompt for table summarization."""


class Options(TypedDict, total=False):
    chunking: OptionsChunking
    """The configuration options for chunking."""

    extraction_mode: Literal["ocr", "metadata", "hybrid"]
    """The mode to use for extraction."""

    figure_summary: OptionsFigureSummary
    """The configuration options for figure summarization."""

    filter_blocks: List[
        Literal[
            "Header",
            "Footer",
            "Title",
            "Section Header",
            "Page Number",
            "List Item",
            "Figure",
            "Table",
            "Key Value",
            "Text",
            "Comment",
        ]
    ]
    """A list of block types to filter from chunk content."""

    force_url_result: bool
    """
    Force the result to be returned in URL form (by default only used for very large
    responses).
    """

    table_summary: OptionsTableSummary
    """The configuration options for table summarization."""


class Webhook(TypedDict, total=False):
    metadata: object
    """JSON metadata included in webhook request body"""

    mode: Literal["disabled", "svix", "direct"]
    """The mode to use for webhook delivery.

    Defaults to 'disabled'. We recommend using 'svix' for production environments.
    """

    url: str
    """The URL to send the webhook to (if using direct webhoook)."""
