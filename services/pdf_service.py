from pypdf import PdfReader

from prompts.pdf_prompts import PDF_SUMMARY_PROMPT

from services.groq_client import get_groq_client


def summarize_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    document_text = ""

    for page in reader.pages:

        document_text += page.extract_text()

    client = get_groq_client()

    prompt = PDF_SUMMARY_PROMPT.format(
        document=document_text
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content