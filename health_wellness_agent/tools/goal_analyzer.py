from agents import function_tool, RunContextWrapper
from pydantic import BaseModel, Field
from context import UserContext  # Assuming this is your custom context
from typing import List

# --- Output Model ---
class GoalAnalysis(BaseModel):
    """Analysis of user fitness goals"""
    is_realistic: bool = Field(description="Whether the goal is realistic and healthy")
    reasoning: str = Field(description="Explanation of the analysis")

# --- Goal Analyzer Tool ---
@function_tool
async def goal_analyzer(wrapper: RunContextWrapper[UserContext]) -> GoalAnalysis:
    """
    Analyze the user's fitness goal from their context and return if it’s realistic.
    """
    goal = wrapper.context.goal
    level = wrapper.context.level
    print("Goal from context:", goal)
    print("Level preference from context:", level)

    # Dummy logic to simulate analysis
    if "lose" in goal.lower() and level == "beginner":
        return GoalAnalysis(
            is_realistic=False,
            reasoning="Losing 10kg might be too ambitious for a beginner. Try setting a smaller, more gradual goal."
        )
    else:
        return GoalAnalysis(
            is_realistic=True,
            reasoning="Your fitness goal appears safe and achievable based on your profile."
        )
