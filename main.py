import pyglet
from pyglet.window import Window,  key


# Constants! Useful to have, wouldn't you say? :)
GRAVITY = 800
MOVEMENT_SPEED = 400
JUMP_VELOCITY = 500

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [self.x, self.y,
                                      self.x + self.width, self.y,
                                      self.x + self.width, self.y + self.height,
                                      self.x, self.y + self.height]),
                             ('c3B', [255, 255, 255] * 4))
    def intersects(self, other):
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)

platforms = []
platforms.append(Platform(200, 200, 200, 20))
platforms.append(Platform(500, 300, 150, 20))

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity_x = 0
        self.velocity_y = 0

    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2f', [self.x, self.y,
                                      self.x + self.width, self.y,
                                      self.x + self.width, self.y + self.height,
                                      self.x, self.y + self.height]),
                             ('c3B', self.color * 4))

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.velocity_y -= GRAVITY * dt

        # Check collisions with platforms
        for platform in platforms:
            if platform.intersects(self):
                self.y = platform.y + platform.height
                self.velocity_y = 0

def update_and_draw(dt):
    window.clear()
    #player.update(dt)

    player.draw()

    player.x += player.velocity_x * dt
    player.velocity_y -= GRAVITY * dt
    player.y += player.velocity_y * dt
    if player.y < 0:
        player.y = 0
        player.velocity_y = 0
    if player.y > 750:
        player.y = 750
    player.draw()


def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        player.velocity_x = -MOVEMENT_SPEED
    elif symbol == key.RIGHT:
        player.velocity_x = MOVEMENT_SPEED
    elif symbol == key.UP or symbol == key.SPACE:
        player.velocity_y = JUMP_VELOCITY
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT and player.velocity_x < 0:
        player.velocity_x = 0
    elif symbol == key.RIGHT and player.velocity_x > 0:
        player.velocity_x = 0

window = Window(width = 1600, height = 800, caption = "My very first game with ChatGPT! :)", resizable=True)
window.set_location(100,100)
# This will be our player! He's just a rectangle for now :)

player = pyglet.shapes.Rectangle(x = 400, y = 300, width = 50, height = 50, color = (255, 255, 255))



player.velocity_x = 0
player.velocity_y = 0
player.jump = 0

pyglet.clock.schedule_interval(update_and_draw, 1 / 60)
window.push_handlers(on_key_press, on_key_release)

pyglet.app.run()

