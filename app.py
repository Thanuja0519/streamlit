import streamlit as st
import random
import time
import plotly.graph_objects as go

# Function to simulate telemetry data
def generate_data():
    # Simulating battery voltage between 0 and 12V
    battery_voltage = round(random.uniform(10, 12), 2)
    imu_sensor = round(random.uniform(-180, 180), 2)
    temperature = round(random.uniform(20, 40), 2)  # Temperature in Celsius
    altitude = round(random.uniform(0, 500), 2)  # Altitude in meters
    gps_data = {"latitude": round(random.uniform(-90, 90), 6),
                "longitude": round(random.uniform(-180, 180), 6)}
    connection_health = random.choice(['Good', 'Poor'])

    return battery_voltage, imu_sensor, temperature, altitude, gps_data, connection_health

# Set the page layout and title
st.set_page_config(page_title="Drone Telemetry Dashboard", layout="wide")
st.title("Real-Time Drone Telemetry Dashboard")

# Display telemetry data in real-time
battery_voltage, imu_sensor, temperature, altitude, gps_data, connection_health = generate_data()

# Create gauges for displaying battery voltage and temperature
col1, col2 = st.columns(2)

with col1:
    # Battery Voltage Gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=battery_voltage,
        title={"text": "Battery Voltage (V)"},
        gauge={'axis': {'range': [None, 12]}, 'bar': {'color': "lightblue"}}))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Temperature Gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=temperature,
        title={"text": "Temperature (°C)"},
        gauge={'axis': {'range': [None, 50]}, 'bar': {'color': "red"}}))
    st.plotly_chart(fig, use_container_width=True)

# Display IMU sensor, altitude, GPS data, and connection health
st.subheader("Telemetry Data")
col3, col4 = st.columns(2)

with col3:
    st.metric("IMU Sensor (°)", imu_sensor)
    st.metric("Altitude (m)", altitude)
    st.metric("GPS Latitude", gps_data['latitude'])
    st.metric("GPS Longitude", gps_data['longitude'])

with col4:
    st.metric("Connection Health", connection_health)

# Simulate live updates (refresh every 2 seconds)
while True:
    battery_voltage, imu_sensor, temperature, altitude, gps_data, connection_health = generate_data()
    time.sleep(2)
    st.experimental_rerun()
