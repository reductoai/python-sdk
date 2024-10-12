# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .parse_response import ParseResponse
from .extract_response import ExtractResponse

__all__ = ["AsyncJobResponse", "Result"]

Result: TypeAlias = Union[ParseResponse, ExtractResponse]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[Result] = None
