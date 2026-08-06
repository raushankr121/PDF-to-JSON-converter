from pydantic import BaseModel
from app.models.block import Block

class Page(BaseModel):
    page_number: int
    width: float
    height: float
    rotation: int

    is_scanned: bool

    text: str

    blocks: list[Block] = []

    image_path: str | None = None