from typing import List

from pydantic import BaseModel


class AddLinks(BaseModel):
    """Add links request model."""

    links: List[str] = []
