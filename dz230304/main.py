import pygame
import random
import logging

logging.basicConfig(level=logging.INFO, filename="logging_snake.py",filemode="w")

W, H = 600, 600
FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
dis = pygame.display.set_mode((W, H))

x0, y0 = W // 2, H // 2
x0_change, y0_change = 0, 0
snake_block = 10
count_food = 0
length_snake = 1


def message(msg, color):
    """
    Отображение теста об окончании игры
    :param msg: текст
    :param color: цвет
    :return: None
    """
    msg = font_style.render(msg, True, color)
    screen.blit(msg, (W // 6 - msg.get_width() // 6, H // 6 - msg.get_height() // 6))


def init_1(running, game_over, foodx, foody, snake_list, x0, y0, length_snake):
    running = True
    game_over = False
    foodx, foody = generate_food()
    #stonex, stoney = generate_stones()
    snake_list = []
    length_snake = 1

    x0, y0 = W // 2, H // 2
    return running, game_over, foodx, foody, snake_list, x0, y0, length_snake


def draw_snake(snake_list):
    """
    Рисует змейку
    :param snake_list: координаты кубиков змеии
    :return: None
    """
    for el in snake_list:
        pygame.draw.rect(screen, RED, (el[0], el[1], snake_block, snake_block))


def generate_food():
    """
    Рисует еду
    """
    x = round(random.randrange(0, W - snake_block) / snake_block) * snake_block
    y = round(random.randrange(0, H - snake_block) / snake_block) * snake_block
    logging.info(f"Нарисована еда{x,y}")
    return x, y


def generate_stones():
    """
    Рисует камни
    """
    a = []
    b = []
    for i in range(10):
        x = round(random.randrange(0, W - snake_block) / snake_block) * snake_block
        y = round(random.randrange(0, H - snake_block) / snake_block) * snake_block
        a.append(x)
        b.append(y)
    logging.info(f"Нарисованы камешки на координатах{a,b}")
    return a, b


def score(score):
    """
    Отображение счёта
    """
    value = score_font.render("Ваш счёт: " + str(score), True, RED)
    dis.blit(value, [0, 0])


def flip(x0, y0, x0_change, y0_change):
    if not game_over:
        x0 += x0_change
        y0 += y0_change
        if x0 < 0:
            x0 = 0
        if y0 < 0:
            y0 = 0
        if x0 > W - snake_block:
            x0 = W - snake_block + 1
        if y0 > H - snake_block:
            y0 = H - snake_block + 1
    logging.info(f"Новые координаты головы змейки: {x0,y0}")
    return x0, y0


if __name__ == "__main__":
    pygame.init()

    running = True
    game_over = False
    foodx, foody = generate_food()
    stonex, stoney=generate_stones()
    snake_list = []

    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Игра Змейка")
    clock = pygame.time.Clock()
    font_style = pygame.font.SysFont(None, 20)
    score_font = pygame.font.SysFont("comicsansms", 35)
    # message_1("Счёт:", count_food, RED)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x0_change = -snake_block
                    y0_change = 0
                elif event.key == pygame.K_RIGHT:
                    x0_change = snake_block
                    y0_change = 0
                elif event.key == pygame.K_UP:
                    x0_change = 0
                    y0_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x0_change = 0
                    y0_change = snake_block
                if game_over and event.key == pygame.K_c:
                    running, game_over, foodx, foody, snake_list, x0, y0, length_snake = init_1(running,game_over,foodx,foody,snake_list,x0, y0,length_snake,)
                    # draw_snake(snake_list)

        x0, y0 = flip(x0, y0, x0_change, y0_change)

        snake_list.append((x0, y0))
        logging.info(f"Голова змейки на {x0,y0}")
        

        if len(snake_list) > length_snake:
            snake_list.pop(0)

        for el in snake_list[:-1]:
            if el == snake_list[-1]:
                logging.info("Змейка врезалась сама в себя")
                game_over = True

        if x0 > W - snake_block or x0 < 0 or y0 > H - snake_block or y0 < 0:
            logging.info("Змейка врезалась в бортик")
            game_over = True

        for i in range(len(stonex)):
            if (x0, y0) == (stonex[i],stoney[i]):
                logging.info("Змейка врезалась в камешек")
                game_over = True

        screen.fill(WHITE)
        if game_over:
            logging.info("Игра закончена")
            message(f"Вы проиграли! Нажмите C для повторной игры {x0, y0, x0_change, y0_change}", RED)

        draw_snake(snake_list)
        pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])
        for i in range(len(stonex)):
            pygame.draw.rect(screen, BLACK, [stonex[i], stoney[i], snake_block, snake_block])

        score(length_snake - 1)

        pygame.display.update()

        if (x0, y0) == (foodx, foody):
            foodx, foody = generate_food()
            length_snake += 1
            count_food += 1
            logging.info("Счёт увеличился на еденичку")
            logging.info("Длина змейки увеличилась на еденичку")
            logging.info(f"Змейка съела еду на координатах {x0,y0}")

        clock.tick(FPS)

    pygame.quit()
    quit()
print(score)
