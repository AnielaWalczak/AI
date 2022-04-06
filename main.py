import os

from agent import *
from ramy_czyli_wiedza_agenta import *

# aby działalo w oknie + rozdzielczość ekranu
# ctypes.windll.shcore.SetProcessDpiAwareness(1)

Okno = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")
Krata = Krata(Okno)
Pomieszczenie = Pomieszczenie(WarunkiPowietrza(0, 0), 0)


def dodaj_agenta():
    # pole_lewe_gorne = PoleKraty(Krata, random.randint(0, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH),
    # random.randint(0, LICZBA_POL_W_POZIOMIE - BOK_AGENTA1_W_POLACH))
    # pole_lewe_gorne = PoleKraty(Krata, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH, int(LICZBA_POL_W_POZIOMIE / 2))
    pole_lewe_gorne = PoleKraty(Krata, 0, 0)
    pom = 'traktor_ikona.png'
    ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                   (BOK_AGENTA1, BOK_AGENTA1))
    Agent(Krata, pole_lewe_gorne, ikona)
    # zawsze na poczatku polnoc
    Krata.agent.kierunek = Kierunek.POLNOC


def dodaj_szafke(numerSzafki, iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_wiersz, poczatek_kolumna):
    wymiary_szafki = Wymiary(0, 0, 0)
    szafka = Szafka(numerSzafki, wymiary_szafki, iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_wiersz,
                    poczatek_kolumna, Krata)
    Pomieszczenie.dodajSzafke(szafka)


def losowy_cel():
    kierunek = Kierunek(random.randint(0, 3))
    wiersz = random.randint(-1, Krata.liczbaPolPionowo - 1)
    kolumna = random.randint(-1, Krata.liczbaPolPoziomo - 1)
    Krata.krata[wiersz][kolumna] = ZawartoscPola.CEL
    return Stan(kierunek, PoleKraty(Krata, wiersz, kolumna))


def main():
    dodaj_szafke("A", 2, 12, "P", 2, 2)
    dodaj_szafke("B", 2, 12, "L", 2, 3)
    dodaj_szafke("C", 2, 5, "P", 1, 6)
    dodaj_szafke("D", 2, 6, "L", 1, 7)
    dodaj_szafke("C", 2, 4, "P", 9, 6)
    dodaj_szafke("D", 2, 3, "L", 10, 7)
    dodaj_szafke("E", 2, 8, "P", 3, 11)
    dodaj_szafke("F", 2, 10, "L", 2, 13)
    dodaj_szafke("H", 2, 12, "L", 1, 18)
    dodaj_szafke("I", 2, 7, "P", 5, 23)
    dodaj_szafke("J", 2, 12, "L", 1, 25)
    dodaj_szafke("G", 2, 10, "P", 5, 29)

    dodaj_agenta()

    # Krata.wyswietlKrate()

    klatkaz = pygame.time.Clock()
    warunek_dzialania = True
    while warunek_dzialania:
        klatkaz.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                warunek_dzialania = False
                break

        # cel to Stan (pole kraty gdzie ma stać agent, aby położyć paczkę na półkę, w obiekcie klasy Miejsce jest to artybut dostęp + kierunek <-na razie niepotrzebny)
        if Krata.agent.cel is None:
            Krata.agent.cel = losowy_cel()
            Krata.krata[Krata.agent.cel.poleStartoweGorne.wiersz][
                Krata.agent.cel.poleStartoweGorne.kolumna] = ZawartoscPola.CEL
            print("CEL:", Krata.agent.cel.poleStartoweGorne.wiersz, Krata.agent.cel.poleStartoweGorne.kolumna)
            Krata.agent.idzDoCelu(klatkaz)

    pygame.quit()


main()
