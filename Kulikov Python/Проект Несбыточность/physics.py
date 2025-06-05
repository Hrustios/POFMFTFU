import pymunk

WIDTH, HEIGHT = 600, 800
ISLAND_WIDTH = 200
ISLAND_HEIGHT = 20

def create_space():
    space = pymunk.Space()
    space.gravity = (0, 900)
    return space

def add_static_island(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (WIDTH // 2, HEIGHT - 100)
    shape = pymunk.Poly.create_box(body, (ISLAND_WIDTH, ISLAND_HEIGHT))
    shape.friction = 1.0
    space.add(body, shape)