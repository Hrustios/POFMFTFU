import pygame
from menu import run_main_menu
from game import run_game

def main():
    pygame.init()
    action = run_main_menu()

    if action == "start":
        run_game()
    elif action == "exit":
        pygame.quit()

if __name__ == "__main__":
    main()
