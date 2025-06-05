import pygame
import pymunk
import random
from physics import create_space, add_static_island
from tetris import TetrisBlock, get_random_block

WIDTH, HEIGHT = 600, 800
BLOCK_SIZE = 30


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Тетрис с физикой")
    clock = pygame.time.Clock()

    space = create_space()
    add_static_island(space)

    blocks = []
    current_block = get_random_block(space)
    next_block = get_random_block(space)
    max_blocks = load_record()

    paused = False
    frame = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 20))  # Тёмно-синий фон

        pygame.display.flip()
        clock.tick(60)
    
    while True:
        screen.fill((15, 15, 25))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_record(max_blocks)
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                elif not paused:
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        current_block.move(-1)
                    elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                        current_block.move(1)
                    elif event.key in [pygame.K_DOWN, pygame.K_s]:
                        current_block.drop()

        if not paused:
            frame += 1
            if frame % 30 == 0:
                current_block.gravity()

            space.step(1/60)

            if current_block.is_static():
                blocks.append(current_block)
                max_blocks = max(max_blocks, len(blocks))
                current_block = next_block
                next_block = get_random_block(space)

        for block in blocks:
            block.draw(screen)
        current_block.draw(screen)

        draw_next_block(screen, next_block)
        draw_record(screen, max_blocks)

        if paused:
            draw_pause(screen)

        pygame.display.flip()
        clock.tick(60)


def draw_next_block(screen, block):
    font = pygame.font.SysFont("arial", 24)
    text = font.render("Следующая:", True, (200, 200, 200))
    screen.blit(text, (WIDTH - 160, 20))
    block.draw_preview(screen, WIDTH - 130, 60)


def draw_record(screen, record):
    font = pygame.font.SysFont("arial", 24)
    text = font.render(f"Рекорд: {record}", True, (200, 200, 255))
    screen.blit(text, (20, HEIGHT - 40))


def draw_pause(screen):
    font = pygame.font.SysFont("arial", 48)
    text = font.render("Пауза", True, (255, 255, 0))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)


def load_record():
    try:
        with open("record.txt", "r") as f:
            return int(f.read())
    except:
        return 0


def save_record(value):
    with open("record.txt", "w") as f:
        f.write(str(value))
