import random
from collections import deque

from bfs import Stan, Akcja, graphsearch
from krata import *


class Agent:
    cel: Stan
    bok = BOK_AGENTA1
    bokWPolach = BOK_AGENTA1_W_POLACH

    def __init__(self, Krata, poleStartoweGorne: PoleKraty, tekstura):
        self.krata = Krata
        self.poleStartoweGorne = poleStartoweGorne
        self.tekstura = tekstura
        self.okreslPolozenie()
        self.obierzLosowyKierunek()
        self.okreslDlugoscDrogi()
        Krata.agent = self
        self.cel = None

    def ruszSie(self):
        if self.droga <= 0:
            self.obierzLosowyKierunek()
            self.okreslDlugoscDrogi()
        self.zrobKrokWMoimKierunku()
        self.droga -= 1
        self.okreslPolozenie()
        if self.wyszedlemPozaKrate() or self.wszedlemWSciane():
            self.cofnijSie()
            self.zawroc()
            self.okreslDlugoscDrogi()

    def obierzLosowyKierunek(self):
        self.kierunek = Kierunek(random.randint(0, 3))
        if self.maxDlugoscDrogiWMoimKierunku() < 1:
            self.obierzLosowyKierunek()

    def okreslDlugoscDrogi(self):
        self.droga = random.randint(1, self.maxDlugoscDrogiWMoimKierunku())

    def cofnijSie(self):
        self.zrobKrokWOdwrotnymKierunku()
        self.okreslPolozenie()

    def okreslPolozenie(self):
        self.okreslPoleKoncoweDolne()
        self.okreslHitbox()

    def okreslHitbox(self):
        self.hitbox = pygame.Rect(self.poleStartoweGorne.start, self.poleStartoweGorne.gora, self.bok, self.bok)

    def okreslPoleKoncoweDolne(self):
        wiersz = self.poleStartoweGorne.wiersz + self.bokWPolach - 1
        kolumna = self.poleStartoweGorne.kolumna + self.bokWPolach - 1
        self.poleKoncoweDolne = PoleKraty(self.krata, wiersz, kolumna)

    def wyszedlemPozaKrate(self):
        if self.poleStartoweGorne.wiersz < 0:
            return True
        elif self.poleKoncoweDolne.wiersz > self.krata.liczbaPolPionowo - 1:
            return True
        elif self.poleStartoweGorne.kolumna < 0:
            return True
        elif self.poleKoncoweDolne.kolumna > self.krata.liczbaPolPoziomo - 1:
            return True
        else:
            return False

    # ZROBIC sciany
    def wszedlemWSciane(self):
        for wiersz in range(self.poleStartoweGorne.wiersz, self.poleKoncoweDolne.wiersz + 1):
            for kolumna in range(self.poleStartoweGorne.kolumna, self.poleKoncoweDolne.kolumna + 1):
                if self.krata.krata[wiersz][kolumna] == ZawartoscPola.SCIANA:
                    return True
        return False

    def zawroc(self):
        if self.kierunek == Kierunek.POLNOC:
            self.kierunek = Kierunek.POLUDNIE
        elif self.kierunek == Kierunek.POLUDNIE:
            self.kierunek = Kierunek.POLNOC
        elif self.kierunek == Kierunek.ZACHOD:
            self.kierunek = Kierunek.WSCHOD
        elif self.kierunek == Kierunek.WSCHOD:
            self.kierunek = Kierunek.ZACHOD

    def maxDlugoscDrogiWMoimKierunku(self):
        if self.kierunek == Kierunek.POLNOC:
            return self.poleStartoweGorne.wiersz
        elif self.kierunek == Kierunek.POLUDNIE:
            return self.krata.liczbaPolPionowo - self.poleKoncoweDolne.wiersz - 1
        elif self.kierunek == Kierunek.ZACHOD:
            return self.poleStartoweGorne.kolumna
        elif self.kierunek == Kierunek.WSCHOD:
            return self.krata.liczbaPolPoziomo - self.poleKoncoweDolne.kolumna - 1

    def zrobKrokWMoimKierunku(self):
        if self.kierunek == Kierunek.POLNOC:
            self.idzNaPolnoc()
        elif self.kierunek == Kierunek.POLUDNIE:
            self.idzNaPoludnie()
        elif self.kierunek == Kierunek.ZACHOD:
            self.idzNaZachod()
        elif self.kierunek == Kierunek.WSCHOD:
            self.idzNaWschod()

    def zrobKrokWOdwrotnymKierunku(self):
        if self.kierunek == Kierunek.POLNOC:
            self.idzNaPoludnie()
        elif self.kierunek == Kierunek.POLUDNIE:
            self.idzNaPolnoc()
        elif self.kierunek == Kierunek.ZACHOD:
            self.idzNaWschod()
        elif self.kierunek == Kierunek.WSCHOD:
            self.idzNaZachod()

    def idzNaPolnoc(self):
        self.poleStartoweGorne.wiersz -= 1

    def idzNaPoludnie(self):
        self.poleStartoweGorne.wiersz += 1

    def idzNaZachod(self):
        self.poleStartoweGorne.kolumna -= 1

    def idzNaWschod(self):
        self.poleStartoweGorne.kolumna += 1

    # def bfs(self,graph, start, cel):
    #     sciezka = [start]
    #     wierzcholek_sciezka = [start, sciezka]
    #     bfs_kolejka = [wierzcholek_sciezka]
    #     odwiedzone = set()
    #     while bfs_kolejka:
    #         aktualne, sciezka = bfs_kolejka.pop(0)
    #         odwiedzone.add(aktualne)
    #         for neighbor in graph[aktualne]:
    #             if neighbor not in odwiedzone:
    #                 if neighbor is cel:
    #                     return sciezka + [neighbor]
    #                 else:
    #                     bfs_kolejka.append([neighbor, sciezka + [neighbor]])

    def idzDoCelu(self, klatkaz):
        stan_poczatkowy = Stan(self.kierunek, self.poleStartoweGorne)
        stos_akcji = graphsearch(stan_poczatkowy, self.cel)
        if stos_akcji == False:
            print("Nie można dotrzeć.")
        else:
            self.wykonaj_stos_akcji(stos_akcji, klatkaz)
            print("Dotarłem.")

        self.krata.krata[self.cel.poleStartoweGorne.wiersz][
            self.cel.poleStartoweGorne.kolumna] = ZawartoscPola.PUSTE  ##chwilowo-przeniesc pozniej

        self.cel = None

    def wykonaj_stos_akcji(self, stos_akcji: deque, klatkaz):
        while stos_akcji:
            klatkaz.tick(FPS)
            self.narysujAgenta()
            akcja = stos_akcji.pop()
            print(akcja.name, end=" ")
            if akcja == Akcja.KROK_W_PRZOD:
                self.zrobKrokWMoimKierunku()
                self.okreslPolozenie()
            elif akcja == Akcja.OBROT_W_LEWO:
                self.obrocSieWLewo()
            elif akcja == Akcja.OBROT_W_PRAWO:
                self.obrocSieWPrawo()
        print()

    def obrocSieWLewo(self):
        self.kierunek = self.kierunek.kierunekNaLewo()

    def obrocSieWPrawo(self):
        self.kierunek = self.kierunek.kierunekNaPrawo()

    def narysujAgenta(self):
        self.krata.narysujKrate()
        self.krata.okno.blit(self.tekstura, (self.hitbox.x, self.hitbox.y))
        pygame.display.update()
