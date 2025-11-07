import arcade
import random

SCREEN_WIDTH = 3440
SCREEN_HEIGHT = 1440
SCREEN_TITLE = "sigmaboy"


class Rom4ik(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE, update_rate=1 / 164.999, fullscreen=True)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) :
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_draw(self):
        arcade.start_render()

    def update(self, delta_time):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass


window = Rom4ik()
arcade.run()