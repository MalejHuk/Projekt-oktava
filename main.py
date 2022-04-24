import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))


def button(screen, position, text):
    pygame.display.set_caption('Hra Snake')
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (50, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (100, 100, 100), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (100, 100, 100), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def lehka():
    import random

    pygame.init()

    bila = (255, 255, 255)
    zelena = (70, 100, 80)
    modra = (100, 10, 50)
    zluta = (150, 100, 20)


    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Hra Snake')

    clock = pygame.time.Clock()

    had_block = 10
    had_speed = 30

    font_style = pygame.font.SysFont("Arial", 25)
    score_font = pygame.font.SysFont("Arial", 35)

    def moje_skore(score):
        value = score_font.render("Vaše skóre: " + str(score), True, zluta)
        dis.blit(value, [280, 0])

    def muj_had(hadik, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, bila, [x[0], x[1], hadik, hadik])

    def message(msg, color):
        assert isinstance(color, object)
        zprava = font_style.render(msg, True, color)
        dis.blit(zprava, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        delka_hada = 1

        jidlo1 = round(random.randrange(0, dis_width - had_block) / 10.0) * 10.0
        jidlo2 = round(random.randrange(0, dis_height - had_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(zelena)

                message("Prohra! Z = Hrát znovu, O = Odejít, T = Těžší úroveň", zluta)
                moje_skore(delka_hada - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_o:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_z:
                            gameLoop()
                        if event.key == pygame.K_t:
                            tezka()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -had_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = had_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -had_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = had_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(zelena)
            pygame.draw.rect(dis, modra, [jidlo1, jidlo2, had_block, had_block])
            hlava = []
            hlava.append(x1)
            hlava.append(y1)
            snake_List.append(hlava)
            if len(snake_List) > delka_hada:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == hlava:
                    game_close = True

            muj_had(had_block, snake_List)
            moje_skore(delka_hada - 1)

            pygame.display.update()

            if x1 == jidlo1 and y1 == jidlo2:
                jidlo1: float = round(random.randrange(0, dis_width - had_block) / 10.0) * 10.0
                jidlo2 = round(random.randrange(0, dis_height - had_block) / 10.0) * 10.0
                delka_hada += 1

            clock.tick(had_speed)

        pygame.quit()
        quit()

    gameLoop()

def tezka():

    import random

    pygame.init()

    bila = (255, 255, 255)
    zelena = (70, 100, 80)
    modra = (100, 10, 50)
    zluta = (150, 100, 20)


    dis_width = 800
    dis_height = 600

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Hra Snake')

    clock = pygame.time.Clock()

    had_block = 10
    had_speed = 50

    font_style = pygame.font.SysFont("Arial", 25)
    score_font = pygame.font.SysFont("Arial", 35)

    def moje_skore(score):
        value = score_font.render("Vaše skóre: " + str(score), True, zluta)
        dis.blit(value, [280, 0])

    def muj_had(hadik, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, bila, [x[0], x[1], hadik, hadik])

    def message(msg, color):
        assert isinstance(color, object)
        zprava = font_style.render(msg, True, color)
        dis.blit(zprava, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        delka_hada = 1

        jidlo1 = round(random.randrange(0, dis_width - had_block) / 10.0) * 10.0
        jidlo2 = round(random.randrange(0, dis_height - had_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(zelena)

                message("Prohra! Z = Hrát znovu, O = Odejít, L = Zkusím lehčí", zluta)

                moje_skore(delka_hada - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_o:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_z:
                            gameLoop()
                        if event.key == pygame.K_l:
                            lehka()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -had_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = had_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -had_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = had_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(zelena)
            pygame.draw.rect(dis, modra, [jidlo1, jidlo2, had_block, had_block])
            hlava = []
            hlava.append(x1)
            hlava.append(y1)
            snake_List.append(hlava)
            if len(snake_List) > delka_hada:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == hlava:
                    game_close = True

            muj_had(had_block, snake_List)
            moje_skore(delka_hada - 1)

            pygame.display.update()

            if x1 == jidlo1 and y1 == jidlo2:
                jidlo1: float = round(random.randrange(0, dis_width - had_block) / 10.0) * 10.0
                jidlo2 = round(random.randrange(0, dis_height - had_block) / 10.0) * 10.0
                delka_hada += 1

            clock.tick(had_speed)

        pygame.quit()
        quit()

    gameLoop()


def menu():
    b1 = button(screen, (230, 200), "Těžká obtížnost")
    b2 = button(screen, (230, 300), "Lehká obtížnost")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    lehka()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    tezka()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    lehka()
        pygame.display.update()

menu()

