from enum import Enum

from stale import *


class Kierunek(Enum):
    POLNOC = 0
    POLUDNIE = 1
    ZACHOD = 2
    WSCHOD = 3

    def kierunekNaLewo(self):
        if self == Kierunek.POLNOC:
            return Kierunek.ZACHOD
        elif self == Kierunek.POLUDNIE:
            return Kierunek.WSCHOD
        elif self == Kierunek.ZACHOD:
            return Kierunek.POLUDNIE
        elif self == Kierunek.WSCHOD:
            return Kierunek.POLNOC

    def kierunekNaPrawo(self):
        if self == Kierunek.POLNOC:
            return Kierunek.WSCHOD
        elif self == Kierunek.POLUDNIE:
            return Kierunek.ZACHOD
        elif self == Kierunek.ZACHOD:
            return Kierunek.POLNOC
        elif self == Kierunek.WSCHOD:
            return Kierunek.POLUDNIE


class ZawartoscPola(Enum):
    PUSTE = 0
    SCIANA = 1
    CEL = 2
    DYWAN = 3
    KALUZA = 4


ZawartoscPolaNaKolorPola = {
    ZawartoscPola.PUSTE: BIALY,
    ZawartoscPola.SCIANA: CIEMNY_BRAZOWY1,
    ZawartoscPola.CEL: ZIELONY1,
    ZawartoscPola.DYWAN: ZOLTY1,
    ZawartoscPola.KALUZA: NIEBIESKI1
}

ZawartoscPolaNaKosztObrotu = {
    ZawartoscPola.PUSTE: 1,
    ZawartoscPola.SCIANA: None,
    ZawartoscPola.CEL: 1,
    ZawartoscPola.DYWAN: 5,
    ZawartoscPola.KALUZA: 3
}

ZawartoscPolaNaKosztWjechania = {
    ZawartoscPola.PUSTE: 2,
    ZawartoscPola.SCIANA: None,
    ZawartoscPola.CEL: 2,
    ZawartoscPola.DYWAN: 5,
    ZawartoscPola.KALUZA: 9
}
