import pygame
import os
import sys
from random import randrange as rd
import write_resultat


FPS = 60
pass_level = 0
collect_balls = 0


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = 'maps/' + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def start_screen():
    intro_text = ['Игра "В поисках bровей".',
                  'Чтоbы пройти игру вам нужно пройти 3 уровня.',
                  "В третьем уровне используйте свою смекалку.",
                  'Для управлением ходьbы Серёжи нужно использовать',
                  '"<=" - влево; "=>" - вправо; "v" - вниз; "^" - вверх.',
                  'Чтобы начать игру нажмите на Space.']

    fon = pygame.transform.scale(load_image('start_background.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 36)
    text_coord = 540
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def end_screen():
    intro_text = [f'Ваш результат: {collect_balls} очков.',
                  'Вы потеряли шанс получить новые брови.',
                  'Ваш дом горит.']

    fon = pygame.transform.scale(load_image('end_background.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = 630
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


def kill_player(count_life):
    if count_life == 0:
        write_resultat.lose(pass_level, count_life, collect_balls)
        end_screen()
    else:
        text = ['bудьте акуратнее.',
                f'У вас осталось {count_life} жизни.',
                'Для продолжения игры нажмите Space.']
        fon = pygame.transform.scale(load_image('kill.png'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 630
        for line in text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        return  # продолжаем игру
            pygame.display.flip()
            clock.tick(FPS)


def pause_screen(count_life, count_ball):
    global pass_level
    screen.fill('grey')
    text = [f'Отлично, вы прошли {pass_level} уровень.', f'Вы собрали {count_ball} очков.']
    if count_life == 1:
        text.append(f'У вас осталось {count_life} жизнь.')
    else:
        text.append(f'У вас осталось {count_life} жизни.')
    text.append('Чтобы продолжить игру нажмите на Space.')
    fon = pygame.transform.scale(load_image(f'pause_background_{pass_level}.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = 590
    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    return  # продолжаем игру
        pygame.display.flip()
        clock.tick(FPS)


def win_screen(count_level, count_life, count_ball):
    intro_text = ['Поздравляю, вы прошли игру!!',
                  f'Количество оставшихся жиней: {count_life}.',
                  f'Ваш результат: {count_ball} очков.']

    if count_ball == 13 * 30:
        intro_text.append('Вы смогли найти свои идеальные брови.')

        fon = pygame.transform.scale(load_image('win_background.png'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 590
        write_resultat.win_full(count_level, count_life, count_ball)
    else:
        intro_text.append('Вы смогли смогли заполучить')
        intro_text.append('свою идеальную монобровь.')
        fon = pygame.transform.scale(load_image('win_background_monobrov.png'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 550
        write_resultat.win_no_full(count_level, count_life, count_ball)

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                terminate()  # продолжаем игру
        pygame.display.flip()
        clock.tick(FPS)


def draw_all(sc):
    screen.fill('black')
    if pass_level == 2:
        eyebrows_group.draw(sc)
    empty_group.draw(sc)
    wall_group.draw(sc)
    patch_group.draw(sc)
    if not pass_level == 2:
        eyebrows_group.draw(sc)
    player_group.draw(sc)
    kill_group.draw(sc)
    heart_on_map_group.draw(sc)
    heart.draw()
    draw_count_ball()


def draw_count_ball():
    font = pygame.font.Font(None, 50)

    string_rendered = font.render(str(collect_balls), 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = 680
    intro_rect.y = 0
    screen.blit(string_rendered, intro_rect)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 750, 750
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('В поисках бровей')

    def generate_level(level):
        new_player, x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                # h - машинка
                # s - сердце
                # p - пластырь
                # r - бритва
                if level[y][x] == '.':
                    Empty('empty', x, y)
                elif level[y][x] == '#':
                    Wall('wall', x, y)
                elif level[y][x] == '@':
                    Empty('empty', x, y)
                    new_player = Player(x, y)
                elif level[y][x] == 'p':
                    Patch(x, y)
                    Empty('empty', x, y)
                elif level[y][x] == 'h':
                    HairClip(x, y, rd(3, 6))
                    Empty('empty', x, y)
                elif level[y][x] == 'f':
                    FalseWall('empty', x, y)
                elif level[y][x] == 'r':
                    Razor(x, y, rd(3, 6))
                    Empty('empty', x, y)
                elif level[y][x] == 'b':
                    Eyebrows(x, y)
                    Empty('empty', x, y)
                elif level[y][x] == 'g':
                    HeartOnMap(x, y)
                    Empty('empty', x, y)
        return new_player, x, y

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def kill_sprites(cls):
        for sprite in cls:
            sprite.kill()

    class Empty(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(empty_group, all_sprites)
            self.image = tile_images[tile_type]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)

    class FalseWall(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(empty_group, all_sprites)
            self.image = load_image('false_wall.png')
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)

    class Wall(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(wall_group, all_sprites)
            self.image = tile_images[tile_type]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)

    class Patch(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__(patch_group, all_sprites)
            self.image = load_image('patch.png', 'black')
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 5, tile_height * pos_y + 10)

    class HeartOnMap(pygame.sprite.Sprite):
        image = load_image('heart.png', 'white')
        image = pygame.transform.scale(image, (36, 36))

        def __init__(self, pos_x, pos_y):
            super().__init__(heart_on_map_group, all_sprites)
            self.image = HeartOnMap.image
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 7, tile_height * pos_y + 7)

    class Eyebrows(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__(eyebrows_group, all_sprites)
            self.image = load_image('eyebrows.png', 'white')
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 5, tile_height * pos_y + 22)

    class Razor(pygame.sprite.Sprite):
        image_up = load_image('razor_up.png', 'white')
        image_down = load_image('razor_down.png', 'white')

        def __init__(self, pos_x, pos_y, speed):
            super().__init__(kill_group, all_sprites)
            self.image = Razor.image_down
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 8, tile_height * pos_y)
            self.speed = speed

        def update(self):
            self.rect = self.rect.move(0, self.speed)
            if pygame.sprite.spritecollide(self, wall_group, dokill=False) or \
                    self.rect[0] < 0 or self.rect[1] < 0:
                self.speed *= -1
            if self.speed < 0:
                self.image = Razor.image_up
            else:
                self.image = Razor.image_down

            if pygame.sprite.spritecollide(self, player_group, dokill=False):
                global click
                click = False
                Heart.count_life -= 1
                kill_player(Heart.count_life)
                player.kill_and_change_cod()
                player.image = player_stan

    class HairClip(pygame.sprite.Sprite):
        image_right = load_image('hair_clipper_right.png', 'white')
        image_left = load_image('hair_clipper_left.png', 'white')

        def __init__(self, pos_x, pos_y, speed):
            super().__init__(kill_group, all_sprites)
            self.image = HairClip.image_right
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)
            self.speed = speed

        def update(self):
            self.rect = self.rect.move(self.speed, 0)
            if pygame.sprite.spritecollide(self, wall_group, dokill=False) or \
                    self.rect[0] < 0 or self.rect[1] < 0:
                self.speed *= -1
            if self.speed < 0:
                self.image = HairClip.image_left
            else:
                self.image = HairClip.image_right
            if pygame.sprite.spritecollide(self, player_group, dokill=False):
                global click
                click = False
                Heart.count_life -= 1
                kill_player(Heart.count_life)
                player.kill_and_change_cod()
                player.image = player_stan

    class Heart(pygame.sprite.Sprite):
        image = load_image('heart.png', 'white')
        image = pygame.transform.scale(image, (50, 50))
        count_life = 3

        def __init__(self, pos_x, pos_y):
            super().__init__(pygame.sprite.Group())
            self.image = Heart.image
            self.x = pos_x
            self.y = pos_y

        def draw(self):
            for i in range(Heart.count_life):
                if i == 0:
                    screen.blit(self.image, (self.x + 50 * i, self.y))
                if i == 1:
                    screen.blit(self.image, (self.x + 50 * i, self.y))
                if i == 2:
                    screen.blit(self.image, (self.x + 50 * i, self.y))
                if i == 3:
                    screen.blit(self.image, (self.x + 50 * i, self.y))

    class Player(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__(player_group, all_sprites)
            self.image = load_image('sereja.png', 'black')
            self.rect = self.image.get_rect().move(
                tile_width * pos_x + 15, tile_height * pos_y + 5)
            self.x_0 = pos_x
            self.y_0 = pos_y

            self.anim_count = 0
            self.speed = 5

        def update(self, event):
            global collect_balls
            deistvie = (0, 0)
            if event.key == pygame.K_UP:
                self.rect = self.rect.move(0, -self.speed)
                deistvie = (0, self.speed)
                self.anim_count += 1
            elif event.key == pygame.K_DOWN:
                self.rect = self.rect.move(0, self.speed)
                deistvie = (0, -self.speed)
                self.anim_count += 1
            elif event.key == pygame.K_RIGHT:
                self.rect = self.rect.move(self.speed, 0)
                deistvie = (-self.speed, 0)
                self.anim_count += 1
            elif event.key == pygame.K_LEFT:
                self.rect = self.rect.move(-self.speed, 0)
                deistvie = (self.speed, 0)
                self.anim_count += 1
            else:
                pass

            if pygame.sprite.spritecollide(self, wall_group, dokill=False) or \
                    self.rect[0] < 0 or self.rect[1] < 0:
                self.rect = self.rect.move(deistvie[0], deistvie[1])
                self.anim_count -= 1
            else:
                if deistvie == (0, self.speed):
                    self.image = walk_up[self.anim_count // 4]
                if deistvie == (0, -self.speed):
                    self.image = walk_down[self.anim_count // 4]
                if deistvie == (self.speed, 0):
                    self.image = walk_left[self.anim_count // 4]
                if deistvie == (-self.speed, 0):
                    self.image = walk_right[self.anim_count // 4]

            if self.anim_count >= 15:
                self.anim_count = 0

            if pygame.sprite.spritecollide(self, patch_group, dokill=True):
                collect_balls += 30

            elif pygame.sprite.spritecollide(self, heart_on_map_group, dokill=True):
                Heart.count_life += 1

            elif pygame.sprite.spritecollide(self, eyebrows_group, dokill=True):
                global player, level_x, level_y, click, pass_level
                pass_level += 1
                if pass_level == 2:
                    pause_screen(Heart.count_life, collect_balls)
                    kill_sprites(all_sprites)
                    click = False

                    global tile_images
                    tile_images = {
                        'wall': load_image('wall.png', 'white'),
                        'empty': load_image('empty_eyebrows.png')}

                    player, level_x, level_y = generate_level(load_level(f'map_{pass_level + 1}.txt'))
                    player.kill_and_change_cod()
                    player.image = player_stan

                elif pass_level == 3:
                    win_screen(pass_level, Heart.count_life, collect_balls)
                    kill_sprites(all_sprites)
                    click = False

                else:
                    pause_screen(Heart.count_life, collect_balls)
                    kill_sprites(all_sprites)
                    click = False

                    player, level_x, level_y = generate_level(load_level(f'map_{pass_level + 1}.txt'))
                    player.kill_and_change_cod()
                    player.image = player_stan

        def kill_and_change_cod(self):
            self.rect = self.image.get_rect().move(
                tile_width * self.x_0 + 15, tile_height * self.y_0 + 5)

    walk_right = [load_image('RIGHT/sereja_right_1.png'),
                  load_image('RIGHT/sereja_right_2.png'),
                  load_image('RIGHT/sereja_right_3.png'),
                  load_image('RIGHT/sereja_right_4.png')]

    walk_left = [load_image('LEFT/sereja_left_1.png'),
                 load_image('LEFT/sereja_left_2.png'),
                 load_image('LEFT/sereja_left_3.png'),
                 load_image('LEFT/sereja_left_4.png')]

    walk_down = [load_image('DOWN/sereja_down_1.png'),
                 load_image('DOWN/sereja_down_2.png'),
                 load_image('DOWN/sereja_down_3.png'),
                 load_image('DOWN/sereja_down_4.png')]

    walk_up = [load_image('UP/sereja_up_1.png'),
               load_image('UP/sereja_up_2.png'),
               load_image('UP/sereja_up_3.png'),
               load_image('UP/sereja_up_4.png')]

    player_stan = load_image('sereja.png', 'black')

    all_sprites = pygame.sprite.Group()
    empty_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    gaming_count = pygame.sprite.Group()
    eyebrows_group = pygame.sprite.Group()
    kill_group = pygame.sprite.Group()
    patch_group = pygame.sprite.Group()
    heart_on_map_group = pygame.sprite.Group()
    heart = Heart(0, 0)

    tile_width = tile_height = 50

    tile_images = {
        'wall': load_image('wall.png', 'white'),
        'empty': load_image('empty.png')}
    running = True
    click = False

    fps = 60
    clock = pygame.time.Clock()
    start_screen()
    hero_sprites = pygame.sprite.Group()
    player, level_x, level_y = generate_level(load_level('map_1.txt'))
    last_event = None

    while running:
        draw_all(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN\
                        or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    click = True
                    last_event = event

            if event.type == pygame.KEYUP:
                #бытсрая победа
                '''if event.key == pygame.K_w:
                    win_screen(3, 3, 13 * 30)
                    kill_sprites(all_sprites)
                    click = False
                elif event.key == pygame.K_q:
                    win_screen(3, 3, 12 * 30)
                    kill_sprites(all_sprites)
                    click = False'''

                click = False
                player.anim_count = 0
                player.image = player_stan
                last_event = event

        if click:
            if last_event.key == pygame.K_UP or last_event.key == pygame.K_DOWN \
                    or last_event.key == pygame.K_LEFT or last_event.key == pygame.K_RIGHT:
                player.update(last_event)

        kill_group.update()
        pygame.time.delay(50)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
