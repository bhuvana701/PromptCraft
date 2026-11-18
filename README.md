

\# ✨ PromptCraft

\### AI-Powered Prompt Engineering Studio



PromptCraft is a Python-based AI application that helps users create, analyze, and improve AI prompts using Google Gemini.



\## 🚀 Features



\### 1. AI Prompt Generator

\- Converts simple ideas into detailed AI prompts.

\- Supports different categories and tones.

\- Generates structured prompts with clear instructions.



\### 2. AI Prompt Analyzer

\- Evaluates prompt quality.

\- Provides a score out of 100.

\- Identifies strengths and weaknesses.

\- Suggests improvements.



\### 3. AI Prompt Improver

\- Enhances existing prompts.

\- Improves clarity and specificity.

\- Adds role, context, instructions, and expected output.



\## 🛠️ Technologies Used



\- Python

\- Streamlit

\- Google Gemini API

\- Google Gen AI SDK



\## 📁 Project Structure



```text

PromptCraft/

│

├── app.py

├── requirements.txt

├── modules/

│   ├── generator.py

│   ├── analyzer.py

│   ├── improver.py

│   └── ai\_generator.py

│

├── .streamlit/

│   └── secrets.toml

│

├── .gitignore

└── README.md

```



\## ⚙️ Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/bhuvana701/PromptCraft.git

```



\### 2. Open the project folder



```bash

cd PromptCraft

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure Gemini API Key



Create a file named `secrets.toml` inside the `.streamlit` folder.



Add:



```toml

GEMINI\_API\_KEY = "YOUR\_GEMINI\_API\_KEY"

```



Replace `YOUR\_GEMINI\_API\_KEY` with your own API key.



\*\*Important:\*\* Never upload your API key to GitHub.



\### 5. Run the application



```bash

streamlit run app.py

```



\## 💡 How to Use



1\. Open the PromptCraft application.

2\. Select Generator, Analyzer, or Improver.

3\. Enter your idea or existing prompt.

4\. Generate the result using AI.

5\. View and download the result.



\## 🌐 GitHub Repository



\[View PromptCraft on GitHub](https://github.com/bhuvana701/PromptCraft)



\## 🔮 Future Enhancements



\- Support for additional AI models.

\- Prompt history and saved prompts.

\- More advanced prompt evaluation.

\- Additional prompt templates and categories.



\## 👩‍💻 Author



Developed as a BCA Final Year Project.



\*\*Project Name:\*\* PromptCraft  

\*\*Domain:\*\* Artificial Intelligence  

\*\*Technology:\*\* Python and Streamlit



