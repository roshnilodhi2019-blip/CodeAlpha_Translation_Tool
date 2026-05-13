import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="CodeAlpha Translator", page_icon="🌐")
st.title("🌐 CodeAlpha AI - Translation Tool")
st.caption("Task 1 for CodeAlpha Artificial Intelligence Internship | #codealpha")

src = st.selectbox("From", ['auto', 'english', 'hindi', 'spanish', 'french'])
dest = st.selectbox("To", ['hindi', 'english', 'spanish', 'french'])

text = st.text_area("Enter text to translate:")
if st.button("Translate"):
    if text:
        result = GoogleTranslator(source=src, target=dest).translate(text)
        st.success(f"Translation: {result}")
    else:
        st.warning("Please enter some text!")