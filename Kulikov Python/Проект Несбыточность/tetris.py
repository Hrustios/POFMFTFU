import random
import pygame
import pymunk

BLOCK_SIZE = 30
COLORS = [(255, 0, 0), (0, 255, 0), (0, 128, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

SHAPES = {
    "I": [(0, 0), (0, 1), (0, 2), (0, 3)],
    "L": [(0, 0), (0, 1), (0, 2), (1, 2)],
    "J": [(1, 0), (1, 1), (1, 2), (0, 2)],
    "O": [(0, 0), (1, 0), (0, 1), (1, 1)],
    "T": [(1, 0), (0, 1), (1, 1), (2, 1)],
    "S": [(1, 0), (2, 0), (0, 1), (1, 1)],
    "Z": [(0, 0), (1, 0), (1, 1), (2, 1)]
}

class TetrisBlock:
    def __init__(self, shape_key, space, color):
        self.shape_key = shape_key  # Запоминаем тип фигуры
        self.blocks = []
        self.color = color
        self.body = pymunk.Body(1, pymunk.moment_for_box(1, BLOCK_SIZE * 4, BLOCK_SIZE * 4))
        self.body.position = 300, 60
        space.add(self.body)
        shape_offsets = SHAPES[shape_key]

        for dx, dy in shape_offsets:
            vs = [(-BLOCK_SIZE/2, -BLOCK_SIZE/2), (BLOCK_SIZE/2, -BLOCK_SIZE/2),
                  (BLOCK_SIZE/2, BLOCK_SIZE/2), (-BLOCK_SIZE/2, BLOCK_SIZE/2)]
            vs = [(x + dx * BLOCK_SIZE, y + dy * BLOCK_SIZE) for x, y in vs]

            shape = pymunk.Poly(self.body, vs)
            shape.color = self.color + (255,)
            shape.friction = 0.4
            space.add(shape)
            self.blocks.append(shape)


    def draw(self, screen):
        for shape in self.blocks:
            points = shape.get_vertices()
            points = [(int(p.x), int(p.y)) for p in points]
            pygame.draw.polygon(screen, self.color, points)

    def draw_preview(self, screen, x, y):
        # Используем self.shape_key, чтобы получить форму для превью
        for dx, dy in SHAPES[self.shape_key]:
            rect = pygame.Rect(x + dx * BLOCK_SIZE, y + dy * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, self.color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)

    def move(self, direction):
        self.body.position += (direction * BLOCK_SIZE, 0)

    def drop(self):
        self.body.position += (0, BLOCK_SIZE)

    def gravity(self):
        self.body.position += (0, 1)

    def is_static(self):
        return abs(self.body.velocity.y) < 1.0


def get_random_block(space):
    shape_key = random.choice(list(SHAPES.keys()))
    color = random.choice(COLORS)
    return TetrisBlock(shape_key, space, color)