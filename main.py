import os

from agent import *

Okno = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")
Krata = Krata(Okno)


def dodaj_agenta():
    # pole_lewe_gorne = PoleKraty(Krata, random.randint(0, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH),
    # random.randint(0, LICZBA_POL_W_POZIOMIE - BOK_AGENTA1_W_POLACH))
    pole_lewe_gorne = PoleKraty(Krata, 1, 1)
    pom = 'traktor_ikona.png'
    ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                   (BOK_AGENTA1, BOK_AGENTA1))
    Agent(Krata, pole_lewe_gorne, ikona)


def main():
    dodaj_agenta()
    klatkaz = pygame.time.Clock()
    warunek_dzialania = True
    while warunek_dzialania:
        klatkaz.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                warunek_dzialania = False
                break
        Krata.wyswietlKrate()
    pygame.quit()


main()
