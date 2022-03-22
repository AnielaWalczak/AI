import pygame

from enumy import *
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
        self.krata = self.utworzPustaKrate()
        self.agent = None

    def utworzPustaKrate(self):
        self.krata = []
        for rzad in range(self.liczbaPolPionowo):
            self.krata.append([])
            for kolumna in range(self.liczbaPolPoziomo):
                self.krata[rzad].append(ZawartoscPola.PUSTE)

    def wyswietlKrate(self):
        self.narysujKrate()
        self.narysujAgenta()
        pygame.display.update()

    def narysujKrate(self):
        self.okno.fill(SZARY1)
        for rzad in range(self.liczbaPolPionowo):
            for kolumna in range(self.liczbaPolPoziomo):
                start = (self.odstepMiedzyPolami + self.bokPola) * kolumna + self.odstepMiedzyPolami
                gora = (self.odstepMiedzyPolami + self.bokPola) * rzad + self.odstepMiedzyPolami
                pygame.draw.rect(self.okno, BIALY, [start, gora, self.bokPola, self.bokPola])

    def narysujAgenta(self):
        if self.agent is not None:
            self.okno.blit(self.agent.tekstura, (self.agent.hitbox.x, self.agent.hitbox.y))
            self.agent.ruszSie()
