import pygame
import sys
import pygame.font
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
BLUE_SKY = (135, 206, 235)
BROWN_GROUND = (160, 82, 45)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Menu')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)
    return text_rect


running = True
start_game_rect = None
one_player_rect = None
two_players_rect = None

while running:
    screen.fill(BLUE_SKY)
    pygame.draw.rect(screen, BROWN_GROUND, (0, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT//2))

    start_game_rect = draw_text('START GAME', font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 70)
    one_player_rect = draw_text('1 PLAYER', font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    two_players_rect = draw_text('2 PLAYERS', font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_game_rect.collidepoint(event.pos):
                print("START GAME Selected")
            elif one_player_rect.collidepoint(event.pos):
                print("1 PLAYER Mode Selected")
            elif two_players_rect.collidepoint(event.pos):
                print("2 PLAYERS Mode Selected")

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
