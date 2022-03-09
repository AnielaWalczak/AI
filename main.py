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
            a.okreslDlugoscDrogi()
        a.ruszSie(Agenci1)
    pygame.display.update()


def dodaj_agenta1():
    los = None
    if len(Agenci1) in range(0, 40):
        los = random.randint(1, 150)
    elif len(Agenci1) in range(40, 50):
        los = random.randint(1, 15)
    if los != None:
        pom = None
        if los in (1, 2) or len(Agenci1) == 0:
            pom = 'wozek.png'
        elif los in (3, 4):
            pom = 'wozek_ze_skrzynka.png'
        elif los == 5 and len(Agenci1) > 6:
            pom = 'traktor_ikona.png'
        if pom != None:
            x, y = random.randint(0, SZEROKOSC_OKNA - BOK_AGENTA1), random.randint(0, WYSOKOSC_OKNA - BOK_AGENTA1)
            hitbox = pygame.Rect(x, y, BOK_AGENTA1, BOK_AGENTA1)
            warunek = True
            for a in Agenci1:
                if a.hitbox.colliderect(hitbox):
                    warunek = False
                    break
            if warunek:
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
