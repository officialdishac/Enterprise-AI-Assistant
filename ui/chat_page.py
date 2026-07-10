import streamlit as st

from services.chat_service import ask_groq


def render_chat_page():

    st.title("🤖 Enterprise AI Productivity Assistant")

    st.caption("Powered by Groq")

    if "messages" not in st.session_state:

        st.session_state.messages = []

    if st.sidebar.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input("Ask me anything...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        try:

            with st.spinner("Thinking..."):

                response = ask_groq(st.session_state.messages)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            with st.chat_message("assistant"):

                st.markdown(response)

        except Exception:

            st.error(
                "Unable to generate a response. Please check your internet connection or Groq API configuration."
            )