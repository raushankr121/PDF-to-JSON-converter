import re
   
from app.models.question import Question

from app.segmenter.base_segmenter import BaseSegmenter


class QuestionSegmenter(BaseSegmenter):

    QUESTION_PATTERN = re.compile(r"^Q(\d+)\.")

    def segment(self, blocks):

        questions = []

        current_question = None

        for block in blocks:

            text = block.text.strip()

            match = self.QUESTION_PATTERN.match(text)

            if match:

                if current_question:
                    questions.append(current_question)

                current_question = Question(
                    question_number=int(match.group(1)),
                    page_number=block.page_number,
                    question_text=text
                )

            elif current_question:

                current_question.question_text += "\n" + text

        if current_question:
            questions.append(current_question)

        return questions