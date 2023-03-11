import pygame
import random

W, H = 100, 100
count_rock = 80
FPS = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
shushunchik_block = 10
allhead = []


# shushunchik_block1 = Point(W // 2, H // 2)

def draw_food(foodx, foody):
    pygame.draw.rect(screen, GREEN, (foodx, foody, shushunchik_block, shushunchik_block))


def draw_shushunchik(head):
    allhead.append((head.x,head.y))
    pygame.draw.rect(screen, PINK, (head.x, head.y, shushunchik_block, shushunchik_block))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __repr__(self):
        return f"({self.x},{self.y})"


class Game:
    def __init__(self):
        self.head = Point(W // 2, H // 2)
        # начальные сдвиг змеи
        self.head_change = Point(0, 0)

    def shushunchik_step(self):
        self.head += self.head_change
        # self.shushunchik_block1 = self.head

    def shushunchik_left(self):
        self.head_change = Point(-shushunchik_block, 0)

    def shushunchik_right(self):
        self.head_change = Point(shushunchik_block, 0)

    def shushunchik_up(self):
        self.head_change = Point(0, -shushunchik_block)

    def shushunchik_down(self):
        self.head_change = Point(0, shushunchik_block)

    def move(self):
        a = random.randint(1, 10)
        if a == 5 or a == 8:
            game.shushunchik_left()
        elif a == 6 or a == 9 or a == 1:
            game.shushunchik_up()
        elif a == 3 or a == 10 or a == 5:
            game.shushunchik_down()
        else:
            game.shushunchik_right()

    def shushunchik_left_field(self):
        # если змея вышла за границы поля
        if self.head.x >= W:
            self.head.x = 0
        elif self.head.x < 0:
            self.head.x = W
        elif self.head.y >= H:
            self.head.y = 0
        elif self.head.y < 0:
            self.head.y = H


if __name__ == "__main__":
    # logging.info(f"{W=} {H=} {count_rock=} {FPS + 100=} {snake_block=}")
    pygame.init()  # инициализируем модуль pygame

    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    font_style = pygame.font.SysFont(None, 50)
    running = True
    game = Game()

    while running:
        for event in pygame.event.get():
            # если пользователь нажал крестик на окне
            if event.type == pygame.QUIT:
                # прерываем основной цикл (чтобы закрыть потом приложение)
                running = False
        game.move()

        game.shushunchik_step()
        # если шушунчик покинул поле
        game.shushunchik_left_field()
        screen.fill(GRAY)
        for i in range(0, 100):
            for j in range(0, 100):
                if not (i == game.head.x) and not (j == game.head.y) and (i,j) not in allhead:
                    draw_food(i, j)
        draw_shushunchik(game.head)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    # закрываем python программу
    quit()
