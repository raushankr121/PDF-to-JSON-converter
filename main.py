import json
import traceback
from pathlib import Path

from app.parser.pdf_reader import PDFReader
from app.renderer.page_renderer import PageRenderer
from app.extractor.question_extractor import QuestionExtractor
from app.schema.schema_loader import SchemaLoader


def main():

    pdf_path = "data/pdfs/JEE Main 2025 (23 Jan Shift 1).pdf"
    reader = PDFReader(pdf_path)

    document = reader.extract_document()

    renderer = PageRenderer(document)

    document = renderer.render_pages()

    schema = SchemaLoader.load("schemas/jee.json")

    extractor = QuestionExtractor()

    all_questions = []

    for page in document.pages:

        print(f"\nProcessing Page {page.page_number}...")

        try:

            response = extractor.extract(page, schema)

            if not isinstance(response, dict):
                print(f"Page {page.page_number}: Invalid response")
                continue

            questions = response.get("questions")

            if questions is None:
                print(f"Page {page.page_number}: No questions found")
                print(response)
                continue

            print(f"Extracted {len(questions)} questions")

            all_questions.extend(questions)

        except Exception as e:

            print(f"\n{'='*80}")
            print(f"Error on Page {page.page_number}")
            print(f"{'='*80}")
            traceback.print_exc()
            print(f"{'='*80}\n")
            continue

    final_output = {
        "questions": all_questions
    }

    output_folder = Path("output")

    output_folder.mkdir(exist_ok=True)

    output_file = output_folder / f"{Path(pdf_path).stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:

        json.dump(
            final_output,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("\n" + "=" * 60)

    print("Extraction Completed Successfully")
    print(f"Total Questions : {len(all_questions)}")
    print(f"Saved JSON      : {output_file}")
    print("=" * 60)
if __name__ == "__main__":
    main()


# import json

# from app.parser.pdf_reader import PDFReader
# from app.renderer.page_renderer import PageRenderer
# from app.extractor.question_extractor import QuestionExtractor
# from app.schema.schema_loader import SchemaLoader


# def main():

#     pdf_path = "data/pdfs/jee.pdf"

#     reader = PDFReader(pdf_path)
#     document = reader.extract_document()

#     renderer = PageRenderer(document)
#     document = renderer.render_pages()

#     schema = SchemaLoader.load("schemas/jee.json")

#     extractor = QuestionExtractor()

#     # Page 3 -> index 2
#     page = document.pages[2]

#     print(f"Processing Page {page.page_number}...\n")

#     response = extractor.extract(page, schema)

#     print("\n================ GEMINI RESPONSE ================\n")
#     print(response)
#     print("\n=================================================\n")


# if __name__ == "__main__":
#     main()