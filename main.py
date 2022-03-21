import os

from agenci import *

Okno = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")
Krata = Krata(Okno)


def dodaj_agenta():
    pole_lewe_gorne = PoleKraty(Krata, random.randint(0, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH),
                                random.randint(0, LICZBA_POL_W_POZIOMIE - BOK_AGENTA1_W_POLACH))
    pom = 'test1_ikona.png'
    ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                   (BOK_AGENTA1, BOK_AGENTA1))
    nowy_agent = Agent(Krata, pole_lewe_gorne, ikona, Kierunek.GORA, 0)


def main():
    klatkaz = pygame.time.Clock()
    warunek_dzialania = True
    while warunek_dzialania:
        klatkaz.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                warunek_dzialania = False
                break
        Krata.wyswietlKrate()
        dodaj_agenta()
        Krata.wyswietlAgenta()
    pygame.quit()


main()
