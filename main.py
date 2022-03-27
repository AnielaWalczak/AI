import os
import ctypes

from agent import *
from ramy_czyli_wiedza_agenta import *

#aby działalo w oknie + rozdzielczość ekranu
ctypes.windll.shcore.SetProcessDpiAwareness(1)



Okno = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")
Krata = Krata(Okno)
Pomieszczenie=Pomieszczenie(0,0)

def dodaj_agenta():
    # pole_lewe_gorne = PoleKraty(Krata, random.randint(0, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH),
    # random.randint(0, LICZBA_POL_W_POZIOMIE - BOK_AGENTA1_W_POLACH))
    pole_lewe_gorne = PoleKraty(Krata, 1, 1)
    pom = 'traktor_ikona.png'
    ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                   (BOK_AGENTA1, BOK_AGENTA1))
    Agent(Krata, pole_lewe_gorne, ikona)

def dodaj_szafke(poczatek_wiersz1, poczatek_kolumna,ilosc_polek):
    #bardzo prosta szafka, później do zmiany i uzupełnienia
    #tworzymy jeden typ szafki składającej się z dużych półek(to znaczy jest jedna półka oraz kilka miejsc na niej), każda z półek zajmuje po 3 pola z każdego boku
    wymiary_szafki = Wymiary(0, 0, 0)
    szafka = Szafka(wymiary_szafki, ilosc_polek, poczatek_wiersz1, poczatek_kolumna, Krata)
    Pomieszczenie.dodajSzafke(szafka)


def main():
    dodaj_szafke(0, 20, 8)
    dodaj_szafke(0, 40, 8)
    dodaj_szafke(0, 60, 8)
    dodaj_szafke(0, 80, 8)
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
