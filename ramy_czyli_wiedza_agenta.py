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


class Miejsce: #wcześniej półka
    def __init__(self, numer, wymiary: Wymiary, udzwig, wysokoscOdPodlogi):
        self.numer=numer
        self.wymiary = wymiary
        self.udzwig = udzwig
        self.wysokoscOdPodlogi = wysokoscOdPodlogi
        #self.status = 'wolne'
        self.dostep=[]
        self.zajmowanePola = []

    def dodajPole(self, pole: PoleKraty):
        self.zajmowanePola.append(pole)

    def dodajDostep(self, pole: PoleKraty):
        self.dostep.append(pole)


class Szafka:
    def __init__(self, numerSzafki, wymiary: Wymiary, iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_kolumna, poczatek_wiersz1, Krata: Krata):
        self.numerSzafki=numerSzafki
        self.wymiary = wymiary
        self.iloscPolek = iloscPolek
        self.iloscMiejscNaPolce = iloscMiejscNaPolce
        self.dostepZeStrony=dostepZeStrony
        self.Miejsca = []
        self.zajmowanePola = []
        self.utworzPustaSzafke(numerSzafki,iloscPolek, iloscMiejscNaPolce, dostepZeStrony, poczatek_kolumna, poczatek_wiersz1,Krata)

    def dodajMiejsce(self, miejsce: Miejsce):
        self.Miejsca.append(miejsce)

    def dodajPole(self, pole: PoleKraty):
        self.zajmowanePola.append(pole)

    def utworzPustaSzafke(self, numerSzafki, iloscPolek, iloscMiejscNaPolce, dostępZeStrony, poczatek_wiersz1, poczatek_kolumna, Krata: Krata):
        for i in range(iloscPolek):
            for j in range(iloscMiejscNaPolce):
                wymiar_miejsca = Wymiary(0, 0, 0)
                numerMiejsca = self.numerSzafki + "/" + str(i) + "/" + str(j)
                miejsce = Miejsce(numerMiejsca,wymiar_miejsca, 0, 0)
                #wypełnianie pól "zajmowane miejsca" i "dostęp"
                for m in range(DUZA_SZAFA):  # wiersz
                    poczatek_wiersz = poczatek_wiersz1 + j * DUZA_SZAFA + m
                    for n in range(DUZA_SZAFA):  # kolumna
                        Krata.krata[poczatek_wiersz][poczatek_kolumna + n] = ZawartoscPola.SCIANA
                        pole = PoleKraty(Krata, poczatek_wiersz, poczatek_kolumna+n)
                        miejsce.dodajPole(pole)
                        self.dodajPole(pole)
                        if dostępZeStrony=="L":
                            pole_dostepu = PoleKraty(Krata, poczatek_wiersz, poczatek_kolumna + n - BOK_AGENTA1_W_POLACH) #dostęp z lewej strony
                            miejsce.dodajDostep(pole_dostepu)
                        elif dostępZeStrony == "P":
                            pole_dostepu = PoleKraty(Krata, poczatek_wiersz, poczatek_kolumna + n + BOK_AGENTA1_W_POLACH)  # dostęp z prawej strony strony
                            miejsce.dodajDostep(pole_dostepu)
                self.dodajMiejsce(miejsce)

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