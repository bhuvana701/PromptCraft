
import streamlit as st
import re
import html

from modules.generator import generate_prompt
from modules.analyzer import analyze_prompt
from modules.improver import improve_prompt
from modules.ai_generator import generate_ai_response


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PromptCraft",
    page_icon="✨",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #F5F6FC;
    color: #252545;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4, p, li, label {
    color: #252545;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background-color: #17172D;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Main action buttons */

.stButton > button {
    background: linear-gradient(90deg, #7055DC, #9276F5);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
}

.stButton > button:hover {
    background: #5940BD;
    color: white !important;
    border: none;
}

/* Download button */

.stDownloadButton > button {
    background: linear-gradient(90deg, #008F83, #16B8A5);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
}

.stDownloadButton > button:hover {
    background: #00766C;
    color: white !important;
    border: none;
}

/* Input fields */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: white;
    color: #252545;
    border-radius: 8px;
}

/* Feature cards */

.feature-card {
    background-color: white;
    border: 1px solid #E5E2F5;
    border-radius: 15px;
    padding: 22px;
    min-height: 155px;
    box-shadow: 0 3px 12px rgba(40, 30, 90, 0.06);
}

/* Home hero section */

.hero {
    background: linear-gradient(120deg, #6046C7, #987AF2);
    padding: 35px;
    border-radius: 18px;
    margin-bottom: 25px;
}

.hero h1 {
    color: white !important;
    font-size: 38px;
}

.hero p {
    color: #EEE9FF !important;
    font-size: 17px;
}

/* Result box */

.result-box {
    background-color: #FFFFFF;
    color: #252545;
    border: 1px solid #DDD8F0;
    border-left: 5px solid #7055DC;
    border-radius: 12px;
    padding: 22px;
    line-height: 1.7;
    font-size: 15px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    box-shadow: 0 3px 12px rgba(40, 30, 90, 0.05);
}

/* SUCCESS MESSAGE - DARK GREEN THEME */

[data-testid="stAlert"] {
    background-color: #14532D !important;
    border: 1px solid #166534 !important;
    border-radius: 10px !important;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] div,
[data-testid="stAlert"] span {
    color: #DCFCE7 !important;
}

[data-testid="stAlert"] svg {
    color: #86EFAC !important;
    fill: #86EFAC !important;
}

/* Footer */

.footer {
    text-align: center;
    color: #555575;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# GEMINI API CONFIGURATION
# --------------------------------------------------

try:
    API_KEY = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    API_KEY = ""


def get_ai_response(
    user_input,
    task,
    category="General",
    tone="Professional"
):

    if not API_KEY:
        raise ValueError("Gemini API key is missing.")

    return generate_ai_response(
        user_input=user_input,
        task=task,
        category=category,
        tone=tone,
        api_key=API_KEY
    )


# --------------------------------------------------
# RESULT DISPLAY FUNCTION
# --------------------------------------------------

def display_result(result, filename):

    st.markdown("### ✨ Your Result")

    safe_result = html.escape(str(result))

    st.markdown(
        f'<div class="result-box">{safe_result}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.download_button(
        label="⬇️ Download Result",
        data=str(result),
        file_name=filename,
        mime="text/plain"
    )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("✨ PromptCraft")

st.caption("AI-Powered Prompt Engineering Studio")

st.markdown(
    '<span style="background:#E5DFFF; color:#593CB8; '
    'padding:6px 12px; border-radius:20px;">'
    '● Gemini AI Powered</span>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.title("✨ PromptCraft")

st.sidebar.caption("Your AI Prompt Engineering Studio")

menu = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Prompt Generator",
        "Prompt Analyzer",
        "Prompt Improver"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Create smarter prompts with the power of Gemini AI."
)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if menu == "Home":

    st.markdown("""
    <div class="hero">
        <h1>Welcome to PromptCraft! 👋</h1>
        <p>
        Transform simple ideas into powerful AI prompts.
        Generate, analyze and improve prompts using
        intelligent Gemini AI assistance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.header("Explore Our Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>✨ Generator</h3>
            <p>Create detailed and effective prompts
            from simple ideas.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🔍 Analyzer</h3>
            <p>Evaluate prompt quality and identify
            areas for improvement.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🚀 Improver</h3>
            <p>Transform basic prompts into clear,
            structured instructions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.header("How PromptCraft Works")

    st.markdown("""
    1. Enter your idea or existing prompt.
    2. Select the feature you want to use.
    3. Gemini AI processes your request.
    4. View, copy or download your result.
    """)

    st.success(
        "Ready to create better prompts? "
        "Choose a feature from the sidebar!"
    )

    st.divider()

    st.markdown("""
    <div class="footer">
        <b>✨ PromptCraft</b><br>
        AI-Powered Prompt Engineering Studio<br>
        Built with Python, Streamlit and Google Gemini AI
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# PROMPT GENERATOR
# --------------------------------------------------

elif menu == "Prompt Generator":

    st.header("✨ AI Prompt Generator")

    st.write(
        "Turn your simple ideas into detailed, "
        "structured and effective AI prompts."
    )

    topic = st.text_area(
        "Enter your idea or topic",
        placeholder="Example: Create a study plan for Python beginners",
        height=130
    )

    col1, col2 = st.columns(2)

    with col1:
        category = st.selectbox(
            "Select Category",
            [
                "Education",
                "Coding",
                "Business",
                "Writing",
                "Image Generation",
                "Marketing",
                "General"
            ]
        )

    with col2:
        tone = st.selectbox(
            "Select Tone",
            [
                "Professional",
                "Simple",
                "Creative",
                "Friendly"
            ]
        )

    if st.button("🚀 Generate Prompt"):

        if not topic.strip():
            st.warning("Please enter your idea first.")

        else:
            try:
                with st.spinner("Gemini AI is generating your prompt..."):

                    result = get_ai_response(
                        topic,
                        "generate",
                        category,
                        tone
                    )

                st.success("Prompt generated successfully!")

            except Exception as e:

                st.warning(
                    "Gemini AI is unavailable. "
                    "Using the local generator instead."
                )

                st.error(f"Gemini Generator Error: {e}")

                result = generate_prompt(topic, category, tone)

            st.session_state["generator_result"] = result

    if "generator_result" in st.session_state:

        display_result(
            st.session_state["generator_result"],
            "generated_prompt.txt"
        )


# --------------------------------------------------
# PROMPT ANALYZER
# --------------------------------------------------

elif menu == "Prompt Analyzer":

    st.header("🔍 AI Prompt Analyzer")

    st.write(
        "Analyze your existing prompt and understand "
        "its quality, clarity and effectiveness."
    )

    prompt = st.text_area(
        "Enter your prompt",
        placeholder="Example: Explain Python.",
        height=180
    )

    if st.button("🔍 Analyze Prompt"):

        if not prompt.strip():
            st.warning("Please enter a prompt to analyze.")

        else:

            try:
                with st.spinner("Gemini AI is analyzing your prompt..."):

                    result = get_ai_response(
                        prompt,
                        "analyze"
                    )

                st.success("Prompt analysis completed!")

                st.session_state["analyzer_result"] = result
                st.session_state["analyzer_local"] = False

            except Exception as e:

                st.warning(
                    "Gemini AI is unavailable. "
                    "Using the local analyzer instead."
                )

                st.error(f"Gemini Analyzer Error: {e}")

                result = analyze_prompt(prompt)

                st.session_state["analyzer_result"] = result
                st.session_state["analyzer_local"] = True

    if "analyzer_result" in st.session_state:

        result = st.session_state["analyzer_result"]

        if st.session_state.get("analyzer_local"):

            st.metric(
                "Prompt Quality Score",
                f"{result['score']}/100"
            )

            st.subheader(result["level"])

            st.markdown("### Improvement Suggestions")

            for suggestion in result["suggestions"]:
                st.write("•", suggestion)

            display_result(result, "prompt_analysis.txt")

        else:

            score_match = re.search(
                r"(?:overall\s+)?(?:quality\s+)?score\s*[:\-]?\s*(\d{1,3})\s*/\s*100",
                result,
                re.IGNORECASE
            )

            if score_match:
                score = min(int(score_match.group(1)), 100)
                st.metric("Prompt Quality Score", f"{score}/100")

            display_result(result, "prompt_analysis.txt")


# --------------------------------------------------
# PROMPT IMPROVER
# --------------------------------------------------

elif menu == "Prompt Improver":

    st.header("🚀 AI Prompt Improver")

    st.write(
        "Improve your basic prompts by making them "
        "clearer, more specific and effective."
    )

    prompt = st.text_area(
        "Enter your existing prompt",
        placeholder="Example: Write about artificial intelligence.",
        height=180
    )

    if st.button("✨ Improve Prompt"):

        if not prompt.strip():
            st.warning("Please enter a prompt first.")

        else:

            try:
                with st.spinner("Gemini AI is improving your prompt..."):

                    result = get_ai_response(
                        prompt,
                        "improve"
                    )

                st.success("Prompt improved successfully!")

            except Exception as e:

                st.error(f"Gemini Improver Error: {e}")

                st.warning(
                    "Using the local improver instead."
                )

                result = improve_prompt(prompt)

            st.session_state["improver_result"] = result

    if "improver_result" in st.session_state:

        display_result(
            st.session_state["improver_result"],
            "improved_prompt.txt"
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.sidebar.divider()

st.sidebar.caption("PromptCraft | Version 1.0")
