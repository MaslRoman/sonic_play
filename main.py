import pygame
import sys
from pytmx.util_pygame import load_pygame#импортировали pytmx для работы с файлами tmx
pygame.init()  # инициализируем Pygame

pygame.mixer.music.load('music/sonic_music.mp3')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)
speed_1 = 1
speed_2 = 1

jump_logika=0

x_sonic = 0
y_sonic = 750
move_up =False#отввечает, нажат пробел или нет
lower_point=750
vertical_speed=-12#эта переменная отвечает за скорость двежения вверх или вниз
jump_power=-30#а сила прыжка отрицательная потому что чем меньше координата тем выше обьект
on_ground=True

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

button_play_rect = pygame.Rect(820, 650, 150, 90)  # шаг 1--создаю формы для кнопки (координаты и размеры)

text_surface = my_font.render('Play', True, (255, 165, 0))
text_rect_play = text_surface.get_rect(center=button_play_rect.center)

sonic_1 = pygame.image.load('move right/sonic1.png')
sonic_1 = pygame.transform.scale(sonic_1, (30, 45))
#превратили картинку в прямоугольниг(rect) что бы потом настроить колизию с другиими обьектами
sonic_rect=sonic_1.get_rect()
print(sonic_rect)



sonic_2 = pygame.image.load('move right/sonic2.png')
sonic_2 = pygame.transform.scale(sonic_2, (30, 45))

sonic_3 = pygame.image.load('move right/sonic3.png')
sonic_3 = pygame.transform.scale(sonic_3, (30, 45))

sonic_4 = pygame.image.load('move right/sonic4.png')
sonic_4 = pygame.transform.scale(sonic_4, (30, 45))

sonic_5 = pygame.image.load('move right/sonic5.png')
sonic_5 = pygame.transform.scale(sonic_5, (30, 45))

sonic_6 = pygame.image.load('move right/sonic6.png')
sonic_6 = pygame.transform.scale(sonic_6, (30, 45))

sonic_7 = pygame.image.load('move right/sonic7.png')
sonic_7 = pygame.transform.scale(sonic_7, (30, 45 ))

tmx_data = load_pygame("tiels/level_1_sonic.tmx")#загрузили карту с помощью load_pygame

time_1 = pygame.time.get_ticks() + 5000


sonic_costume=[sonic_1, sonic_2, sonic_3, sonic_4, sonic_5, sonic_6, sonic_7]
costume_number=0
index_costume=sonic_costume[costume_number]


direction = "right"
move_left = False
move_right = False
running = True
while running:#итерация это-одно выполнение тела цикла
    #print(logika)
    time_2 = pygame.time.get_ticks()
    if time_2 >= time_1:
        time_1 = pygame.time.get_ticks() + 5000
        print('прошло 5 секунд')

    # первый уровень-    игровой цикл
    for events in pygame.event.get():
        #print(events)
        # второй уровень-    цикл спроверки соббытий (проверка нажатии мышки или клавиатуры)
        if events.type == pygame.QUIT:
            running = False  # выключаем функцыю



        if events.type == pygame.MOUSEBUTTONDOWN:
            x = events.pos[0]
            y = events.pos[1]
            #метод collidepoint определяет нажатие по обьекту rect используя координаты мыши
            if button_play_rect.collidepoint(events.pos):#
                logika = 1


            if x >= 520 and x <= 700 and y >= 650 and y <= 740:
                running = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_d:#условие сработает если нажата клавиша d
                move_right = True
                direction = "right"#указываем направление что бы правельно менять костюмы персонажа

            if events.key == pygame.K_a:
                move_left = True
                direction = "left"

            if events.key == pygame.K_SPACE:
                move_up = True
                direction = "up"




        if events.type == pygame.KEYUP:
            if events.key == pygame.K_d:
                move_right = False

            if events.key == pygame.K_a:
                move_left = False

            if events.key == pygame.K_SPACE:
                move_up = False

        if move_right or move_left:
            costume_number+=1
        if costume_number>=7:
            costume_number=0

    keys=pygame.key.get_pressed()
    move_right=keys[pygame.K_d]
    move_left=keys[pygame.K_a]
    move_up=keys[pygame.K_SPACE]

    if move_right and not move_left:
        direction="right"
    if move_left and not move_right:
        direction="left"





    if move_left==True:
        speed_1+=0.05
    if move_left==False:
        speed_1=0

    if move_right==True:
        speed_2+=0.05
    if move_right==False:
        speed_2=0


    if move_left and x_sonic>0:
        x_sonic -= speed_1

    if move_right and x_sonic<1520:
        x_sonic += speed_2



    if y_sonic>=lower_point:#проверка нахождения соника внизу и изменение значений
        y_sonic=lower_point
        on_ground=True
        vertical_speed=-12
    else:
        on_ground=False

    if move_up==True and on_ground==True:#если пробел нажат то тогда происходит начало прыжка
        on_ground=False
        y_sonic+=vertical_speed
        vertical_speed+=1
        jump_logika=1

    if on_ground==False:#если соник в воздухе то тогда поднимает вверх а потом со временем его начинает опускать
        if jump_logika==1:
            y_sonic+=vertical_speed
            vertical_speed+=1
        if on_ground==True:
            jump_logika=0
    on_ground=True


    print(y_sonic)


    if logika == 0:





        screen.blit(image_1, (0, 0))

        pygame.draw.ellipse(screen, (135, 206, 250),
                            button_play_rect)  # шаг 1--отобразили объект и установили характиристики

        pygame.draw.ellipse(screen, (135, 206, 250), button_exit)

        screen.blit(text_surface, text_rect_play)

        screen.blit(text_exit, text_rect_exit)
    elif logika == 1:

        # Получаем размеры тайлов и сохраняем их в отдельные переменные
        tile_width = tmx_data.tilewidth  # Ширина одного тайла (например, 32 пикселя)
        tile_height = tmx_data.tileheight  # Высота одного тайла (например, 32 пикселя)

        # Проходимся по всем видимым слоям ТМХ карты
        for layer in tmx_data.visible_layers:
            if hasattr(layer, 'data'):  # Проверяем, что слой содержит данные (т.е. это тайловый слой)
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)  # Получаем изображение тайла по его идентификатору
                    if tile:
                        # Вычисляем координаты для отрисовки тайла в пикселях, используя заранее сохранённые размеры
                        pixel_x = x * tile_width  # х-координата в пикселях
                        pixel_y = y * tile_height  # у-координата в пикселях
                        screen.blit(tile, (pixel_x, pixel_y))  # Отрисовываем тайл на экране
            if hasattr(layer, 'objects'):
                print(f"Найден слой объектов: '{layer.name}'")











        if direction == "right":
            screen.blit(sonic_costume[costume_number], (x_sonic, y_sonic))

        elif direction == "left":
        #метод transform.flip отображает обьект в зависемости от настроек(по вертикале или по горизонтали)
            flipped_sonic = pygame.transform.flip(sonic_costume[costume_number], True, False)
            screen.blit(flipped_sonic, (x_sonic, y_sonic))
            print(y_sonic)

    pygame.display.flip()  # обнавляем экран FPS

    pygame.time.Clock().tick(60)

pygame.quit()  # завершение работы Pygame
sys.exit()