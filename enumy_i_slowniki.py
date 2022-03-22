from enum import Enum

from stale import *


class Kierunek(Enum):
    GORA = 0
    DOL = 1
    LEWO = 2
    PRAWO = 3


class ZawartoscPola(Enum):
    PUSTE = 0
    SCIANA = 1


ZawartoscPolaNaKolorPola = {
    ZawartoscPola.PUSTE: BIALY,
    ZawartoscPola.SCIANA: CIEMNY_BRAZOWY1
}
