from typing import Set

from pydantic import BaseModel


class AddVisitedLinksResponse(BaseModel):
    """Visited links response model."""

    status: str
    insert_timestamp: float


class GetVisitedDomainsResponse(BaseModel):
    """Visited domains response model."""

    status: str
    domains: Set[str]
