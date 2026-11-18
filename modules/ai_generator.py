
import time
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
        raise ValueError(
            "Gemini API key is missing. Check secrets.toml."
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

    # Connect to Gemini
    client = genai.Client(
        api_key=api_key,
        http_options={"timeout": 120000}
    )

    # Automatic retry settings
    max_attempts = 3

    for attempt in range(max_attempts):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=instruction
            )

            if not response.text:
                raise ValueError("Gemini returned an empty response.")

            return response.text

        except Exception as e:
            if attempt < max_attempts - 1:
                wait_time = 2 ** attempt

                print(
                    f"Gemini attempt {attempt + 1} failed. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:
                raise RuntimeError(
                    f"Gemini failed after {max_attempts} attempts: {e}"
                ) from e
