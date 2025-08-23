# Reflexion Agent Workflow

This repository contains a minimal, clean implementation of a reflexion-based agent workflow using Large Language Models (LLMs) and LangGraph. All unnecessary files have been removed; only the main notebook and essential files remain.

## Main Notebook
- **reflexion_graph.ipynb**: The core notebook demonstrating a reflexion agent that answers questions, critiques its own answers, and revises them using search results and self-reflection.

## Features
- **LLM Integration**: Uses Google Gemini and Anthropic models via LangChain.
- **Search Tool**: Integrates Tavily search for real-time information retrieval.
- **Self-Reflection**: Agent critiques and improves its own answers in multiple steps.
- **Graph Workflow**: Utilizes LangGraph to structure agent steps (draft, execute tools, revise).

## Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/MehmetCelik53/multi-agent-llm-workflow.git
   cd multi-agent-llm-workflow
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run `reflexion_graph.ipynb` in Jupyter or VS Code. Enter your API keys when prompted.

## Requirements
- Python 3.10+
- See `requirements.txt` for required packages

## Usage
- Open `reflexion_graph.ipynb` and follow the cells to run the agent workflow.
- The agent will answer, reflect, and revise using search results.

## License
MIT
