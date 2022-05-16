import pygame

from enumy_i_slowniki import *
from obserwacja import *
from stale import *


class PoleKraty:
    gora: any
    start: any

    def __init__(self, krata, wiersz, kolumna):
        self.krata = krata
        self.bok = self.krata.bokPola
        self._wiersz = wiersz
        self._kolumna = kolumna
        self.okreslGore()
        self.okreslStart()

    def okreslGore(self):
        self.gora = (self.bok + self.krata.odstepMiedzyPolami) * self.wiersz + self.krata.odstepMiedzyPolami

    def okreslStart(self):
        self.start = (self.bok + self.krata.odstepMiedzyPolami) * self.kolumna + self.krata.odstepMiedzyPolami

    def getWiersz(self):
        return self._wiersz

    def setWiersz(self, x):
        self._wiersz = x
        self.okreslGore()

    def getKolumna(self):
        return self._kolumna

    def setKolumna(self, x):
        self._kolumna = x
        self.okreslStart()

    wiersz = property(getWiersz, setWiersz)
    kolumna = property(getKolumna, setKolumna)

    def skopiuj(self):
        return PoleKraty(self.krata, self.wiersz, self.kolumna)


class Krata(Obserwowany):
    krata: []

    def __init__(self, okno):
        self.okno = okno
        self.liczbaPolPoziomo = LICZBA_POL_W_POZIOMIE
        self.liczbaPolPionowo = LICZBA_POL_W_PIONIE
        self.bokPola = BOK_POLA
        self.odstepMiedzyPolami = ODSTEP_MIEDZY_POLAMI
        self.utworzPustaKrate()
        self.agent = None

    def utworzPustaKrate(self):
        self.krata = []
        for wiersz in range(self.liczbaPolPionowo):
            self.krata.append([])
            for kolumna in range(self.liczbaPolPoziomo):
                zawartosc_pola = ZawartoscPola.PUSTE
                self.krata[wiersz].append(zawartosc_pola)

    def narysujKrate(self):
        self.okno.fill(SZARY1)
        for wiersz in range(self.liczbaPolPionowo):
            for kolumna in range(self.liczbaPolPoziomo):
                start = (self.odstepMiedzyPolami + self.bokPola) * kolumna + self.odstepMiedzyPolami
                gora = (self.odstepMiedzyPolami + self.bokPola) * wiersz + self.odstepMiedzyPolami
                kolor_pola = ZawartoscPolaNaKolorPola[self.krata[wiersz][kolumna]]
                if kolor_pola == IKONA:
                    osoba_ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'osoba2.png')),
                                                         (BOK_AGENTA1, BOK_AGENTA1))
                    self.okno.blit(osoba_ikona, [start, gora, self.bokPola, self.bokPola])
                elif kolor_pola == KALUZA:
                    osoba_ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'kaluza.png')),
                                                         (BOK_AGENTA1, BOK_AGENTA1))
                    self.okno.blit(osoba_ikona, [start, gora, self.bokPola, self.bokPola])
                elif kolor_pola == DYWAN:
                    osoba_ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'dywan.png')),
                                                         (BOK_AGENTA1, BOK_AGENTA1))
                    self.okno.blit(osoba_ikona, [start, gora, self.bokPola, self.bokPola])

                else:
                    pygame.draw.rect(self.okno, kolor_pola, [start, gora, self.bokPola, self.bokPola])

    def narysujKrateAlternatywnie(self):
        self.okno.fill(SZARY1)
        for i in range(LICZBA_POL_W_POZIOMIE + 1):
            new_height = i * (BOK_POLA + ODSTEP_MIEDZY_POLAMI)
            new_width = i * (BOK_POLA + ODSTEP_MIEDZY_POLAMI)
            pygame.draw.line(self.okno, CZARNY, (0, new_height), (SZEROKOSC_OKNA, new_height), ODSTEP_MIEDZY_POLAMI)
            pygame.draw.line(self.okno, CZARNY, (new_width, 0), (new_width, WYSOKOSC_OKNA), ODSTEP_MIEDZY_POLAMI)

    def powiadomObserwatorow(self):
        for obserwator in self.obserwatorzy:
            obserwator.odbierzPowiadomienie(self)
