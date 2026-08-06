import json

# pyrefly: ignore [missing-import]

from app.prompt.prompt_builder import PromptBuilder
from app.llm.gemini_client import GeminiClient


class QuestionExtractor:

    def __init__(self):

        self.llm = GeminiClient()

    def extract(self, page, schema):

        prompt = PromptBuilder.build(page, schema)

        response = self.llm.generate(
            prompt=prompt,
            image_path=page.image_path
        )

        # response = self.llm.generate(
        #     prompt=prompt,
        #     image_path=page.image_path
        # )
        # print(response)
        # return json.loads(response)

        text = response.strip()
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        return json.loads(text)