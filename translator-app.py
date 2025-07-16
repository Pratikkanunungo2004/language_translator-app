import streamlit as st
from deep_translator import GoogleTranslator
from better_profanity import profanity

# Initialize profanity filter
profanity.load_censor_words()

languages = {
    "Arabic": "ar",
    "Bengali": "bn",
    "Chinese": "zh-CN",
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
    if profanity.contains_profanity(text):
        st.error("⚠ Translation blocked due to inappropriate content.")
    else:
        try:
            translated = GoogleTranslator(source='auto', target=languages[lang_choice]).translate(text)
            st.success(f"Translated Text ({lang_choice}): {translated}")
        except Exception:
            st.error("Something went wrong while translating.......")