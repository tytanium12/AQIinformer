from fetchCurrent import Fetch
import pandas as pd

class AQIVisualizer:
    def __init__(self, canvas, latitude, longitude):
        self.canvas = canvas  # Receive the canvas from the userInterface
        self.latitude = latitude
        self.longitude = longitude

        # Initialize the fetcher and fetch data
        self.fetcher = Fetch(latitude=self.latitude, longitude=self.longitude)
        self.aqi_data = self.fetcher.fetch_aqi_data()

        # Get current rounded time
        self.rounded_time = self.fetcher.fetch_rounded_time()

        # Select specific time points (e.g., -72, -48, ..., 72 hours)
        self.selected_times = [-72, -48, -24, -8, -3, -1, 0, 1, 3, 8, 24, 48, 72]
        self.selected_time_points = [self.rounded_time + pd.Timedelta(hours=t) for t in self.selected_times]

        # Get corresponding AQI values for the selected time points
        self.selected_aqi = []
        for time_point in self.selected_time_points:
            closest_time = self.aqi_data.iloc[(self.aqi_data['time'] - time_point).abs().argsort()[:1]]
            self.selected_aqi.append(closest_time['us_aqi'].values[0])

        # Time frame lengths (proportional to hours) for rectangles
        self.time_frames = [10, 10, 10, 8, 5, 3, 3, 3, 5, 8, 10, 10, 10]

        # Bind the window resize event to redraw the rectangles
        self.canvas.bind("<Configure>", self.draw_rectangles)

    # Function to draw rectangles dynamically based on the window width
    def draw_rectangles(self, event=None):
        # Clear the canvas before redrawing
        self.canvas.delete("all")

        # Get the current window width
        total_width = self.canvas.winfo_width()
        total_height = self.canvas.winfo_height()

        # Set the rectangle height and initial x-coordinate offset
        rect_height = 200
        y_offset = total_height // 4  # Vertically center the rectangles

        # Maximum time frame for proportional width calculation
        max_time_frame = max(self.time_frames)

        # Add the title for the time graph at the top
        self.canvas.create_text(total_width // 2, y_offset - 15, text="AQI Over Time", font=("Helvetica", 16, "bold"),
                                fill="black", anchor="center")

        # Calculate the width proportionally to the time frames
        current_x = 10  # Starting x position
        for i, aqi in enumerate(self.selected_aqi):
            # Proportional width calculation adjusted for total canvas width
            rect_width = (self.time_frames[i] / max_time_frame) * total_width / len(self.time_frames) * 1.2
            x1 = current_x
            y1 = y_offset
            x2 = x1 + rect_width
            y2 = y1 + rect_height

            # Draw rectangle with color based on AQI severity
            color = self.fetcher.get_aqi_color(aqi)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            # Check if this is the "current time" and update text
            time_text = f"AQI: {int(aqi)}            {self.selected_times[i]} hr"  # Default AQI text
            if self.selected_times[i] == 0:  # If the time is 0 (current time), display "NOW"
                time_text = f"AQI: {int(aqi)}            NOW"

            # Display AQI value and time inside the rectangle (bold and vertically aligned)
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            self.canvas.create_text(mid_x, mid_y - 10, text=time_text, font=("Helvetica", 11, "bold"), fill="black",
                                    anchor="center", angle=90)

            # Update current_x to place the next rectangle adjacent
            current_x = x2  # Move x to the end of this rectangle

        # Draw AQI legend
        self.draw_aqi_legend(total_width, total_height)

        # Add the caption below the rectangles
        caption_text = (
            "The graph shows AQI (Air Quality Index) over time. \n"
            "The current time is labeled 'NOW' and past/future time points are shown in hours relative to the current time.\n"
            "The Legend applies to both graphs."
        )

        # Calculate y_offset for the caption, just below the last rectangle
        caption_y_offset = y_offset + rect_height + 30  # A few pixels below the time graph
        self.canvas.create_text(total_width // 2, caption_y_offset, text=caption_text, font=("Helvetica", 12),
                                fill="black", anchor="center")

    def draw_aqi_legend(self, total_width, total_height):
        # Define AQI categories, their colors, and corresponding AQI ranges
        aqi_categories = [
            ("Good", "#00e400", "0-50"),  # Green
            ("Moderate", "#ffff00", "51-100"),  # Yellow
            ("Unhealthy for \n Sensitive Groups", "#ff7e00", "101-150"),  # Orange
            ("Unhealthy", "#ff0000", "151-200"),  # Red
            ("Very Unhealthy", "#8f3f97", "201-300"),  # Purple
            ("Hazardous", "#7e0023", "301-500")  # Maroon
        ]

        # Calculate the width for each legend rectangle, keeping the total width same as the timeline
        total_legend_width = total_width * .8769  # Adjust if needed
        rect_width = total_legend_width / len(aqi_categories)  # Equal width for each category
        rect_height = 50
        y_offset = (total_height // 4) - rect_height - 50

        # Calculate starting x position to align the legend with the graph
        current_x = 10

        # Draw the "Legend" title aligned to the left
        legend_title_y_offset = y_offset + rect_height - 65  # Position a bit above the legend rectangles
        self.canvas.create_text(current_x, legend_title_y_offset, text="Legend", font=("Helvetica", 14, "bold"),
                                fill="black", anchor="w")

        # Draw the rectangles and labels for the legend
        for category, color, aqi_range in aqi_categories:
            x1 = current_x
            y1 = y_offset
            x2 = x1 + rect_width
            y2 = y1 + rect_height

            # Draw rectangle with the AQI color
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            # Display AQI category name and range inside the rectangle (center-aligned)
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2

            # Create the text with category and AQI range
            label_text = f"{category}\n{aqi_range}"
            self.canvas.create_text(mid_x, mid_y, text=label_text, font=("Helvetica", 10), fill="black",
                                    anchor="center")

            # Move to the next rectangle position
            current_x = x2  # Move x to the end of this rectangle
    # def draw_aqi_legend(self, total_width, total_height):
    #     # Define AQI categories and their corresponding colors
    #     aqi_categories = [
    #         ("Good", "#00e400"),  # Green
    #         ("Moderate", "#ffff00"),  # Yellow
    #         ("Unhealthy for \n Sensitive Groups", "#ff7e00"),  # Orange
    #         ("Unhealthy", "#ff0000"),  # Red
    #         ("Very Unhealthy", "#8f3f97"),  # Purple
    #         ("Hazardous", "#7e0023")  # Maroon
    #     ]
    #
    #     # Calculate the width for each legend rectangle, keeping the total width same as the timeline
    #     total_legend_width = total_width * .8769  # Adjust if needed
    #     rect_width = total_legend_width / len(aqi_categories)  # Equal width for each category
    #     rect_height = 40
    #     y_offset = (total_height // 4) - rect_height - 50
    #
    #
    #     # Calculate starting x position to center the legend
    #     current_x = 10
    #
    #     # legend Title
    #     legend_title_y_offset = y_offset + rect_height - 55  # Position a bit above the legend rectangles
    #     self.canvas.create_text((current_x + 10) // 2, legend_title_y_offset, text="Legend", font=("Helvetica", 14, "bold"),
    #                             fill="black", anchor="w")
    #
    #     # Draw the rectangles and labels for the legend
    #     for category, color in aqi_categories:
    #         x1 = current_x
    #         y1 = y_offset
    #         x2 = x1 + rect_width
    #         y2 = y1 + rect_height
    #
    #         # Draw rectangle with the AQI color
    #         self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    #
    #         # Display AQI category name inside the rectangle (horizontally)
    #         mid_x = (x1 + x2) / 2
    #         mid_y = (y1 + y2) / 2
    #         self.canvas.create_text(mid_x, mid_y, text=category, font=("Helvetica", 10), fill="black", anchor="center")
    #
    #         # Move to the next rectangle position
    #         current_x = x2  # Add a small gap between legend items
