from dotenv import load_dotenv
from agents import Agent, WebSearchTool
from agents.model_settings import ModelSettings
import os 

load_dotenv(override=True)

model = os.getenv("DEFAULT_LLM_MODEL_NAME", "gpt-5.4-mini")

instructions = """
You are a research assistant. Given a search term, you search the web for that term and 
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
"""

model_settings = ModelSettings(tool_choice="required")

tools = [WebSearchTool()]

the_search_agent = Agent(
    name = "The Search Agent", 
    instructions = instructions, 
    tools = tools, 
    model = model, 
    model_settings = model_settings
    )
