from agents import Agent
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os

load_dotenv(override=True)
model = os.getenv("DEFAULT_LLM_MODEL_NAME", "gpt-5.4-mini")

instructions = """
You are a senior researcher tasked with writing a cohesive report for a research query.
You will be provided with the original query, and some research.
Generate a comprehensive report based on the research and the query.
The final output should be in markdown format, and it should be lengthy and detailed. Aim 
for 5-8 pages of content, at least 900 words.
"""


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


the_writer_agent = Agent(
    name = "The Writer Agent",
    instructions = instructions, 
    model = model, 
    output_type = ReportData
    )