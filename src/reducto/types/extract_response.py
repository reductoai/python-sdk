# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ExtractResponse", "Usage"]


class Usage(BaseModel):
    num_fields: int

    num_pages: int


class ExtractResponse(BaseModel):
    citations: List[object]
    """The citations corresponding to the extracted response."""

    result: List[object]
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disbale_chunking is True (default), then it
    will be a list of length one.
    """

    usage: Usage
