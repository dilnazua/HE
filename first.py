import pygame
import random
import sys

pygame.init()
window = (1536, 864)
screen = pygame.display.set_mode(window)
t = False
pygame.display.set_caption("Russian language learning app")


def tform(ima):
    return pygame.transform.scale(pygame.image.load(ima), (205, 196))


def makeleft(im):
    return pygame.transform.flip(tform(im), True, False)


def create_spr(spr, rt):
    for i in spr:
        sprite = pygame.sprite.Sprite()
        sprite.image = i
        sprite.rect = sprite.image.get_rect()
        rt.add(sprite)


arr_r = pygame.sprite.Group()
arr_l = pygame.sprite.Group()
arr_s = pygame.sprite.Group()

walkRight = [tform('Walk (1).png'), tform('Walk (2).png'), tform('Walk (3).png'), tform('Walk (4).png'),
             tform('Walk (5).png'), tform('Walk (6).png'), tform('Walk (7).png'), tform('Walk (8).png'),
             tform('Walk (9).png'), tform('Walk (10).png'), tform('Walk (11).png'), tform('Walk (12).png'),
             tform('Walk (13).png'), tform('Walk (14).png'), tform('Walk (15).png')]
create_spr(walkRight, arr_r)
stand = [tform('Idle (1).png'), tform('Idle (2).png'), tform('Idle (3).png'), tform('Idle (4).png'),
         tform('Idle (5).png'), tform('Idle (6).png'), tform('Idle (7).png'), tform('Idle (8).png'),
         tform('Idle (9).png'), tform('Idle (10).png'), tform('Idle (11).png'), tform('Idle (12).png'),
         tform('Idle (13).png'), tform('Idle (14).png'), tform('Idle (15).png')]
create_spr(stand, arr_s)
walkleft = [makeleft('Walk (1).png'), makeleft('Walk (2).png'), makeleft('Walk (3).png'), makeleft('Walk (4).png'),
            makeleft('Walk (5).png'), makeleft('Walk (6).png'), makeleft('Walk (7).png'), makeleft('Walk (8).png'),
            makeleft('Walk (9).png'), makeleft('Walk (10).png'), makeleft('Walk (11).png'), makeleft('Walk (12).png'),
            makeleft('Walk (13).png'), makeleft('Walk (14).png'), makeleft('Walk (15).png')]
create_spr(walkleft, arr_l)

# walkleft.reverse()


a_image = pygame.transform.scale(pygame.image.load('A.png'), (150, 100))

b_image = pygame.transform.scale(pygame.image.load('B.png'), (150, 100))

c_image = pygame.transform.scale(pygame.image.load('C.png'), (150, 100))

a = random.randint(500, 800)
b = random.randint(25, 325)
c = random.randint(970, 1350)

isJump = False
jumpCount = 10
right = False
left = True
num = 0
r = True
w = -10
number_of_ques = 1
num1 = 0
run = True
boo = False
clock = pygame.time.Clock()
start_ticks = 0


class Sprite:

    def __init__(self, x, y, name):
        self.x = x

        self.y = y

        self.image = pygame.transform.scale(pygame.image.load(name), (150, 100))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def render(self):
        screen.blit(self.image, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y
        # pygame.draw.rect(screen, (45, 45, 45), self.rect, 1)
        self.y += 3


letterA = Sprite(a, w, 'A.png')
letterB = Sprite(b, w, 'B.png')
letterC = Sprite(c, w, 'C.png')
bk = pygame.transform.scale(pygame.image.load('great.png'), (1536, 864))
x, y, width, height, speed = 50, 530, 250, 200, 10

d = {1: 'Особенности лексики научного стиля',
     2: 'К какому стилю относятся жанры: роман, повесть, рассказ?',
     3: 'Откуда, умная, бредешь ты, голова? (И.Крылов) Какой троп содержиться в тексте?',
     4: 'К какому стилю относятся жанры: диссертация, доклад, рецензия?',
     5: 'Цели разговорного стиля.',
     6: 'Перенос значения по сходству, например, осень жизни, шляпка гвоздя – это...',
     7: 'Эффект «присутствия», использование ярких деталей относятся к жанру …',
     8: 'Жанр публицистики без оценок автора и выводов',
     9: 'Каким средством выразительности является эпифора?',
     10: 'Основные жанры разговорного стиля',
     11: 'Ваш результат '}
ans = {1: 1, 2: 2, 3: 1, 4: 3, 5: 2, 6: 3, 7: 3, 8: 3, 9: 2, 10: 2}
q1 = {1: 'Абстрактная лексика', 2: 'Публицистический стиль', 3: 'Ирония',
      4: 'Жанры научного стиля', 5: 'Воздействовать на читателя и информировать его.', 6: 'гротеск',
      7: 'заметка', 8: 'роман', 9: 'Преувеличение',
      10: 'Спор, диалог, статья'}
q2 = {1: 'Образные средства', 2: 'Художественный стиль', 3: 'гротеск',
      4: 'Жанры публицистического стиля', 5: 'Обменяться сведениями, мыслями или поделиться чувствами с людьми.',
      6: 'аллегория',
      7: 'статья', 8: 'доклад', 9: 'Повторение слов или выражений в конце предложения',
      10: 'Диалог, история, беседа'}
q3 = {1: 'Призывность', 2: 'Научный стиль', 3: 'эпифора',
      4: 'Жанры официально-делового стиля', 5: 'Сообщить сведения, дать точные указания.', 6: 'метафора',
      7: 'репортаж', 8: 'отчет', 9: 'Повторение слов или выражений в начале предложения',
      10: 'Беседа, разговор, репортаж'}


class Boy:

    def __init__(self, x, y):
        self.x = x

        self.y = y
        if right:

            self.rect = walkRight[num // 3].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

        elif left:
            self.rect = walkleft[num // 3].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

        else:
            self.rect = stand[num1 // 3].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def render(self):
        global num, num1
        global walkleft, walkRight, stand

        if right:
            screen.blit(walkRight[num // 3], (x, y))
            # pygame.draw.rect(screen, (45, 45, 45), self.rect, 1)

            num += 1
        elif left:
            screen.blit(walkleft[num // 3], (x, y))
            # pygame.draw.rect(screen, (45, 45, 45), self.rect, 1)
            num += 1
        else:
            screen.blit(stand[num1 // 3], (x, y))
            # pygame.draw.rect(screen, (45, 45, 45), self.rect, 1)
            num1 += 1

        if num + 1 >= 30:
            num = 0
        if num1 + 1 >= 30:
            num1 = 0

    def chh(self, sprr):
        self.rect.colliderect(sprr)


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for j in range(0, self.height):
            for i in range(0, self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                                  self.cell_size), 1)


def sttext(n, xf, yf):
    font = pygame.font.Font('r.ttf', 32)
    text_coord = yf
    string_rendered = font.render(d[n], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = xf
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord = yf + 50
    string_rendered = font.render('A   ' + q1[n], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = xf
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord = yf + 100
    string_rendered = font.render('B   ' + q2[n], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = xf
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)

    text_coord = yf + 150
    string_rendered = font.render('C   ' + q3[n], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = xf
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)


check = False
score = 0

vb = 0

imp = True


def checking_coll():
    if (w >= y) and ((a - x) <= 294 or x - a <= 100):
        return 1
    elif (w >= y) and ((b - x) <= 294 or x - b <= 100):
        return 2
    elif (w >= y) and ((c - x) <= 294 or x - c <= 100):
        return 3


er = 0

board = Board(2, 5)


def scre():
    global r, number_of_ques, check
    global w, t, a, b, c, vb, er
    global num, score
    global num1, imp
    global start_ticks

    screen.blit(bk, (0, 0))
    boy = Boy(x, y)
    boy.render()
    if letterB.y < 500 and check is False and number_of_ques < 11:

        letterA.render()
        letterB.render()
        letterC.render()
        sttext(number_of_ques, 300, 50)
    elif letterB.y >= 500 and check is False and number_of_ques < 11:
        letterB.y = -10
        letterA.y = -10
        letterC.y = -10
        if number_of_ques < 11:
            number_of_ques += 1
        letterA.x = random.randint(500, 800)
        letterB.x = random.randint(25, 350)
        letterC.x = random.randint(950, 1350)
    if pygame.sprite.collide_rect(boy, letterA) == 1:
        vb = 1
        if ans[number_of_ques] == vb:
            score += 1
    elif pygame.sprite.collide_rect(boy, letterB) == 1:
        vb = 2
        if ans[number_of_ques] == vb:
            score += 1
    elif pygame.sprite.collide_rect(boy, letterC) == 1:
        vb = 3
        if ans[number_of_ques] == vb:
            score += 1
    if imp:
        er = score // 34

    if number_of_ques == 10:
        imp = False
        seconds = pygame.time.get_ticks() / 1000
        if seconds > 3:
            check = True
            font = pygame.font.Font('r.ttf', 40)
            text_coord = 400
            string_rendered = font.render(d[11] + str(er), 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = text_coord
            intro_rect.x = 50
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        t = True
    elif keys[pygame.K_RIGHT] and x < 1536 - width - 5:
        x += speed
        left = False
        right = True
        t = True
    else:
        right = False
        left = False
        num = 0
        num1 = 0
    if not (isJump):
        """if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < 864 - height - 15:
            y += speed"""
        if keys[pygame.K_SPACE]:
            isJump = True
            t = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    scre()
    board.render()

    pygame.display.update()

pygame.quit()
