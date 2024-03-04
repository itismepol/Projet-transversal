import pygame
import button
# import pygame_menu
# from pygame_menu import themes


def main():
    # pygame setup
    pygame.init()
    logo = pygame.image.load('fire_water.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("My game")
    screen = pygame.display.set_mode((1344, 840))  # taille écran x0,7
    clock = pygame.time.Clock()
    screen_height = screen.get_height()
    screen_width = screen.get_width()

    # game variables
    game_paused = False
    menu_state = "main"

    jump_height = 100  # Hauteur du saut
    initial_jump_speed = 10  # Vitesse initiale du saut
    gravity = 1  # Gravité

    x = 50
    y = screen_height - 100
    y_speed = 0
    is_jumping = False

    # define colours
    black = (0, 0, 0)
    text_col = (255, 255, 255)

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

    def draw_text(text, font, text_colo, x, y):
        img = font.render(text, True, text_colo)
        screen.blit(img, (x, y))

    # square hit box of the character
    fire_boy = pygame.image.load('fire_boy.png').convert_alpha()
    fire_boy = pygame.transform.scale(fire_boy, (50, 80))
    hit_box_fire = fire_boy.get_rect()
    hit_box_fire.bottomleft = (200, screen_height-200)

    run = True
    # game loop
    while run:
        screen.fill(black)
        back_ground = pygame.image.load('temple_background.jpg').convert()
        back_ground = pygame.transform.scale(back_ground, (screen_width, screen_height))
        screen.blit(back_ground, (0, 0))
        clock.tick(60)


        # check if game is paused
        if game_paused:
            screen.fill((52, 78, 91))
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

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and not is_jumping:  # remove in the future
                hit_box_fire.move_ip(0, -5)
            if keys[pygame.K_DOWN] and not is_jumping:
                hit_box_fire.move_ip(0, 5)
            if keys[pygame.K_LEFT]:
                hit_box_fire.move_ip(-5, 0)
            if keys[pygame.K_RIGHT]:
                hit_box_fire.move_ip(5, 0)

            # Mise à jour de la position du personnage
            if is_jumping:
                y_speed += gravity
                hit_box_fire.y += y_speed

                if hit_box_fire.y >= screen_height - 200:  # Si le personnage touche le sol
                    hit_box_fire.y = screen_height - 200
                    is_jumping = False

            screen.blit(fire_boy, hit_box_fire)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # press SPACE button to pause the game
                    game_paused = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    y_speed = -initial_jump_speed

            if event.type == pygame.QUIT:  # pygame.QUIT event means the user clicked X to close your window
                run = False
        pygame.display.update()

    pygame.quit()

    # water_girl = pygame.image.load('watergirl_pixel.jpg').convert_alpha()
    # water_girl = pygame.transform.scale(water_girl, (200, 100))
    #

    # screen.blit(water_girl, player_pos2)
    #

    # if pygame.Rect(player_pos,):  # handle collide of the player
    # player_pos.y -= 300 * dt
    # player_pos2.y -= 300 * dt

    # if pygame.sprite.spritecollideany(player1, all_sprites): # issue collide is always true!!
    # player_pos.y += 300 * dt


if __name__ == "__main__":
    # call the main function
    main()


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
