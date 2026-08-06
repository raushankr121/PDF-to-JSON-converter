from pydantic import BaseModel
from typing import List

from app.models.page import Page


class Document(BaseModel):
    file_name: str
    total_pages: int
    pages: List[Page]
    metadata: dict