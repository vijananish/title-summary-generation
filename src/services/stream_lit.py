import streamlit as st


def generate_stream(text):
    data = st.text_area("Text", text, height=100)
    return data
