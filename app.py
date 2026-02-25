import streamlit as st
import random
from model import predict_impact
from llm import generate_advice

st.set_page_config(page_title="GreenMind", layout="centered")

# ---------------- HEADER ----------------

st.title("🌱 GreenMind")
st.subheader("Generative AI Climate & Health Intelligence Platform")

st.write("""
GreenMind analyzes your lifestyle, predicts carbon emissions using ML,
and uses a Generative AI Climate Copilot to provide personalized sustainability guidance.
""")

st.divider()

# ---------------- USER INPUTS ----------------

st.header("📥 Lifestyle Inputs")

city = st.text_input("City")

travel = st.selectbox(
    "Primary Travel Mode",
    ["Car", "Bike", "Bus", "Walk"]
)

electricity = st.slider("Monthly Electricity Usage (kWh)", 0, 500, 150)

diet = st.selectbox(
    "Diet Type",
    ["Vegetarian", "Mixed", "Non-Vegetarian"]
)

exercise = st.selectbox(
    "Outdoor Activity Frequency",
    ["Low", "Medium", "High"]
)

# ---------------- SIMULATED AQI + WEATHER ----------------

def get_environment(city):
    if city == "":
        return 0, 0
    aqi = random.randint(70, 190)
    temp = random.randint(22, 38)
    return aqi, temp

# ---------------- MAIN BUTTON ----------------

if st.button("Analyze My Environmental Impact"):

    aqi, temp = get_environment(city)

    # ML prediction
    carbon, health, eco_score = predict_impact(travel, electricity, diet, exercise, aqi)

    st.success("✅ Analysis Completed")

    # ---------------- DASHBOARD ----------------

    st.header("📊 Your Impact Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🌍 Carbon Score", round(carbon, 1))
    c2.metric("❤️ Health Risk", round(health, 1))
    c3.metric("🍃 Eco Score", eco_score)
    c4.metric("🌫 AQI", aqi)

    st.caption(f"Temperature: {temp}°C")

    st.divider()

    # ---------------- HEALTH INTERPRETATION ----------------

    st.subheader("🩺 Health Status")

    if health < 5:
        st.success("Low Risk – Safe for outdoor activity.")
    elif health < 10:
        st.warning("Moderate Risk – Limit long exposure.")
    else:
        st.error("High Risk – Avoid outdoor activity today.")

    # ---------------- LLM CLIMATE COPILOT ----------------

    st.subheader("🤖 GreenMind AI Climate Copilot")

    advice = generate_advice(
        city=city,
        carbon=carbon,
        health=health,
        eco=eco_score,
        aqi=aqi,
        travel=travel,
        electricity=electricity,
        diet=diet,
        exercise=exercise
    )

    st.write(advice)

    st.divider()

    # ---------------- WEEKLY ACTION PLAN ----------------

    st.subheader("📅 Your AI-Generated Weekly Eco Plan")

    st.markdown("""
    • Reduce electricity usage by 10%  
    • Prefer public transport twice this week  
    • Avoid outdoor activity during high AQI  
    • Increase plant-based meals  
    • Monitor dashboard daily  
    """)

    st.divider()

    # ---------------- RESPONSIBLE AI ----------------

    st.caption("""
    Responsible AI Note:
    GreenMind does not store personal data.
    All recommendations are advisory and explainable.
    Users retain full decision control.
    """)

    st.info("ML predicts. LLM explains. People act.")

# ---------------- FOOTER ----------------

st.caption("Built for Hack For Green Bharat | GreenMind AI")
