import tkinter as tk
from tkinter import messagebox
import random

# Mock database for soil data and crop recommendations
soil_data = {
    "soil_type": "Loamy",
    "pH_level": 6.5,
    "moisture": "Moderate"
}

crop_recommendations = {
    "Loamy": ["Rice", "Wheat", "Vegetables"],
    "Sandy": ["Potatoes", "Carrots"],
    "Clay": ["Sugarcane", "Peanuts"]
}

def get_weather(location):
    """
    Fetches weather data from an API.
    This example uses mock data; you can replace it with actual API calls.
    """
    weather_data = {
        "location": location,
        "temperature": random.uniform(20, 35),
        "humidity": random.randint(50, 90),
        "forecast": "Sunny"
    }
    return weather_data

def get_soil_recommendations(soil_type):
    """
    Provides crop recommendations based on soil type.
    """
    return crop_recommendations.get(soil_type, ["No data available"])

def advisory_system(location):
    """
    Main function for personalized agricultural advisory.
    """
    # Fetch weather information
    weather = get_weather(location)
    weather_info = (
        f"Weather in {weather['location']}:\n"
        f"Temperature: {weather['temperature']:.1f}°C\n"
        f"Humidity: {weather['humidity']}%\n"
        f"Forecast: {weather['forecast']}\n"
    )

    # Add soil data
    soil_info = "Soil Data:\n"
    for key, value in soil_data.items():
        soil_info += f"{key}: {value}\n"

    # Get crop recommendations
    recommended_crops = get_soil_recommendations(soil_data["soil_type"])
    crop_info = f"\nRecommended Crops:\n{', '.join(recommended_crops)}"

    return weather_info + soil_info + crop_info

def display_advisory():
    """
    Event handler for the 'Get Advisory' button.
    """
    location = location_entry.get()  # Get the location from the input field
    if not location.strip():
        messagebox.showerror("Input Error", "Please enter a valid location.")
        return

    # Get the advisory information and display it in a messagebox
    advisory = advisory_system(location)
    messagebox.showinfo("Agricultural Advisory", advisory)

# Create the main GUI application
root = tk.Tk()
root.title("Agricultural Advisory System")

# Add widgets to the GUI
tk.Label(root, text="Enter Your Location:").grid(row=0, column=0, padx=10, pady=10)
location_entry = tk.Entry(root, width=30)
location_entry.grid(row=0, column=1, padx=10, pady=10)

get_advisory_button = tk.Button(root, text="Get Advisory", command=display_advisory)
get_advisory_button.grid(row=1, column=0, columnspan=2, pady=20)

# Run the GUI application
root.mainloop()