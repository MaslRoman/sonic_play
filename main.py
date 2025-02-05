import pygame
import sys
from pytmx.util_pygame import load_pygame#импортировали pytmx для работы с файлами tmx
pygame.init()  # инициализируем Pygame

pygame.mixer.music.load('music/sonic_music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


logika = 0
screen_width = 1550  # задаем размеры окна
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('window')  # даем окну название

blue = (0, 0, 255)  # задали переменной blue синий цвет
my_font = pygame.font.SysFont('timesnewroman', 40, bold=True, italic=False)  # шаг 1--создали обьект шрифта

# available_fonts=pygame.font.get_fonts()
# available_fonts.sort()
# print('доступные шрифты:')

image_1 = pygame.image.load('picture/sonic_image.png')
image_1 = pygame.transform.scale(image_1, (1550, 920))

button_exit = pygame.Rect(520, 650, 150, 90)

text_exit = my_font.render(('Exit'), False, (255, 165, 0))
text_rect_exit = text_exit.get_rect(center=button_exit.center)

button_rect = pygame.Rect(820, 650, 150, 90)  # шаг 1--создаю формы для кнопки (координаты и размеры)

text_surface = my_font.render('Play', True, (255, 165, 0))
text_rect_play = text_surface.get_rect(center=button_rect.center)

sonic_1 = pygame.image.load('move right/sonic1.png')
sonic_1 = pygame.transform.scale(sonic_1, (75, 100))

sonic_2 = pygame.image.load('move right/sonic2.png')
sonic_2 = pygame.transform.scale(sonic_2, (75, 100))

sonic_3 = pygame.image.load('move right/sonic3.png')
sonic_3 = pygame.transform.scale(sonic_3, (75, 100))

sonic_4 = pygame.image.load('move right/sonic4.png')
sonic_4 = pygame.transform.scale(sonic_4, (75, 100))

sonic_5 = pygame.image.load('move right/sonic5.png')
sonic_5 = pygame.transform.scale(sonic_5, (75, 100))

sonic_6 = pygame.image.load('move right/sonic6.png')
sonic_6 = pygame.transform.scale(sonic_6, (75, 100))

sonic_7 = pygame.image.load('move right/sonic7.png')
sonic_7 = pygame.transform.scale(sonic_7, (75, 100))

tmx_data = load_pygame("tiels/level_1_sonic.tmx")#загрузили карту

time_1 = pygame.time.get_ticks() + 5000

x_sonic = 0
y_sonic = 0

sonic_costume=[sonic_1, sonic_2, sonic_3, sonic_4, sonic_5, sonic_6, sonic_7]
costume_number=0
index_costume=sonic_costume[costume_number]


direction = "right"
move_left = False
move_right = False
running = True
while running:
    time_2 = pygame.time.get_ticks()
    if time_2 >= time_1:
        time_1 = pygame.time.get_ticks() + 5000
        print('прошло 5 секунд')

    # первый уровень-    игровой цикл
    for events in pygame.event.get():
        print(events)
        # второй уровень-    цикл спроверки соббытий (проверка нажатии мышки или клавиатуры)
        if events.type == pygame.QUIT:
            running = False  # выключаем функцыю



        if events.type == pygame.MOUSEBUTTONDOWN:
            # print(events.pos)
            x = events.pos[0]
            y = events.pos[1]
            if x >= 820 and x <= 970 and y >= 650 and y <= 740:
                logika = 1

            if x >= 520 and x <= 700 and y >= 650 and y <= 740:
                running = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_d:
                move_right = True
                direction = "right"
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_d:
                move_right = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_a:
                move_left = True
                direction = "left"
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_a:
                move_left = False

        if move_right or move_left:
            costume_number+=1
        if costume_number>=7:
            costume_number=0

    keys=pygame.key.get_pressed()
    move_right=keys[pygame.K_d]
    move_left=keys[pygame.K_a]

    if move_right and not move_left:
        direction="right"
    if move_left and not move_right:
        direction="left"


    if move_left:
        x_sonic -= 1

    if move_right:
        x_sonic += 1

    if logika == 0:





        screen.blit(image_1, (0, 0))

        pygame.draw.ellipse(screen, (135, 206, 250),
                            button_rect)  # шаг 1--отобразили объект и установили характиристики

        pygame.draw.ellipse(screen, (135, 206, 250), button_exit)

        screen.blit(text_surface, text_rect_play)

        screen.blit(text_exit, text_rect_exit)
    elif logika == 1:


        screen.fill(blue)  # делаем экран синего цвета

        if direction == "right":
            screen.blit(sonic_costume[costume_number], (x_sonic, y_sonic))

        elif direction == "left":
        #метод transform.flip отображает обьект в зависемости от настроек(по вертикале или по горизонтали)
            flipped_sonic = pygame.transform.flip(sonic_costume[costume_number], True, False)
            screen.blit(flipped_sonic, (x_sonic, y_sonic))


    pygame.display.flip()  # обнавляем экран FPS

    pygame.time.Clock().tick(60)

pygame.quit()  # завершение работы Pygame
sys.exit()