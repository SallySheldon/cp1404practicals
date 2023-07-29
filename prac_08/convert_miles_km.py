"""
CP1404 Practical 08
Miles to Kilometres converter
Author: Sally Sheldon

Estimated time to complete: 45 mins
Actual time to complete: 80 mins
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

KM_PER_MILE = 1.609344


class ConvertMilesToKmApp(App):
    """ConvertMilesToKm App is a Kivy app for converting miles to kilometres."""
    km_output = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_miles_to_km(self, miles_input):
        """Handle conversion of miles to km; output km to output_label widget."""
        # Convert miles_input text to a number
        miles = self.convert_text_to_number(miles_input)
        # Calculate conversion and display km in output_label
        self.km_output = str(miles * KM_PER_MILE)

    def handle_increment(self, increment):
        """Handle up/down button press by increasing/decreasing miles_input by 1."""
        # Convert miles_input text to a number
        miles = self.convert_text_to_number(self.root.ids.miles_input.text)
        # Increment miles up or down
        miles += increment
        # Update miles_input text to reflect increment
        self.root.ids.miles_input.text = str(miles)

    @staticmethod
    def convert_text_to_number(text):
        """Convert text string to a float, with default value 0.0."""
        try:
            number = float(text)
        except ValueError:
            number = 0.0
        return number


ConvertMilesToKmApp().run()
