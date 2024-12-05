import tkinter as tk
from tkinter import messagebox
from fetchCurrent import Fetch
from timeGraph import AQIVisualizer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from areaGraph import generate_area_graph
import geocoder

# Create the WeatherApp interface using tkinter
class WeatherApp:
    def __init__(self, root):
        # Initialize tkinter
        self.root = root
        self.root.title("AQIinformer")
        self.root.geometry("1000x1000")

        # Default font size for labels
        self.fontsize = 14

        # Default values for latitude and longitude (University of Washington, Seattle Campus, Bagley Hall)
        self.default_lat = 47.65
        self.default_lon = -122.31

        # Latitude and Longitude User Inputs
        self.lat_label = tk.Label(root, text="Latitude:", font=("Helvetica", self.fontsize))
        self.lat_label.grid(row=0, column=0, padx=10, pady=0)
        self.lat_entry = tk.Entry(root, font=("Helvetica", self.fontsize))
        self.lat_entry.insert(0, str(self.default_lat))  # Set default latitude value
        self.lat_entry.grid(row=0, column=1, padx=10, pady=0)

        self.lon_label = tk.Label(root, text="Longitude:", font=("Helvetica", self.fontsize))
        self.lon_label.grid(row=1, column=0, padx=10, pady=0)
        self.lon_entry = tk.Entry(root, font=("Helvetica", self.fontsize))
        self.lon_entry.insert(0, str(self.default_lon))  # Set default longitude value
        self.lon_entry.grid(row=1, column=1, padx=10, pady=0)

        # Button to refresh data
        self.refresh_button = tk.Button(root, text="Refresh Data", command=self.refresh_data, font=("Helvetica", self.fontsize, "bold"))
        self.refresh_button.grid(row=2, column=0, columnspan=1, pady=10, padx=5)

        # Button to fetch location
        self.fetch_button = tk.Button(root, text="Get Current Location", command=self.fetch_location, font=("Helvetica", self.fontsize, "bold"))
        self.fetch_button.grid(row=2, column=1, columnspan=1, pady=10, padx=5)

        # Labels for displaying current data
        self.city_label = tk.Label(root, text="Current City:", font=("Helvetica", self.fontsize))
        self.city_label.grid(row=3, column=0, padx=10, pady=0)
        self.city_value = tk.Label(root, text="", font=("Helvetica", self.fontsize))  # Empty label for the current city
        self.city_value.grid(row=3, column=1, padx=10, pady=0)

        self.time_label = tk.Label(root, text="Current Time:", font=("Helvetica", self.fontsize))
        self.time_label.grid(row=4, column=0, padx=10, pady=0)
        self.time_value = tk.Label(root, text="", font=("Helvetica", self.fontsize))  # Empty label for the current time
        self.time_value.grid(row=4, column=1, padx=10, pady=0)

        self.aqi_label = tk.Label(root, text="AQI (Current):", font=("Helvetica", self.fontsize))
        self.aqi_label.grid(row=5, column=0, padx=10, pady=0)
        self.aqi_value = tk.Label(root, text="", font=("Helvetica", self.fontsize))  # Empty label for AQI value
        self.aqi_value.grid(row=5, column=1, padx=10, pady=0)

        self.temp_label = tk.Label(root, text="Temperature:", font=("Helvetica", self.fontsize))
        self.temp_label.grid(row=6, column=0, padx=10, pady=0)
        self.temp_value = tk.Label(root, text="", font=("Helvetica", self.fontsize))  # Empty label for temperature
        self.temp_value.grid(row=6, column=1, padx=10, pady=0)

        self.precip_label = tk.Label(root, text="Precipitation: \n (past 1 hour)", font=("Helvetica", self.fontsize))
        self.precip_label.grid(row=7, column=0, padx=10, pady=0)
        self.precip_value = tk.Label(root, text="", font=("Helvetica", self.fontsize))  # Empty label for precipitation
        self.precip_value.grid(row=7, column=1, padx=10, pady=0)

        self.wind_label = tk.Label(root, text="Wind Speed:", font=("Helvetica", self.fontsize))
        self.wind_label.grid(row=8, column=0, padx=10, pady=0)
        self.wind_value = tk.Label(root, text="", font=("Helvetica", self.fontsize))  # Empty label for wind speed
        self.wind_value.grid(row=8, column=1, padx=10, pady=0)

        # Configuring column sizes and weights for best looking interface
        self.root.grid_columnconfigure(0, weight=0, minsize=10)
        self.root.grid_columnconfigure(1, weight=0, minsize=10)
        self.root.grid_columnconfigure(2, weight=1, minsize=50)

        # Frame to hold the AQIVisualizer (graph)
        self.graph_frame = tk.Frame(root)
        self.graph_frame.grid(row=9, column=0, columnspan=3, pady=20, padx=100)

        # Canvas to display the AQI graph, set to fill horizontally with flexible height
        self.canvas = tk.Canvas(self.graph_frame, height=600, width=800)
        self.canvas.pack(side=tk.TOP, anchor=tk.CENTER, fill=tk.BOTH, expand=True)

        # Frame to hold the areaGraph (graph)
        self.graph_frame2 = tk.Frame(root)
        self.graph_frame2.grid(row=0, column=2, pady=0, rowspan=9)

        # Canvas to display the area graph, set to fill horizontally with flexible height
        self.canvas2 = tk.Canvas(self.graph_frame, height=300, width=1000)
        self.canvas2.pack(side=tk.TOP, anchor=tk.CENTER, fill=tk.BOTH, expand=True)

        # Automatically refresh data upon opening
        self.refresh_data()

    def refresh_data(self):
        try:
            # Get the latitude and longitude from the user input
            latitude = float(self.lat_entry.get())
            longitude = float(self.lon_entry.get())

            # Fetch weather and AQI data using the Fetch class
            fetch = Fetch(latitude, longitude)
            aqi_data = fetch.fetch_aqi_data()
            weather_data = fetch.fetch_weather_data()

            # Get current rounded time
            current_time = fetch.fetch_rounded_time()

            # Find the AQI value closest to the current time
            closest_time_row = aqi_data.iloc[(aqi_data['time'] - current_time).abs().argsort()[:1]]
            aqi_value = closest_time_row['us_aqi'].values[0]

            # Get weather data
            closest_time_row_weather = weather_data.iloc[(weather_data['time'] - current_time).abs().argsort()[:1]]
            temperature = closest_time_row_weather['temperature_2m'].values[0]
            precipitation = closest_time_row_weather['precipitation'].values[0]
            wind_speed = closest_time_row_weather['wind_speed_10m'].values[0]

            # Get current city
            current_city = fetch.get_city_from_coordinates(lat=latitude, lon=longitude)

            # Get current local time from coordinates
            local_time = fetch.get_local_time(latitude, longitude)

            # Update the labels with the fetched data
            self.city_value.config(text=current_city)
            self.time_value.config(text=local_time.strftime("%m/%d/%Y %I:%M %p"))
            self.aqi_value.config(text=str(aqi_value))
            self.temp_value.config(text=f"{temperature} °F")
            self.precip_value.config(text=f"{precipitation} inches")
            self.wind_value.config(text=f"{wind_speed} mph")

            # Create and display the AQIVisualizer graph in the canvas
            self.display_aqi_graph(self.canvas, latitude, longitude)

            # Create and display the AQIVisualizer graph in the canvas
            self.display_area_graph(latitude, longitude)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_aqi_graph(self, canvas, latitude, longitude):
        # Clear the previous graph
        self.canvas.delete("all")

        # Create an AQIVisualizer instance and display the graph
        visualizer = AQIVisualizer(self.canvas, latitude=latitude, longitude=longitude)
        visualizer.draw_rectangles()  # Assuming the AQIVisualizer has a method to draw the graph

    def display_area_graph(self, latitude, longitude):
        # Clear the previous graph
        for widget in self.graph_frame2.winfo_children():
            widget.destroy()

        # Generate and display the area graph for surrounding locations
        fig, ax = generate_area_graph(latitude, longitude)

        # Create a canvas for the graph and display it
        canvas2 = FigureCanvasTkAgg(fig, self.graph_frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def fetch_location(self):
        # Get the user's current location based on IP address
        g = geocoder.ip('me')
        if g.ok:
            lat, lon = g.latlng
            # Populate the latitude and longitude entry fields
            self.lat_entry.delete(0, tk.END)  # Clear existing content
            self.lat_entry.insert(0, str(lat))  # Insert the latitude

            self.lon_entry.delete(0, tk.END)  # Clear existing content
            self.lon_entry.insert(0, str(lon))  # Insert the longitude
        else:
            print("Unable to fetch location")

# Initialize Tkinter root window
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()