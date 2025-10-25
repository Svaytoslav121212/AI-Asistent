from PIL import ImageGrab
import ctypes
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:#нужнонажать на пробел, чтобы сделать скриншот
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot.png")
        print('Готово!')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
