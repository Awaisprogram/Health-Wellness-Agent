# Health & Wellness Planner Agent

This project implements an AI-powered Health & Wellness Planner Agent using the OpenAI Agents SDK and Chainlit for the user interface.

## Overview

The Health & Wellness Planner Agent acts as a personal digital coach, interacting with users in natural language to understand their fitness and dietary goals, provide personalized plans, track progress, and offer support.

## Features

-   **Natural Language Understanding:** Collects user goals through multi-turn conversations.
-   **Personalized Planning:** Generates structured health plans (e.g., 7-day vegetarian meal plan, weekly strength training workout plan).
-   **Context & State Management:** Remembers past conversations and user progress using a shared `UserSessionContext`.
-   **Real-time Streaming:** Provides an engaging, chatbot-like experience by streaming responses.
-   **Input & Output Guardrails:** Ensures valid user input and structured, trustworthy tool output.
-   **Handoffs to Specialized Agents:** Delegates complex or specific user needs to specialized agents like:
    -   `EscalationAgent`: For requests to speak to a human coach.
    -   `NutritionExpertAgent`: For complex dietary needs (e.g., diabetes, allergies).
    -   `InjurySupportAgent`: For physical limitations or injury-specific workouts.
-   **(Optional) Lifecycle Hooks:** Tracks tool usage, logging, and handoff activities (implemented in `hooks.py`).

## Project Structure