# llm.py

# ---------------- Context Builder ----------------

def build_user_context(city, carbon, health, eco, aqi, travel, electricity, diet, exercise):

    context = {
        "city": city,
        "carbon": carbon,
        "health": health,
        "eco": eco,
        "aqi": aqi,
        "travel": travel,
        "electricity": electricity,
        "diet": diet,
        "exercise": exercise
    }

    return context


# ---------------- Risk Classification ----------------

def classify_air_quality(aqi):
    if aqi < 80:
        return "Good"
    elif aqi < 120:
        return "Moderate"
    elif aqi < 160:
        return "Poor"
    else:
        return "Severe"


def classify_health_risk(health):
    if health < 5:
        return "Low"
    elif health < 10:
        return "Medium"
    else:
        return "High"


# ---------------- Recommendation Engine ----------------

def carbon_reduction_tips(travel, diet, electricity):
    tips = []

    if travel == "Car":
        tips.append("Use public transport or walking twice a week.")
    else:
        tips.append("Continue low-emission travel habits.")

    if electricity > 200:
        tips.append("Reduce electricity usage by 10–15% this month.")
    else:
        tips.append("Maintain efficient electricity consumption.")

    if diet == "Non-Vegetarian":
        tips.append("Increase plant-based meals for lower carbon impact.")

    return tips


def health_safety_tips(aqi, exercise):
    tips = []

    if aqi > 150:
        tips.append("Avoid outdoor activities during peak pollution hours.")

    if exercise == "High":
        tips.append("Prefer indoor workouts on high AQI days.")

    tips.append("Drink adequate water and monitor air quality daily.")

    return tips


# ---------------- Weekly Plan Generator ----------------

def generate_weekly_plan():
    return [
        "Monday–Tuesday: Energy saving focus",
        "Wednesday: Public transport day",
        "Thursday: Plant-based meals",
        "Friday: Indoor workout",
        "Weekend: Monitor Eco Score and plan improvements"
    ]


# ---------------- Main LLM Simulation ----------------

def generate_advice(city, carbon, health, eco, aqi, travel, electricity, diet, exercise):

    user = build_user_context(city, carbon, health, eco, aqi, travel, electricity, diet, exercise)

    air_status = classify_air_quality(aqi)
    health_status = classify_health_risk(health)

    carbon_tips = carbon_reduction_tips(travel, diet, electricity)
    health_tips = health_safety_tips(aqi, exercise)
    weekly_plan = generate_weekly_plan()

    report = f"""
🌱 GreenMind AI Climate Report – {city}

Environmental Status:
• AQI Level: {aqi} ({air_status})
• Carbon Score: {round(carbon,2)}
• Health Risk: {round(health,2)} ({health_status})
• Eco Score: {eco}/100

📉 Carbon Reduction Tips:
"""

    for tip in carbon_tips:
        report += f"• {tip}\n"

    report += "\n❤️ Health Guidance:\n"

    for tip in health_tips:
        report += f"• {tip}\n"

    report += "\n📅 Weekly Sustainability Plan:\n"

    for day in weekly_plan:
        report += f"• {day}\n"

    report += """

This plan is generated using GreenMind’s Generative Intelligence engine
combining ML prediction with context-aware AI reasoning.

Small daily actions lead to big environmental impact.
"""

    return report


# ---------------- Chatbot Reasoning ----------------

def chat_with_ai(question, carbon, health, aqi):

    air_status = classify_air_quality(aqi)
    health_status = classify_health_risk(health)

    response = f"""
You asked: {question}

Current Status:
• AQI: {aqi} ({air_status})
• Health Risk: {health_status}

GreenMind recommends:
• Reduce vehicle usage
• Save electricity during peak hours
• Limit outdoor exposure if AQI is high
• Maintain hydration and indoor air quality

Your choices today shape tomorrow’s climate.
"""

    return response
