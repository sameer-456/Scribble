import google.generativeai as genai

def process_with_ai(raw_text):

    prompt = f"""
Clean this OCR text, correct spelling using context,
and extract to-do tasks separately.

OCR Text:
{raw_text}

Output format:

Clean Notes:
- ...

To-Do List:
- ...
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text