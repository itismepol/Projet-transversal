import pygame
import button
import Player
import World
import time


def main():

    screen_height = screen.get_height()
    screen_width = screen.get_width()

    # game variables
    game_paused = False
    audio = False
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
    back_grey = (45, 45, 45)

    # define fonts
    main_font = pygame.font.SysFont("arial black", 40)
    title_font = pygame.font.SysFont("arial black", 50)  # Roboto ,Open Sans, Lobster, Press Start 2P, Bebas Neue

    # reset the background
    screen.fill(back_grey)

    # load music
    pygame.mixer.music.load("lofi_background.mp3")
    pygame.mixer.music.play(-1)

    # load button images
    resume_img = pygame.image.load("buttons/resume_button.png").convert_alpha()
    quit_img = pygame.image.load("buttons/quit_button.png").convert_alpha()
    audio_img = pygame.image.load('buttons/audio_button.png').convert_alpha()
    back_img = pygame.image.load('buttons/back_button.png').convert_alpha()
    plus_img = pygame.image.load('buttons/plus_button.png').convert_alpha()
    minus_img = pygame.image.load('buttons/minus_button.png').convert_alpha()
    pause_img = pygame.image.load('buttons/play_button.png').convert_alpha()
    play_img = pygame.image.load('buttons/pause_button.png').convert_alpha()
    retry_img = pygame.image.load('buttons/retry_button.png').convert_alpha()
    home_img = pygame.image.load('buttons/home_button.png').convert_alpha()
    credit_img = pygame.image.load('buttons/credit_button.png').convert_alpha()
    start_img = pygame.image.load('buttons/start_button.png').convert_alpha()
    levels_img = pygame.image.load('buttons/levels_button.png').convert_alpha()
    first_lev_img = pygame.image.load('buttons/one_button.png').convert_alpha()
    second_lev_img = pygame.image.load('buttons/two_button.png').convert_alpha()
    third_lev_img = pygame.image.load('buttons/three_button.png').convert_alpha()

    # Game over image
    game_over_img = pygame.image.load('tiles/game_over.png').convert_alpha()
    game_over_img = pygame.transform.scale(game_over_img, (playground_width/2.5, playground_height/2.5))
    win_img = pygame.image.load('tiles/win.png').convert_alpha()
    win_img = pygame.transform.scale(win_img, (playground_width / 2.5, playground_height / 2.5))

    # backgrounds images
    start_background = pygame.image.load('backgrounds/back_ground2.png')
    start_background = pygame.transform.scale(start_background, (screen_width, screen_height))
    back_ground = pygame.image.load('backgrounds/castle-transformedx4.jpeg').convert()
    back_ground = pygame.transform.scale(back_ground, (playground_width, playground_height))

    # create instance of the button
    # start menu
    start_button = button.Button(screen_width // 2, screen_height // 2 - 210, start_img, 0.585)
    credit_button = button.Button(screen_width // 2, screen_height // 2 - 70, credit_img, 0.545)
    levels_button = button.Button(screen_width // 2, screen_height // 2 + 70, levels_img, 0.925)
    quit_button = button.Button(screen_width // 2, screen_height // 2 + 210, quit_img, 0.575)

    # pause menu
    resume_button = button.Button(screen_width//2, screen_height//2-175, resume_img, 0.545)
    retry_button = button.Button(screen_width // 2, screen_height // 2-50, retry_img, 0.585)
    audio_button = button.Button(screen_width//2,  screen_height // 2+75, audio_img, 0.545)
    levels_button2 = button.Button(screen_width // 2, screen_height // 2 + 200, levels_img, 0.925)
    home_button_pause = button.Button(screen_width // 2, screen_height // 2 + 325, home_img, 0.925)

    # audio menu
    plus_button = button.Button(screen_width // 2-150, screen_height // 2, plus_img, 0.925)
    minus_button = button.Button(screen_width // 2+150, screen_height // 2, minus_img, 0.925)
    pause_button = button.Button(screen_width // 2-100, screen_height // 2+100, pause_img, 1.1)
    play_button = button.Button(screen_width // 2+100, screen_height // 2+100, play_img, 0.925)
    back_button = button.Button(screen_width//2, screen_height // 2+200, back_img, 0.585)

    # Lost and Win
    retry_button2 = button.Button(screen_width//2, screen_height//2+100, retry_img, 0.585)
    home_button = button.Button(screen_width // 2, screen_height//2+250, home_img, 0.925)

    # levels button

    first_level_button = button.Button(screen_width//2-175, screen_height//2, first_lev_img, 1.5)
    second_level_button = button.Button(screen_width//2, screen_height//2, second_lev_img, 1.5)
    third_level_button = button.Button(screen_width//2+175, screen_height//2, third_lev_img, 1.5)
    back_button2 = button.Button(screen_width // 2, screen_height // 2 + 150, back_img, 0.585)

    def draw_text(text, font, text_colo, x_cor, y_cor):
        text_print = font.render(text, True, text_colo)
        text_rect = text_print.get_rect(center=(x_cor, y_cor))
        screen.blit(text_print, text_rect)

    def draw_grid():
        for horizontal in range(16):
            # horizontal lines
            pygame.draw.line(screen, white, (250, horizontal * tile_size + 65),
                             (1250, horizontal * tile_size + 65))
        for vertical in range(21):
            # vertical lines
            pygame.draw.line(screen, black, (250+vertical*tile_size, 65),
                             (250+vertical*tile_size, 815))

    # création des cartes (tiles list)
    data_level_one = [
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
    data_level_two = [
        [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 9, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 3, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 3, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 3, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 1, 0, 0, 3, 3, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 8, 8, 8, 8, 8, 1, 7, 0, 0, 0, 6, 1],
        [1, 0, 0, 3, 1, 3, 0, 0, 0, 3, 3, 3, 3, 3, 1, 3, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    ]
    data_level_three = [
        [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1],
        [1, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1],
        [1, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
        [1, 7, 7, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 6, 6, 1],
        [1, 3, 3, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 3, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 8, 8, 1, 8, 8, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 0, 0, 3, 3, 1, 3, 3, 0, 0, 0, 3, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 7, 7, 7, 7, 7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 6, 6, 6, 6, 6, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    ]
    for row in range(rows):
        for col in range(cols):
            print(data_level_one[row][col], end=' ')
        print()

    run = True

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

    def change_level(level):
        if level == "1":
            the_world = World.World(data_level_one, tile_size)
        elif level == "2":
            the_world = World.World(data_level_two, tile_size)
        elif level == "3":
            the_world = World.World(data_level_three, tile_size)

        else:
            raise ValueError(f"Level {level} is not a valid level")
        p1 = Player.Player(the_world.tiles_list, player1_controls, player1_images, 'W')
        p2 = Player.Player(the_world.tiles_list, player2_controls, player2_images, 'F')
        return the_world, p1, p2

    def reset_game(p1, p2, w):
        p1.rect.x, p1.rect.y = start_pos_p1_x, start_pos_y
        p2.rect.right, p2.rect.y = start_pos_p2_x, start_pos_y
        p1.is_jumping, p2.is_jumping = False, False
        p1.win, p2.win = False, False
        p1.door1, p2.door1 = False, False
        p1.door2, p2.door2 = False, False
        w.door_open1 = False
        w.door_open2 = False

    world = change_level("1")[0]

    player1 = change_level("1")[1]
    player2 = change_level("1")[2]

    start_pos_p1_x = 325
    start_pos_p2_x = 1225
    start_pos_y = 760

    win_condition_met_time = None

    # game loop
    while run:
        clock.tick(60)
        button_clicked = False

        if menu_state == "start_menu":
            screen.blit(start_background, (0, 0))
            draw_text("THE ELEMENTARY ADVENTURE STARTS NOW!", title_font, white, screen_width // 2, 70)

            if credit_button.draw(screen):
                menu_state = "credit"
            if start_button.draw(screen):
                player1.rect.x, player1.rect.y = start_pos_p1_x, start_pos_y
                player2.rect.right, player2.rect.y = start_pos_p2_x, start_pos_y
                menu_state = "game"
            if levels_button.draw(screen):
                menu_state = "levels"
            if quit_button.draw(screen):
                run = False

        if menu_state == "game":

            screen.fill(back_grey)
            screen.blit(back_ground, (250, 65))

            world.draw()

            if player1.door1:
                world.door_open1 = True
            else:
                world.door_open1 = False

            if player2.door2:
                world.door_open2 = True
            else:
                world.door_open2 = False

            draw_text("PRESS P TO PAUSE", main_font, white, playground_width-250, 30)

            world.update_world()
            player1.update()
            player2.update()

            # pygame.draw.rect(screen, white,(player2.rect.x, player2.rect.y, player2.rect.width,player2.rect.height),2)
            #  can help with rect of the player

            if player1.win and player2.win:
                if win_condition_met_time is None:
                    win_condition_met_time = time.time()

            current_time = time.time()

            if win_condition_met_time and (current_time - win_condition_met_time) >= 0.7:
                menu_state = "win"

        if not (player1.win and player2.win):
            win_condition_met_time = None
            if player1.win and player2.win:
                menu_state = "win"

        if (pygame.sprite.spritecollide(player1, world.lava_group, False) and player1.power == "W"
                or pygame.sprite.spritecollide(player2, world.water_group, False) and player2.power == "F"):
            # check for collision with lava or water
            menu_state = "game_over"

        if (pygame.sprite.spritecollide(player2, world.poison_group, False)
                or pygame.sprite.spritecollide(player1, world.poison_group, False)):
            menu_state = "game_over"

        if menu_state == "levels":
            screen.fill(back_grey)
            pygame.draw.rect(screen, black, (0, screen_height // 2, screen_width, screen_height // 2))
            draw_text("CHOOSE YOUR LEVEL", title_font, white, screen_width // 2, screen_height // 2 - 100)
            reset_game(player1, player2, world)
            print(f"Current menu_state: {menu_state}")

            if first_level_button.draw(screen) and not button_clicked:
                print("first boutton clicked")
                world = change_level("1")[0]
                player1 = change_level("1")[1]
                player2 = change_level("1")[2]
                reset_game(player1, player2, world)
                button_clicked = True
                menu_state = "game"

                print(f"Changed menu_state to: {menu_state}")

            elif second_level_button.draw(screen) and not button_clicked:
                print("second boutton clicked")
                world = change_level("2")[0]
                player1 = change_level("2")[1]
                player2 = change_level("2")[2]
                reset_game(player1, player2, world)
                button_clicked = True
                menu_state = "game"

                print(f"Changed menu_state to: {menu_state}")
            elif third_level_button.draw(screen) and not button_clicked:
                print("third boutton clicked")
                world = change_level("3")[0]
                player1 = change_level("3")[1]
                player2 = change_level("3")[2]
                reset_game(player1, player2, world)
                button_clicked = True
                menu_state = "game"

                print(f"Changed menu_state to: {menu_state}")

            elif not button_clicked and back_button2.draw(screen):
                menu_state = "start_menu"
                button_clicked = True

                print(f"Changed menu_state to: {menu_state}")

            print(f"Final menu_state after checks: {menu_state}")

        if menu_state == "game_over":
            reset_game(player1, player2, world)
            screen.fill(back_grey)
            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
            screen.blit(game_over_img, (playground_width//2, playground_height//5-50))

            if retry_button2.draw(screen):
                reset_game(player1, player2, world)
                menu_state = "game"

            if home_button.draw(screen):
                reset_game(player1, player2, world)
                menu_state = "start_menu"

        if menu_state == "win":
            reset_game(player1, player2, world)
            screen.fill(back_grey)

            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
            screen.blit(win_img, (playground_width//2, playground_height//5-50))

            if retry_button2.draw(screen):
                menu_state = "game"

            if home_button.draw(screen):
                menu_state = "start_menu"

        # check if game is paused
        if game_paused:
            screen.fill(back_grey)
            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)

            draw_text("GAME PAUSED", title_font, white, screen_width // 2, screen_height // 2 - 300)
            # check if the audio menu is open
            if audio:
                screen.fill(back_grey)
                pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
                draw_text("AUDIO MENU", title_font, white, screen_width // 2, screen_height // 2 - 150)
                draw_text("Music", title_font, white, screen_width // 2, screen_height // 2)
                current_volume = pygame.mixer.music.get_volume()
                if plus_button.draw(screen):
                    pygame.mixer.music.set_volume(current_volume + 0.2)
                    if current_volume > 0.2:
                        pygame.mixer.music.unpause()
                if minus_button.draw(screen):
                    if current_volume <= 0.2:
                        print("Volume at minimum")
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.set_volume(current_volume - 0.2)

                if pause_button.draw(screen):
                    pygame.mixer.music.unpause()
                if play_button.draw(screen):
                    pygame.mixer.music.pause()
                if back_button.draw(screen):
                    audio = False

            # draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if audio_button.draw(screen):
                audio = True

            if home_button_pause.draw(screen):
                reset_game(player1, player2, world)
                game_paused = False
                menu_state = "start_menu"

            if levels_button2.draw(screen):
                game_paused = False
                menu_state = "levels"

            if retry_button.draw(screen):
                reset_game(player1, player2, world)
                game_paused = False
                menu_state = "game"

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

    logo = pygame.image.load('backgrounds/fire_water.jpg')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("THE ELEMENTARY ADVENTURE")
    main()
    pygame.quit()

