from agents import function_tool, RunContextWrapper
from pydantic import BaseModel, Field
from typing import Optional
from context import UserContext

# --- Input and Output Schemas ---

class CheckinSchedulerInput(BaseModel):
    frequency: str = Field(
        default="weekly",
        description="Frequency of check-ins, e.g., 'weekly', 'bi-weekly'."
    )
    day_of_week: Optional[str] = Field(
        default="Monday",
        description="Preferred day of the week for check-ins."
    )

class CheckinSchedulerOutput(BaseModel):
    status: str = Field(description="Status of the scheduling request (e.g., 'success').")
    message: str = Field(description="Confirmation or result message.")

# --- Tool Function ---

@function_tool
async def schedule_checkin(wrapper: RunContextWrapper[UserContext], input: CheckinSchedulerInput) -> CheckinSchedulerOutput:
    """
    Schedules recurring weekly progress checks with the user.
    """

    context = wrapper.context

    # Optional: You can log current workout plan or reference it
    workout_plan = context.workout_plan
    print("Workout plan from context:", workout_plan)

    message = (
        f"I've scheduled a {input.frequency} progress check-in for you,. "
        f"starting every {input.day_of_week}. Look forward to tracking your progress!"
    )

    # Add a progress log
    context.progress_logs.append({
        "event": "Check-in Scheduled",
        "details": message
    })

    return CheckinSchedulerOutput(
        status="success",
        message=message
    )
