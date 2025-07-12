from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl
from agents import Runner
from hooks import MyHooks


async def stream_response(agent, user_input, context, run_config,hooks, history):

    
    msg = cl.Message(content="")
    await msg.send()


    result = Runner.run_streamed(
        agent,
        input=user_input,
        context=context,
        hooks = hooks,
        run_config=run_config
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    history.append({"role": "assistant", "content": result.final_output}) 
    cl.user_session.set("history", history)
        


    