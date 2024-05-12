import pygame


class World:
    def __init__(self, data, tile_size):
        self.tiles_list = []
        self.data = data
        self.tile_size = tile_size
        self.screen = pygame.display.get_surface()
        # load images
        dirt_img = pygame.image.load('dirt.png')
        # grass_img = pygame.image.load('grass.png')
        self.stone = pygame.image.load('green_ground.png')
        half_stone_img = pygame.image.load('half_stone.png')
        stone2 = pygame.image.load('green_stone.png')
        self.image1 = pygame.transform.scale(stone2, (self.tile_size, self.tile_size))
        self.image3 = pygame.transform.scale(half_stone_img, (self.tile_size, self.tile_size / 2))
        self.image2 = pygame.transform.scale(self.stone, (self.tile_size, self.tile_size))

        row_count = 0

        for list_row in self.data:
            col_count = 0
            for tiles in list_row:

                if tiles == 1:
                    # rect2 = image2.get_rect()
                    # image = pygame.transform.scale(dirt_img, (self.tile_size, self.tile_size))
                    rect2 = self.image1.get_rect()
                    rect2.x = 250 + col_count * self.tile_size
                    rect2.y = 65 + row_count * self.tile_size

                    the_tiles = (self.image1, rect2, tiles)
                    self.tiles_list.append(the_tiles)

                if tiles == 2:
                    rect = self.image2.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 65 + row_count * self.tile_size
                    the_tiles = (self.image2, rect, tiles)
                    self.tiles_list.append(the_tiles)

                if tiles == 3:
                    rect = self.image3.get_rect()
                    rect.x = 250 + col_count * self.tile_size
                    rect.y = 65 + row_count * self.tile_size
                    the_tiles = (self.image3, rect, tiles)
                    self.tiles_list.append(the_tiles)

                col_count += 1
            row_count += 1

    def get_tiles_list(self):
        return self.tiles_list

    def draw(self):
        for tiles in self.tiles_list:
            self.screen.blit(tiles[0], tiles[1])
            # pygame.draw.rect(self.screen, (255, 255, 255), tiles[1],2)  # can help with rect
