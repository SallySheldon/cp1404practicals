"""
CP1404 Practical 08 - GUI program to demo Kivy box layouts
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy App to demonstrate box layouts."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Print greeting."""
        # print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear input box and reset label."""
        print("test")
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
