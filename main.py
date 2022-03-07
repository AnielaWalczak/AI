import os

import pygame

FPS = 60
SZEROKOSC_OKNA = 800
WYSOKOSC_OKNA = 600
BIALY = (255, 255, 255)

OKNO = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")

TEST1_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'test1_ikona.png')), (500, 500))
TRAKTOR_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'traktor_ikona.png')), (100, 100))


def wyswietl_okno():
    OKNO.fill((150, 200, 150))
    OKNO.blit(TEST1_IKONA,
              (SZEROKOSC_OKNA / 2 - TEST1_IKONA.get_width() / 2, WYSOKOSC_OKNA / 2 - TEST1_IKONA.get_height() / 2))
    OKNO.blit(TRAKTOR_IKONA, (0, 0))
    OKNO.blit(TRAKTOR_IKONA, (SZEROKOSC_OKNA - TRAKTOR_IKONA.get_width(), 0))
    OKNO.blit(TRAKTOR_IKONA, (SZEROKOSC_OKNA - TRAKTOR_IKONA.get_width(), WYSOKOSC_OKNA - TRAKTOR_IKONA.get_height()))
    OKNO.blit(TRAKTOR_IKONA, (0, WYSOKOSC_OKNA - TRAKTOR_IKONA.get_height()))
    pygame.display.update()


klatkaz = pygame.time.Clock()
warunek_dzialania = True
while warunek_dzialania:
    klatkaz.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            warunek_dzialania = False
            break

    wyswietl_okno()

pygame.quit()
