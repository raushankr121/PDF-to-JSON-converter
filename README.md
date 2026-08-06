# PDF to JSON Converter

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Google Gemini API](https://img.shields.io/badge/LLM-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![PyMuPDF](https://img.shields.io/badge/PDF%20Parser-PyMuPDF-green.svg)](https://pymupdf.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

An intelligent, schema-driven PDF extraction tool powered by **Google Gemini Vision API** and **PyMuPDF**. This application parses complex document PDFs (such as JEE examination papers), renders high-resolution page images, and uses multimodal LLMs to convert raw text and visual content into structured JSON data according to customizable schemas.

---

## 🌟 Key Features

- 📄 **Multimodal PDF Processing**: Converts PDF pages to high-DPI images (300 DPI) and processes both text and visual layouts (diagrams, math formulas, multiple choice options).
- 🎯 **Schema-Driven Extraction**: Dynamic schema loading allowing customizable extraction structures for different document types (e.g., JEE Main papers).
- 🤖 **Resilient Gemini LLM Integration**: Built-in fallback mechanism across Google Gemini models (`gemini-2.5-flash`, `gemini-2.0-flash`, `gemini-2.0-flash-lite`, `gemini-flash-latest`) with automatic retry logic for rate limits and server errors.
- 📐 **Math & Diagram Handling**: Captures complete question text including mathematical expressions, subject categorization, marking schemes, and image references.
- 📦 **Automated Batch Processing**: Merges page-by-page extractions into a consolidated, clean JSON file saved in UTF-8 encoding.

---

## 🏗️ Architecture & Project Structure

```
json-pdf-generator/
│
├── app/                        # Application core modules
│   ├── config.py               # Environment configuration & API keys
│   ├── extractor/              # LLM-based question extraction logic
│   │   └── question_extractor.py
│   ├── llm/                    # Gemini API wrapper with retry & fallback model support
│   │   └── gemini_client.py
│   ├── models/                 # Data models for Page and Document objects
│   ├── parser/                 # PyMuPDF reader for inspecting & extracting PDF pages
│   │   └── pdf_reader.py
│   ├── prompt/                 # Prompt generation templates based on schema
│   │   └── prompt_builder.py
│   ├── renderer/               # PDF page to image rendering engine
│   │   └── page_renderer.py
│   └── schema/                 # JSON schemas for target extraction formats
│       ├── schema_loader.py
│       └── jee.json
│
├── data/                       # Input storage
│   ├── pdfs/                   # Place input PDF files here
│   └── images/                 # Rendered page images output directory
│
├── output/                     # Formatted JSON output directory
│
├── main.py                     # Main execution pipeline entry point
├── requirements.txt            # Python dependencies
├── .env                        # Environment variable configuration (API keys)
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A Google Gemini API Key (Get one from [Google AI Studio](https://aistudio.google.com/))

### 1. Clone the Repository

```bash
git clone https://github.com/raushankr121/PDF-to-JSON-converter.git
cd PDF-to-JSON-converter
```

### 2. Create and Activate Virtual Environment

```bash
# On Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 💻 Usage

1. Place your target PDF file inside the `data/pdfs/` folder (e.g., `data/pdfs/JEE Main 2025 (23 Jan Shift 1).pdf`).
2. Run the main execution script:

```bash
python main.py
```

3. The system will:
   - Load and inspect the PDF document.
   - Render high-resolution images of each page into `data/images/`.
   - Process each page image using Gemini API using the specified schema (`app/schema/jee.json`).
   - Export the consolidated results into `output/<pdf_name>.json`.

---

## 📋 Custom Schema Example

Schemas define the structure and constraints for extracted JSON output. For example, `app/schema/jee.json`:

```json
{
  "type": "object",
  "name": "JEE Question Paper",
  "description": "Extract all questions from a JEE question paper according to this schema.",
  "fields": {
    "questions": {
      "type": "array",
      "items": {
        "type": "object",
        "fields": {
          "subject": { "type": "string" },
          "questionText": { "type": "string" },
          "optionA": { "type": "string" },
          "optionB": { "type": "string" },
          "optionC": { "type": "string" },
          "optionD": { "type": "string" },
          "correctOption": { "type": "string", "nullable": true },
          "positiveMarks": { "type": "integer", "default": 4 },
          "negativeMarks": { "type": "integer", "default": -1 }
        },
        "required": ["subject", "questionText", "optionA", "optionB", "optionC", "optionD"]
      }
    }
  }
}
```

---

## 🛠️ Tech Stack

- **[Google GenAI SDK](https://pypi.org/project/google-genai/)**: Gemini multimodal AI API integration
- **[PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)**: Fast PDF rendering and text/metadata extraction
- **[Pydantic](https://docs.pydantic.dev/)**: Data validation and structure definition
- **[python-dotenv](https://github.com/theskumar/python-dotenv)**: Secure environment variable management

---

## 📄 License

This project is licensed under the MIT License.
