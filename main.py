import pygame
import button
import Player
import World


def main():
    # hit_box_player = fire_boy.get_rect()
    # hit_box_player.bottomleft = (200, screen_height - 200)
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
    # screen.blit(fire_boy, hit_box_fire)
    # water_girl = pygame.image.load('watergirl_pixel.jpg').convert_alpha()
    # water_girl = pygame.transform.scale(water_girl, (200, 100))
    # screen.blit(water_girl, player_pos2)

    # square hit box of the character
    # fire_boy = pygame.image.load('fire_boy.png').convert_alpha()
    # fire_boy = pygame.transform.scale(fire_boy, (50, 80))
    # hit_box_fire = fire_boy.get_rect()
    # hit_box_fire.bottomleft = (200, screen.get_height() - 200)

    screen_height = screen.get_height()
    screen_width = screen.get_width()

    # game variables
    game_paused = False
    menu_state = "main"
    tile_size = 50
    cols = 21
    rows = 16

    playground_width = tile_size * cols
    playground_height = tile_size * rows
    print("The width is ", playground_width, "and the height is ", playground_height)

    # define colours
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (52, 78, 91)

    # define fonts
    main_font = pygame.font.SysFont("arial black", 40)

    # reset the background
    screen.fill(black)

    # load music
    # pygame.mixer.music.load("lofi_background.mp3")
    # pygame.mixer.music.play(-1)

    # load button images
    resume_img = pygame.image.load("button_resume.png").convert_alpha()
    quit_img = pygame.image.load("button_quit.png").convert_alpha()
    audio_img = pygame.image.load('button_audio.png').convert_alpha()
    back_img = pygame.image.load('button_back.png').convert_alpha()
    sound_img = pygame.image.load('button_sound.png').convert_alpha()
    plus_img = pygame.image.load('Plus_sound.png').convert_alpha()
    minus_img = pygame.image.load('Minus_sound.png').convert_alpha()
    pause_img = pygame.image.load('Play.png').convert_alpha()
    play_img = pygame.image.load('Pause_button.png').convert_alpha()
    retry_img = pygame.image.load('button_retry.png').convert_alpha()

    # create instance of the button
    resume_button = button.Button(590, 130, resume_img, 1.2)
    quit_button = button.Button(625, 497, quit_img, 1.2)
    audio_button = button.Button(500, 250, audio_img, 1.2)
    back_button = button.Button(600, 450, back_img, 1.2)
    sound_button = button.Button(555, 200, sound_img, 1.2)
    plus_button = button.Button(sound_button.get_coordinate()[0] - plus_img.get_width()-50,
                                sound_button.get_coordinate()[1], plus_img, 1.5)
    minus_button = button.Button(sound_button.get_coordinate()[0]+sound_button.get_dimension()[0]+50,
                                 sound_button.get_coordinate()[1], minus_img, 1.5)
    pause_button = button.Button(sound_button.get_coordinate()[0]+50,
                                 sound_button.get_coordinate()[1]+sound_img.get_height()+50, pause_img, 1.5)
    play_button = button.Button(sound_button.get_coordinate()[0]-50,
                                sound_button.get_coordinate()[1]+sound_img.get_height()+50, play_img, 1.5)
    retry_button = button.Button(590, 375, retry_img, 1.2)

    playground = [
        pygame.Rect(250, 810, 1000, 10),  # bottom horizontal -
        pygame.Rect(250, 65, 1000, 10),  # top horizontal -
        pygame.Rect(250, 65, 10, 750),  # left vertical |
        pygame.Rect(1240, 65, 10, 750)  # right vertical |
    ]

    def draw_text(text, font, text_colo, x_cor, y_cor):
        img = font.render(text, True, text_colo)
        screen.blit(img, (x_cor, y_cor))

    # create empty tile list
    world_data = []
    for row in range(rows):
        r = [0] * cols
        world_data.append(r)

    # create boundary for the map
    for tile in range(0, 16):
        world_data[tile][0] = 1
        world_data[tile][20] = 1

    for end in range(0, 21):
        world_data[0][end] = 1
        world_data[15][end] = 2

    world_data[13][19] = 3
    world_data[13][18] = 3
    world_data[13][19] = 3
    world_data[13][18] = 3
    world_data[13][1] = 3
    world_data[13][2] = 3

    def draw_grid():
        for horizontal in range(16):
            # horizontal lines
            pygame.draw.line(screen, white, (250, horizontal * tile_size + 65),
                             (1250, horizontal * tile_size + 65))
        for vertical in range(21):
            # vertical lines
            pygame.draw.line(screen, black, (250+vertical*tile_size, 65),
                             (250+vertical*tile_size, 815))

    for row in range(rows):
        for col in range(cols):
            print(world_data[row][col], end=' ')
        print()

    run = True

    world = World.World(world_data, tile_size)
    player = Player.Player(world.tiles_list)
    player.rect.x = 300
    player.rect.y = 760
    player.y_ground = 760
    back_ground = pygame.image.load('castle-transformedx4.jpeg').convert()
    back_ground = pygame.transform.scale(back_ground, (playground_width, playground_height))

    # game loop
    while run:
        # print(player.rect.y)
        # print(player.rect.bottom)
        screen.fill(blue)
        screen.blit(back_ground, (250, 65))
        world.draw()
        draw_text("Press P to pause", main_font, white, 600, 10)
        # for line in playground:
        #     pygame.draw.rect(screen, white, line)
        
        # draw_grid()

        player.update()
        pygame.draw.rect(screen, white, (player.rect.x, player.rect.y, player.rect.width, player.rect.height), 2)
        #  can help with rect of the player

        clock.tick(60)

        # check if game is paused
        if game_paused:
            screen.fill(blue)
            for platform in playground:
                pygame.draw.rect(screen, white, platform)
            # check if is the menu
            if menu_state == "main":
                # draw pause screen buttons
                if resume_button.draw(screen):
                    game_paused = False
                if audio_button.draw(screen):
                    menu_state = "audio"
                if retry_button.draw(screen):
                    print("Retry Game !")

                if quit_button.draw(screen):
                    run = False

            # check if the audio menu is open
            if menu_state == "audio":
                current_volume = pygame.mixer.music.get_volume()
                if plus_button.draw(screen):
                    pygame.mixer.music.set_volume(current_volume+0.2)
                    if current_volume > 0.2:
                        pygame.mixer.music.unpause()
                if minus_button.draw(screen):
                    if current_volume <= 0.2:
                        print("Volume at minimum")
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.set_volume(current_volume-0.2)
                if pause_button.draw(screen):
                    pygame.mixer.music.unpause()
                if play_button.draw(screen):
                    pygame.mixer.music.pause()
                if sound_button.draw(screen):
                    print("sound audio")
                if back_button.draw(screen):
                    menu_state = "main"

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # press SPACE button to pause the game
                    game_paused = True

            if event.type == pygame.QUIT:  # pygame.QUIT event means the user clicked X to close your window
                pygame.mixer.music.unload()
                run = False

        pygame.display.update()
        

if __name__ == "__main__":
    '''Pygame set up and call the main function '''

    pygame.init()  # Start graphics system
    pygame.mixer.init()  # Start audio system
    screen = pygame.display.set_mode((1500, 875))
    clock = pygame.time.Clock()  # Create game clock

    logo = pygame.image.load('fire_water.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("THE ADVENTURE")
    main()
    pygame.quit()

