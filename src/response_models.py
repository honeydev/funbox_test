from typing import Set

from pydantic import BaseModel


class AddVisitedLinksResponse(BaseModel):

    status: str
    insert_timestamp: float


class GetVisitedDomainsResponse(BaseModel):

    status: str
    domains: Set[str]
