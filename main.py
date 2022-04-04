import os
import ctypes

from agent import *
from ramy_czyli_wiedza_agenta import *
from bfs import *

#aby działalo w oknie + rozdzielczość ekranu
#ctypes.windll.shcore.SetProcessDpiAwareness(1)

Okno = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")
Krata = Krata(Okno)
Pomieszczenie=Pomieszczenie(0,0)

def dodaj_agenta():
    # pole_lewe_gorne = PoleKraty(Krata, random.randint(0, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH),
    # random.randint(0, LICZBA_POL_W_POZIOMIE - BOK_AGENTA1_W_POLACH))
    pole_lewe_gorne = PoleKraty(Krata, LICZBA_POL_W_PIONIE-BOK_AGENTA1_W_POLACH, int(LICZBA_POL_W_POZIOMIE/2))
    pom = 'traktor_ikona.png'
    ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                   (BOK_AGENTA1, BOK_AGENTA1))
    Agent(Krata, pole_lewe_gorne, ikona)

def dodaj_szafke(numerSzafki, iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_kolumna, poczatek_wiersz1):
    wymiary_szafki = Wymiary(0, 0, 0)
    szafka = Szafka(numerSzafki,wymiary_szafki, iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_kolumna, poczatek_wiersz1, Krata)
    Pomieszczenie.dodajSzafke(szafka)

def main():
    dodaj_szafke("A", 2, 7, "P", 0, 0)
    dodaj_szafke("B", 2, 7, "L", 0, 3)
    dodaj_szafke("C", 2, 7, "P", 0, 4)
    dodaj_szafke("D", 2, 7, "L", 0, 7)
    dodaj_szafke("E", 2, 7, "P", 0, 8)
    dodaj_szafke("F", 2, 7, "L", 0, 11)
    dodaj_szafke("G", 2, 7, "P", 0, 12)
    dodaj_szafke("H", 2, 7, "L", 0, 15)
    dodaj_szafke("I", 2, 7, "P", 0, 16)
    dodaj_szafke("J", 2, 7, "L", 0, 19)
    dodaj_agenta()
    # cel to pole kraty gdzie ma stać agent, aby położyć paczkę na półkę, w obiekcie klasy Miejsce jest to artybut dostęp
    cel = PoleKraty(Krata, 1, 14)
    # start to pole startowe agenta, == pole_lewe_gorne
    start = PoleKraty(Krata, LICZBA_POL_W_PIONIE-BOK_AGENTA1_W_POLACH, int(LICZBA_POL_W_POZIOMIE/2))
    bfsList = bfs(Krata, start, cel)

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
