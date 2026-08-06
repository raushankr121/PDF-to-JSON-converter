import json
class PromptBuilder:

    @staticmethod
    def build(page, schema):

        return f"""
You are an expert AI that extracts JEE Main Previous Year Questions.

The attached image is one page of a JEE paper.

The extracted text is provided only as supporting context because mathematical equations may be incomplete.

YOUR PRIMARY SOURCE IS THE IMAGE.
Extract EVERY question visible on this page.
Extract EVERY complete MCQ visible on this page.

Rules:

1. Return ONLY valid JSON.
2. Do not explain anything.
3. Do not wrap the JSON inside ```json.
4. Preserve mathematical equations exactly.
5. Do not determine the correct answer.
6.Always set "correctOption" to null.
7.The correct answers will be filled later from the answer-key page.
8. If a question contains a diagram, set imageUrl to the diagram filename, otherwise null.
9. Every question must have four options.
10. Do not skip any question.
11.Count the question numbers before answering.
12.Return one JSON object for every visible question.
13.Verify that all question numbers have been extracted.

JSON Schema:

{json.dumps(schema, indent=2)}

Supporting Text:

{page.text}
"""