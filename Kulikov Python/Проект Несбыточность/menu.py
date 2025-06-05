import pygame
import sys

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600, 800
FONT = pygame.font.SysFont("arial", 36)

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)

def draw_button(screen, text, rect, is_hovered):
    color = GRAY if not is_hovered else DARK_GRAY
    pygame.draw.rect(screen, color, rect)
    label = FONT.render(text, True, WHITE)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

def run_main_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris Menu")

    clock = pygame.time.Clock()

    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 50)
    exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 10, 200, 50)

    while True:
        screen.fill((30, 30, 30))

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        start_hover = start_button.collidepoint(mouse_pos)
        exit_hover = exit_button.collidepoint(mouse_pos)

        draw_button(screen, "Начать игру", start_button, start_hover)
        draw_button(screen, "Выйти", exit_button, exit_hover)

        if mouse_clicked:
            if start_hover:
                return "start"
            elif exit_hover:
                return "exit"

        pygame.display.flip()
        clock.tick(60)
