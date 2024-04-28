from textwrap import dedent
from crewai import Task

class MeetingPrepTasks():
	def data_solutioning_task(self, agent, context):
		return Task(
			description=dedent(f"""\
				Develop potential data, machine learning, and artificial intelligence use cases
                that could help solve current industry challenges. 

				Meeting Context: {context}"""),
			expected_output=dedent("""\
				A detailed report summarizing key findings about each use case highlighting
				the business problem, the AI/ML/Data approach or solution being used, and the potential outcomes of the solution."""),
			async_execution=True,
			agent=agent
		)
	def engineering_task(self, agent, context):
		return Task(
			description=dedent(f"""\
				Ideate on a front end that's most suitable for the solutions provided by the Data Scientist. Architect a rough plan for its implementation and 
                specify whether it will be a web application, a mobile application, a collection of scripts, a cloud function, an API, etc.

				Meeting Context: {context}"""),
			expected_output=dedent("""\
				A technical report that identifies appropriate front-end and provides high-level steps
                on its architecture and how it can be implemented."""),
			async_execution=True,
			agent=agent
		)
    

	def industry_analysis_task(self, agent, context):
		return Task(
			description=dedent(f"""\
				Analyze the current industry trends, challenges, and opportunities
				relevant to the meeting's context. Consider market reports, recent
				developments, and expert opinions to provide a comprehensive
				overview of the industry landscape.

				Meeting Context: {context}"""),
			expected_output=dedent("""\
				An insightful analysis that identifies major trends, potential
				challenges, and strategic opportunities."""),
			async_execution=True,
			agent=agent
		)

	def meeting_strategy_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Develop strategic talking points, questions, and discussion angles
				for the meeting based on the research and industry analysis conducted

				Meeting Context: {context}
				Meeting Objective: {objective}"""),
			expected_output=dedent("""\
				Complete report with a list of key talking points, strategic questions
				to ask to help achieve the meetings objective during the meeting."""),
			agent=agent
		)

	def summary_and_briefing_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Compile all the research findings, industry analysis, and strategic
				talking points into a concise, comprehensive briefing document for
				the meeting.
				Ensure the briefing is easy to digest and equips the meeting
				participants with all necessary information and strategies.

				Meeting Context: {context}
				Meeting Objective: {objective}"""),
			expected_output=dedent("""\
				A well-structured briefing document that includes sections for
				participant bios, industry overview, talking points, and
				strategic recommendations."""),
			agent=agent
		)
