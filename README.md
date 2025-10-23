# AI Assignment Solver

An intelligent assignment solver that processes PDF and DOCX files, solves questions, and exports formatted solutions.

## Features

- 📄 **Multi-format Input**: Upload assignments in PDF or DOCX format
- 🧠 **Smart Question Detection**: Automatically identifies and understands document layout
- ✅ **Question Solver**: Solves the questions provided in the assignment
- 📝 **Layout Preservation**: Formats solutions matching the original document structure
- 💾 **Export Options**: Download solutions as Word (.docx) or PDF files

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **File Processing**: python-docx, PyPDF2/pdfplumber
- **AI/LLM**: (To be integrated)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd AI-ssignment

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run the Streamlit app
streamlit run app.py
```

## Project Structure

```
AI-ssignment/
├── app.py              # Streamlit UI
├── requirements.txt    # Python dependencies
├── utils/             # Helper modules
└── README.md          # Project documentation
```

## License

MIT

