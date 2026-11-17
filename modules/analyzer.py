
def analyze_prompt(prompt):

    score = 0
    suggestions = []

    # Check whether prompt is empty
    if not prompt.strip():
        return {
            "score": 0,
            "level": "Invalid",
            "suggestions": ["Please enter a prompt."]
        }

    # Check prompt length
    if len(prompt.split()) >= 10:
        score += 20
    else:
        suggestions.append("Make your prompt more detailed.")

    # Check role
    if any(word in prompt.lower() for word in ["act as", "you are", "role"]):
        score += 20
    else:
        suggestions.append("Add a role, such as 'Act as a teacher'.")

    # Check context
    if any(word in prompt.lower() for word in ["context", "background", "about"]):
        score += 20
    else:
        suggestions.append("Provide more background or context.")

    # Check instructions
    if any(word in prompt.lower() for word in ["explain", "create", "write", "generate", "analyze"]):
        score += 20
    else:
        suggestions.append("Use a clear action or instruction.")

    # Check output format
    if any(word in prompt.lower() for word in ["bullet points", "table", "steps", "format", "list"]):
        score += 20
    else:
        suggestions.append("Specify the desired output format.")

    # Determine quality level
    if score >= 80:
        level = "Excellent"
    elif score >= 60:
        level = "Good"
    elif score >= 40:
        level = "Average"
    else:
        level = "Needs Improvement"

    if not suggestions:
        suggestions.append("Your prompt contains all five checked elements!")

    return {
        "score": score,
        "level": level,
        "suggestions": suggestions
    }
