import streamlit as st

st.set_page_config(layout="wide")

with open("finance.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=2000, scrolling=True)
