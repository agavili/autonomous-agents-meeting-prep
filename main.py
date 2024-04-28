from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import MeetingPrepTasks
from agents import MeetingPrepAgents

tasks = MeetingPrepTasks()
agents = MeetingPrepAgents()

print("## Welcome to the Meeting Prep Crew")
print('-------------------------------')
# participants = input("What are the emails for the participants (other than you) in the meeting?\n")
context = input("What is the context of the meeting?\n")
objective = input("What is your objective for this meeting?\n")

# Create Agents
data_scientist_agent = agents.data_scientist_agent()
software_engineer_agent = agents.software_engineer_agent()
industry_analyst_agent = agents.industry_analyst_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

# Create Tasks
data_solutioning = tasks.data_solutioning_task(data_scientist_agent, context)
engineering = tasks.engineering_task(software_engineer_agent, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, context)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

data_solutioning.context = [industry_analysis]
engineering.context = [industry_analysis, data_solutioning]
meeting_strategy.context = [industry_analysis, data_solutioning, engineering]
summary_and_briefing.context = [industry_analysis, data_solutioning, engineering, meeting_strategy]

# Create Crew responsible for Copy
crew = Crew(
	agents=[
        data_scientist_agent,
        software_engineer_agent,
		industry_analyst_agent,
		meeting_strategy_agent,
		summary_and_briefing_agent
	],
	tasks=[
		industry_analysis,
        data_solutioning,
        engineering,
		meeting_strategy,
		summary_and_briefing
	]
)

game = crew.kickoff()


# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
with open("meeting_brief.txt", "a") as myfile:
    myfile.write(game)

