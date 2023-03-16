
import pygame

pygame.init()

# Установка размера экрана



screen_width = 1200
screen_height = 1400
screen = pygame.display.set_mode((screen_width, screen_height))
# Задаем цвет заливки
bg_color = (255, 0, 0)  # красный

# Заполняем экран цветом заливки
screen.fill(bg_color)
# Загрузка картинки
image_path = "images/Minotaur_02_Idle_000.png"
image = pygame.image.load(image_path).convert()

# Создание спрайта из картинки
sprite = pygame.sprite.Sprite()
sprite.image = image
sprite.rect = sprite.image.get_rect()
sprite.rect.center = (screen_width // 2, screen_height // 2)

# Создание группы спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite)

# Флаг для отслеживания зажатой клавиши S
moving_down = False
#vm
moving_up = False

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_up = True
            elif event.key == pygame.K_d:
                moving_down = True  # запуск движения вниз
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_down = False  # остановка движения вниз
            if event.key == pygame.K_d:
                moving_up = False  # остановка движения вниз
    
    
    # Перемещение спрайта при зажатой клавише S
    if moving_down:
        sprite.rect.x += 1  # движение вниз

    if moving_up:
        sprite.rect.x -= 1  # движение вниз
    
    # Очистка экрана
    screen.fill((255, 255, 255))
    
    # Рисование спрайтов
    all_sprites.draw(screen)
    
    # Обновление экрана
    pygame.display.update()
