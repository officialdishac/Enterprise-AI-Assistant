PDF_SUMMARY_PROMPT = """
You are an expert document analyst.

Read the following document and produce a professional summary.

Return the response using this format:

### Summary
Provide a concise overview.

### Key Topics
- Topic 1
- Topic 2
- Topic 3

### Important Insights
- Insight 1
- Insight 2

### Conclusion
A short concluding paragraph.

Document:

{document}
"""