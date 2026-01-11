import streamlit as st
import os

st.set_page_config(
    page_title="Finance & Investments",
    layout="wide"
)

# Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE_DIR, "finance.html")

# Load HTML
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=3000, scrolling=True)
