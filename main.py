import os

import pygame

from agenci import *
from stale import *

OKNO = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")

Agenci1 = []


def wyswietl_okno():
    OKNO.fill(JASNOSZARY1)
    for a in Agenci1:
        OKNO.blit(a.tekstura, (a.hitbox.x, a.hitbox.y))
        if a.droga == 0:
            a.obierzNowyKierunek()
        a.ruszSie()
    pygame.display.update()


def dodaj_agenta1():
    los = random.randint(1, 240)
    if len(Agenci1) < 50:
        pom = None
        if los in (1, 2) or len(Agenci1) == 0:
            pom = 'wozek.png'
        elif los in (2, 3):
            pom = 'wozek_ze_skrzynka.png'
        elif los == 4 and len(Agenci1) > 6:
            pom = 'traktor_ikona.png'
        if pom != None:
            hitbox = pygame.Rect(random.randint(0, SZEROKOSC_OKNA - BOK_AGENTA1),
                                 random.randint(0, WYSOKOSC_OKNA - BOK_AGENTA1), BOK_AGENTA1,
                                 BOK_AGENTA1)
            ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                           (BOK_AGENTA1, BOK_AGENTA1))
            Agenci1.append(Agent1(hitbox, ikona, KIERUNEK.GORA, 0))


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
        dodaj_agenta1()

    pygame.quit()


main()
pygame.quit()
