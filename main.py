import sys, pygame
from setting import Setting
from cell import Cell

array_matrix = [[50, 350, 650],[]]

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    pygame.init()
    st = Setting()
    screen = pygame.display.set_mode(st.SCREEN_SIZE)
    pygame.display.set_caption('Tik Tak V3')
    clock = pygame.time.Clock()
    sprites = pygame.sprite.Group()
    number = 0
    for row in range (st.BLOKS):
        for column in range(st.BLOKS):
            number += 1
            w = column*st.SIZE_BLOKS+(column+1)*st.MARGIN
            h = row*st.SIZE_BLOKS+(row+1)*st.MARGIN
            cell = Cell(w, h, number, st)
            sprites.add(cell)

    running = True
    # Цикл игры
    while running:
        # Держим цикл на правильной скорости
        clock.tick(st.FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sprite: Cell
                    for sprite in sprites:
                        if sprite.mouse_click(pygame.mouse.get_pos()):
                            sprite.cell_change(st)
                            print(sprite.number)


        # Обновление
        sprites.update()

        # Рендеринг
        screen.fill(st.BLACK)
        sprites.draw(screen)

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())