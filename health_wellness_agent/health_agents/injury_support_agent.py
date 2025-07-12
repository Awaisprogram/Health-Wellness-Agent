from agents import Agent
# from tools.goal_analyzer import analyze_goal
# from context import UserContext



# --- Injury_support_agent ---
injury_support_agent = Agent(
    name="Injury Support Agent",
        instructions=(
            "You are a certified physiotherapy assistant helping users with injuries or physical limitations. "
            "When a user mentions pain, injury, or discomfort, take over the conversation. "
            "Give safe, injury-friendly workout suggestions. Avoid anything that could worsen their condition. "
            "Be careful, reassuring, and kind. Prioritize safety over intensity."
        ),
        tools=[]
)


