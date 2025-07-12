from dataclasses import dataclass
import asyncio
from typing import List, Optional, Dict
from pydantic import BaseModel, Field

from agents import RunContextWrapper, function_tool
from context import UserContext  # your actual Pydantic model

class MealPlan(BaseModel):
    daily_calories: int = Field(description="Recommended daily calorie intake")
    meal_suggestions: List[str] = Field(description="Simple meal ideas")
    notes: str = Field(description="Dietary advice and tips")
    


print("Function: ")

@function_tool
async def meal_planner(wrapper: RunContextWrapper[UserContext]) -> MealPlan:
    """
    Suggest a basic 7-day meal plan based on the user's dietary preference.
    """
    diet_preferences = wrapper.context.diet_preferences
    print("Diet preference from context:", diet_preferences)

    try:
        if diet_preferences and diet_preferences.lower() == "vegetarian":
            meals = [
                "Oatmeal with fruits", "Vegetable curry with brown rice",
                "Chickpea salad", "Lentil soup", "Grilled paneer",
                "Tofu stir fry", "Veggie wraps"
            ]
            return MealPlan(
                daily_calories=1800,
                meal_suggestions=meals,
                notes="This is a high-fiber vegetarian meal plan suitable for most healthy adults."
            )

        elif diet_preferences and diet_preferences.lower() == "keto":
            meals = [
                "Scrambled eggs with avocado", "Zucchini noodles with pesto",
                "Grilled chicken and cheese", "Keto egg muffins",
                "Bunless beef burger", "Cauliflower rice", "Keto smoothie"
            ]
            return MealPlan(
                daily_calories=2000,
                meal_suggestions=meals,
                notes="Low-carb, high-fat meals to support ketosis."
            )

        else:
            meals = [
                "Boiled eggs & toast", "Grilled chicken with rice", "Tuna sandwich", 
                "Greek yogurt with fruits", "Vegetable omelette", "Chicken salad", "Rice and lentils"
            ]
            return MealPlan(
                daily_calories=1900,
                meal_suggestions=meals,
                notes="Balanced diet with moderate carbs, proteins, and fats."
            )

    except Exception as e:
        return MealPlan(
            daily_calories=0,
            meal_suggestions=[],
            notes=f"Could not generate meal plan due to: {str(e)}"
        )

async def main():
    # ✅ All required fields for your Pydantic model
    context = UserContext(name="Awais", uid=123, diet_preferences="vegetarian")
    wrapper = RunContextWrapper(context)
    await meal_planner(wrapper)

if __name__ == "__main__":
    asyncio.run(main())
