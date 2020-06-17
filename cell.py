import pygame
from setting import Setting

class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, number, st: Setting):
        super().__init__()
        self.number = number
        self.status = st.STATUS["empty"]
        self.images = []
        # self.images.append(pygame.Surface((st.SIZE_BLOKS, st.SIZE_BLOKS)))
        self.image = pygame.image.load('img/empty.png')
        self.image = pygame.transform.scale(self.image, (st.SIZE_BLOKS, st.SIZE_BLOKS))
        self.images.append(self.image)
        self.image = pygame.image.load('img/zero.png')
        self.image = pygame.transform.scale(self.image, (st.SIZE_BLOKS, st.SIZE_BLOKS))
        self.images.append(self.image)
        self.image = pygame.image.load('img/cross.png')
        self.image = pygame.transform.scale(self.image, (st.SIZE_BLOKS, st.SIZE_BLOKS))
        self.images.append(self.image)
        self.image = self.images[0]
        # self.image.fill(st.BLUE)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # print(self.number)
        pass

    def mouse_click(self, pos):
        result = False
        if self.rect.collidepoint(pos):
            result =  True
        return result

    def cell_change(self):
        if self.status == "empty":
            print("empty")
        elif self.status == "zero":
            print("zero")
        elif self.status == "cross":
            print('cross')
        pass

