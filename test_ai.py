
import streamlit as st
from modules.ai_generator import generate_ai_response

st.set_page_config(page_title="Gemini AI Test")

st.title("PromptCraft - Gemini AI Test")

st.write("Click the button below to test Gemini AI.")

if st.button("Test Gemini AI"):
    try:
        api_key = st.secrets["GEMINI_API_KEY"]

        with st.spinner("Connecting to Gemini AI..."):
            result = generate_ai_response(
                user_input="Create a study plan for Python beginners",
                task="generate",
                category="Education",
                tone="Professional",
                api_key=api_key
            )

        st.success("Gemini AI connected successfully!")
        st.write(result)

    except Exception as e:
        st.error(f"AI Test Failed: {e}")
