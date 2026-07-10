from prompts.email_prompts import EMAIL_SUMMARY_PROMPT

from services.groq_client import get_groq_client


def summarize_email(email_text):

    client = get_groq_client()

    prompt = EMAIL_SUMMARY_PROMPT.format(
        email=email_text
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