from dotenv import load_dotenv
from agents import Agent, trace, Runner
from pydantic import BaseModel, Field
import os

load_dotenv(override = True)

model = os.getenv("DEFAULT_LLM_MODEL_NAME", "gpt-5.4-mini")
number_of_searches = os.getenv("NUMBER_OF_SEARCHES", 4)

instructions = f"""
You are a research assistant. Given a user query, come up with a set of web searches
to perform to best answer the query. Output {number_of_searches} terms to query for.
"""

class WebSearchItem(BaseModel):

    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    search_query: str = Field(description="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")


the_planner_agent = Agent(
    name = "The Planner Agent",
    instructions = instructions,
    model = model,
    output_type = WebSearchPlan
)