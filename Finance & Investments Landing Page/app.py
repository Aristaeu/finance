import streamlit as st

st.set_page_config(
    page_title="Finance & Investments",
    layout="wide"
)

# Read HTML safely
with open("finance.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Render HTML
st.components.v1.html(
    html_content,
    height=3000,
    scrolling=True
)
