import streamlit as st


def render_home_page():
    
    st.title("🤖 Enterprise AI Productivity Assistant")

    st.caption(
        "An AI-powered productivity assistant built using Groq, Streamlit, and Python."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Features", "3")

    with col2:
        st.metric("LLM", "GPT-OSS-120B")

    with col3:
        st.metric("Framework", "Streamlit")

    st.divider()

    st.subheader("🚀 Available Features")

    st.success("💬 AI Chat")
    st.write(
        "Ask questions, solve programming problems, and receive AI-powered assistance."
    )

    st.success("📧 Email Summarizer")
    st.write(
        "Generate concise summaries, identify key points, action items, and deadlines."
    )

    st.success("📄 PDF Summarizer")
    st.write(
        "Upload PDF documents and generate structured summaries within seconds."
    )

    st.divider()

    st.subheader("🛠 Technology Stack")

    st.markdown("""
- 🐍 Python
- 🎈 Streamlit
- ⚡ Groq API
- 🤖 GPT-OSS-120B
- 📄 PyPDF
""")

    st.divider()

    st.subheader("🏗 Project Architecture")

    st.code(
        """
User
   │
   ▼
Streamlit UI
   │
   ▼
UI Layer
   │
   ▼
Service Layer
   │
   ▼
Prompt Layer
   │
   ▼
Groq API
""",
        language="text"
    )

    st.info("👈 Select a feature from the sidebar to begin.")
