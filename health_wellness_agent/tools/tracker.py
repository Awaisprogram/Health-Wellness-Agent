from agents import function_tool, RunContextWrapper
from context import UserContext
import chainlit as cl

@function_tool
async def update_progress(wrapper: RunContextWrapper[UserContext], update: str) -> str:
    # Get context from wrapper
    context = wrapper.context

    # Add progress update
    context.progress_logs.append({"update": update})

    # Save back to Chainlit user session
    cl.user_session.set("context", context)

    return f"✅ Progress updated: {update}"
