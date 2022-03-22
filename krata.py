import pygame

from enumy_i_slowniki import *
from stale import *


class PoleKraty:
    def __init__(self, Krata, wiersz, kolumna):
        self.krata = Krata
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


class Krata:
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
                # ZROBIC sciany
                # if wiersz in (0, self.liczbaPolPionowo - 1) or kolumna in (0, self.liczbaPolPoziomo - 1):
                #      zawartosc_pola = ZawartoscPola.SCIANA
                # if wiersz in range(6,18) and kolumna in (5,15,25,35):
                #      zawartosc_pola = ZawartoscPola.SCIANA
                # if wiersz in (4,22) and kolumna in range (10,35):
                #      zawartosc_pola = ZawartoscPola.SCIANA
                self.krata[wiersz].append(zawartosc_pola)

    def wyswietlKrate(self):
        self.narysujKrate()
        # self.narysujKrateAlternatywnie()
        self.narysujAgenta()
        pygame.display.update()

    def narysujKrate(self):
        self.okno.fill(SZARY1)
        for wiersz in range(self.liczbaPolPionowo):
            for kolumna in range(self.liczbaPolPoziomo):
                start = (self.odstepMiedzyPolami + self.bokPola) * kolumna + self.odstepMiedzyPolami
                gora = (self.odstepMiedzyPolami + self.bokPola) * wiersz + self.odstepMiedzyPolami
                kolor_pola = ZawartoscPolaNaKolorPola[self.krata[wiersz][kolumna]]
                pygame.draw.rect(self.okno, kolor_pola, [start, gora, self.bokPola, self.bokPola])

    def narysujKrateAlternatywnie(self):
        self.okno.fill(SZARY1)
        # for i in range(stale.NUMBER_OF_BLOCKS_WIDE):
        #     new_height = round(i * BLOCK_HEIGHT)
        #     new_width = round(i * BLOCK_HEIGHT)
        #     pygame.draw.line(surface, BLACK, (0, new_height), (SZEROKOSC_OKNA, new_height), 2)
        #     pygame.draw.line(surface, BLACK, (new_width, 0), (new_width, WYSOKOSC_OKNA), 2)
        for i in range(LICZBA_POL_W_POZIOMIE + 1):
            new_height = i * (BOK_POLA + ODSTEP_MIEDZY_POLAMI)
            new_width = i * (BOK_POLA + ODSTEP_MIEDZY_POLAMI)
            pygame.draw.line(self.okno, CZARNY, (0, new_height), (SZEROKOSC_OKNA, new_height), ODSTEP_MIEDZY_POLAMI)
            pygame.draw.line(self.okno, CZARNY, (new_width, 0), (new_width, WYSOKOSC_OKNA), ODSTEP_MIEDZY_POLAMI)

    def narysujAgenta(self):
        if self.agent is not None:
            self.okno.blit(self.agent.tekstura, (self.agent.hitbox.x, self.agent.hitbox.y))
            self.agent.ruszSie()
