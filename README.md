# 🌐 Text Translator

A simple web-based text translation tool using a clean user interface and an API-powered backend.

## 🚀 Features

- Select source and target languages
- Translate input text with a single click
- Minimal and elegant UI
- Backend powered by Flask or direct API requests

## 🛠️ Technologies Used

- HTML, CSS
- JavaScript
- Flask (optional)
- Translation API (LibreTranslate, Google Translate, DeepL, etc.)

## 📷 Screenshot

![screenshot](screenshots/translator_ui.png)

## 🔧 How to Run

### Option 1: HTML-Only (Client-Side API Call)

1. Open `index.html` in your browser.
2. Enter the text, choose languages, and click **Translate**.

> You'll need to connect this to an API endpoint (see JS example below).

### Option 2: Flask Server (Recommended)

1. Install Flask:
   ```bash
   pip install flask
