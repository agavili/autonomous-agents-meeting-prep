from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.ExaSearchTool import ExaSearchTool


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class MeetingPrepAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="mistral")

    def industry_analyst_agent(self):
        return Agent(
            role="Industry Analyst",
            backstory=dedent(f"""Analyze the current industry trends, challenges, and opportunities"""),
            goal=dedent(f"""\
                    As an Industry Analyst, your analysis will identify key technology trends,
					challenges facing the industry, and potential opportunities that
					could be leveraged during the meeting for strategic advantage."""),
            tools=ExaSearchTool.tools(),
            verbose=True,
            llm=self.Ollama,
        )

    def data_scientist_agent(self):
        return Agent(
            role="Data Scientist",
            backstory=dedent(f"""Identify artificial intelligence and machine learning solutions that can potentially help solve industry challenges."""),
            goal=dedent(f"""\
                    As a Data Scientist, your role is to take the technology trends/challenges for given industry and map them 
                    to AI/ML algorithms and solutions that can help solve them. 
                    """),
            tools=ExaSearchTool.tools(),
            verbose=True,
            llm=self.Ollama,
        )

    def software_engineer_agent(self):
        return Agent(
            role="Software Engineer",
            backstory=dedent(f"""Identify and build out front-end or medium for solutions."""),
            goal=dedent(f"""\
                    As a software engineer, your role is to identify the optimal front end to deliver the AI/ML solutions to
                    taking into account effectiveness, feasibility, and time of delivery. Examples of 
                    these front ends can be a web applications, mobile application, APIs, etc."""),
            tools=ExaSearchTool.tools(),
            verbose=True,
            llm=self.Ollama,
        )

    def meeting_strategy_agent(self):
        return Agent(
            role='Meeting Strategy Advisor',
            goal='Develop talking points, questions, and strategic angles for the meeting',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                    As a Strategy Advisor, your expertise will guide the development of
                    talking points, insightful questions, and strategic angles
                    to ensure the meeting's objectives are achieved."""),
            verbose=True,
            llm=self.Ollama,
        )

    def summary_and_briefing_agent(self):
        return Agent(
            role='Briefing Coordinator',
            goal='Compile all gathered information into a concise, informative briefing document',
            tools=ExaSearchTool.tools(),
            backstory=dedent("""\
                    As the Briefing Coordinator, your role is to consolidate the research,
                    analysis, and strategic insights."""),
            verbose=True,
            llm=self.Ollama,
        )