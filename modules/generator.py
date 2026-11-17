
def generate_prompt(topic, category, tone):

    prompt = f"""
Act as an expert in {category}.

Your task is to create a detailed response about: {topic}

Tone: {tone}

Instructions:
1. Understand the topic clearly.
2. Provide accurate and relevant information.
3. Organize the response using headings.
4. Include useful examples.
5. Make the response easy to understand.

Provide a clear and well-structured answer.
"""

    return prompt.strip()
