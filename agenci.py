import random

from klasy import *


# poleKoncoweDolne -> wiersz+bokWPolach-1  kolumna+bokWPolach-1
class Agent:
    bok = BOK_AGENTA1
    bokWPolach = BOK_AGENTA1_W_POLACH

    def __init__(self, Krata, poleStartoweGorne, tekstura, kierunek, droga):
        self.krata = Krata
        self.poleStartoweGorne = poleStartoweGorne
        self.okreslHitbox()
        self.okreslPoleKoncoweDolne()
        self.tekstura = tekstura
        self.kierunek = kierunek
        self.droga = droga
        Krata.agent = self

    def okreslHitbox(self):
        self.hitbox = pygame.Rect(self.poleStartoweGorne.start, self.poleStartoweGorne.gora, self.bok, self.bok)

    def okreslPoleKoncoweDolne(self):
        wiersz = self.poleStartoweGorne.wiersz + self.bokWPolach - 1
        kolumna = self.poleStartoweGorne.kolumna + self.bokWPolach - 1
        self.poleKoncoweDolne = PoleKraty(self.krata, wiersz, kolumna)

    def obierzNowyKierunek(self):
        self.kierunek = Kierunek(random.randint(0, 3))

    def okreslDlugoscDrogi(self):
        losowa_droga = None
        if self.kierunek == Kierunek.GORA:
            losowa_droga = random.randint(0, self.poleStartoweGorne.wiersz)
        elif self.kierunek == Kierunek.DOL:
            losowa_droga = random.randint(0, (self.krata.liczbaPolPionowo - 1) - (
                        self.poleStartoweGorne.wiersz + self.bokWPolach - 1))
        elif self.kierunek == Kierunek.LEWO:
            losowa_droga = random.randint(0, self.poleStartoweGorne.kolumna)
        elif self.kierunek == Kierunek.PRAWO:
            losowa_droga = random.randint(0, (self.krata.liczbaPolPoziomo - 1) - (
                        self.poleStartoweGorne.wiersz + self.bokWPolach - 1))
        self.droga = losowa_droga

    def idzWGore(self):
        self.poleStartoweGorne.wiersz -= 1

    def idzWDol(self):
        self.poleStartoweGorne.wiersz += 1

    def idzWLewo(self):
        self.poleStartoweGorne.kolumna -= 1

    def idzWPrawo(self):
        self.poleStartoweGorne.kolumna += 1

    def wyszedlemPozaKrate(self):
        if self.poleStartoweGorne.wiersz not in range(0, (self.krata.liczbaPolWPionie - 1) - (self.bokWPolach - 1)):
            return False
        elif self.poleStartoweGorne.kolumna in range(0, (self.krata.liczbaPolWPoziomie - 1) - (self.bokWPolach - 1)):
            return False
        else:
            return True

    def ruszSie(self):
        if self.kierunek == Kierunek.GORA:
            self.idzWGore()
        elif self.kierunek == Kierunek.DOL:
            self.idzWDol()
        elif self.kierunek == Kierunek.LEWO:
            self.idzWLewo()
        elif self.kierunek == Kierunek.PRAWO:
            self.idzWPrawo()
        if self.wyszedlemPozaKrate():
            self.cofnijSie()
            self.zawroc()
            self.okreslDlugoscDrogi()

    def cofnijSie(self):
        if self.kierunek == Kierunek.GORA:
            self.idzWDol()
        elif self.kierunek == Kierunek.DOL:
            self.idzWGore()
        elif self.kierunek == Kierunek.LEWO:
            self.idzWPrawo()
        elif self.kierunek == Kierunek.PRAWO:
            self.idzWLewo()

    def zawroc(self):
        if self.kierunek == Kierunek.GORA:
            self.kierunek = Kierunek.DOL
        elif self.kierunek == Kierunek.DOL:
            self.kierunek = Kierunek.GORA
        elif self.kierunek == Kierunek.LEWO:
            self.kierunek = Kierunek.PRAWO
        elif self.kierunek == Kierunek.PRAWO:
            self.kierunek = Kierunek.LEWO
