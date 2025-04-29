# Promptly

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Promptly** is a lightweight command-line tool for improving prompts for OpenAI models.  
It allows you to generate, refine, and grade prompts based on a context file — and automatically save your work into a Markdown file.

---

## ✨ Features

- 🛠 Generate meta-prompts using context documents.
- ✍️ Iteratively refine prompts with additional instructions.
- 📄 Save all improved prompts automatically to a `prompts.md` file in your current working directory.
- 📊 Built-in grading system to evaluate prompt quality.
- 🔍 Context-based prompting: supply any any file in your current working directory as context for the model.

---

## 🚨 **Before You Start**

**Important!**  
In order to use Promptly, you **must export your OpenAI API key** in the terminal where you're running the program. 

**To do this, run:**

```bash
export OPENAI_API_KEY="your-api-key-here"
```

You can get your API key from [OpenAI API keys](https://platform.openai.com/account/api-keys).  
Make sure to replace `"your-api-key-here"` with your actual key.

---

## 🚀 Installation

> **Coming soon to PyPI!**

Once available, you can install directly via pip:

```bash
pip install promptly
```

Until then, you can install manually:

```bash
git clone https://github.com/yourusername/promptly.git
cd promptly
pip install .
```

---

## 🛠 Usage

After installing, simply run:

```bash
promptly
```

You’ll be guided through:
1. **Entering a base prompt** you want to improve.
2. **Selecting a context file** (e.g., `background.txt`). For now, the casing for the file needs to exactly match. Soon we will match files even if the casing is not exactly correct.
3. **Choosing verbosity** ('low', 'medium', or 'high' detail).
4. **Refining** allows you to refine the prompt further instructions. Once you're finished refining, the prompt will be graded versus the first prompt you entered in the program.
5. **Grading** and saving the final prompt to `prompts.md`.

---

## 📋 Example CLI Session

```plaintext
Prompt:
> Summarize the key points from the article.

Context:
> article.txt

Verboseness:
> medium

==== RAW META-PROMPT TEMPLATE ====

...

==== IMPROVED PROMPT ====

...

Refine this prompt? (y/N):
> y
Enter refinement instructions:
> Make it shorter.

==== REFINED PROMPT ====

...
```

Each final prompt is appended into a local `prompts.md` file with a timestamp.

---

## 📄 prompts.md Example

```markdown
## Prompt at 2024-04-27 10:32:12

Summarize the main points of the article in a concise, bulleted format.
```

---

## 📦 Project Structure

```bash
promptly/
├── promptly/
│   ├── main.py          # Core CLI tool
│   ├── meta_prompt.py   # Meta-prompt templates
│   ├── grading_prompt.py# Grading templates
│   └── grading_test.py  # Grading logic
├── README.md
├── LICENSE
└── pyproject.toml
```

---

## 🧰 Requirements

- Python 3.8+
- `openai`
- `python-dotenv`

Install them manually:

```bash
pip install openai python-dotenv
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

# ✅ Summary

**Promptly** is a CLI tool to improve and refine your prompts to get the most out of your AI-powered IDEs.
