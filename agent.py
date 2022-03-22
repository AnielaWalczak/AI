import random

from krata import *


class Agent:
    bok = BOK_AGENTA1
    bokWPolach = BOK_AGENTA1_W_POLACH

    def __init__(self, Krata, poleStartoweGorne, tekstura):
        self.krata = Krata
        self.poleStartoweGorne = poleStartoweGorne
        self.tekstura = tekstura
        self.okreslPolozenie()
        self.obierzNowyKierunek()
        self.okreslDlugoscDrogi()
        Krata.agent = self

    def ruszSie(self):
        if self.droga <= 0:
            self.obierzNowyKierunek()
            self.okreslDlugoscDrogi()
        self.zrobKrokWMoimKierunku()
        self.droga -= 1
        self.okreslPolozenie()
        if self.wyszedlemPozaKrate():
            self.cofnijSie()
            self.zawroc()
            self.okreslDlugoscDrogi()

    def obierzNowyKierunek(self):
        self.kierunek = Kierunek(random.randint(0, 3))
        if self.maxDlugoscDrogiWMoimKierunku() < 1:
            self.obierzNowyKierunek()

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
    # def wszedlemWSciane(self):
    #     for wiersz in range (self.poleStartoweGorne.wiersz,self.poleKoncoweDolne.wiersz):
    #         for kolumna in range(self.poleStartoweGorne.kolumna,self.poleKoncoweDolne.kolumna):
    #             if self.krata.krata[wiersz][kolumna]==ZawartoscPola.SCIANA:
    #                 return True
    #     return False

    def zawroc(self):
        if self.kierunek == Kierunek.GORA:
            self.kierunek = Kierunek.DOL
        elif self.kierunek == Kierunek.DOL:
            self.kierunek = Kierunek.GORA
        elif self.kierunek == Kierunek.LEWO:
            self.kierunek = Kierunek.PRAWO
        elif self.kierunek == Kierunek.PRAWO:
            self.kierunek = Kierunek.LEWO

    def maxDlugoscDrogiWMoimKierunku(self):
        if self.kierunek == Kierunek.GORA:
            return self.poleStartoweGorne.wiersz
        elif self.kierunek == Kierunek.DOL:
            return self.krata.liczbaPolPionowo - self.poleKoncoweDolne.wiersz - 1
        elif self.kierunek == Kierunek.LEWO:
            return self.poleStartoweGorne.kolumna
        elif self.kierunek == Kierunek.PRAWO:
            return self.krata.liczbaPolPoziomo - self.poleKoncoweDolne.kolumna - 1

    def zrobKrokWMoimKierunku(self):
        if self.kierunek == Kierunek.GORA:
            self.idzWGore()
        elif self.kierunek == Kierunek.DOL:
            self.idzWDol()
        elif self.kierunek == Kierunek.LEWO:
            self.idzWLewo()
        elif self.kierunek == Kierunek.PRAWO:
            self.idzWPrawo()

    def zrobKrokWOdwrotnymKierunku(self):
        if self.kierunek == Kierunek.GORA:
            self.idzWDol()
        elif self.kierunek == Kierunek.DOL:
            self.idzWGore()
        elif self.kierunek == Kierunek.LEWO:
            self.idzWPrawo()
        elif self.kierunek == Kierunek.PRAWO:
            self.idzWLewo()

    def idzWGore(self):
        self.poleStartoweGorne.wiersz -= 1

    def idzWDol(self):
        self.poleStartoweGorne.wiersz += 1

    def idzWLewo(self):
        self.poleStartoweGorne.kolumna -= 1

    def idzWPrawo(self):
        self.poleStartoweGorne.kolumna += 1
