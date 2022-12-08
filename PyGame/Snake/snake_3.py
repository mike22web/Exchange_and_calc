import pygame, random, time

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (58, 181, 44)
gold = (200, 222, 60)

disp_x = 800
disp_y = 500
dis = pygame.display.set_mode((disp_x, disp_y))
background = pygame.image.load('snake2.jpg').convert()  # общий фон игры
background = pygame.transform.smoothscale(background, dis.get_size())
background_bang = pygame.image.load('snake_bang.png').convert()  # фон при столкновении
background_bang = pygame.transform.smoothscale(background_bang, dis.get_size())
pygame.display.set_caption("Snake")

pygame.mixer.music.load("music.mp3")  # фоновая музыка
pygame.mixer.music.play(-1)
food_sound = pygame.mixer.Sound("food.wav")  # звук при поедании
bang_sound = pygame.mixer.Sound("bang.wav")  # звук при столкновении

font_snake = pygame.font.SysFont('verdana', 30)
score_font = pygame.font.SysFont('verdana', 30)

life = 3
clock = pygame.time.Clock()


# функция для создания змейки, голова - белая, тело - зелёное
def snake(snake_list, x1, y1):
    for x in snake_list:
        if x[0] == x1 and x[1] == y1:
            pygame.draw.rect(dis, white, [x[0], x[1], 10, 10])
        else:
            pygame.draw.rect(dis, green, [x[0], x[1], 10, 10])


# ф-ция для отображения счета: текущего {score} и необходимого для прохождения уровня {level_score}
def score_snake(score, level_score):
    val = score_font.render(f'Score: {score}/{level_score}', True, green)
    dis.blit(val, [0, 0])


# отображает текущий уровень
def level_img(level):
    val = score_font.render(f'Level: {level}', True, green)
    dis.blit(val, [0, 40])


# для вывода сообщений по ходу игры
def message_game(msg, color, img_x, img_y):
    message = font_snake.render(msg, True, color)
    dis.blit(message, [img_x, img_y])


# основная ф-ция игры, в параметрах скорость и уровень - меняются в зависимости от прохождения
def game_ok(speed=5, level=1, total_score=0):
    global life
    level_score = level * 3

    x1, y1 = 300, 300
    x1_change = 0
    y1_change = 0
    list_x = list(range(0, disp_x, 10))  # все клетки игрового поля по Х
    list_y = list(range(0, disp_y, 10))  # все клетки игрового поля по Y
    list_x.remove(x1)
    list_y.remove(y1)

    left_flag = False
    right_flag = False
    up_flag = False
    down_flag = False
    flag_now = left_flag

    wall_x1 = round(random.randint(10, disp_x - 10), -1)  # создаем рандомные препятствия
    wall_y1 = round(random.randint(10, disp_y - 10), -1)
    wall_x2 = round(random.randint(10, disp_x - 10), -1)
    wall_y2 = round(random.randint(10, disp_y - 10), -1)
    wall_x3 = round(random.randint(10, disp_x - 10), -1)
    wall_y3 = round(random.randint(10, disp_y - 10), -1)
    # клетки, занятые препятствиями, помещаем в отдельный список
    list_obj_x = list(range(wall_x1, wall_x1 + 200, 10)) + list(range(wall_x2, wall_x2 + 100, 10))
    list_obj_x.append(wall_x3)
    list_obj_y = list(range(wall_y3, wall_y3 + 150, 10))
    list_obj_y.append(wall_y1)
    list_obj_y.append(wall_y2)
    # удаляем занятые клетки из списка игрового поля (еда будет появлятся только на свободных клетках)
    list_x = [x for x in list_x if x not in list_obj_x]
    list_y = [y for y in list_y if y not in list_obj_y]

    # координаты еды
    food_x = random.choice(list_x)
    food_y = random.choice(list_y)

    snake_list = []
    len_snake = 1
    score = len_snake - 1

    game_over = False
    bang = False

    while not game_over:
        while bang:  # если врезались
            if life == 1:
                dis.fill((247, 247, 247))
                dis.blit(background_bang, (-200, 0))
                message_game(f'Your score {total_score}', red, disp_x / 2 + 100, disp_y / 5 - 50)
                message_game('Bang-Bang!!!', red, disp_x / 2 + 100, disp_y / 5)
                message_game('Continue?', red, disp_x / 2 + 120, disp_y / 5 + 50)
                message_game('press Y or N', red, disp_x / 2 + 110, disp_y / 5 + 100)
                pygame.display.update()
            else:
                dis.fill((247, 247, 247))
                dis.blit(background_bang, (-200, 0))
                message_game('Bang-Bang!!!', red, disp_x / 2 + 100, disp_y / 5)
                message_game('Continue?', red, disp_x / 2 + 120, disp_y / 5 + 50)
                message_game('press Y or N', red, disp_x / 2 + 110, disp_y / 5 + 100)
                pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        life -= 1
                        if life > 0 and level != 1:  # если есть жизни (life) - продолжаем с текущего уровня
                            game_ok(speed, level, total_score)  # если врезались на 1-м уровне - жизни не отнимаются
                        else:
                            life = 3
                            game_ok()  # если life=0 - начинаем сначала
                    elif event.key == pygame.K_n:  # выход из игры
                        game_over = True
                        bang = False
        while score == level_score:  # переход на следующий уровень
            dis.blit(background, (0, 0))
            message_game(f'Level {level + 1}, press SPASE', white, disp_x / 3, disp_y / 3)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        total_score += score
                        level += 1
                        speed += 3
                        game_ok(speed, level, total_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and right_flag == False:
                    x1_change = -10
                    y1_change = 0
                    left_flag = True
                    up_flag = False
                    down_flag = False
                elif event.key == pygame.K_RIGHT and left_flag == False:
                    x1_change = 10
                    y1_change = 0
                    right_flag = True
                    up_flag = False
                    down_flag = False
                elif event.key == pygame.K_UP and down_flag == False:
                    x1_change = 0
                    y1_change = -10
                    up_flag = True
                    left_flag = False
                    right_flag = False
                elif event.key == pygame.K_DOWN and up_flag == False:
                    x1_change = 0
                    y1_change = 10
                    down_flag = True
                    left_flag = False
                    right_flag = False
                elif event.key == pygame.K_SPACE:
                    x1_change = 0
                    y1_change = 0

        if x1 >= disp_x or x1 < 0 or y1 >= disp_y or y1 < 0:
            bang_sound.play()
            total_score += score
            bang = True

        x1 += x1_change
        y1 += y1_change
        dis.blit(background, (0, 0))
        pygame.draw.circle(dis, gold, [food_x + 5, food_y + 5], 5)  # еда будет круглая)
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > len_snake:
            del snake_list[0]
        for x_y in snake_list[:-1]:  # условие, если врезается сама в себя
            if x_y == snake_head:
                bang_sound.play()
                total_score += score
                bang = True

        wall_1 = [range(wall_x1, wall_x1 + 200, 10), wall_y1]  # преграды
        wall_2 = [range(wall_x2, wall_x2 + 100, 10), wall_y2]
        wall_3 = [wall_x3, range(wall_y3, wall_y3 + 150, 10)]

        if snake_head[0] in wall_1[0] and snake_head[1] == wall_1[1]:  # если врезались в преграду
            bang_sound.play()
            total_score += score
            bang = True
        elif snake_head[0] in wall_2[0] and snake_head[1] == wall_2[1]:
            bang_sound.play()
            total_score += score
            bang = True
        elif snake_head[0] == wall_3[0] and snake_head[1] in wall_3[1]:
            bang_sound.play()
            total_score += score
            bang = True

        if x1 == food_x and y1 == food_y:  # если достигли еды
            food_sound.play()
            food_x = random.choice(list_x)
            food_y = random.choice(list_y)
            len_snake += 1

        pygame.draw.rect(dis, red, [wall_x1, wall_y1, 200, 10])
        pygame.draw.rect(dis, red, [wall_x2, wall_y2, 100, 10])
        pygame.draw.rect(dis, red, [wall_x3, wall_y3, 10, 150])
        pygame.display.update()
        snake(snake_list, x1, y1)
        score = len_snake - 1
        score_snake(score, level_score)
        message_game(f'Speed: {speed}', green, 0, 80)
        message_game(f'Life: {life}', green, 0, 120)
        # message_game(f'total: {total_score}', green, 0, 160)
        level_img(level)

        pygame.display.update()

        clock.tick(speed)

    pygame.quit()
    quit()


game_ok()
