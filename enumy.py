from enum import Enum


class Kierunek(Enum):
    GORA = 0
    DOL = 1
    LEWO = 2
    PRAWO = 3


class ZawartoscPola(Enum):
    PUSTE = 0
    AGENT = 1
    LAWA = 2
