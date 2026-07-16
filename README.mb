# Technical Chatbot

A simple AI-powered technical assistant built using the **OpenAI Python SDK** and **Ollama**. The chatbot explains computer science and software engineering concepts in a clear, beginner-friendly manner while providing practical examples and concise summaries.

## Features

* Explain technical concepts in simple language
* Beginner-friendly explanations
* Step-by-step breakdown of concepts
* Python examples where applicable
* Common mistakes and misconceptions
* Concise summaries for quick revision
* Runs locally using Ollama
* Easy to switch between Ollama and other OpenAI-compatible providers

## Tech Stack

* Python
* Ollama
* OpenAI Python SDK
* Jupyter Notebook / VS Code

## Prerequisites

* Python 3.10 or later
* Ollama installed and running
* A locally downloaded language model (e.g., `llama3.2`)

Install the required Python packages:

```bash
pip install openai python-dotenv ipython
```

## Install the Model

Download a model using Ollama:

```bash
ollama pull llama3.2
```

Verify that the model is installed:

```bash
ollama list
```

## Project Structure

```text
technical-chatbot/
│
├── chatbot.ipynb
├── .env
├── README.md
└── requirements.txt
```

## Configuration

If you plan to use cloud providers in addition to Ollama, create a `.env` file:

```text
OPENAI_API_KEY=your_key
GOOGLE_API_KEY=your_key
GROQ_API_KEY=your_key
GROK_API_KEY=your_key
```

For Ollama, configure the client as follows:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
```

## Usage

Run the notebook or Python script and ask any technical question.

Example:

```python
answer_user_question("What is a REST API?")
```

Some questions you can try:

* What is Docker?
* Explain recursion.
* Difference between a process and a thread.
* What is Kubernetes?
* Explain vector databases.
* How does HTTPS work?
* Difference between TCP and UDP.

## Example Response

Each response is structured into the following sections:

* **Overview**
* **How It Works**
* **Example**
* **Common Mistakes**
* **Summary**

The responses are rendered in Markdown for better readability.
