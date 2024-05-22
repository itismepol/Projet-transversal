import pygame


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, side):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.side = side
        self.box_speed = 0
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.screen = pygame.display.get_surface()
        box_img = pygame.image.load('box.png').convert_alpha()
        self.image = pygame.transform.scale(box_img, (self.side, self.side))

    def draw_rect(self):
        self.screen.blit(self.image, self.rect)


