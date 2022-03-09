import os
import random
from enum import Enum

import pygame


class KIERUNEK(Enum):
    GORA = 0
    DOL = 1
    LEWO = 2
    PRAWO = 3


FPS = 120

SZEROKOSC_OKNA = 1280
WYSOKOSC_OKNA = 960

BOK_AGENTA1 = 100

BIALY = (255, 255, 255)
JASNOSZARY1 = (180, 180, 180)
ZIELONY1 = (26, 122, 26)

OKNO = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")

TEST1_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'test1_ikona.png')), (500, 500))
TRAKTOR_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'traktor_ikona.png')), (100, 100))
wozek_ikona = pygame.image.load(os.path.join('Ikony', 'wozek.png'))
wozek_ze_skrzynka_ikona = pygame.image.load(os.path.join('Ikony', 'wozek_ze_skrzynka.png'))
agent1 = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'wozek_ze_skrzynka.png')),
                                (BOK_AGENTA1, BOK_AGENTA1))
Agenci = []
HitboxyAgentow = []
DrogiAgentow = []
KierunkiAgentow = []


def wyswietl_okno():
    OKNO.fill(ZIELONY1)
    KROK_WOZKA = 2
    for a in range(len(Agenci)):
        OKNO.blit(Agenci[a], (HitboxyAgentow[a].x, HitboxyAgentow[a].y))
        if DrogiAgentow[a] == 0:
            KierunkiAgentow[a] = KIERUNEK(random.randint(0, 3))
            losowa_droga = None
            if KierunkiAgentow[a] == KIERUNEK.GORA:
                losowa_droga = random.randint(0, HitboxyAgentow[a].y)
            elif KierunkiAgentow[a] == KIERUNEK.DOL:
                losowa_droga = random.randint(0, WYSOKOSC_OKNA - HitboxyAgentow[a].y)
            elif KierunkiAgentow[a] == KIERUNEK.LEWO:
                losowa_droga = random.randint(0, HitboxyAgentow[a].x)
            elif KierunkiAgentow[a] == KIERUNEK.PRAWO:
                losowa_droga = random.randint(0, SZEROKOSC_OKNA - HitboxyAgentow[a].x)
            DrogiAgentow[a] = losowa_droga - losowa_droga % KROK_WOZKA
        if KierunkiAgentow[a] == KIERUNEK.GORA:
            if HitboxyAgentow[a].y - KROK_WOZKA > 0:
                HitboxyAgentow[a].y -= KROK_WOZKA
                DrogiAgentow[a] -= KROK_WOZKA
            else:
                DrogiAgentow[a] = 0
        elif KierunkiAgentow[a] == KIERUNEK.DOL:
            if HitboxyAgentow[a].y + KROK_WOZKA < WYSOKOSC_OKNA - HitboxyAgentow[a].height:
                HitboxyAgentow[a].y += KROK_WOZKA
                DrogiAgentow[a] -= KROK_WOZKA
            else:
                DrogiAgentow[a] = 0
        elif KierunkiAgentow[a] == KIERUNEK.LEWO:
            if HitboxyAgentow[a].x - KROK_WOZKA > 0:
                HitboxyAgentow[a].x -= KROK_WOZKA
                DrogiAgentow[a] -= KROK_WOZKA
            else:
                DrogiAgentow[a] = 0
        elif KierunkiAgentow[a] == KIERUNEK.PRAWO:
            if HitboxyAgentow[a].x + KROK_WOZKA < SZEROKOSC_OKNA - HitboxyAgentow[a].width:
                HitboxyAgentow[a].x += KROK_WOZKA
                DrogiAgentow[a] -= KROK_WOZKA
            else:
                DrogiAgentow[a] = 0
    pygame.display.update()


def main():
    klatkaz = pygame.time.Clock()
    warunek_dzialania = True
    while warunek_dzialania:
        klatkaz.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                warunek_dzialania = False
                break

        wyswietl_okno()
        los = random.randint(1, 240)
        if len(Agenci) < 50:
            pom = None
            if los in (1, 2) or len(Agenci) == 0:
                pom = 'wozek.png'
            elif los in (2, 3):
                pom = 'wozek_ze_skrzynka.png'
            elif los == 4 and len(Agenci) > 6:
                pom = 'traktor_ikona.png'
            if pom != None:
                Agenci.append(pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                                     (BOK_AGENTA1, BOK_AGENTA1)))
                HitboxyAgentow.append(pygame.Rect(random.randint(0, SZEROKOSC_OKNA - BOK_AGENTA1),
                                                  random.randint(0, WYSOKOSC_OKNA - BOK_AGENTA1), BOK_AGENTA1,
                                                  BOK_AGENTA1))
                DrogiAgentow.append(0)
                KierunkiAgentow.append(KIERUNEK.GORA)

    pygame.quit()


main()
