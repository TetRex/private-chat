import wax.core
from wax.core import Application, Frame, Panel, Button

class MainFrame(Frame):
    def __init__(self):
        super().__init__(title="Hello WAX")
        panel = Panel(self)
        button = Button(panel, label="Click me", event=self.on_click)
        panel.AddComponent(button, expand='both')
        panel.Pack()
        self.AddComponent(panel, expand='both')
        self.Pack()

    def on_click(self, event):
        print("Button clicked!")

app = Application(MainFrame)
app.Run()