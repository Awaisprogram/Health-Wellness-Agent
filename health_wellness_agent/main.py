# main.py
import chainlit as cl
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig 
import os
from dotenv import load_dotenv
from context import UserContext
from agent_flow import agent
from utils.streaming import stream_response 
from hooks import MyHooks 
from typing import Optional, Dict


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
  api_key = gemini_api_key,
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
  model = "gemini-2.0-flash",
  openai_client = provider,
)

start_hook = MyHooks()

config = RunConfig(
  model = model,
  
  model_provider = provider,
  tracing_disabled = True,
)


@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token : str,
  row_user_data: Dict[str,str],
  default_user: cl.User,
) -> Optional[cl.User]:
  """
  Handle the oAuth callback from authentication providers (GitHub or Google)
  Return the user object if authentication is successful
  """
  print(f"Provider: {provider_id}")
  print(f"Row user data: {row_user_data}")
  
  
  if provider_id == "github":
    print(f"GitHub user authenticated: {row_user_data.get('login', 'Unknown')}")
  elif provider_id == "google":
    # Custom handling for Google authentication
    print(f"Google user authenticated: {row_user_data.get('email', 'Unknown')}")
  
  return default_user


@cl.on_chat_start
async def start():
    # --- Statefull or Multi Turn ---
    cl.user_session.set("history" ,[]) 
    
    context = UserContext(
    name="Awais",
    uid=1234,
    diet_preferences="keto",
    level = "beginner",
    goal = "lose weight",
    workout_plan={
        "days_per_week": 5,
        "exercises": ["Push-ups", "Pull-ups", "Deadlifts", "Squats"]
    },
    injury_notes = "no injury",
    progress_logs = []
    
)
    cl.user_session.set("context", context)  

    await cl.Message(content="👋 Hello! I'm your Health Wellness agent . What's your fitness goal?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    context = cl.user_session.get("context")  

    history.append({"role": "user", "content":message.content})
    

    await stream_response(  
        agent=agent,
        user_input= history,
        context=context,
        run_config=config,
        hooks= start_hook,
        history=history
    )
     

    