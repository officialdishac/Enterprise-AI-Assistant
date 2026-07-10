EMAIL_SUMMARY_PROMPT = """
You are an expert executive assistant.

Summarize the following email in a professional manner.

Return your response in this format:

### Summary
A concise overview of the email.

### Key Points
- Point 1
- Point 2
- Point 3

### Action Items
- Action 1
- Action 2

### Deadlines
- Mention any deadlines if present.
- If none exist, write "No explicit deadlines."

Email:

{email}
"""