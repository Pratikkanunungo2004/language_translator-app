import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌐 Language Translator")

text = st.text_area("Enter text in English:")
lang = st.selectbox("Translate to:", ["hi", "fr", "es", "de", "bn", "ta", "te", "ur", "ja"])

if st.button("Translate"):
    if text.strip() != "":
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
        st.success(translated)
    else:
        st.warning("Please enter some text.")