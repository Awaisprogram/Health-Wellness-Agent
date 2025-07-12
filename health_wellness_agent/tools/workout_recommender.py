from agents import function_tool, RunContextWrapper
from pydantic import BaseModel, Field
from typing import List, Optional
from context import UserContext


# --- Output Schema ---

class WorkoutRecommenderOutput(BaseModel):
    workout_type: str
    duration_per_session: str
    sessions_per_week: int
    example_exercises: List[str]
    notes: Optional[str] = None


# --- Tool Function ---

@function_tool
async def workout_recommender(
    wrapper: RunContextWrapper[UserContext]
) -> WorkoutRecommenderOutput:
    """
    Recommends a workout plan using fitness goal, injury notes, and experience level from context.
    """

    context = wrapper.context

    # Extracting values from context safely
    goal = None
    if isinstance(context.goal, list) and context.goal:
        goal = context.goal[0].lower()
    elif isinstance(context.goal, str):
        goal = context.goal.lower()

    experience = getattr(context, "experience_level", "beginner").lower()
    injury = context.injury_notes

    print(f"🧠 Context: goal={goal}, experience={experience}, injury={injury}")

    # Default workout plan
    workout_type = "General Fitness"
    duration = "45 minutes"
    sessions = 3
    exercises = ["Push-ups", "Lunges", "Yoga", "Light Cardio"]
    notes = None

    # Adjust plan based on goal
    if goal == "lose_weight":
        workout_type = "Cardio & Strength"
        duration = "60 minutes"
        sessions = 4
        exercises = ["Jogging", "Burpees", "Squats", "Plank"]
    elif goal == "build_muscle":
        workout_type = "Strength Training"
        duration = "75 minutes"
        sessions = 3
        exercises = ["Deadlifts", "Bench Press", "Rows", "Overhead Press"]

    # Add injury note
    if injury:
        notes = f"⚠️ User has injury note: '{injury}'. Please consult a professional before starting."
        context.injury_notes = injury 

    # Build the plan
    plan = WorkoutRecommenderOutput(
        workout_type=workout_type,
        duration_per_session=duration,
        sessions_per_week=sessions,
        example_exercises=exercises,
        notes=notes
    )

    # Store it in context for multi-turn memory
    context.workout_plan = plan.dict()
    return plan
