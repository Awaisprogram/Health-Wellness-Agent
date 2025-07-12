# agent flow
from agents import Agent,InputGuardrail
from context import UserContext
from health_agents.escalation_agent  import escalation_agent 
from health_agents.nutrition_expert_agent import nutrition_expert_agent
from health_agents.injury_support_agent import injury_support_agent
from guardrails import Health_welness_guardrail
from tools.meal_planner import meal_planner
from tools.goal_analyzer import goal_analyzer
from tools.scheduler import schedule_checkin
from tools.workout_recommender import workout_recommender
from tools.tracker import update_progress 


instructions = """
    Collect user fitness and dietary goals through multi-turn natural language conversation.
    
    Use:
    - `goal_analyzer` to verify if the user's fitness goal is realistic.
    - `meal_planner` if the user mentions dietary preferences or asks for meals.
    - `workout_recommender` if the user mentions goals like 'lose weight' or 'build muscle'.
    - `schedule_checkin` if the user wants reminders or check-ins.
    - `update_progress` when user shares achievements or progress.
    
    If the user mentions pain or injury, hand off to the Injury Support Agent.
    If the user has medical dietary needs (like diabetes), use the Nutrition Expert Agent.
    If the user requests to speak with a human, escalate to the Escalation Agent.
    """,

agent = Agent[UserContext](
    name="Wellness Agent",
    instructions= instructions,
    tools=[goal_analyzer,meal_planner,schedule_checkin,workout_recommender,update_progress],  
    handoffs=[
        escalation_agent,
        nutrition_expert_agent,
        injury_support_agent
    ],
    input_guardrails=[
        InputGuardrail(guardrail_function=Health_welness_guardrail),
    ] 
)
