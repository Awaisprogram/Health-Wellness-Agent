# chainlit_app.py
import chainlit as cl
from context import UserSessionContext
from main import run_agent_conversation

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("context", UserSessionContext(
        name="Awais",
        uid=123
    ))

@cl.on_message
async def on_message(message: cl.Message):
    context = cl.user_session.get("context")

    async for step in run_agent_conversation(message.content, context):
        await cl.Message(content=step.pretty_output).send()
