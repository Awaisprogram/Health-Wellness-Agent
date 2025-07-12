from agents import RunHooks, Agent, RunContextWrapper
from context import UserContext

class MyHooks(RunHooks):
    async def on_agent_start(self, context: RunContextWrapper[UserContext], agent: Agent):
        print(f"🟢 Agent started: {agent.name} | Usage: {context.usage}")

    async def on_agent_end(self, context: RunContextWrapper, agent: Agent, output: str):
        print(f"✅ Agent Ended: {agent.name}, Output: {output}")

    async def on_tool_start(self, context: RunContextWrapper[UserContext], tool_name: str, input: str):
        print(f"🛠️ Tool started: {tool_name} | Input: {input}")

    async def on_tool_end(self, context: RunContextWrapper, tool_name: str, input: str, output: str):
        print(f"✅ Tool Ended: {tool_name} | Input: {input} | Output: {output}")

    async def on_handoff(self, context: RunContextWrapper[UserContext], from_agent: Agent, to_agent: Agent, input: str):
        print(f"🔄 Handoff: {from_agent.name} → {to_agent.name} | Input: {input}")
