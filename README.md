# Autonomous Agents for Meeting Prep

This repo contains scripts that leverage the CrewAI framework to automate the process of prepping for an interal tech sales call. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to identify use cases and put together a solution to solve a specific industry problem.

## Details & Explanation
- **Running the Script**: Execute ```python main.py``` and input your idea when prompted. The script will leverage the CrewAI framework to process the idea and generate a meeting brief document.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./tasks.py`: Main file with the tasks prompts.
  - `./agents.py`: Main file with the agents creation.
  - `./tools`: Contains tool classes used by the agents.

## Implementation
### Agents
1. ```data_scientist_agent```
2. ```software_engineer_agent```
3. ```industry_analyst_agent```
4. ```meeting_strategy_agent```
5. ```summary_and_briefing_agent```

### Tasks
1. ```data_solutioning```
2. ```engineering```
3. ```industry_analysis```
4. ```meeting_strategy```
5. ```summary_and_briefing```

### Tools
ExaSearchTool was used. 


## Running the Script
It uses GPT-4 by default so you should have access to that to run it, however you can use local models with Ollama. Update your ```.env``` file accordingly. 

***Disclaimer:** This will use gpt-4 unless you changed it 
not to, and by doing so it will cost you money.*

- **Configure Environment**: Copy ``.env.example` and set up the environment variables for [Browseless](https://www.browserless.io/), [Serper](https://serper.dev/) and [OpenAI](https://platform.openai.com/api-keys)
- 
  **Execute the Script**: Run `python3 main.py` and input your idea.
