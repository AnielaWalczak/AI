import os
import random

import pygame

FPS = 10

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
lista_agentow = []
lista_hitboxow_agentow = []


def wyswietl_okno():
    OKNO.fill(JASNOSZARY1)
    for a in range(len(lista_agentow)):
        OKNO.blit(lista_agentow[a], (lista_hitboxow_agentow[a].x, lista_hitboxow_agentow[a].y))
        os = random.randint(0, 1)
        odleglosc = random.randint(20, 100)
        znak = random.randint(0, 1)
        if znak == 1:
            odleglosc = 0 - odleglosc
        if os == 0:
            if lista_hitboxow_agentow[a].x + odleglosc < SZEROKOSC_OKNA - lista_hitboxow_agentow[a].width and \
                    lista_hitboxow_agentow[a].x + odleglosc > 0:
                lista_hitboxow_agentow[a].x += odleglosc
        else:
            if lista_hitboxow_agentow[a].y + odleglosc < WYSOKOSC_OKNA - lista_hitboxow_agentow[a].height and \
                    lista_hitboxow_agentow[a].y + odleglosc > 0:
                lista_hitboxow_agentow[a].y += odleglosc
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

        wyswietl_okno()
        print(agent1_hitbox.x, agent1_hitbox.y)
        # wyswietl_agenta1(agent1_hitbox)
        los = random.randint(1, 30)
        if len(lista_agentow) < 20:
            pom = None
            if los == 1:
                pom = 'wozek_ze_skrzynka.png'
            elif los == 2:
                pom = 'wozek.png'
            elif los == 3 and len(lista_agentow) > 6:
                pom = 'traktor_ikona.png'
            if pom != None:
                lista_agentow.append(pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                                            (BOK_AGENTA1, BOK_AGENTA1)))
                lista_hitboxow_agentow.append(pygame.Rect(random.randint(0, SZEROKOSC_OKNA - BOK_AGENTA1),
                                                          random.randint(0, WYSOKOSC_OKNA - BOK_AGENTA1), BOK_AGENTA1,
                                                          BOK_AGENTA1))

    pygame.quit()


main()
