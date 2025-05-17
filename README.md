# 🧠 AI-ssignment

**AI-ssignment** is a web-based tool that helps students solve academic assignment questions using advanced AI models. Designed with simplicity and practicality in mind, the app allows users to input assignment questions and receive AI-generated answers instantly.

## 🚀 Features

- 🔍 Natural language input for assignment questions  
- 🤖 Intelligent answer generation powered by LLMs  
- 🌐 Clean, responsive web interface built with Flask, JavaScript, HTML, and CSS  
- 📄 File upload support (PDF, DOCX, etc.) *(planned)*  
- 🧰 Modular codebase for easy extension and maintenance  

## 🏗️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Flask  
- **AI Model**: OpenAI's GPT-based LLM (via API)  
- **Others**: Jinja2 for templating, `requests`, `python-dotenv`  

## 📁 Project Structure
AI-ssignment/
├── app/
│ ├── static/ # CSS, JS, image files
│ ├── templates/ # HTML templates
│ ├── routes/ # Flask route definitions
│ ├── utils/ # Helper functions (e.g., text cleaning, formatting)
│ ├── pipeline/ # Core logic for interacting with the LLM
│ └── init.py # Flask app factory
├── models/ # (Optional) Prompt structures or saved configs
├── tests/ # Unit tests
├── requirements.txt # Python dependencies
├── run.py # Entry point to run the app
├── README.md # Project overview and instructions
└── .gitignore # Files to ignore in Git

