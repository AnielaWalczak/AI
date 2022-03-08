import os
import random

import pygame

FPS = 60

SZEROKOSC_OKNA = 1280
WYSOKOSC_OKNA = 960

BOK_AGENTA1 = 100

BIALY = (255, 255, 255)
JASNOSZARY1 = (180, 180, 180)

OKNO = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")

TEST1_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'test1_ikona.png')), (500, 500))
TRAKTOR_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'traktor_ikona.png')), (100, 100))
wozek_ikona = pygame.image.load(os.path.join('Ikony', 'wozek.png'))
wozek_ze_skrzynka_ikona = pygame.image.load(os.path.join('Ikony', 'wozek_ze_skrzynka.png'))
agent1 = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'wozek_ze_skrzynka.png')),
                                (BOK_AGENTA1, BOK_AGENTA1))


def wyswietl_okno(agent1_hitbox):
    OKNO.fill(BIALY)
    OKNO.blit(agent1, (agent1_hitbox.x, agent1_hitbox.y))
    os = random.randint(0, 1)
    odleglosc = random.randint(20, 120)
    znak = random.randint(0, 1)
    if znak == 1:
        odleglosc = 0 - odleglosc
    if os == 0:
        if agent1_hitbox.x + odleglosc < SZEROKOSC_OKNA - agent1_hitbox.width and agent1_hitbox.x + odleglosc > 0:
            agent1_hitbox.x += odleglosc
    else:
        if agent1_hitbox.y + odleglosc < WYSOKOSC_OKNA - agent1_hitbox.height and agent1_hitbox.y + odleglosc > 0:
            agent1_hitbox.y += odleglosc
    pygame.display.update()


def main():
    klatkaz = pygame.time.Clock()
    agent1_hitbox = pygame.Rect(SZEROKOSC_OKNA / 2 - BOK_AGENTA1 / 2,
                                WYSOKOSC_OKNA / 2 - BOK_AGENTA1 / 2, BOK_AGENTA1,
                                BOK_AGENTA1)
    warunek_dzialania = True
    while warunek_dzialania:
        klatkaz.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                warunek_dzialania = False
                break

        wyswietl_okno(agent1_hitbox)
        print(agent1_hitbox.x, agent1_hitbox.y)
        # wyswietl_agenta1(agent1_hitbox)

    pygame.quit()


main()
