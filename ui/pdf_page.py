import streamlit as st

from services.pdf_service import summarize_pdf


def render_pdf_page():

    st.title("📄 AI PDF Summarizer")

    st.write("Upload a PDF document and click **Summarize PDF**.")

    uploaded_pdf = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if st.button("Summarize PDF"):

        if uploaded_pdf is None:

            st.warning("Please upload a PDF first.")

        else:

            try:

                with st.spinner("Reading and summarizing PDF..."):

                    summary = summarize_pdf(uploaded_pdf)

                st.success("Summary Generated!")

                with st.expander("📄 View Summary", expanded=True):

                    st.markdown(summary)

                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="pdf_summary.txt",
                    mime="text/plain"
                )

            except Exception:

                st.error(
                    "Unable to summarize the PDF. Please upload a readable PDF and try again."
                )