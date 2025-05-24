# 🛡️ ReconBot: Cybersecurity Chat Assistant

ReconBot is an interactive cybersecurity assistant built using Streamlit and Google's Gemini Pro (via `google.generativeai`). It provides AI-powered answers to security-related questions while filtering unsafe inputs. Designed for students, security analysts, and enthusiasts looking to explore cyber concepts in a safe and responsive environment.


## 📌 Overview

- **Live Chat UI** built with Streamlit
- **Gemini 1.5 Flash model** integration via Google's Generative AI SDK
- **Input sanitization** to block prompt injection or unsafe terms
- **Secure logging** and basic rate limiting
- **Downloadable chat history**
- Inspired by real-world SOC tools but built for education and experimentation

<img width="1509" alt="Screenshot 2025-05-24 at 10 18 37 AM" src="https://github.com/user-attachments/assets/e0f6c4c8-2649-4240-8415-559dc04ab0ba" />

## ⚙️ Setup Instructions

Create a virtual environment
```
python -m venv venv
```
Activate the environment:

On Windows:
```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```

## 📦 Dependencies

Make sure you have Python 3.9+ installed. Install all dependencies via pip:

bash
```
pip install -r requirements.txt
```
Required Python Packages:

streamlit

python-dotenv

google-generativeai

## 🔐 Environment Setup

Create a .env file in the root directory with your Google API Key:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```
Get your Gemini API key from: https://makersuite.google.com/app/apikey

## 🚀 Usage

Run the Streamlit app with:
```
streamlit run app.py
```
## 💡 Features

* 🤖 Conversational UI: Asks and answers cybersecurity queries in a clean interface
* ⛔ Sanitization Layer: Blocks dangerous terms (<script>, sudo, etc.)
* 🔄 Session History: Tracks Q&A exchanges during session
* ⏱️ Rate Limiting: Prevents spamming by enforcing query intervals

## 🔧 Development Structure
```
YourProject/
├── app.py                     # Main Streamlit application
├── chat_security_utils.py    # Utility functions for input sanitization, logging
├── .env                      # Environment variables (API keys)
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```
$$ 🛡️ Security Considerations

This app includes a basic input filter but should not be deployed in production without additional security controls. For example:

* Implement stricter input validation
* Secure logging with sensitive redaction
* Use cloud-hosted API backends with quotas and access control
