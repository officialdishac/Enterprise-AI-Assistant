import streamlit as st

from ui.home_page import render_home_page
from ui.chat_page import render_chat_page
from ui.email_page import render_email_page
from ui.pdf_page import render_pdf_page

st.set_page_config(
    page_title="Enterprise AI Productivity Assistant",
    page_icon="🤖",
    layout="centered"
)

st.sidebar.title("🤖 Enterprise AI")

feature = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💬 AI Chat",
        "📧 Email Summarizer",
        "📄 PDF Summarizer"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### Built With")

st.sidebar.markdown("""
- 🐍 Python
- ⚡ Groq API
- 🤖 Llama 3.3 70B
- 🎈 Streamlit
""")

st.sidebar.divider()

st.sidebar.caption("Version 1.0")

if feature == "🏠 Home":

    render_home_page()

elif feature == "💬 AI Chat":

    render_chat_page()

elif feature == "📧 Email Summarizer":

    render_email_page()

elif feature == "📄 PDF Summarizer":

    render_pdf_page()