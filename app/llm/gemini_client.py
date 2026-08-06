import time
from typing import Optional
from google import genai
from google.genai import types
from google.genai.errors import ServerError, APIError

from app.config import GEMINI_API_KEY


class GeminiClient:
    """
    Wrapper around the Gemini API.

    Responsibilities:
    - Send prompt
    - Send page image
    - Return raw response text

    This class should NOT contain any prompt-building logic.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str, image_path: Optional[str] = None) -> str:
        """
        Generate a response using a prompt and an optional image.

        Args:
            prompt (str): Prompt text.
            image_path (str, optional): Path to the rendered page image.

        Returns:
            str: Raw response from Gemini.
        """
        contents = [prompt]

        if image_path:
            with open(image_path, "rb") as img:
                image_bytes = img.read()
            contents.append(
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png",
                )
            )

        models_to_try = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-flash-latest"]
        last_exception = None

        for model_name in models_to_try:
            for attempt in range(3):
                try:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=contents,
                        config=types.GenerateContentConfig(
                            response_mime_type="application/json",
                        ),
                    )
                    # response = self.client.models.generate_content(
                    #     model="gemini-2.5-flash",
                    #     contents=[
                    #         prompt,
                    #         types.Part.from_bytes(
                    #             data=image_bytes,
                    #             mime_type="image/png",
                    #         ),
                    #     ],
                    #     config=types.GenerateContentConfig(
                    #         response_mime_type="application/json"
                    #     ),
                    # )
                    return response.text
                except (ServerError, APIError) as e:
                    last_exception = e
                    if "503" in str(e) or "UNAVAILABLE" in str(e) or "429" in str(e):
                        time.sleep(2 * (attempt + 1))
                        continue
                    else:
                        break

        if last_exception:
            raise last_exception
        raise RuntimeError("Failed to generate content from Gemini API")