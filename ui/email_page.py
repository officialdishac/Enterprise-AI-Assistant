import streamlit as st

from services.email_service import summarize_email


def render_email_page():

    st.title("📧 AI Email Summarizer")

    st.write("Paste an email below and click **Summarize Email**.")

    email_text = st.text_area(
        "Email",
        height=300,
        placeholder="Paste your email here..."
    )

    if st.button("Summarize Email"):

        if email_text.strip() == "":

            st.warning("Please paste an email first.")

        else:

            try:

                with st.spinner("Summarizing..."):

                    summary = summarize_email(email_text)

                st.success("Summary Generated!")

                with st.expander("📄 View Summary", expanded=True):

                    st.markdown(summary)

                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="email_summary.txt",
                    mime="text/plain"
                )

            except Exception:

                st.error(
                    "Unable to summarize the email. Please try again later."
                )