from enumy_i_slowniki import *
from stale import *
from krata import *


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
        # zakładamy że aby położyć paczkę na półkę, agent musi stać dokładnie na polach kraty, określonych w atrybucie dostęp
        # atrybut dostęp składa się z 9 pól ponieważ tyle miejsca na kracie zajmuje agent
        # utworzyłam szafki "wertykalnie" oraz zakładam że do półki można się dostać tylko z jednej strony (na razie tylko z lewej, ale można teżdodać, że tylko z prawej)
        self.dostep = []
        self.zajmowanePola = []

    def dodajPole(self, pole: PoleKraty):
        self.zajmowanePola.append(pole)

    def dodajDostep(self, pole: PoleKraty):
        self.dostep.append(pole)


class Szafka:
    def __init__(self, wymiary: Wymiary, ilosc_polek, poczatek_kolumna, poczatek_wiersz1, Krata: Krata):
        self.wymiary = wymiary
        self.Polki = []
        self.zajmowanePola = []
        self.utworzPustaSzafke(ilosc_polek, poczatek_kolumna, poczatek_wiersz1, Krata)

    def dodajPolke(self, polka: Polka):
        self.Polki.append(polka)

    def dodajPole(self, pole: PoleKraty):
        self.zajmowanePola.append(pole)

    def utworzPustaSzafke(self, ilosc_polek, poczatek_wiersz1, poczatek_kolumna, Krata: Krata):
        for i in range(ilosc_polek):
            wymiar_polki = Wymiary(0, 0, 0)
            polka = Polka(wymiar_polki, 0, 0)
            for m in range(DUZA_SZAFA):  # wiersz
                poczatek_wiersz = poczatek_wiersz1 + i * 3 + m
                for n in range(DUZA_SZAFA):  # kolumna
                    Krata.krata[poczatek_wiersz][poczatek_kolumna + n] = ZawartoscPola.SCIANA
                    pole = PoleKraty(Krata, poczatek_wiersz, poczatek_kolumna)
                    polka.dodajPole(pole)
                    self.dodajPole(pole)
                    pole_dostepu = PoleKraty(Krata, poczatek_wiersz, poczatek_kolumna + n - BOK_AGENTA1_W_POLACH) #dostęp z lewej strony
                    polka.dodajDostep(pole_dostepu)
            self.dodajPolke(polka)


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