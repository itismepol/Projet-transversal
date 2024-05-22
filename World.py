import pygame
import Lava_Water


class World:
    def __init__(self, data, tile_size):
        self.tiles_list = []
        self.data = data
        self.tile_size = tile_size
        self.screen = pygame.display.get_surface()
        self.door_open1 = False
        self.door_open2 = False

        # load images
        stone = pygame.image.load('green_ground.png')
        half_stone_img = pygame.image.load('half_stone.png')
        stone2 = pygame.image.load('green_stone.png')
        blue_door_close = pygame.image.load('blue_door_close.png')
        red_door_close = pygame.image.load('red_door_close.png')
        blue_door_open = pygame.image.load('blue_door.png')
        red_door_open = pygame.image.load('red_door.png')

        self.image1 = pygame.transform.scale(stone2, (self.tile_size, self.tile_size))
        self.image2 = pygame.transform.scale(stone, (self.tile_size, self.tile_size))
        self.image3 = pygame.transform.scale(half_stone_img, (self.tile_size, self.tile_size / 2))
        self.image9 = pygame.transform.scale(blue_door_close, (self.tile_size, self.tile_size*(3/2)))
        self.image10 = pygame.transform.scale(red_door_close, (self.tile_size, self.tile_size * (3/2)))
        self.image11 = pygame.transform.scale(blue_door_open, (self.tile_size, self.tile_size * (3 / 2)))
        self.image12 = pygame.transform.scale(red_door_open, (self.tile_size, self.tile_size * (3 / 2)))

        self.lava_group = pygame.sprite.Group()
        self.water_group = pygame.sprite.Group()
        self.poison_group = pygame.sprite.Group()

        row_count = 0

        for list_row in self.data:
            col_count = 0
            for tiles in list_row:

                # Mur au extrémité
                if tiles == 1:
                    # rect2 = image2.get_rect()
                    # image = pygame.transform.scale(dirt_img, (self.tile_size, self.tile_size))
                    rect2 = self.image1.get_rect()
                    rect2.x = 250 + col_count * self.tile_size
                    rect2.y = 65 + row_count * self.tile_size

                    the_tiles = (self.image1, rect2, tiles)
                    self.tiles_list.append(the_tiles)

                # Sol
                if tiles == 2:
                    rect = self.image2.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 65 + row_count * self.tile_size
                    the_tiles = (self.image2, rect, tiles)
                    self.tiles_list.append(the_tiles)

                # Plateforme haut
                if tiles == 3:
                    rect = self.image3.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 65 + row_count * self.tile_size
                    the_tiles = (self.image3, rect, tiles)
                    self.tiles_list.append(the_tiles)

                # Plateforme bas
                if tiles == 5:
                    rect = self.image3.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 90 + row_count * self.tile_size
                    the_tiles = (self.image3, rect, tiles)
                    self.tiles_list.append(the_tiles)

                # Plafond
                if tiles == 4:
                    rect = self.image1.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 65 + row_count * self.tile_size
                    the_tiles = (self.image1, rect, tiles)
                    self.tiles_list.append(the_tiles)

                # Lave
                if tiles == 6:
                    lave = Lava_Water.Lava(250 + col_count * self.tile_size, 90 + row_count * self.tile_size)
                    self.lava_group.add(lave)

                # Eau
                if tiles == 7:
                    water = Lava_Water.Water(250 + col_count * self.tile_size, 90 + row_count * self.tile_size)
                    self.water_group.add(water)

                # Poison
                if tiles == 8:
                    poison = Lava_Water.Poison(250 + col_count * self.tile_size, 90 + row_count * self.tile_size)
                    self.poison_group.add(poison)

                # Porte
                if tiles == 9:
                    rect = self.image9.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 40 + row_count * self.tile_size

                    the_tiles = (self.image9, rect, tiles)
                    self.tiles_list.append(the_tiles)

                if tiles == 10:
                    rect = self.image10.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 40 + row_count * self.tile_size

                    the_tiles = (self.image10, rect, tiles)
                    self.tiles_list.append(the_tiles)

                col_count += 1
            row_count += 1

    def get_tiles_size(self):
        return self.tile_size

    def draw(self):
        for tiles in self.tiles_list:
            self.screen.blit(tiles[0], tiles[1])
            self.lava_group.draw(self.screen)
            self.water_group.draw(self.screen)
            self.poison_group.draw(self.screen)
            # pygame.draw.rect(self.screen, (255, 255, 255), tiles[1], 2)  # can help with rect

    def update_world(self):
        for i, tile_img in enumerate(self.tiles_list):
            if tile_img[2] == 9:
                if self.door_open1:
                    self.tiles_list[i] = (self.image11, tile_img[1], tile_img[2])
                else:
                    self.tiles_list[i] = (self.image9, tile_img[1], tile_img[2])
            if tile_img[2] == 10:
                if self.door_open2:
                    self.tiles_list[i] = (self.image12, tile_img[1], tile_img[2])
                else:
                    self.tiles_list[i] = (self.image10, tile_img[1], tile_img[2])
