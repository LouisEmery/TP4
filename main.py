import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.csscolor.BLUE, arcade.csscolor.RED, arcade.color.YELLOW]

class Balle:
    #def ball
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x=x
        self.y=y
        self.change_x=change_x
        self.change_y=change_y
        self.rayon=rayon
        self.color=color
    #change la position de la balle 60 fois par secondes
    def update(self):
        #update and what it does
        self.x += self.change_x
        self.y += self.change_y
        if self.x < self.rayon:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
    def draw(self):
        #draw balls
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rect:
    #make rectangles
    def __init__(self, x2, y2, change_x2, change_y2, base, hauteur, color,angle):
        self.x2 = x2
        self.y2 = y2
        self.change_x2 = change_x2
        self.change_y2 = change_y2
        self.base = base
        self.hauteur=hauteur
        self.color = color
        self.angle=angle
    #changes the rectangles position 60 times per second
    def update2(self):
        #rectangle updates
        self.x2 += self.change_x2
        self.y2 += self.change_y2
        if self.x2 < self.base:
            self.change_x2 *= -1
        elif self.x2 > SCREEN_WIDTH - self.base:
            self.change_x2 *= -1
        if self.y2 < self.hauteur:
            self.change_y2 *= -1
        if self.y2 > SCREEN_HEIGHT - self.hauteur:
            self.change_y2 *= -1




    def draw2(self):
        #draws rectangles
        arcade.draw_rectangle_filled(self.x2,self.y2,self.base,self.hauteur,self.color,self.angle)



class MyGame(arcade.Window):
    #create lists to store circles and rectangles.
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.list_cercle = []
        self.list_rectangles = []

    def on_update(self, delta_time: float):
        #make the updates happen
        global x,y,rayon,change_y,change_x,x2,y2,change_y2,hange_x2,base,hauteur
        for Balle in self.list_cercle:
            Balle.update()
        for Rect in self.list_rectangles:
            Rect.update2()

    def setup(self):
        pass

    def on_draw(self):
        #draws everything when button is pressed
        arcade.start_render()
        for balle in self.list_cercle:
            balle.draw()
        for rect in self.list_rectangles:
            rect.draw2()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        #when abutton is pressed(left = ball and right = rectangle)
        if button == arcade.MOUSE_BUTTON_LEFT:
            #create ball and store it in the list
            balle = Balle(x,y,3,3,random.randint(10,30),random.choice(COLORS))
            self.list_cercle.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            #create rectangle and store it in the list
            rect = Rect(x,y,3,3,random.randint(10,30),random.randint(10,30),random.choice(COLORS),random.randint(0,180))
            self.list_rectangles.append(rect)




def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()