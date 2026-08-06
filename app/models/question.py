from pydantic import BaseModel, Field


class Question(BaseModel):
    question_number: int

    page_number: int

    question_text: str = ""

    options: list[str] = Field(default_factory=list)

    images: list[str] = Field(default_factory=list)

    equations: list[str] = Field(default_factory=list)

    metadata: dict = Field(default_factory=dict)