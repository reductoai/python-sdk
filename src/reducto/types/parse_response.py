# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ParseResponse",
    "Result",
    "ResultFullResult",
    "ResultFullResultChunk",
    "ResultFullResultChunkBlock",
    "ResultFullResultChunkBlockBbox",
    "ResultURLResult",
    "Usage",
]


class ResultFullResultChunkBlockBbox(BaseModel):
    height: float

    left: float

    page: int
    """The page number of the bounding box (1-indexed)."""

    top: float

    width: float


class ResultFullResultChunkBlock(BaseModel):
    bbox: ResultFullResultChunkBlockBbox
    """The bounding box of the block extracted from the document."""

    content: str
    """The content of the block extracted from the document."""

    type: Literal[
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
    """The type of block extracted from the document."""


class ResultFullResultChunk(BaseModel):
    blocks: List[ResultFullResultChunkBlock]

    content: str
    """The content of the chunk extracted from the document."""

    embed: str
    """Chunk content optimized for embedding and retrieval."""

    enriched: str
    """The enriched content of the chunk extracted from the document."""

    enrichment_success: Optional[bool] = None
    """Whether the enrichment was successful."""


class ResultFullResult(BaseModel):
    chunks: List[ResultFullResultChunk]

    type: Literal["full"]
    """type = 'full'"""

    custom: Optional[object] = None


class ResultURLResult(BaseModel):
    result_id: str

    type: Literal["url"]
    """type = 'url'"""

    url: str


Result: TypeAlias = Union[ResultFullResult, ResultURLResult]


class Usage(BaseModel):
    num_pages: int


class ParseResponse(BaseModel):
    duration: float
    """The duration of the parse request in seconds."""

    result: Result
    """The resopnse from the document processing service.

    Note that there can be two types of responses, Full Result and URL Result. This
    is due to limitations on the max return size on HTTPS. If the response is too
    large, it will be returned as a presigned URL in the URL response. You should
    handle this in your application.
    """

    usage: Usage

    pdf_url: Optional[str] = None
    """The storage URL of the converted PDF file."""
