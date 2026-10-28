from dotenv import load_dotenv
from agents import Agent, ModelSettings, function_tool
from messenger import send_email, push
import os 

load_dotenv(override=True)

model = os.getenv("DEFAULT_LLM_MODEL_NAME", "gpt-5.4-mini")
use_email = os.getenv("USE_EMAIL", "true").lower() == "true"

model_settings = ModelSettings(tool_choice="required")

@function_tool
def email_sender_tool(subject: str, text_body: str, html_body: str) -> str:
    """
    Send out an email with the given subject and body
    
    Args:
        subject: The subject of the email
        text_body: The body of the email as plain text
        html_body: The HTML body of the email
    """
    if use_email:
        send_email(subject, text_body, html_body)
    else:
        push(f"Subject: {subject}\n\n{text_body}")
    return "Email sent successfully"


instructions = """
You are provided with a detailed report. Use your tool to send an email, converting the report into
a clean, well presented HTML email with an appropriate subject line.
"""

the_emailer_agent = Agent(
    name = "The Email Sender Agent", 
    instructions = instructions,
    model = model, 
    tools = [email_sender_tool],  
    model_settings = model_settings
    )
