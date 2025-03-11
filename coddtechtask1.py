import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "cdeb392b5668531e53613bca4a427fc2"  # Replace with your actual API key
CITY = "Bangalore"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    # Extract relevant weather data
    dates = []
    temperatures = []
    humidity = []
    pressure = []

    for forecast in data.get("list", []):
        dates.append(forecast["dt_txt"])
        temperatures.append(forecast["main"]["temp"])  # Already in Celsius
        humidity.append(forecast["main"]["humidity"])
        pressure.append(forecast["main"]["pressure"])

    # Reduce number of labels on x-axis
    step = max(len(dates) // 10, 1)  # Show only every 10th date
    reduced_dates = dates[::step]

    # Create a visualization dashboard
    plt.figure(figsize=(12, 5))

    # Temperature Plot
    sns.lineplot(x=dates, y=temperatures, label="Temperature (°C)", marker="o", color="r")
    plt.xticks(range(0, len(dates), step), reduced_dates, rotation=45, fontsize=8)
    plt.title(f"Temperature Trend in {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid()
    plt.show()

    # Humidity and Pressure Plot
    plt.figure(figsize=(12, 5))
    sns.lineplot(x=dates, y=humidity, label="Humidity (%)", marker="o", color="b")
    sns.lineplot(x=dates, y=pressure, label="Pressure (hPa)", marker="o", color="g")
    plt.xticks(range(0, len(dates), step), reduced_dates, rotation=45, fontsize=8)
    plt.title(f"Humidity & Pressure Trend in {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Values")
    plt.legend()
    plt.grid()
    plt.show()

else:
    print("Error fetching data:", response.json().get("message", "Unknown error"))