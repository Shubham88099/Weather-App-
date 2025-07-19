import tkinter as tk
import requests

# Your API Key
api_key = '30d4741c779ba94c470ca1f63045390a'

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
        )
        data = response.json()

        if data.get('cod') == '404':
            result_label.config(text="No City Found")
        else:
            weather = data['weather'][0]['main']
            temp_f = round(data['main']['temp'])
            temp_c = round((temp_f - 32) * 5 / 9)
            result_label.config(text=f"{weather}\nTemperature: {temp_f}°F / {temp_c}°C")

    except:
        result_label.config(text="Error fetching data")

# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x300")

# Entry field
city_entry = tk.Entry(root, width=20, font=("Arial", 14))
city_entry.pack(pady=10)

# Button
search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
search_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the app
root.mainloop()



