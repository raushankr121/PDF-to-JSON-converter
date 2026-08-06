from pydantic import BaseModel


class Block(BaseModel):

    id: int

    page_number: int

    block_number: int

    block_type: str

    bbox: list[float]

    text: str

    font: str | None = None

    font_size: float | None = None