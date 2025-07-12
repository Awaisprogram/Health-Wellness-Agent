from agents import Agent, Runner, GuardrailFunctionOutput
from pydantic import BaseModel, Field
from typing import List

# --- Output Schema ---
class GoalAnalysis(BaseModel):
    """Analysis of user fitness goals"""
    is_realistic: bool = Field(description="Whether the goal is realistic and healthy")
    reasoning: str = Field(description="Explanation of the analysis")

# --- Guardrail Agent ---
goal_analysis_agent = Agent(
    name="Goal Analyzer",
    instructions="""
    You analyze fitness goals to determine if they are realistic and healthy.
    Losing more than 2 pounds per week is generally considered unsafe.
    """,
    output_type=GoalAnalysis,
)

# --- Input Guardrail Function ---
async def Health_welness_guardrail(ctx, agent, input_data):
    """Check if the user's fitness goals are realistic and safe."""
    try:
        analysis_prompt = f"The user said: {input_data}.\nAnalyze if their fitness goal is realistic and healthy."
        result = await Runner.run(goal_analysis_agent, analysis_prompt)
        final_output = result.final_output_as(GoalAnalysis)
        return GuardrailFunctionOutput(
            output_info=final_output,
            tripwire_triggered=not final_output.is_realistic,
        )
    except Exception as e:
        return GuardrailFunctionOutput(
            output_info=GoalAnalysis(
                is_realistic=True,
                reasoning=f"Error analyzing goal: {str(e)}"
            ),
            tripwire_triggered=False
        )
