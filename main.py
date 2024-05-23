import pygame
import button
import Player
import World
import Box
import time


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
    resume_img = pygame.image.load("resume_button.png").convert_alpha()
    quit_img = pygame.image.load("quit_button.png").convert_alpha()
    audio_img = pygame.image.load('audio_button.png').convert_alpha()
    back_img = pygame.image.load('back_button.png').convert_alpha()
    sound_img = pygame.image.load('sound_button.png').convert_alpha()
    plus_img = pygame.image.load('plus_button.png').convert_alpha()  # look for the imageS
    minus_img = pygame.image.load('minus_button.png').convert_alpha()
    pause_img = pygame.image.load('play_button.png').convert_alpha()
    play_img = pygame.image.load('pause_button.png').convert_alpha()
    retry_img = pygame.image.load('retry_button.png').convert_alpha()
    home_img = pygame.image.load('home_button.png').convert_alpha()
    credit_img = pygame.image.load('credit_button.png').convert_alpha()
    start_img = pygame.image.load('start_button.png').convert_alpha()
    levels_img = pygame.image.load('levels_button.png').convert_alpha()
    game_over_img = pygame.image.load('game_over.png').convert_alpha()
    first_lev_img = pygame.image.load('first_level_button.png').convert_alpha()
    second_lev_img = pygame.image.load('second_level_button.png').convert_alpha()
    third_lev_img = pygame.image.load('third_level_button.png').convert_alpha()

    # create instance of the button
    resume_button = button.Button(screen_width//2, 130, resume_img, 0.545)
    quit_button = button.Button(screen_width//2, screen_height//2+210, quit_img, 0.575)
    audio_button = button.Button(screen_width//2, 250, audio_img, 0.545)
    back_button = button.Button(screen_width//2, 450, back_img, 0.585)
    sound_button = button.Button(screen_width//2, 200, sound_img, 0.585)
    plus_button = button.Button(sound_button.get_coordinate()[0] - plus_img.get_width()-50,
                                sound_button.get_coordinate()[1], plus_img, 1.5)
    minus_button = button.Button(sound_button.get_coordinate()[0]+sound_button.get_dimension()[0]+50,
                                 sound_button.get_coordinate()[1], minus_img, 0.585)
    pause_button = button.Button(sound_button.get_coordinate()[0]+50,
                                 sound_button.get_coordinate()[1]+sound_img.get_height()+50, pause_img, 0.585)
    play_button = button.Button(sound_button.get_coordinate()[0]-50,
                                sound_button.get_coordinate()[1]+sound_img.get_height()+50, play_img, 0.585)
    retry_button = button.Button(screen_width//2, 375, retry_img, 0.585)
    retry_button2 = button.Button(screen_width//2, screen_height//2+100, retry_img, 0.585)
    home_button = button.Button(screen_width//2, 200, home_img, 0.400)
    home_button2 = button.Button(screen_width // 2, screen_height//2+200, home_img, 0.400)
    credit_button = button.Button(screen_width//2, screen_height//2-70, credit_img, 0.545)
    start_button = button.Button(screen_width//2, screen_height//2-210, start_img, 0.585)
    # levels button
    levels_button = button.Button(screen_width//2, screen_height//2+70, levels_img, 0.254)
    first_level_button = button.Button(screen_width//2, screen_height//2 + 220, first_lev_img, 0.1)
    second_level_button = button.Button(screen_width//2, screen_height//2-220, second_lev_img,0.1)
    third_level_button = button.Button(screen_width//2, screen_height//2, third_lev_img, 0.1)

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
        [1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 3,1],
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
        [1, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 8, 8, 1, 8, 8, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 0, 0, 3, 3, 1, 3, 3, 0, 0, 0, 3, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 6, 6, 6, 6, 6, 0, 0, 0, 9, 1, 10, 0, 0, 0, 7, 7, 7, 7, 7, 1],
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
            the_world = world1
        elif level == "2":
            the_world = world2
        else:
            the_world = world3
        return the_world

    def reset_game(p1, p2, w):
        p1.rect.x, p1.rect.y = start_pos_p1_x, start_pos_y
        p2.rect.right, p2.rect.y = start_pos_p2_x, start_pos_y
        p1.is_jumping, p2.is_jumping = False, False
        p1.win, p2.win = False, False
        p1.door1, p2.door1 = False, False
        p1.door2, p2.door2 = False, False
        w.door_open1 = False
        w.door_open2 = False

    world1 = World.World(data_level_one, tile_size)
    world2 = World.World(data_level_two, tile_size)
    world3 = World.World(data_level_three, tile_size)

    world = change_level("1")

    player1 = Player.Player(world.tiles_list, player1_controls, player1_images, 'W')
    player2 = Player.Player(world.tiles_list, player2_controls, player2_images, 'F')
    start_pos_p1_x = 325
    start_pos_p2_x = 1225
    start_pos_y = 760
    back_ground = pygame.image.load('castle-transformedx4.jpeg').convert()
    back_ground = pygame.transform.scale(back_ground, (playground_width, playground_height))
    box_x, box_y = 350, 150
    box = Box.Box(box_x, box_y, 50)
    win_condition_met_time = None

    # game loop
    while run:
        clock.tick(60)

        if menu_state == "start_menu":
            screen.fill(blue)
            draw_text("THE ELEMENTARY ADVENTURE STARTS NOW!", title_font, white, screen_width // 2, 70)
            pygame.draw.rect(screen, black, (0, screen_height // 2, screen_width, screen_height // 2))

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

        if menu_state == "levels":
            screen.fill(blue)
            pygame.draw.rect(screen, black, (0, screen_height // 2, screen_width, screen_height // 2))
            reset_game(player1, player2, world)
            if first_level_button.draw(screen):
                world = change_level("1")
                menu_state = "game"
            if second_level_button.draw(screen):
                world = change_level("2")
                menu_state = "game"
            if third_level_button.draw(screen):
                world = change_level("3")
                menu_state = "game"

        if menu_state == "game":
            screen.fill(blue)
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

            # draw_grid()

            world1.update_world()
            player1.update()
            player2.update()

            box.draw_rect()

            player1.collide_box(box)
            player2.collide_box(box)

            # pygame.draw.rect(screen, white,(player2.rect.x, player2.rect.y, player2.rect.width,player2.rect.height),2)
            #  can help with rect of the player

            if player1.win and player2.win:
                if win_condition_met_time is None:
                    win_condition_met_time = time.time()

            current_time = time.time()

            if win_condition_met_time and (current_time - win_condition_met_time) >= 1:
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
            # check for collision with poison
            menu_state = "game_over"

        if menu_state == "game_over":
            reset_game(player1, player2, world)
            screen.fill(blue)
            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)

            screen.blit(game_over_img, (playground_width//2+121, playground_height/4))

            if retry_button2.draw(screen):
                menu_state = "game"

            if home_button2.draw(screen):
                menu_state = "start_menu"

        if menu_state == "win":
            reset_game(player1, player2, world)
            screen.fill(blue)

            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
            draw_text("SUCCEED !", main_font, white, (playground_width+250)//2, (playground_height+65)//2)
            if retry_button2.draw(screen):
                menu_state = "game"

            if home_button.draw(screen):
                menu_state = "start_menu"

        # check if game is paused
        if game_paused:
            screen.fill(blue)
            pygame.draw.rect(screen, white, (250, 65, playground_width, playground_height), 10)
            # check if is the menu
            # draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if audio_button.draw(screen):
                menu_state = "audio"
            if retry_button.draw(screen):
                reset_game(player1, player2, world)
                menu_state = "game"
                game_paused = False

            if levels_button.draw(screen):
                menu_state = "levels"
                game_paused = False

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

