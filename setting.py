class Setting():
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        self.BLOKS = 3
        self.SIZE_BLOKS = 100
        self.MARGIN = 10
        self.WIDTH = self.BLOKS * self.SIZE_BLOKS + (self.BLOKS + 1) * self.MARGIN
        self.HEIGHT = self.BLOKS * self.SIZE_BLOKS + (self.BLOKS + 1) * self.MARGIN

        self.SCREEN_SIZE = (self.WIDTH, self.HEIGHT)
        self.FPS = 60

        self.STATUS = {"empty": 0, "zero": 1, "cross": 2}
