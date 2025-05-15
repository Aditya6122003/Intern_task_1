import streamlit as st  # type: ignore
import requests # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

# Streamlit page configuration
st.set_page_config(page_title="Weather Dashboard", layout="wide")

# API Key
API_KEY = "576394c0719741fdb41103e65bb6ddb9"  # Replace with your actual Weatherbit API key

# Title of the app
st.title("🌤️ Real-Time Weather Dashboard")

# User input for city
city = st.text_input("Enter City Name", "London")

# API URL
URL = f"https://api.weatherbit.io/v2.0/current?city={city}&key={API_KEY}&units=M"

# Fetch and display weather data
if st.button("Get Weather Data"):
    response = requests.get(URL)
    data = response.json()

    if "data" in data:
        weather = data["data"][0]

        # Extract and display weather information
        weather_data = {
            "Temperature (°C)": weather["temp"],
            "Feels Like (°C)": weather["app_temp"],
            "Humidity (%)": weather["rh"],
            "Pressure (hPa)": weather["pres"],
            "Wind Speed (m/s)": weather["wind_spd"],
            "Air Quality Index (AQI)": weather["aqi"],
            "Cloud Cover (%)": weather["clouds"],
        }

        # Convert to DataFrame
        df = pd.DataFrame(weather_data, index=[0])

        # Display weather data table
        st.subheader(f"Weather Data for {city}")
        st.dataframe(df)

        # Visualization
        st.subheader("📊 Weather Metrics Visualization")
        sns.set(style="whitegrid")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=df.columns, y=df.iloc[0], palette="coolwarm", ax=ax)
        plt.xticks(rotation=30)
        st.pyplot(fig)

    else:
        st.error("❌ City not found! Please enter a valid city name.")
 