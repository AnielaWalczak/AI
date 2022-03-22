from enumy_i_slowniki import *
from stale import *


class Wymiary:
    def __init__(self, dlugosc, szerokosc, wysokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc


class Mapa:
    def __init__(self):
        self.liczbaPolPoziomo = LICZBA_POL_W_POZIOMIE
        self.liczbaPolPionowo = LICZBA_POL_W_PIONIE
        self.bokPola = BOK_POLA
        self.odstepMiedzyPolami = ODSTEP_MIEDZY_POLAMI
        self.utworzPustaMape()
        self.agent = None

    def utworzPustaMape(self):
        self.krata = []
        for wiersz in range(self.liczbaPolPionowo):
            self.krata.append([])
            for kolumna in range(self.liczbaPolPoziomo):
                zawartosc_pola = ZawartoscPola.PUSTE
                nowe_pole = PoleMapy(self, wiersz, kolumna, zawartosc_pola)
                self.krata[wiersz].append(nowe_pole)


class PoleMapy:
    def __init__(self, mapa: Mapa, wiersz, kolumna, zawartosc: ZawartoscPola):
        self.mapa = mapa
        self.bok = self.mapa.bokPola
        self.wiersz = wiersz
        self.kolumna = kolumna
        self.zawartosc = zawartosc


class WarunkiPowietrza:
    def __init__(self, temperatura, wilgotnosc):
        self.temperatura = temperatura
        self.wilgotnosc = wilgotnosc


class Polka:
    def __init__(self, wymiary: Wymiary, udzwig, wysokoscOdPodlogi):
        self.wymiary = wymiary
        self.udzwig = udzwig
        self.wysokoscOdPodlogi = wysokoscOdPodlogi


class Szafka:
    def __init__(self, wymiary: Wymiary):
        self.wymiary = wymiary
        self.Polki = []
        self.zajmowanePola = []

    def dodajPolke(self, polka: Polka):
        self.Polki.append(polka)

    def dodajPole(self, pole: PoleMapy):
        self.zajmowanePola.append(pole)


class Pomieszczenie:
    def __init__(self, warunkiPowietrza: WarunkiPowietrza, wysokoscSufitu):
        self.warunkiPowietrza = warunkiPowietrza
        self.wysokoscSufitu = wysokoscSufitu
        self.Szafki = []
        self.zajmowanePola = []

    def dodajSzafke(self, szafka: Szafka):
        self.Szafki.append(szafka)

    def dodajPole(self, pole: PoleMapy):
        self.zajmowanePola.append(pole)
