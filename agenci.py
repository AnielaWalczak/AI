import random
from enum import Enum

from stale import *


class KIERUNEK(Enum):
    GORA = 0
    DOL = 1
    LEWO = 2
    PRAWO = 3


class Agent1:
    def __init__(self, hitbox, tekstura, kierunek, droga):
        self.hitbox = hitbox
        self.tekstura = tekstura
        self.kierunek = kierunek
        self.droga = droga

    def obierzNowyKierunek(self):
        self.kierunek = KIERUNEK(random.randint(0, 3))
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

    def ruszSie(self):
        if self.kierunek == KIERUNEK.GORA:
            if self.hitbox.y - KROK_AGENTA1 > 0:
                self.hitbox.y -= KROK_AGENTA1
                self.droga -= KROK_AGENTA1
            else:
                self.droga = 0
        elif self.kierunek == KIERUNEK.DOL:
            if self.hitbox.y + KROK_AGENTA1 < WYSOKOSC_OKNA - self.hitbox.height:
                self.hitbox.y += KROK_AGENTA1
                self.droga -= KROK_AGENTA1
            else:
                self.droga = 0
        elif self.kierunek == KIERUNEK.LEWO:
            if self.hitbox.x - KROK_AGENTA1 > 0:
                self.hitbox.x -= KROK_AGENTA1
                self.droga -= KROK_AGENTA1
            else:
                self.droga = 0
        elif self.kierunek == KIERUNEK.PRAWO:
            if self.hitbox.x + KROK_AGENTA1 < SZEROKOSC_OKNA - self.hitbox.width:
                self.hitbox.x += KROK_AGENTA1
                self.droga -= KROK_AGENTA1
            else:
                self.droga = 0
