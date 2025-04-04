import pygame
import Box
from Resource_path import resource_path

class Player:
    def __init__(self, tiles_list, controls_keys, set_image, power):
        self.player_stand = pygame.transform.scale(pygame.image.load(resource_path(set_image['stand'])).convert_alpha(), (39.5, 55.2))
        self.player_jump = pygame.transform.scale(pygame.image.load(resource_path(set_image['jump'])).convert_alpha(), (39.5, 55.2))
        self.player_land = pygame.transform.scale(pygame.image.load(resource_path(set_image['land'])).convert_alpha(), (39.5, 55.2))

        # Load walking images
        player_right = [pygame.image.load(resource_path(path)).convert_alpha() for path in set_image['right']]
        self.player_right = [pygame.transform.scale(image, (39.5, 55.2)) for image in player_right]
        self.player_left = [pygame.transform.flip(image, True, False) for image in self.player_right]

        self.tile_size = 50

        # Variable to remember which frame is displayed
        self.player_right_frame = 0
        self.player_left_frame = 0
        self.player_jump_frame = 0
        self.tiles_list = tiles_list
        self.direction = "stand"
        self.is_jumping = False
        self.jump_speed = 17
        self.gravity = 1.6
        self.y_speed = 0
        self.rect = self.player_stand.get_rect()
        self.y_ground = 760
        self.width = self.player_stand.get_width()
        self.height = self.player_stand.get_height()
        self.power = power
        self.jump_cooldown = 28
        self.controls_keys = controls_keys
        self.win = False
        self.door2 = False
        self.door1 = False
        box_x, box_y = 600, 200
        self.box = Box.Box(box_x, box_y, self.tile_size)

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
                    self.door1 = True
                    self.win = True

                elif my_tile[2] != 9 and not self.direction == "stand":
                    self.door1 = False

                if my_tile[2] == 10 and self.power == 'F':
                    self.door2 = True
                    self.win = True

                elif my_tile[2] != 10 and not self.direction == "stand":
                    self.door2 = False

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
            self.box.box_speed = -self.jump_speed
            self.direction = "jump"

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
        self.rect.y += self.y_speed + self.gravity

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

    def collide_box(self, the_box):
        for my_tile in self.tiles_list:
            if my_tile[1].colliderect(self.box.rect):
                if my_tile[2] == 1:
                    if self.direction == "left":
                        self.box.rect.left = my_tile[1].right

                    if self.direction == "right":
                        self.box.rect.right = my_tile[1].left

                if my_tile[2] in (3, 4, 5):
                    if self.box.box_speed < 0:
                        self.box.rect.top = my_tile[1].bottom

                    if self.box.box_speed >= 0:
                        self.box.rect.bottom = my_tile[1].top

        if the_box.box_speed > 10:
            the_box.box_speed = 10

        the_box.box_speed += 1
        the_box.rect.y += the_box.box_speed

        if the_box.rect.y >= self.y_ground:
            the_box.rect.y = self.y_ground

        if self.rect.colliderect(the_box):
            if self.direction == "left":
                the_box.rect.right = self.rect.left

            if self.direction == "right":
                the_box.rect.left = self.rect.right

            # if self.direction == 'right':
            #     the_box.x = self.rect.right + the_box.rect.width
            # if self.direction == 'left':
            #     the_box.x = self.rect.left - the_box.rect.width
            # if self.direction == 'stand' and self.y_speed <= 0:
            #     self.rect.bottom = the_box.rect.top

        if the_box.y >= self.y_ground:  # Si la box touche le sol
            the_box.y = self.y_ground
