import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def get_groq_client():
    """
    Creates and returns a Groq client.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. Please check your .env file."
        )

    return Groq(api_key=api_key)