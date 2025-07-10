import streamlit as st
from deep_translator import GoogleTranslator
from profanity_check import predict  # AI-based profanity detection

languages = {
    "Arabic": "ar",
    "Bengali": "bn",
    "Chinese": "zh",
    "French": "fr",
    "German": "de",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Marathi": "mr",
    "Odia": "or",
    "Punjabi": "pa",
    "Russian": "ru",
    "Spanish": "es",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur"
}

st.title("🌍 Language Translator App")

text = st.text_input("Enter text in English:")
lang_choice = st.selectbox("Select output language:", sorted(languages.keys()))

if text:
    # AI-based check for abusive content
    if predict([text])[0] == 1:
        st.error("⚠ Translation blocked due to abusive or inappropriate content.")
    else:
        try:
            translated = GoogleTranslator(source='auto', target=languages[lang_choice]).translate(text)
            st.success(f"Translated Text ({lang_choice}): {translated}")
        except Exception:
            st.error(" Something went wrong while translating.")