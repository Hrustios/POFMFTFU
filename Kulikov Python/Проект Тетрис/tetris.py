import pygame
import random
import sys

pygame.init()

#Спектр цветов игры
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
TRANSPARENT_BLACK = (0, 0, 0, 180)

# Разметка игрового пространства
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
GAME_AREA_LEFT = BLOCK_SIZE

# Фигуры тетриса
SHAPES = [
    [[1, 1, 1, 1]],  # палка
    [[1, 1], [1, 1]],  # квадрат
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L - 1
    [[1, 1, 1], [0, 0, 1]],  # L - 2
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Цвета фигур
SHAPES_COLORS = [CYAN, YELLOW, MAGENTA, BLUE, ORANGE, GREEN, RED]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тетрис")

# Шрифты
font = pygame.font.SysFont('Arial', 25)
big_font = pygame.font.SysFont('Arial', 50)

# Фон меню
menu_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
menu_bg.fill(DARK_GRAY)
menu_bg.set_alpha(200)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=10)
        
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

class Tetris:
    def __init__(self):
        self.grid = [[0 for x in range(GRID_WIDTH)] for x in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.paused = False
        self.score = 0
        self.high_score = 0
        self.lines_cleared = 0
        self.pieces_placed = 0
        self.clock = pygame.time.Clock()
        self.fall_time = 0
        self.fall_speed = 500
        
    def new_piece(self):
        shape = random.choice(SHAPES)
        color = SHAPES_COLORS[SHAPES.index(shape)]
        
        # Позиция инициализации новой фигуры
        x = GRID_WIDTH // 2 - len(shape[0]) // 2
        y = 0
        
        return {'shape': shape, 'color': color, 'x': x, 'y': y}
    
    def valid_move(self, piece, x_offset=0, y_offset=0):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece['x'] + x + x_offset
                    new_y = piece['y'] + y + y_offset
                    
                    if (new_x < 0 or new_x >= GRID_WIDTH or 
                        new_y >= GRID_HEIGHT or 
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True
    
    def rotate_piece(self):
        rotated = []
        for x in range(len(self.current_piece['shape'][0])):
            new_row = []
            for y in range(len(self.current_piece['shape']) - 1, -1, -1):
                new_row.append(self.current_piece['shape'][y][x])
            rotated.append(new_row)
        
        old_shape = self.current_piece['shape']
        self.current_piece['shape'] = rotated
        
        if not self.valid_move(self.current_piece):
            self.current_piece['shape'] = old_shape
    
    def lock_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = self.current_piece['color']
        
        self.pieces_placed += 1
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        
        if not self.valid_move(self.current_piece):
            self.game_over = True
            if self.lines_cleared > self.high_score:
                self.high_score = self.lines_cleared
    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_cleared += 1
                for y2 in range(y, 0, -1):
                    self.grid[y2] = self.grid[y2-1][:]
                self.grid[0] = [0 for x in range(GRID_WIDTH)]
        
        self.lines_cleared += lines_cleared
        
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
            
        if lines_cleared > 0 and lines_cleared % 10 == 0:
            self.fall_speed = max(100, self.fall_speed - 50)
    
    def update(self):
        if self.game_over or self.paused:
            return
            
        current_time = pygame.time.get_ticks()
        if current_time - self.fall_time > self.fall_speed:
            self.fall_time = current_time
            if self.valid_move(self.current_piece, 0, 1):
                self.current_piece['y'] += 1
            else:
                self.lock_piece()
    
    def draw(self):
        screen.fill(BLACK)
        
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(screen, GRAY, 
                                 (GAME_AREA_LEFT + x * BLOCK_SIZE, y * BLOCK_SIZE, 
                                  BLOCK_SIZE, BLOCK_SIZE), 1)
                if self.grid[y][x]:
                    pygame.draw.rect(screen, self.grid[y][x], 
                                     (GAME_AREA_LEFT + x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1, 
                                      BLOCK_SIZE - 2, BLOCK_SIZE - 2))
        
        if not self.game_over:
            for y, row in enumerate(self.current_piece['shape']):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(screen, self.current_piece['color'], 
                                         (GAME_AREA_LEFT + (self.current_piece['x'] + x) * BLOCK_SIZE + 1, 
                                          (self.current_piece['y'] + y) * BLOCK_SIZE + 1, 
                                          BLOCK_SIZE - 2, BLOCK_SIZE - 2))
        
        next_text = font.render("Следующая:", True, WHITE)
        screen.blit(next_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 10))
        
        for y, row in enumerate(self.next_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.next_piece['color'], 
                                     (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 30 + x * BLOCK_SIZE, 
                                      50 + y * BLOCK_SIZE, 
                                      BLOCK_SIZE - 2, BLOCK_SIZE - 2))
        
        score_text = font.render(f"Очки: {self.score}", True, WHITE)
        screen.blit(score_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 120))
        
        high_score_text = font.render(f"Рекорд линий: {self.high_score}", True, WHITE)
        screen.blit(high_score_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 150))
        
        lines_text = font.render(f"Линии: {self.lines_cleared}", True, WHITE)
        screen.blit(lines_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 180))
        
        controls_text = [
            "Управление:",
            "A/D, J/L, ←/→ - влево/вправо",
            "S/K, ↓ - вниз",
            "R/W/I, ↑ - поворот",
            "Пробел - уронить",
            "ESC/P - пауза"
        ]
        
        for i, text in enumerate(controls_text):
            control_line = font.render(text, True, WHITE)
            screen.blit(control_line, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 250 + i * 25))
        
        if self.paused:
            screen.blit(menu_bg, (0, 0))
            pause_text = big_font.render("ПАУЗА", True, WHITE)
            text_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
            screen.blit(pause_text, text_rect)
            
            resume_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 30, 200, 50, "Продолжить", GREEN, BLUE)
            menu_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 40, 200, 50, "В меню", BLUE, GREEN)
            exit_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 110, 200, 50, "Выйти", RED, ORANGE)
            
            mouse_pos = pygame.mouse.get_pos()
            resume_button.check_hover(mouse_pos)
            menu_button.check_hover(mouse_pos)
            exit_button.check_hover(mouse_pos)
            
            resume_button.draw(screen)
            menu_button.draw(screen)
            exit_button.draw(screen)
            
            return {'resume': resume_button, 'menu': menu_button, 'exit': exit_button}
        
        if self.game_over:
            screen.blit(menu_bg, (0, 0))
            game_over_text = big_font.render("ИГРА ОКОНЧЕНА", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
            screen.blit(game_over_text, text_rect)
            
            score_text = big_font.render(f"Линий: {self.lines_cleared}", True, WHITE)
            text_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30))
            screen.blit(score_text, text_rect)
            
            restart_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 30, 200, 50, "Заново", GREEN, BLUE)
            menu_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 100, 200, 50, "В меню", BLUE, GREEN)
            exit_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 170, 200, 50, "Выйти", RED, ORANGE)
            
            mouse_pos = pygame.mouse.get_pos()
            restart_button.check_hover(mouse_pos)
            menu_button.check_hover(mouse_pos)
            exit_button.check_hover(mouse_pos)
            
            restart_button.draw(screen)
            menu_button.draw(screen)
            exit_button.draw(screen)
            
            return {'restart': restart_button, 'menu': menu_button, 'exit': exit_button}
        
        return None

def show_menu(high_score):
    play_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 60, 200, 50, "Играть", GREEN, BLUE)
    controls_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 20, 200, 50, "Управление", BLUE, GREEN)
    exit_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 100, 200, 50, "Выйти", RED, ORANGE)
    
    title_text = big_font.render("ТЕТРИС", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//4))
    
    high_score_text = font.render(f"Рекорд линий: {high_score}", True, WHITE)
    high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//4 + 60))
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if play_button.is_clicked(mouse_pos, event):
                return 'play'
            if controls_button.is_clicked(mouse_pos, event):
                return 'controls'
            if exit_button.is_clicked(mouse_pos, event):
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        screen.blit(title_text, title_rect)
        screen.blit(high_score_text, high_score_rect)
        
        play_button.check_hover(mouse_pos)
        controls_button.check_hover(mouse_pos)
        exit_button.check_hover(mouse_pos)
        
        play_button.draw(screen)
        controls_button.draw(screen)
        exit_button.draw(screen)
        
        pygame.display.flip()

def show_controls():
    back_button = Button(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT - 100, 200, 50, "Назад", BLUE, GREEN)
    
    controls_text = [
        "A/D, J/L, ←/→ - перемещение влево/вправо",
        "S/K, ↓ - ускорить падение",
        "R/W/I, ↑ - повернуть фигуру",
        "Пробел - мгновенно уронить фигуру",
        "ESC/P - пауза",
    ]
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if back_button.is_clicked(mouse_pos, event):
                return
        
        screen.fill(BLACK)
        
        title_text = big_font.render("Управление", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 60))
        screen.blit(title_text, title_rect)
        
        for i, text in enumerate(controls_text):
            if not text:
                continue
            control_line = font.render(text, True, WHITE)
            screen.blit(control_line, (50, 120 + i * 30))
        
        back_button.check_hover(mouse_pos)
        back_button.draw(screen)
        
        pygame.display.flip()

def main(): # Я не привык писать комментарии, простите за это
    high_score = 0
    
    while True:
        action = show_menu(high_score)
        
        if action == 'controls':
            show_controls()
            continue
        elif action == 'play':
            game = Tetris()
            game.high_score = high_score
        
        running = True
        while running:
            buttons = game.draw()
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if game.game_over:
                        if buttons:
                            if event.key == pygame.K_r: 
                                for btn_name, btn in buttons.items():
                                    if btn_name == 'restart' and btn.is_hovered:
                                        game = Tetris()
                                        game.high_score = high_score
                                        break
                    elif game.paused:
                        if event.key in (pygame.K_ESCAPE, pygame.K_p):
                            game.paused = False
                    else:
                        if event.key in (pygame.K_ESCAPE, pygame.K_p):
                            game.paused = True
                        elif event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_j):
                            if game.valid_move(game.current_piece, -1, 0):
                                game.current_piece['x'] -= 1
                        elif event.key in (pygame.K_RIGHT, pygame.K_d, pygame.K_l):
                            if game.valid_move(game.current_piece, 1, 0):
                                game.current_piece['x'] += 1
                        elif event.key in (pygame.K_DOWN, pygame.K_s, pygame.K_k):
                            if game.valid_move(game.current_piece, 0, 1):
                                game.current_piece['y'] += 1
                        elif event.key in (pygame.K_UP, pygame.K_r, pygame.K_w, pygame.K_i):
                            game.rotate_piece()
                        elif event.key == pygame.K_SPACE:
                            while game.valid_move(game.current_piece, 0, 1):
                                game.current_piece['y'] += 1
                            game.lock_piece()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if buttons:
                        for btn_name, btn in buttons.items():
                            if btn.rect.collidepoint(mouse_pos):
                                if btn_name == 'resume':
                                    game.paused = False
                                elif btn_name == 'restart':
                                    game = Tetris()
                                    game.high_score = high_score
                                elif btn_name == 'menu':
                                    running = False
                                    if game.lines_cleared > high_score:
                                        high_score = game.lines_cleared
                                elif btn_name == 'exit':
                                    pygame.quit()
                                    sys.exit()
                                break
            
            game.update()
            game.clock.tick(60)
            if not running and game.lines_cleared > high_score:
                high_score = game.lines_cleared

if __name__ == "__main__":
    main()