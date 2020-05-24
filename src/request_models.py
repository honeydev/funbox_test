from typing import List

from pydantic import BaseModel


class Links(BaseModel):

    links: List[str] = []
