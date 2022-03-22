import random

from stale import *


class Agent1:
    def __init__(self, hitbox, tekstura, kierunek, droga):
        self.hitbox = hitbox
        self.tekstura = tekstura
        self.kierunek = kierunek
        self.droga = droga

    def obierzNowyKierunek(self):
        self.kierunek = KIERUNEK(random.randint(0, 3))

    def okreslDlugoscDrogi(self):
        losowa_droga = None
        if self.kierunek == KIERUNEK.GORA:
            losowa_droga = random.randint(0, self.hitbox.y)
        elif self.kierunek == KIERUNEK.DOL:
            losowa_droga = random.randint(0, WYSOKOSC_OKNA - self.hitbox.y)
        elif self.kierunek == KIERUNEK.LEWO:
            losowa_droga = random.randint(0, self.hitbox.x)
        elif self.kierunek == KIERUNEK.PRAWO:
            losowa_droga = random.randint(0, SZEROKOSC_OKNA - self.hitbox.x)
        self.droga = losowa_droga - losowa_droga % KROK_AGENTA1

    def idzWGore(self):
        if self.hitbox.y - KROK_AGENTA1 > 0:
            self.hitbox.y -= KROK_AGENTA1
            self.droga -= KROK_AGENTA1
        else:
            self.droga = 0

    def idzWDol(self):
        if self.hitbox.y + KROK_AGENTA1 < WYSOKOSC_OKNA - self.hitbox.height:
            self.hitbox.y += KROK_AGENTA1
            self.droga -= KROK_AGENTA1
        else:
            self.droga = 0

    def idzWLewo(self):
        if self.hitbox.x - KROK_AGENTA1 > 0:
            self.hitbox.x -= KROK_AGENTA1
            self.droga -= KROK_AGENTA1
        else:
            self.droga = 0

    def idzWPrawo(self):
        if self.hitbox.x + KROK_AGENTA1 < SZEROKOSC_OKNA - self.hitbox.width:
            self.hitbox.x += KROK_AGENTA1
            self.droga -= KROK_AGENTA1
        else:
            self.droga = 0

    def czyWszedlesWInnegoAgenta(self, Agenci):
        for a in Agenci:
            if a.hitbox.colliderect(self.hitbox) and a != self:
                return True
        return False

    def ruszSie(self, Agenci):
        if self.kierunek == KIERUNEK.GORA:
            self.idzWGore()
        elif self.kierunek == KIERUNEK.DOL:
            self.idzWDol()
        elif self.kierunek == KIERUNEK.LEWO:
            self.idzWLewo()
        elif self.kierunek == KIERUNEK.PRAWO:
            self.idzWPrawo()
        if self.czyWszedlesWInnegoAgenta(Agenci):
            self.cofnijSie()
            self.zawroc()
            self.okreslDlugoscDrogi()
            # self.ruszSie(Agenci)

    def cofnijSie(self):
        if self.kierunek == KIERUNEK.GORA:
            self.idzWDol()
        elif self.kierunek == KIERUNEK.DOL:
            self.idzWGore()
        elif self.kierunek == KIERUNEK.LEWO:
            self.idzWPrawo()
        elif self.kierunek == KIERUNEK.PRAWO:
            self.idzWLewo()

    def zawroc(self):
        if self.kierunek == KIERUNEK.GORA:
            self.kierunek = KIERUNEK.DOL
        elif self.kierunek == KIERUNEK.DOL:
            self.kierunek = KIERUNEK.GORA
        elif self.kierunek == KIERUNEK.LEWO:
            self.kierunek = KIERUNEK.PRAWO
        elif self.kierunek == KIERUNEK.PRAWO:
            self.kierunek = KIERUNEK.LEWO
