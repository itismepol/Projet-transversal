import pygame


class Player:
    def __init__(self, tiles_list, controls_keys, set_image, power):
        self.player_stand = pygame.transform.scale(pygame.image.load(set_image['stand']).convert_alpha(), (39.5, 55.2))
        self.player_jump = pygame.transform.scale(pygame.image.load(set_image['jump']).convert_alpha(), (39.5, 55.2))
        self.player_land = pygame.transform.scale(pygame.image.load(set_image['land']).convert_alpha(), (39.5, 55.2))

        # Load walking images
        player_right = [pygame.image.load(path).convert_alpha() for path in set_image['right']]
        self.player_right = [pygame.transform.scale(image, (39.5, 55.2)) for image in player_right]
        self.player_left = [pygame.transform.flip(image, True, False) for image in self.player_right]

        # Variable to remember which frame is displayed
        self.player_right_frame = 0
        self.player_left_frame = 0
        self.player_jump_frame = 0
        self.tiles_list = tiles_list
        self.direction = "stand"
        self.is_jumping = False
        self.jump_speed = 17
        self.gravity = 1.45
        self.y_speed = 0
        self.rect = self.player_stand.get_rect()
        self.y_ground = 760
        self.width = self.player_stand.get_width()
        self.height = self.player_stand.get_height()
        self.power = power
        self.jump_cooldown = 28
        self.controls_keys = controls_keys
        self.win = False
        self.door = False

    def update(self):
        self.keys_management()
        self.collision()
        self.animate()

    def collision(self):
        # check for collision
        for my_tile in self.tiles_list:
            if my_tile[1].colliderect(self.rect.x, self.rect.y, self.width, self.height):

                if my_tile[2] == 1:
                    # check for collision in x direction
                    if self.direction == "left":
                        self.rect.left = my_tile[1].right

                    if self.direction == "right":
                        self.rect.right = my_tile[1].left

                # check for collision in y direction
                if my_tile[2] in (3, 4, 5):
                    # check if the player is below the tile
                    if self.y_speed < 0:
                        self.rect.y = my_tile[1].bottom

                    # check if the player is above the tile
                    if self.y_speed >= 0:
                        self.rect.bottom = my_tile[1].top
                        self.is_jumping = False

                if my_tile[2] == 9 and self.power == 'W':
                    self.door = True
                    self.win = True

                if my_tile[2] == 10 and self.power == 'F':
                    self.door = True
                    self.win = True

    def keys_management(self):
        self.jump_cooldown += 1
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.controls_keys["left"]]:
            self.rect.x -= 5
            self.direction = "left"

        if keys_pressed[self.controls_keys["right"]]:
            self.rect.x += 5
            self.direction = "right"

        if keys_pressed[self.controls_keys["jump"]] and not self.is_jumping and self.jump_cooldown > 27:
            self.jump_cooldown = 0
            self.is_jumping = True
            self.y_speed = -self.jump_speed
            self.direction = "jump"

        if keys_pressed[self.controls_keys["down"]]:
            self.direction = "land"

        # Mise à jour de la position du personnage
        if self.is_jumping:
            self.y_speed += self.gravity
            self.rect.y += self.y_speed

            if self.rect.y >= self.y_ground:  # Si le personnage touche le sol
                self.rect.y = self.y_ground
                self.is_jumping = False

        # ajout de la gravité
        if self.y_speed > 10:
            self.y_speed = 10
        self.rect.y += self.y_speed

        if sum(keys_pressed) == 0:  # Le joueur ne bouge pas
            self.direction = "stand"

        if self.rect.y >= self.y_ground:  # Si le personnage touche le sol
            self.rect.y = self.y_ground

    def animate(self):
        screen = pygame.display.get_surface()
        # Draw the player
        if self.direction == "left":
            screen.blit(self.player_left[self.player_left_frame], (self.rect.x, self.rect.y))
            self.player_left_frame = (self.player_left_frame + 1) % len(self.player_left)
        elif self.direction == "right":
            screen.blit(self.player_right[self.player_right_frame], (self.rect.x, self.rect.y))
            self.player_right_frame = (self.player_right_frame + 1) % len(self.player_right)
        elif self.direction == "jump":
            screen.blit(self.player_jump, (self.rect.x, self.rect.y))
        elif self.direction == "land":
            screen.blit(self.player_land, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.player_stand, (self.rect.x, self.rect.y))
