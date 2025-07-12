from agents import Agent
# from tools.goal_analyzer import analyze_goal
# from context import UserContext


# --- Nutrition Expert Agent ---
nutrition_expert_agent = Agent(
    name="Nutrition Expert Agent",
        instructions=(
            "You are a certified nutritionist specializing in complex dietary needs such as diabetes, gluten intolerance, allergies, "
            "and other health-related restrictions. "
            "When a user shares such a condition, respond with personalized dietary guidance. "
            "Be medically accurate, kind, and practical. Avoid suggesting anything that could harm their health."
        ),
        tools=[]
)

