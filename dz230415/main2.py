import pygame
import random
import numpy as np

WIDTH = 500
HEIGHT = 500
FPS = 100
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Violet = (238, 130, 238)
DarkViolet = (148, 0, 211)
BlueViolet = (138, 43, 226)
Magenta = (255, 0, 255)
MediumPurple = (147, 112, 219)
MediumOrchid = (186, 85, 211)
Plum =(221, 160, 221)
color = [DarkViolet,BlueViolet,MediumPurple, MediumOrchid,Magenta,Violet,Plum]
r = 2
x = 500
k = 1
l = 1
dt = 1
speed = 0
xs = np.ones(10000)
ys = np.ones(10000)
vxs = np.ones(10000)
vys = np.ones(10000)

for i in range(10000):
    xs[i] = random.random() * WIDTH
    ys[i] = random.random() * HEIGHT
    vxs[i] = random.random()
    vys[i] = random.random()

print(xs, ys, vxs, vys)

def message(msg, color,f,g):
    msg1 = font.render(msg, True, color)
    screen.blit(msg1, (f,g))

# def mes(score):
#     value = message.render("temperature: " + tmp, True, WHITE)
#     dis.blit(value, [0, 0])
# def draw_line(surface: pygame.surface.Surface, color: pygame.color.Color, x: list[int], y: list[int]) -> None:
#     y = y + vx * dt
#     x = x + vx * dt
#     for i in range(1, len(xs)):
#         x2 = xs[i]
#         y2 = ys[i]
#         pygame.draw.line(surface, color, (x1, y1), (x2, y2))
#         # print(x1,y1, x2, y2)
#         x1, y1 = x2, y2

pygame.init()
# pygame.mixer.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Цикл игры
running = True

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверяем хотят ли выйти
        if event.type == pygame.QUIT:
            running = False

    ys = ys + vys * dt
    xs = xs + vxs * dt
    x -= 0.5


    vxs[xs < 0] = np.abs(vxs[xs < 0])
    vys[ys < 0] = np.abs(vys[ys < 0])
    vxs[xs > x] = -(np.abs(vxs[xs > x])+0.5)
    vys[ys > WIDTH] = -np.abs(vys[ys > WIDTH])
    speed = np.sum(np.sum((vxs[xs > x])**2)+np.sum(vys[ys > WIDTH]**2)+np.sum(vys[ys < 0]**2)+np.sum(vxs[xs < 0]**2))
    print(speed)
    tmp = (np.mean(np.sqrt(vxs**2 + vys**2)))**2


    screen.fill(BLACK)
    for i in range(10000):
        pygame.draw.circle(screen, color[random.randint(0,6)], [xs[i], ys[i]], r)
    pygame.draw.aaline(screen,WHITE,(x,0),(x,HEIGHT))
    message(f"temperature:{tmp}", WHITE,15,25)
    message(f"volume:{x*500}", WHITE,15,10)
    message(f"pressure:{speed/(x+500)*2}", WHITE, 15, 40)
    pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    pass
