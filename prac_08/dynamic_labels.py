"""
CP1404 Practical 08
Dynamic Labels exercise
Author: Sally Sheldon

Estimated time to complete: 45 mins
Actual time to complete:  mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy app to create label widgets dynamically from a list."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["Harry", "Sally", "Jack", "Imogen", "Haylen", "Kris"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create label widgets from data and add them to the GUI."""
        for name in self.names:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            # add the label to the "labels_box" layout widget
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabelsApp().run()
