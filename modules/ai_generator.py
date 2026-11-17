
from google import genai


def generate_ai_response(
    user_input,
    task="generate",
    category="General",
    tone="Professional",
    api_key=None
):
    # Check API key
    if not api_key:
        raise ValueError("Gemini API key is missing. Check secrets.toml.")

    # Connect to Gemini with a 30-second timeout
    client = genai.Client(
        api_key=api_key,
        http_options={"timeout": 120000}
    )

    # Prepare instructions
    if task == "generate":
        instruction = f"""
        Act as an expert prompt engineer.

        Create a detailed and effective AI prompt.

        User idea: {user_input}
        Category: {category}
        Tone: {tone}

        Include:
        1. Clear instructions
        2. Relevant context
        3. Specific requirements
        4. Expected output format

        Return only the final prompt.
        """

    elif task == "analyze":
        instruction = f"""
        Act as a professional prompt engineering analyst.

        Analyze this prompt:
        {user_input}

        Evaluate:
        1. Clarity
        2. Specificity
        3. Context
        4. Instructions

        Give a quality score out of 100.
        Explain strengths, weaknesses and suggestions.
        """

    elif task == "improve":
        instruction = f"""
        Act as an expert prompt engineer.

        Improve this prompt:
        {user_input}

        Make it clearer, more specific and effective.

        Include:
        1. Role
        2. Context
        3. Instructions
        4. Expected output

        Return the improved prompt and explain the improvements.
        """

    else:
        raise ValueError("Invalid task selected.")

    # Send request to Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=instruction
    )

    # Validate response
    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    return response.text
