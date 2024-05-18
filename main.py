import pygame
import button
import Player
import World


def main():

    screen_height = screen.get_height()
    screen_width = screen.get_width()

    # game variables
    game_paused = False
    menu_state = "start_menu"
    tile_size = 50
    cols = 21
    rows = 16

    playground_width = tile_size * cols
    playground_height = tile_size * rows

    # define colours
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (52, 78, 91)

    # define fonts
    main_font = pygame.font.SysFont("arial black", 40)
    title_font = pygame.font.SysFont("arial black", 50)  # Roboto ,Open Sans, Lobster, Press Start 2P, Bebas Neue

    # reset the background
    screen.fill(black)

    # load music
    pygame.mixer.music.load("lofi_background.mp3")
    pygame.mixer.music.play(-1)

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
    home_img = pygame.image.load('button_home.png').convert_alpha()
    # credit_img = pygame.image.load('button_credit.png').convert_alpha()

    # create instance of the button
    resume_button = button.Button(590, 130, resume_img, 1.2)
    quit_button = button.Button(screen_width//2, screen_height//2+70, quit_img, 1.2)
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
    retry_button2 = button.Button(590, 575, retry_img, 1.2)
    home_button = button.Button(590, 200, home_img, 1.2)

    def draw_text(text, font, text_colo, x_cor, y_cor):
        text_print = font.render(text, True, text_colo)
        text_rect = text_print.get_rect(center=(x_cor, y_cor))
        screen.blit(text_print, text_rect)

    def draw_text2(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)
        return text_rect

    def draw_grid():
        for horizontal in range(16):
            # horizontal lines
            pygame.draw.line(screen, white, (250, horizontal * tile_size + 65),
                             (1250, horizontal * tile_size + 65))
        for vertical in range(21):
            # vertical lines
            pygame.draw.line(screen, black, (250+vertical*tile_size, 65),
                             (250+vertical*tile_size, 815))

    # création de la carte (tile list)
    world_data = [
        [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 0, 1, 0, 0, 0, 5, 5, 5, 0, 0, 0, 1, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 1, 0, 0, 0, 10, 0, 9, 0, 0, 0, 1, 3, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 1, 0, 3, 3, 0, 0, 0, 3, 3, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 6, 6, 6, 6, 8, 7, 7, 7, 7, 1, 0, 0, 0, 0, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    ]

    for row in range(rows):
        for col in range(cols):
            print(world_data[row][col], end=' ')
        print()

    run = True
    start_game_rect = None

    player1_controls = {'left': pygame.K_q, 'right': pygame.K_d, 'jump': pygame.K_z, 'down': pygame.K_s}
    player2_controls = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP,
                        'down': pygame.K_DOWN}
    player2_images = {
        'stand': "walk_P1/p3_stand.png",
        'jump': "walk_P1/p3_jump.png",
        'land': "walk_P1/p3_duck.png",
        'right': [
            "walk_P1/p3_walk01.png",
            "walk_P1/p3_walk02.png",
            "walk_P1/p3_walk03.png",
            "walk_P1/p3_walk04.png",
            "walk_P1/p3_walk05.png",
            "walk_P1/p3_walk06.png",
            "walk_P1/p3_walk07.png",
            "walk_P1/p3_walk08.png",
            "walk_P1/p3_walk09.png",
            "walk_P1/p3_walk10.png",
            "walk_P1/p3_walk11.png",
        ]
    }

    player1_images = {
        'stand': "walk_P2/p2_stand.png",
        'jump': "walk_P2/p2_jump.png",
        'land': "walk_P2/p2_duck.png",
        'right': [
            "walk_P2/p2_walk01.png",
            "walk_P2/p2_walk02.png",
            "walk_P2/p2_walk03.png",
            "walk_P2/p2_walk04.png",
            "walk_P2/p2_walk05.png",
            "walk_P2/p2_walk06.png",
            "walk_P2/p2_walk07.png",
            "walk_P2/p2_walk08.png",
            "walk_P2/p2_walk09.png",
            "walk_P2/p2_walk10.png",
            "walk_P2/p2_walk11.png",
        ]
    }

    world = World.World(world_data, tile_size)
    player1 = Player.Player(world.tiles_list, player1_controls, player1_images, 'W')
    player2 = Player.Player(world.tiles_list, player2_controls, player2_images, 'F')
    start_pos_p1_x = 325
    start_pos_p2_x = 1225
    start_pos_y = 760
    back_ground = pygame.image.load('castle-transformedx4.jpeg').convert()
    back_ground = pygame.transform.scale(back_ground, (playground_width, playground_height))

    # game loop
    while run:
        clock.tick(60)

        if menu_state == "start_menu":
            screen.fill(blue)
            draw_text("THE ELEMENTARY ADVENTURE STARTS NOW!", title_font, white, screen_width // 2, 70)
            pygame.draw.rect(screen, black, (0, screen_height // 2, screen_width, screen_height // 2))

            start_game_rect = draw_text2('START GAME', main_font, white, screen, screen_width // 2,
                                         screen_height // 2-70)
            if quit_button.draw(screen):
                run = False

        if menu_state == "game":
            screen.fill(blue)
            screen.blit(back_ground, (250, 65))
            world.draw()
            draw_text("PRESS P TO PAUSE", main_font, white, 600, 10)

            # draw_grid()

            player1.update()
            player2.update()
            # pygame.draw.rect(screen, white, (player.rect.x, player.rect.y, player.rect.width, player.rect.height), 2)
            #  can help with rect of the player
        if player1.door:
            pass

        if player1.win and player2.win:
            menu_state = "win"

        if (pygame.sprite.spritecollide(player1, world.lava_group, False) and player1.power == "W"
                or pygame.sprite.spritecollide(player2, world.water_group, False) and player2.power == "F"):
            # check for collision with lava or water
            menu_state = "game_over"

        if (pygame.sprite.spritecollide(player2, world.poison_group, False)
                or pygame.sprite.spritecollide(player1, world.poison_group, False)):
            # check for collision with poison
            menu_state = "game_over"

        if menu_state == "game_over":
            screen.fill(blue)

            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
            draw_text("GAME OVER", main_font, white, (playground_width+250)//2, (playground_height+65)//2)
            if retry_button2.draw(screen):
                player1.rect.x, player1.rect.y = start_pos_p1_x, start_pos_y
                player2.rect.right, player2.rect.y = start_pos_p2_x, start_pos_y
                menu_state = "game"

            if home_button.draw(screen):
                player1.rect.x, player1.rect.y = start_pos_p1_x, start_pos_y
                player2.rect.right, player2.rect.y = start_pos_p2_x, start_pos_y
                menu_state = "start_menu"

        if menu_state == "win":
            screen.fill(blue)
            player1.win = False
            player2.win = False

            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
            draw_text("SUCCEED !", main_font, white, (playground_width+250)//2, (playground_height+65)//2)
            if retry_button2.draw(screen):
                player1.rect.x, player1.rect.y = start_pos_p1_x, start_pos_y
                player2.rect.right, player2.rect.y = start_pos_p2_x, start_pos_y
                menu_state = "game"

            if home_button.draw(screen):
                menu_state = "start_menu"

        # check if game is paused
        if game_paused:
            screen.fill(blue)
            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
            # check if is the menu
            if menu_state == "game":
                # draw pause screen buttons
                if resume_button.draw(screen):
                    game_paused = False
                if audio_button.draw(screen):
                    menu_state = "audio"
                if retry_button.draw(screen):
                    game_paused = False
                    player1.rect.x, player1.rect.y = start_pos_p1_x, start_pos_y
                    player2.rect.right, player2.rect.y = start_pos_p2_x, start_pos_y
                    menu_state = "game"

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
                    menu_state = "game"

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # press SPACE button to pause the game
                    game_paused = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_rect.collidepoint(event.pos):
                    player1.rect.x, player1.rect.y = start_pos_p1_x, start_pos_y
                    player2.rect.right, player2.rect.y = start_pos_p2_x, start_pos_y
                    menu_state = "game"

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
    pygame.display.set_caption("THE ELEMENTARY ADVENTURE")
    main()
    pygame.quit()

