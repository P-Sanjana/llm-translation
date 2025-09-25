import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from languages_list import languages
llm = GoogleGenerativeAI(model='gemini-2.5-flash', api_key=st.secrets['GEMINI_API_KEY'])

st.title('AI Translator')

st.divider()

input_text = st.text_area('Enter the text you want to translate:')

source_language = st.selectbox('Select source language:', languages)
target_language = st.selectbox('Select target language:', languages)

def translate_text(input_text, source_language, target_language):
    prompt = f'Translate this from {source_language} to {target_language}: {input_text}'
    translated_text = llm.invoke(prompt)
    return translated_text

if st.button('Translate'):
    if input_text:
        translation = translate_text(input_text, source_language, target_language)
        st.write('Translation: ', translation)

        st.download_button(
            label='Download translation as .txt file',
            data=translation,
            file_name='translation.txt',
            mime='text/plain')
    else:
        st.write('Please enter some text to translate.')

