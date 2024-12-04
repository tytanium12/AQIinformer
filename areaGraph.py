import matplotlib.pyplot as plt
from fetchCurrent import Fetch
import math

# Function to fetch AQI data and color
def fetch_aqi_info(latitude, longitude):
    fetcher = Fetch(latitude, longitude)
    aqi_data = fetcher.fetch_aqi_data()

    # Get the rounded current time
    rounded_time = fetcher.fetch_current_time()

    # Find the AQI value closest to the current rounded time
    closest_time_row = aqi_data.iloc[(aqi_data['time'] - rounded_time).abs().argsort()[:1]]
    aqi_value = closest_time_row['us_aqi'].values[0]  # Extract the AQI value for the closest time
    color = fetcher.get_aqi_color(aqi_value)

    return aqi_value, color

def generate_area_graph(latitude, longitude):
    # Get AQI for the central location (My Location)
    aqi_value_my_loc, color_my_loc = fetch_aqi_info(latitude, longitude)

    # Get AQI for nearby locations
    # North
    lat_north = latitude + 0.29
    aqi_value_north, color_north = fetch_aqi_info(lat_north, longitude)

    # South
    lat_south = latitude - 0.29
    aqi_value_south, color_south = fetch_aqi_info(lat_south, longitude)

    # East
    miles_per_degree_longitude = 69.172
    distance_miles = 20
    delta_longitude = distance_miles / (math.cos(math.radians(latitude)) * miles_per_degree_longitude)
    east_longitude = longitude + delta_longitude
    aqi_value_east, color_east = fetch_aqi_info(latitude, east_longitude)

    # West
    west_longitude = longitude - delta_longitude
    aqi_value_west, color_west = fetch_aqi_info(latitude, west_longitude)

    # Set up the figure and axis
    fig, ax = plt.subplots()

    # Define the square dimensions (limits for the plot)
    ax.set_xlim([-1, 1])  # x-axis range
    ax.set_ylim([-1, 1])  # y-axis range

    # Fill each triangle section with a different color
    ax.fill([0, -1, 1], [0, 1, 1], color_north)  # North triangle
    ax.fill([0, 1, 1], [0, 1, -1], color_east)  # East triangle
    ax.fill([0, -1, 1], [0, -1, -1], color_south)  # South triangle
    ax.fill([0, -1, -1], [0, -1, 1], color_west)  # West triangle

    # Draw the X diagonal lines but cut them at the circle's boundary (so they don't cross the center)
    circle_radius = 0.3  # Set a radius for the central circle
    ax.plot([-1, -circle_radius], [-1, -circle_radius], color='black')  # Bottom-left to center-left
    ax.plot([1, circle_radius], [1, circle_radius], color='black')  # Top-right to center-right
    ax.plot([-1, -circle_radius], [1, circle_radius], color='black')  # Top-left to center-left
    ax.plot([1, circle_radius], [-1, -circle_radius], color='black')  # Bottom-right to center-right

    # Plot the central point representing your location (large circle marker)
    ax.plot(0, 0, 'o', markersize=120, color=color_my_loc, markeredgecolor='black', markeredgewidth=2,
            label=f"My Location")  # Central circle

    # Place labels in the center of each triangle
    ax.text(0, 0.7, f"North \n AQI: {aqi_value_north}", fontsize=14, ha='center', va='center',
            color='black')  # North triangle
    ax.text(0.7, 0, f"East \n AQI: {aqi_value_east}", fontsize=14, ha='center', va='center',
            color='black')  # East triangle
    ax.text(0, -0.7, f"South \n AQI: {aqi_value_south}", fontsize=14, ha='center', va='center',
            color='black')  # South triangle
    ax.text(-0.7, 0, f"West \n AQI: {aqi_value_west}", fontsize=14, ha='center', va='center',
            color='black')  # West triangle

    # Add the "My Location" label in the center of the circle
    ax.text(0, 0, f"Selected \n Location \n AQI: {aqi_value_my_loc}", fontsize=14, ha='center', va='center', color='black',
            zorder=3)  # Centered text

    # Customize the plot
    ax.set_xticks([])  # Remove x-axis ticks
    ax.set_yticks([])  # Remove y-axis ticks
    ax.set_aspect('equal')  # Ensure the plot is a square

    # Add a title
    ax.set_title("AQI in Selected Location and Nearby Areas \n (20 miles in each direction)")

    return fig, ax  # Return the figure and axis
