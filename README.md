# LLM Translation App

This is a Streamlit app that uses the GoogleGenerativeAI library to translate text from one language to another. It allows users to input text, select the source and target languages, and then translate the text.

## Prerequisites

Before running the app, make sure you have the following installed:

- Python 3.x
- Streamlit
- GoogleGenerativeAI library

You can install the required libraries by running the following command:

```bash
pip install streamlit langchain-google-genai
```
Create a Google API key by following [Google AI Studio](https://aistudio.google.com/app/api-keys)

## Usage
1. Clone this repository:

```bash
git clone https://github.com/P-Sanjana/llm-translation.git
```
2. Set up the environment variables:
- Create a .streamlit/secrets.toml file in the root directory of the repository.
- Add the following line to the secrets.toml file:
```bash
GEMINI_API_KEY='<your-api-key>'
```
- Replace your-api-key with your actual Google Generative AI API key.

3. Run the app:

```bash
streamlit run translator.py
```
4. Open your web browser and navigate to http://localhost:8501.
5. Enter the text you want to translate in the input field.
6. Select the source and target languages from the dropdown menus.
7. Click the "Translate" button to see the translation.
8. To download the translation as a .txt file, click the "Download translation as .txt file" button.

## Features
- Translate text from one language to another using Google Generative AI.
- Select the source and target languages from the dropdown menus.
- Download the translation as a .txt file.

## Acknowledgemts
- [GoogleGenerativeAI](https://python.langchain.com/docs/integrations/providers/google/) for providing the translation functionality.
- [Streamlit](https://docs.streamlit.io/) for the framework used to build the app.

