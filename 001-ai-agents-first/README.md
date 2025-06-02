🧠 AI Agents First
Welcome to AI Agents First, a beginner-friendly, hands-on journey into AI agents using modern and powerful tools like OpenRouter, LiteLLM, and the OpenAI Agents SDK. This repository is designed to provide clear examples, practical setups, and code walkthroughs that help you build and experiment with AI agents from scratch.

📁 Folder Structure & Description
00_swarm.txt

Detailed notes and references about the Swarm framework for multi-agent collaboration.

Concepts on how multiple AI agents can communicate, cooperate, and solve complex problems together.

Setup instructions and best practices.

01_uv.txt

Guide to using UV, a lightning-fast Python package manager.

Helps you create isolated and reproducible Python environments tailored for AI projects.

Tips on managing dependencies efficiently.

02_openrouter/

Experiments demonstrating the use of the OpenRouter API.

Examples showing how to route requests seamlessly through multiple Large Language Model providers like OpenAI, Anthropic, and Mistral via a single API endpoint.

Useful for building scalable AI applications with flexible backend model choices.

03_litellm_openai_agents/

Integration examples of LiteLLM with OpenAI Agents SDK.

Showcases function-calling agents with simplified model routing for optimized cost and performance.

Perfect for developers aiming to create modular and efficient AI workflows.

04_hello_agents/

A simple “Hello, World” example using OpenAI Agents SDK.

Teaches how to define tools, build a basic agent, and handle user interactions with minimal setup.

Great starting point for beginners.

🚀 Getting Started
Clone the Repository
git clone https://github.com/fatima-zahra-github-account/agentic-ai-q4
cd 01-ai-agents-first

Set Up Python Environment Using UV
Create a virtual environment:
uv venv
Activate the environment:
source .venv/bin/activate  # On Linux/Mac
.\.venv\Scripts\activate   # On Windows

Install Required Packages
uv pip install -r requirements.txt

Run Example Projects
Navigate to any example folder, e.g.:
cd 02_openrouter
python example.py

Modify and experiment with the code to deepen your understanding.

📚 Technologies Used
OpenRouter: Unified API for multiple LLM providers.

LiteLLM: Lightweight model abstraction for efficient routing and usage.

OpenAI Agents SDK: Framework to create multi-tool AI agents with customizable behaviors.

Python 3.10+: Programming language used for development.

UV: Ultra-fast Python package manager focusing on isolated environments.

🔧 Tips & Best Practices
Always work inside the virtual environment to avoid dependency conflicts.

Read through 00_swarm.txt carefully to understand multi-agent coordination.

Use the “Hello Agents” example to get comfortable before moving to complex integrations.

Experiment with OpenRouter’s API keys and multiple providers to test fallback and routing behavior.

Profile your agents using built-in tracing tools in OpenAI Agents SDK for debugging.

📄 License
This project is licensed under the MIT License, giving you freedom to use, modify, and distribute the code.

✨ Creator
Made with 💖 by Fatima Zahra

