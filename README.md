# 🧠 Health-Wellness-Agent

**An AI-powered Health and Wellness Assistant built with **Chainlit** and the **OpenAI Agents SDK**. It supports natural conversations to help users achieve fitness goals through personalized workouts, meal plans, and progress tracking.**

---

## 🚀 Features

- ✅ Multi-turn conversations
- ✅ Uses persistent session context
- ✅ Custom tools:
  - `goal_analyzer`
  - `meal_planner`
  - `workout_recommender`
  - `schedule_checkin`
  - `update_progress`
- ✅ Modular agents with intelligent handoffs
- ✅ Input guardrails for validation
- ✅ Auth support (Google / GitHub)
- ✅ Built on OpenAI / Gemini models

---

## 🧩 Project Structure

health_wellness_agent/
├── main.py # Chainlit entrypoint
├── context.py # UserContext definition
├── agent_flow.py # Main agent config + handoffs
├── hooks.py # Custom lifecycle hooks
├── guardrails.py # Input validation logic
├── tools/
│ ├── goal_analyzer.py
│ ├── meal_planner.py
│ ├── workout_recommender.py
│ ├── schedule_checkin.py
│ └── update_progress.py
├── health_agents/
│ ├── escalation_agent.py
│ ├── nutrition_expert_agent.py
│ └── injury_support_agent.py
├── utils/
│ └── streaming.py # Streaming function for LLM responses
├── .env # Your API keys
├── .env.example # Sample environment file
└── README.md # 📄 Project documentation


---

health_wellness_agent/
├── main.py # Chainlit entrypoint
├── context.py # UserContext definition
├── agent_flow.py # Main agent config + handoffs
├── hooks.py # Custom lifecycle hooks
├── guardrails.py # Input validation logic
├── tools/
│ ├── goal_analyzer.py
│ ├── meal_planner.py
│ ├── workout_recommender.py
│ ├── schedule_checkin.py
│ └── update_progress.py
├── health_agents/
│ ├── escalation_agent.py
│ ├── nutrition_expert_agent.py
│ └── injury_support_agent.py
├── utils/
│ └── streaming.py # Streaming function for LLM responses
├── .env # Your API keys
├── .env.example # Sample environment file
└── README.md # 📄 Project documentation


---

## ⚙️ Setup Instructions

1. **Clone the repo**
   
git clone https://github.com/yourname/health-wellness-agent.git
cd health-wellness-agent

2. **Install dependencies**

pip install -r requirements.txt

3. **Configure environment**

cp .env.example .env

Add your API keys inside .env:

GEMINI_API_KEY=your_gemini_key
or
OPENAI_API_KEY=your_openai_key

4. **Run Chainlit**
   
chainlit run main.py

## 🧠 Agent & Tools Overview

| Component              | Description                                              |
| ---------------------- | -------------------------------------------------------- |
| `Wellness Agent`       | Main agent for collecting user fitness/diet goals        |
| `goal_analyzer`        | Analyzes if user’s goal is realistic                     |
| `meal_planner`         | Generates 7-day meal plan from dietary preferences       |
| `workout_recommender`  | Suggests workouts from fitness level and goal            |
| `schedule_checkin`     | Schedules recurring check-in reminders                   |
| `update_progress`      | Tracks progress updates in session context               |
| `Injury Support Agent` | Handles injuries, pain, and safety concerns              |
| `Nutrition Agent`      | Handles restrictive diets, allergies, and medical issues |


## 🧠 Agent Instruction Flow

👤 User: I want to lose 10kg.
🤖 Agent: Got it. You're a beginner, right? Here's a safe plan to get started!
🛠️ Tools Triggered: goal_analyzer → workout_recommender → meal_planner

## 🔐 Auth Support

Integrated OAuth callback logic for GitHub and Google in Chainlit.

@cl.oauth_callback
def oauth_callback(...):
    ** Logs authentication provider and user info**

## 🛠️ Tech Stack

🔗 Chainlit (Frontend UI & agent lifecycle)

🧠 OpenAI Agent SDK

🧠 Gemini-Flash API (for model inference)

💬 Pydantic + AsyncIO

📦 Python 3.10+    

## 📌 Author

👤 Awais
Frontend Developer | AI Enthusiast

## 📜 License

This project is under the MIT License — or keep it private if you wish.


