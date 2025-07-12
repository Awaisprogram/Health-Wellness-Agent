from typing import Optional, List, Dict
from pydantic import BaseModel

class UserContext(BaseModel):
    name: str
    uid: int
    level: Optional[str] = None
    goal: Optional[str] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
