class Lamp:
    def __init__(self, color: str):
        self.on: bool = False
        self.color = color

    def toggle_switch(self):
        self.on = not self.on

    def state(self):
        if self.on:
            return 'The lamp is on.'
        return 'The lamp is off.'
