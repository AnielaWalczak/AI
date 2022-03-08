import math
import os
import random

import pygame

FPS = 1

SZEROKOSC_OKNA = 1280
WYSOKOSC_OKNA = 960

LICZBA_POL_W_POZIOMIE = 8
LICZBA_POL_W_PIONIE = 6

Krata = []
for rzad in range(LICZBA_POL_W_PIONIE):
    Krata.append([])
    for kolumna in range(LICZBA_POL_W_POZIOMIE):
        Krata[rzad].append(random.randint(0, 9))

bok_pola = min(int(SZEROKOSC_OKNA / LICZBA_POL_W_POZIOMIE), int(WYSOKOSC_OKNA / LICZBA_POL_W_PIONIE))
odstep_miedzy_polami = max(1, math.floor(0.0625 * bok_pola))
bok_pola -= odstep_miedzy_polami

BIALY = (255, 255, 255)
JASNOSZARY1 = (180, 180, 180)

OKNO = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")

TEST1_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'test1_ikona.png')), (500, 500))
TRAKTOR_IKONA = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'traktor_ikona.png')), (100, 100))
wozek_ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'wozek.png')),
                                     (bok_pola - odstep_miedzy_polami, bok_pola - odstep_miedzy_polami))
wozek_ze_skrzynka_ikona = pygame.image.load(os.path.join('Ikony', 'wozek_ze_skrzynka.png'))


def wyswietl_okno():
    OKNO.fill(JASNOSZARY1)

    for rzad in range(LICZBA_POL_W_PIONIE):
        for kolumna in range(LICZBA_POL_W_POZIOMIE):
            pygame.draw.rect(OKNO, BIALY, [(odstep_miedzy_polami + bok_pola) * kolumna + odstep_miedzy_polami,
                                           (odstep_miedzy_polami + bok_pola) * rzad + odstep_miedzy_polami,
                                           bok_pola, bok_pola])
    pygame.display.update()


def wyswietl_wozek():
    for rzad in range(LICZBA_POL_W_PIONIE):
        for kolumna in range(LICZBA_POL_W_POZIOMIE):
            pom = Krata[rzad][kolumna]
            if pom == 0:
                pom = wozek_ikona
            elif pom == 1:
                pom = wozek_ze_skrzynka_ikona
            elif pom == 2:
                pom = TRAKTOR_IKONA
            else:
                pom = None
            if pom != None:
                pom = pygame.transform.scale(pom, (bok_pola - odstep_miedzy_polami, bok_pola - odstep_miedzy_polami))
                OKNO.blit(pom, (((
                                             odstep_miedzy_polami + bok_pola) * kolumna + odstep_miedzy_polami) + bok_pola / 2 - pom.get_width() / 2,
                                ((
                                             odstep_miedzy_polami + bok_pola) * rzad + odstep_miedzy_polami) + bok_pola / 2 - pom.get_height() / 2))
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
    wyswietl_wozek()

    pom = Krata[LICZBA_POL_W_PIONIE - 1][LICZBA_POL_W_POZIOMIE - 1]
    for rzad in range(LICZBA_POL_W_PIONIE - 1, -1, -1):
        for kolumna in range(LICZBA_POL_W_POZIOMIE - 1, 0, -1):
            Krata[rzad][kolumna] = Krata[rzad][(kolumna - 1)]
        Krata[rzad][0] = Krata[rzad - 1][LICZBA_POL_W_POZIOMIE - 1]
    Krata[0][0] = pom
    print(Krata)

pygame.quit()
