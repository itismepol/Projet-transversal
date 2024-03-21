import pygame
import button
from pytmx.util_pygame import load_pygame


def main():

    screen_height = screen.get_height()
    screen_width = screen.get_width()

    # game variables
    game_paused = False
    menu_state = "main"

    initial_jump_speed = 15  # Initial speed of the jump
    gravity = 1  # Gravity
    y_ground = screen_height - 200
    x = 50
    y = y_ground
    y_speed = 0
    is_jumping = False

    # define colours
    black = (0, 0, 0)
    text_col = (255, 255, 255)
    blue = (52, 78, 91)

    # define fonts
    main_font = pygame.font.SysFont("arial black", 40)

    # reset the background
    screen.fill(black)

    # load button images
    resume_img = pygame.image.load("button_resume.png").convert_alpha()
    options_img = pygame.image.load("button_options.png").convert_alpha()
    quit_img = pygame.image.load("button_quit.png").convert_alpha()
    video_img = pygame.image.load('button_video.png').convert_alpha()
    audio_img = pygame.image.load('button_audio.png').convert_alpha()
    keys_img = pygame.image.load('button_keys.png').convert_alpha()
    back_img = pygame.image.load('button_back.png').convert_alpha()

    # create instance of the button
    resume_button = button.Button(554, 125, resume_img, 1.2)
    options_button = button.Button(547, 250, options_img, 1.2)
    quit_button = button.Button(576, 375, quit_img, 1.2)
    video_button = button.Button(476, 75, video_img, 1.2)
    audio_button = button.Button(465, 200, audio_img, 1.2)
    keys_button = button.Button(466, 325, keys_img, 1.2)
    back_button = button.Button(582, 450, back_img, 1.2)

    # tmxdata = load_pygame("map_Test.tmx")
    tmxdata = load_pygame("Test2.tmx")

    def draw_text(text, font, text_colo, x1, y1):
        img = font.render(text, True, text_colo)
        screen.blit(img, (x1, y1))

    # square hit box of the character
    fire_boy = pygame.image.load('fire_boy.png').convert_alpha()
    fire_boy = pygame.transform.scale(fire_boy, (50, 80))
    hit_box_fire = fire_boy.get_rect()
    hit_box_fire.bottomleft = (200, screen_height-200)

    # Load a single image for standing still
    player_stand = pygame.image.load("walk_P1/p3_stand.png").convert_alpha()
    player_stand = pygame.transform.scale(player_stand, (45, 63))   # Resize to 50 wide 70 high
    # Jumping
    player_jump = pygame.image.load("walk_P1/p3_jump.png").convert_alpha()
    player_jump = pygame.transform.scale(player_jump, (45, 63))   # Resize to 50 wide 70 high
    # Landing
    player_land = pygame.image.load("walk_P1/p3_duck.png").convert_alpha()
    player_land = pygame.transform.scale(player_land, (45, 63))   # Resize to 50 wide 70 high
    # Create a list of images for walking left
    player_right = [
        pygame.image.load("walk_P1/p3_walk01.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk02.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk03.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk04.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk05.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk06.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk07.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk08.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk09.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk10.png").convert_alpha(),
        pygame.image.load("walk_P1/p3_walk11.png").convert_alpha(),
    ]
    # Resize all images in the list to 50x70
    player_right = [pygame.transform.scale(image, (45, 63)) for image in player_right]
    # Variable to remember which frame from the list we last displayed
    player_right_frame = 0
    # Create moving left images by flipping the right facing ones on the horizontal axis
    player_left = [pygame.transform.flip(image, True, False) for image in player_right]
    player_left_frame = 0
    # Maintain the direction
    direction = "stand"
    world_offset = [0, 0]
    # hit_box_player = fire_boy.get_rect()
    # hit_box_player.bottomleft = (200, screen_height - 200)
    run = True
    # game loop
    while run:
        screen.fill(blue)
        # back_ground = pygame.image.load('temple_background.jpg').convert()
        # back_ground = pygame.transform.scale(back_ground, (screen_width, screen_height))
        # screen.blit(back_ground, (0, 0))
        blit_all_tiles(screen, tmxdata, world_offset)
        clock.tick(60)

        # check if game is paused
        if game_paused:
            screen.fill(blue)
            # check if is the menu
            if menu_state == "main":
                # draw pause screen buttons
                if resume_button.draw(screen):
                    game_paused = False
                if options_button.draw(screen):
                    menu_state = "options"
                if quit_button.draw(screen):
                    run = False

            # check if the options menu is open
            if menu_state == "options":
                # draw the different options buttons
                if video_button.draw(screen):
                    print("Video Settings")
                if audio_button.draw(screen):
                    print("Audio Settings")
                if keys_button.draw(screen):
                    print("Change Key Bindings")
                if back_button.draw(screen):
                    menu_state = "main"
        else:
            draw_text("Press P to pause", main_font, text_col, 500, 100)

            square = [
                pygame.Rect(250, 760, 810, 10),  # bottom horizontal -
                pygame.Rect(250, 70, 800, 10),  # top horizontal -
                pygame.Rect(250, 70, 10, 700),  # left vertical |
                pygame.Rect(1050, 70, 10, 700)  # right vertical |
            ]

            for platform in square:
                pygame.draw.rect(screen, text_col, platform)

            # keys = pygame.key.get_pressed()
            #
            # if keys[pygame.K_UP] and not is_jumping:  # remove in the future
            #     hit_box_fire.move_ip(0, -5)
            #     direction = "up"
            # if keys[pygame.K_DOWN] and not is_jumping: # remove in the future
            #     hit_box_fire.move_ip(0, 5)
            #     direction = "down"
            # if keys[pygame.K_LEFT]:
            #     hit_box_fire.move_ip(-5, 0)
            #     direction = "left"
            # if keys[pygame.K_RIGHT]:
            #     hit_box_fire.move_ip(5, 0)
            #     direction = "right"
            # if not sum(keys):
            #     direction = "stand"
            #
            # # Keep player within screen limits
            # if hit_box_fire.y < 0:
            #     hit_box_fire.y = 0
            # if hit_box_fire.y >= screen.get_height() - 50:
            #     hit_box_fire.y = screen.get_height() - 50
            # if hit_box_fire.x < 0:
            #     hit_box_fire.x = 0
            # if hit_box_fire.x >= screen.get_width() - 50:
            #     hit_box_fire.x = screen.get_width() - 50

            keyspressed = pygame.key.get_pressed()

            if keyspressed[pygame.K_LEFT]:
                left_tile = get_tile_properties(tmxdata, x-10, y+17, world_offset)
                if not left_tile["solid"]:
                    x -= 5
                    direction = "left"
            if keyspressed[pygame.K_RIGHT]:
                right_tile = get_tile_properties(tmxdata, x+25+10, y+17, world_offset)
                if not right_tile["solid"]:
                    x += 5
                    direction = "right"
            standing_on = get_tile_properties(tmxdata, x + 12, y + 35, world_offset)

            if keyspressed[pygame.K_SPACE] or keyspressed[pygame.K_UP] and not is_jumping:

                is_jumping = True
                y_speed = -initial_jump_speed
                y -= 20
                direction = "jump"

            if keyspressed[pygame.K_DOWN]:
                y += 10
                direction = "land"

            if sum(keyspressed) == 0:  # No key is pressed
                direction = "stand"

            # Keep player within screen limits
            if y < 0:
                y = 0
            if y >= y_ground:
                y = y_ground
            if x < 0:
                x = 0
            if x >= screen.get_width() - 50:
                x = screen.get_width() - 50

            # Draw the player
            if direction == "left":
                screen.blit(player_left[player_left_frame], (x, y))
                player_left_frame = (player_left_frame + 1) % len(player_left)
            elif direction == "right":
                screen.blit(player_right[player_right_frame], (x, y))
                player_right_frame = (player_right_frame + 1) % len(player_right)
            elif direction == "jump":
                screen.blit(player_jump, (x, y))
            elif direction == "land":
                screen.blit(player_land, (x, y))
            else:
                screen.blit(player_stand, (x, y))

            # Mise à jour de la position du personnage
            if is_jumping:
                y_speed += gravity
                hit_box_fire.y += y_speed
                y += y_speed

                if hit_box_fire.y >= screen_height - 200:  # Si le personnage touche le sol
                    hit_box_fire.y = screen_height - 200
                    is_jumping = False

                if y >= screen_height - 200:  # Si le personnage touche le sol
                    y = screen_height - 200
                    is_jumping = False

            # screen.blit(fire_boy, hit_box_fire)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # press SPACE button to pause the game
                    game_paused = True

            if event.type == pygame.QUIT:  # pygame.QUIT event means the user clicked X to close your window
                run = False
        pygame.display.update()

    pygame.quit()

    # water_girl = pygame.image.load('watergirl_pixel.jpg').convert_alpha()
    # water_girl = pygame.transform.scale(water_girl, (200, 100))
    #

    # screen.blit(water_girl, player_pos2)


def blit_all_tiles(window, tmxdata, world_offset):
    for layer in tmxdata:
        for tile in layer.tiles():
            # tile[0] .... x grid location
            # tile[1] .... y grid location
            # tile[2] .... image data for blitting
            img = pygame.transform.scale( tile[2], (50, 50))
            x_pixel = tile[0] * 50 + world_offset[0]
            y_pixel = tile[1] * 50 + world_offset[1]
            window.blit(img, (x_pixel, y_pixel))


def get_tile_properties(tmxdata, x, y, world_offset):
    world_x = x - world_offset[0]
    world_y = y - world_offset[1]
    tile_x = world_x // 35
    tile_y = world_y // 35
    layer = tmxdata.layers[0]
    try:
        properties = tmxdata.get_tile_properties(tile_x, tile_y, 0)
    except ValueError:
        properties = {"climbable": False, "ground": False, "health": -10000,
                      "points": 0, "provides": "", "requires": "", "solid": False}
    if properties is None:
        properties = {"climbable": False, "ground": False, "health": 0,
                      "points": 0, "provides": "", "requires": "", "solid": False}
    return properties


if __name__ == "__main__":
    '''Pygame set up and call the main function '''

    width, height = 800, 600  # Set screen width,height
    pygame.init()  # Start graphics system
    pygame.mixer.init()  # Start audio system
    screen = pygame.display.set_mode((1344, 840))  # screen x0,7
    clock = pygame.time.Clock()  # Create game clock
    pygame.init()
    logo = pygame.image.load('fire_water.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("My game")
    main()
    pygame.quit()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fireboy_pixel.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pass

    def move(self):

        dt = pygame.time.Clock().tick(60) / 1000
        # position of the player
        player_x, player_y = self.rect.x, self.rect.y
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            player_y -= 300 * dt
            if player_y < 0:  # verify if the player has reached the top of the screen
                player_y = 0
        if keys[pygame.K_s]:
            player_y += 300 * dt
            if player_y > 720 - self.rect.height:  # verify if the player has reached the bottom of the screen
                player_y = 720 - self.rect.height
        if keys[pygame.K_q]:
            player_x -= 300 * dt
            if player_x < 0:  # verify if the player has reached the left side of the screen
                player_x = 0
        if keys[pygame.K_d]:
            player_x += 300 * dt
            if player_x > 1280 - self.rect.width:  # verify if the player has reached the right side of the screen
                player_x = 1280 - self.rect.width

        self.rect.x, self.rect.y = player_x, player_y
