# Multi-Agent LLM Reflexion Workflow

This repository demonstrates a multi-agent workflow using Large Language Models (LLMs) and reflexion techniques. The main notebook is `reflexion_graph.ipynb`, which showcases:

## Features
- **Reflexion Agent Graph**: Implements a research agent that answers, critiques, and revises its own outputs using LangChain, LangGraph, and Tavily search.
- **Search Integration**: Uses Tavily API for web search to improve answers.
- **Self-Reflection**: The agent critiques its own answers and iteratively improves them.
- **Graph-Based Workflow**: Utilizes LangGraph to structure agent steps (draft, execute tools, revise).
- **Extensible Python Modules**: Includes supporting scripts for chains, tool execution, and schema definitions.

## Main Files
- `reflexion_graph.ipynb`: Main notebook with agent workflow and reflexion logic.
- `reflexion_graph.py`: Python script version of the agent workflow.
- `Multi_agents.py`: Example multi-agent implementation.
- `chains.py`, `execute_tools.py`, `schema.py`: Supporting modules for agent logic.
- `requirements.txt`: Python dependencies.

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
3. Add your API keys for Google Gemini and Tavily when prompted in the notebook.
4. Run `reflexion_graph.ipynb` in Jupyter or VS Code.

## Requirements
- Python 3.10+
- See `requirements.txt` for required packages

## Usage
- Open `reflexion_graph.ipynb` and follow the cells to run the agent workflow.
- You can adapt the agent logic for your own research or multi-agent applications.

## License
MIT
