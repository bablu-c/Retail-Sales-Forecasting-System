import sys
import os

# Fix path for src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.data_loader import load_data
from src.model import train_model, predict
from src.inventory import inventory_logic
import pandas as pd
import plotly.graph_objects as go

# Title
st.title("📊 Retail Sales Forecasting Dashboard")

# Load Data
df = load_data()

# Train Model
model, df = train_model(df)

# Predict
forecast = predict(model, df)

# Inventory Logic
inventory = inventory_logic(forecast)

# ================= DATA =================
st.subheader("📅 Sales Data")
st.write(df.tail())

# ================= GRAPH =================
st.subheader("📈 Forecast Graph")

fig = go.Figure()

# Actual Sales
fig.add_trace(go.Scatter(
    x=df["date"],
    y=df["sales"],
    mode='lines',
    name='Actual Sales',
    line=dict(color='blue')
))

# Future Dates
future_dates = pd.date_range(
    start=df["date"].iloc[-1],
    periods=len(forecast)+1
)[1:]

# Forecast
fig.add_trace(go.Scatter(
    x=future_dates,
    y=forecast,
    mode='lines',
    name='Forecast',
    line=dict(color='red', dash='dash')
))

# Layout
fig.update_layout(
    title="Sales Forecast",
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Show graph
st.plotly_chart(fig, use_container_width=True)

import os

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# Save graph
try:
    fig.write_image("outputs/forecast.png")
    st.success("✅ Graph saved successfully!")
except Exception as e:
    st.error(f"❌ Error saving graph: {e}")

fig.write_image("outputs/forecast.png")

# ================= FORECAST =================
st.subheader("🔮 Forecast Values")
st.write(forecast)

# ================= INVENTORY =================
st.subheader("📦 Inventory Recommendation")
st.write(inventory)