
import pygame
import os 

# инициализация Pygame
pygame.init()

# установка частоты кадров
FPS = 60
fps_clock = pygame.time.Clock()

# установка размера окна
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 700
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# загрузка спрайта игрока
player_image = pygame.image.load("/Users/programmer/Documents/CODER/StreetFighter/images/minotaur_02_idle_000.png")
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.bottom = WINDOW_HEIGHT - 10

os.chdir('/Users/programmer/Documents/CODER/StreetFighter/')
# скорость игрока
player_speed = 5

# основной игровой цикл
while True:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_d]:
        player_rect.move_ip(player_speed, 0)

    # отрисовка игровых объектов
    window_surface.fill((255, 255, 255))
    window_surface.blit(player_image, player_rect)

    # обновление экрана
    pygame.display.update()

    # задержка до следующего кадра
    fps_clock.tick(FPS)
