import ctypes
import os
import threading

import pygame.transform

from agent import *
from okno import *
from ramy_czyli_wiedza_agenta import *
from rescue import *
from neural_network import *
# aby działalo w oknie + rozdzielczość ekranu
# ctypes.windll.shcore.SetProcessDpiAwareness(1)

okno_pygame = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")
krata_magazynu = Krata(okno_pygame)
Pomieszczenie = Pomieszczenie(WarunkiPowietrza(0, 0), 0)


def dodaj_agenta():
    # pole_lewe_gorne = PoleKraty(krata_magazynu, random.randint(0, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH),
    # random.randint(0, LICZBA_POL_W_POZIOMIE - BOK_AGENTA1_W_POLACH))
    # pole_lewe_gorne = PoleKraty(krata_magazynu, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH, int(LICZBA_POL_W_POZIOMIE / 2))
    pole_lewe_gorne = PoleKraty(krata_magazynu, 0, 0)
    pom = 'wozek_widlowy.png'
    ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                   (BOK_AGENTA1, BOK_AGENTA1))
    Agent(krata_magazynu, pole_lewe_gorne, ikona)
    # zawsze na poczatku polnoc
    krata_magazynu.agent.kierunek = Kierunek.POLNOC


def dodaj_szafke(numerSzafki, iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_wiersz, poczatek_kolumna):
    wymiary_szafki = Wymiary(0, 0, 0)
    szafka = Szafka(numerSzafki, wymiary_szafki, iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_wiersz,
                    poczatek_kolumna, krata_magazynu)
    Pomieszczenie.dodajSzafke(szafka)


def losowy_cel():
    kierunek = Kierunek(random.randint(0, 3))
    wiersz = random.randint(0, krata_magazynu.liczbaPolPionowo - 1)
    kolumna = random.randint(0, krata_magazynu.liczbaPolPoziomo - 1)
    return Stan(kierunek, PoleKraty(krata_magazynu, wiersz, kolumna))


def zaznacz_cel_na_mapie(cel: Stan):
    wiersz = cel.poleStartoweGorne.wiersz
    kolumna = cel.poleStartoweGorne.kolumna
    if krata_magazynu.krata[wiersz][kolumna] == ZawartoscPola.PUSTE:
        krata_magazynu.krata[wiersz][kolumna] = ZawartoscPola.CEL


def nadaj_cel_agentowi(agent: Agent):
    agent.cel = losowy_cel()
    zaznacz_cel_na_mapie(agent.cel)
    print("CEL:", agent.cel.poleStartoweGorne.wiersz, agent.cel.poleStartoweGorne.kolumna)

def zdarzenie_osoba():
    global flaga1
    flaga1=1

def losowa_osoba():
    wiersz = random.randint(0, krata_magazynu.liczbaPolPionowo - 1)
    kolumna = random.randint(0, krata_magazynu.liczbaPolPoziomo - 1)
    osoba = PoleKraty(krata_magazynu, wiersz, kolumna)
    return osoba


def main():
    # dla kraty 30 x 15
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
    dodaj_szafke("G", 2, 9, "P", 5, 28)

    # # dla kraty 10 x 10
    # dodaj_szafke("A", 1, 8, "P", 1, 1)
    # dodaj_szafke("B", 1, 8, "L", 1, 4)
    # dodaj_szafke("C", 1, 8, "P", 1, 6)
    # dodaj_szafke("C", 1, 8, "P", 1, 8)

    # # dla kraty 5 x 5
    # dodaj_szafke("A", 1, 3, "P", 1, 1)
    # dodaj_szafke("B", 1, 3, "L", 1, 3)

    for i in (
            (1, 10), (1, 3), (3, 23), (2, 23), (5, 15), (4, 15), (9, 12), (11, 20), (11, 27), (11, 26), (14, 19),
            (14, 18),
            (14, 20), (8, 29), (9, 29)):
        krata_magazynu.krata[i[0]][i[1]] = ZawartoscPola.DYWAN
    for i in (
            (0, 10), (13, 20), (13, 6), (13, 14), (14, 13), (9, 26), (9, 16), (9, 15), (9, 27), (9, 16), (9, 26),
            (5, 8),
            (5, 9), (7, 9), (7, 10)):
        krata_magazynu.krata[i[0]][i[1]] = ZawartoscPola.KALUZA

    for i in range(LICZBA_POL_W_PIONIE):
        krata_magazynu.krata[i][21] = ZawartoscPola.SCIANA2
    krata_magazynu.krata[0][21]=ZawartoscPola.PUSTE
    krata_magazynu.krata[7][21] = ZawartoscPola.PUSTE
    krata_magazynu.krata[14][21] = ZawartoscPola.PUSTE

    dodaj_agenta()
    okno1 = Okno(krata_magazynu, krata_magazynu.agent)
    okno1.wyswietlOkno()

    t = threading.Timer(5.0, zdarzenie_osoba).start()
    osoba = PoleKraty(krata_magazynu, 0, 0)
    clf=drzewo_decyzyjne()
    global flaga1
    flaga1 = 0

    while True:
        # cel to Stan (pole kraty gdzie ma stać agent, aby położyć paczkę na półkę, w obiekcie klasy Miejsce jest to artybut dostęp + kierunek <-na razie niepotrzebny)
        if krata_magazynu.agent.cel is None:
            nadaj_cel_agentowi(krata_magazynu.agent)
            krata_magazynu.agent.idzDoCelu()
            recognition()

        if flaga1 == 1:
            osoba.krata.krata[osoba.wiersz][osoba.kolumna] = ZawartoscPola.PUSTE
            okno1.wyswietlOkno()
            osoba = losowa_osoba()
            while osoba.krata.krata[osoba.wiersz][osoba.kolumna] != ZawartoscPola.PUSTE:
                osoba = losowa_osoba()
            osoba.krata.krata[osoba.wiersz][osoba.kolumna] = ZawartoscPola.OSOBA
            okno1.wyswietlOkno()
            pygame.time.wait(1000)
            answer = decyzja_osoba(osoba, clf)
            if answer == 1:
                osoba.krata.krata[osoba.wiersz][osoba.kolumna] = ZawartoscPola.PUSTE
                okno1.wyswietlOkno()
                bieg = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'bieg.png')),
                                              (BOK_AGENTA1, BOK_AGENTA1))
                okno_pygame.blit(bieg, (osoba.kolumna * (BOK_POLA + 1) + 1, osoba.wiersz * (BOK_POLA + 1) + 1))
                pygame.display.flip()
                pygame.time.wait(1500)
            flaga1 = 0
            t = threading.Timer(5.0, zdarzenie_osoba).start()


try:
    main()
except pygame.error:
    pygame.quit()
