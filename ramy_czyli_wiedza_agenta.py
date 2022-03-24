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

class Etykieta:
    def __init__(self, nazwaTowaru, nazwaNadawcy, dataZapakowania, id, niePietrowac, zachowacSuchosc, ostroznie, uwagaSzklo):
        # realistyczne? informacje na paczce
        # kategoryzowanie towaru może odbywać się na podstawie jego nazwy
        self.nazwaTowaru = nazwaTowaru
        self.nazwaNadawcy = nazwaNadawcy
        self.dataZapakowania = dataZapakowania
        self.id = id
        # nalepki na paczce - być może nie będą na etykiecie, a trzeba je będzie rozpoznać na obrazie
        self.niePietrowac = niePietrowac
        self.zachowacSuchosc = zachowacSuchosc
        self.ostroznie = ostroznie
        self.uwagaSzklo = uwagaSzklo

class Paczka:
    def __init__(self,wymiary: Wymiary, waga, etykieta: Etykieta):
        self.wymiary = wymiary
        self.waga = waga
        self.etykieta = etykieta

class Paleta:
    def __init__(self):
        self.Paczki = []

    def dodajPaczke(self, paczka: Paczka):
        self.Paczki.append(paczka)

class Nadawca:
    def __init__(self,nazwa, id):
        self.nazwa = nazwa
        self.id = id
        # plus dodatkowe informacje mogące wpływać na priorytet rozpakowania transportu / miejsce składowania paczek?

class Transport:
    def __init__(self, dataPrzyjecia, nadawca: Nadawca, id):
        Palety = []
        self.dataPrzyjecia = dataPrzyjecia
        self.nadawca = nadawca
        self.id = id

    # wyliczanie priorytetu rozpakowania transportu ?
    # def okrescPriorytet(self):
    #     self.priorytet =