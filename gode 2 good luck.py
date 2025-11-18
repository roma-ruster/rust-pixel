import arcade
import random

SCREEN_WIDTH = 3440
SCREEN_HEIGHT = 1440
SCREEN_TITLE = "sigmaboy"


class Chibzik(arcade.Sprite):
    def __init__(self, ):
        super().__init__(scale=1, filename="images (1) (3).png", )
        self.center_x = 100
        self.center_y = 100
        # self.DBuXEHUE = [
        #     arcade.load_texture("Bman_B_f00.png"),
        #     arcade.load_texture("Bman_S_f00.png"),
        #     arcade.load_texture("Bman_F_f00.png"),
        #     arcade.load_texture("Bman_S_f00.png", flipped_horizontally=True),
        self.ckorost = 2
    def logic(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class Ship(arcade.Sprite):
    def __init__(self, ):
        super().__init__(scale=1, filename="KORABL/ship13.png", )
        self.center_x = 400
        self.center_y = 100
        self.plavat_D = arcade.load_texture("KORABL/ship13.png")
        self.plavat_W = arcade.load_texture("KORABL/ship1.png")
        self.plavat_A = arcade.load_texture("KORABL/ship5.png")
        self.plavat_S = arcade.load_texture("KORABL/ship9.png")
        self.plavat_Dup = arcade.load_texture("KORABL/ship15.png")
        self.plavat_Ddown = arcade.load_texture("KORABL/ship11.png")
        self.plavat_Aup = arcade.load_texture("KORABL/ship3.png")
        self.plavat_Adown = arcade.load_texture("KORABL/ship7.png")
        self.ckorost = 2
    def logic(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
    def update_animation(self, delta_time: float = 1 / 60):

        dx = self.change_x
        dy = self.change_y

        if dx == 0 and dy == 0:
            return

        # horiz
        if dx > 0 and dy == 0:
            self.texture = self.plavat_D
        if dx < 0 and dy == 0:
            self.texture = self.plavat_A

        # vertic
        if dy > 0 and dx == 0:
            self.texture = self.plavat_W
        if dy < 0 and dx == 0:
            self.texture = self.plavat_S

        # diagon
        if dx > 0 and dy > 0:
            self.texture = self.plavat_Dup
        if dx < 0 and dy > 0:
            self.texture = self.plavat_Aup
        if dx > 0 and dy < 0:
            self.texture = self.plavat_Ddown
        if dx < 0 and dy < 0:
            self.texture = self.plavat_Adown

class Rom4ik(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE, update_rate=1 / 164.999, fullscreen=False)
        self.chibzik = Chibzik()
        self.ship = Ship()
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) :
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.chibzik.change_x = self.chibzik.ckorost
            # self.chibzik.texture = self.chibzik.DBuXEHUE[1]
        if symbol == arcade.key.A :
            # self.chibzik.texture = self.chibzik.DBuXEHUE[3]
            self.chibzik.change_x = -self.chibzik.ckorost
        if symbol == arcade.key.W:
            self.chibzik.change_y = self.chibzik.ckorost
            # self.chibzik.texture = self.chibzik.DBuXEHUE[0]
        if symbol == arcade.key.S:
            self.chibzik.change_y = -self.chibzik.ckorost
            # self.chibzik.texture = self.chibzik.DBuXEHUE[2]

        if symbol == arcade.key.D:
            self.ship.change_x = self.ship.ckorost
            # self.chibzik.texture = self.chibzik.DBuXEHUE[1]
        if symbol == arcade.key.A:
            # self.chibzik.texture = self.chibzik.DBuXEHUE[3]
            self.ship.change_x = -self.ship.ckorost
        if symbol == arcade.key.W:
            self.ship.change_y = self.ship.ckorost
            # self.chibzik.texture = self.chibzik.DBuXEHUE[0]
        if symbol == arcade.key.S:
            self.ship.change_y = -self.ship.ckorost
            # self.chibzik.texture = self.chibzik.DBuXEHUE[2]

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D :
            self.chibzik.change_x = 0
        if symbol == arcade.key.A :
            self.chibzik.change_x = 0
        if symbol == arcade.key.W:
            self.chibzik.change_y = 0
        if symbol == arcade.key.S:
            self.chibzik.change_y = 0
        if symbol in (arcade.key.A, arcade.key.D):
            self.ship.change_x = 0
        if symbol in (arcade.key.W, arcade.key.S):
            self.ship.change_y = 0

    def on_draw(self):
        arcade.start_render()
        self.chibzik.draw()
        self.ship.draw()


    def update(self, delta_time):
        self.chibzik.logic()
        self.ship.logic()
        self.ship.update_animation(delta_time)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass


window = Rom4ik()
arcade.run()

"""
Добавить героя в игру, просто создать спрайт (класс)
Отрисовать его + заспавнить

+ передвигаться в разные стороны
"""