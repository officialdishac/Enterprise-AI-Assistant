from prompts.chat_prompts import SYSTEM_PROMPT

from services.groq_client import get_groq_client


def ask_groq(messages):

    client = get_groq_client()

    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(messages)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation
    )

    return response.choices[0].message.content