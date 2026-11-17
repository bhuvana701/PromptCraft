
def improve_prompt(prompt):

    if not prompt.strip():
        return "Please enter a prompt first."

    improved = f"""
Act as an expert in the requested subject.

Task:
{prompt}

Instructions:
1. Understand the task clearly.
2. Provide detailed and accurate information.
3. Organize the response using clear headings.
4. Include relevant examples.
5. Use simple and understandable language.

Output Format:
Present the answer in a structured format with bullet points wherever appropriate.
"""

    return improved.strip()
