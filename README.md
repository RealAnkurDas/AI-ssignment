# Lab Assignment Generator

An automated lab assignment generator that uses AI to create complete lab reports with code solutions and executed outputs. Built with Streamlit and powered by Groq's LLM API.

## 📋 Overview

This application automatically generates lab assignment documents by:
- Taking student information and lab questions as input
- Generating Python code solutions using Groq's AI API (Llama 3.1)
- Executing the generated code and capturing output
- Creating professional Word documents with formatted questions, code, and terminal-style output images

## 🚀 Features

- **AI-Powered Code Generation**: Uses Groq's Llama 3.1 model to generate Python solutions
- **Automatic Code Execution**: Runs generated code and captures console output
- **Professional Output**: Creates styled output images with black background and white text
- **Word Document Generation**: Produces formatted `.docx` files ready for submission
- **User-Friendly Interface**: Streamlit-based web interface for easy interaction
- **Customizable**: Supports multiple lab numbers and various question types

## 📁 Project Structure

```
AI-ssignment/
├── Backend/
│   ├── __init__.py
│   └── create_lab_file.py      # Core logic for document generation
├── Frontend/
│   └── main.py                  # Streamlit UI
├── utils/
│   ├── __init__.py
│   └── image_utils.py           # Image generation utilities
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com))

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-ssignment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🎯 Usage

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run Frontend/main.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8501`

3. **Fill in the form**
   - **Student Name**: Enter your full name
   - **AUD Number**: Enter your student ID
   - **Subject**: Select Python or Algorithms
   - **Lab Number**: Enter the lab week number
   - **Lab Date**: Select the date of the lab
   - **Questions**: Enter lab questions (one per line)
   - **Output Format**: Choose Word or PDF (currently Word is implemented)

4. **Generate Document**
   - Click "Generate Lab Document"
   - Wait for the AI to generate solutions
   - Download the generated Word document

### Example Questions

```
WAP to print the first 10 natural numbers
WAP to find factorial of n
WAP to implement recursive quicksort
WAP to calculate Fibonacci series up to n terms
```

## 🏗️ Architecture

### Backend Module

**`Backend/create_lab_file.py`**
- `LabFile` class with `create_python_lab_file()` method
- Integrates with Groq API using OpenAI client
- Executes generated code in a sandboxed environment
- Formats output into Word documents

### Frontend Module

**`Frontend/main.py`**
- Streamlit-based user interface
- Form validation and user input handling
- Document download functionality

### Utils Module

**`utils/image_utils.py`**
- `create_output_image()`: Generates terminal-style output images
- Black background with white monospace text
- Automatic sizing based on content

## 🔧 Configuration

### Groq API Settings

The application uses the following default settings:
- **Model**: `llama-3.1-8b-instant`
- **Temperature**: 0.7
- **Base URL**: `https://api.groq.com/openai/v1`

You can modify these in `Backend/create_lab_file.py`.

## 📦 Dependencies

Key dependencies include:
- **streamlit**: Web interface framework
- **openai**: API client for Groq
- **python-docx**: Word document generation
- **Pillow**: Image processing
- **python-dotenv**: Environment variable management

See `requirements.txt` for the complete list.

## 🔒 Security Notes

- Code execution is sandboxed using Python's `exec()` with limited scope
- Temporary files are automatically cleaned up after use
- API keys are managed through environment variables
- No user input is directly executed without AI processing

## 🐛 Error Handling

The application includes:
- Input validation for all required fields
- Exception handling during code generation and execution
- Graceful error messages displayed in the UI
- Automatic cleanup of temporary resources

## 🚧 Current Limitations

- Only Word (.docx) output is currently implemented (PDF option in UI not yet functional)
- Primarily designed for Python lab assignments
- Requires internet connection for API access
- Code execution timeout not implemented

## 🔮 Future Enhancements

### Planned Subject Support

The application will be expanded to support lab files for multiple subjects:
- [ ] **Algorithms** - Algorithm design and analysis assignments
- [ ] **Data Structures** - Implementation and analysis of data structures
- [ ] **Java** - Java programming lab exercises
- [ ] **C** - C programming lab assignments
- [ ] **C++** - C++ programming exercises
- [ ] **Database Management System** - SQL queries, database design, and normalization
- [ ] **Operating Systems** - OS concepts, process management, and scheduling
- [ ] **Data Communication and Computer Networks** - Networking lab reports

### Generic Assignment Section

- [ ] Add a separate section for **generic assignments** (non-lab coursework)
  - Essay-style assignments
  - Project reports
  - Research papers
  - Case study analysis
  - Homework assignments

### Other Enhancements

- [ ] PDF output support
- [ ] Code execution timeout mechanism
- [ ] Batch processing of multiple lab assignments
- [ ] Custom styling templates for different subjects
- [ ] Offline mode with cached responses
- [ ] Multi-language code execution environments
- [ ] Template customization for different universities/institutions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

This project is provided as-is for educational purposes.

## 👤 Author

Created for automated lab assignment generation.

## 🙏 Acknowledgments

- Powered by [Groq](https://groq.com) and Llama 3.1
- Built with [Streamlit](https://streamlit.io)
- Uses [python-docx](https://python-docx.readthedocs.io) for document generation

---

**Note**: Remember to keep your Groq API key confidential and never commit it to version control.

