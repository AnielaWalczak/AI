import os
import pygame

FPS = 20
#
# SZEROKOSC_OKNA = 1500
# WYSOKOSC_OKNA = 750
#
LICZBA_POL_W_POZIOMIE = 30
LICZBA_POL_W_PIONIE = 15
BOK_POLA = 45
ODSTEP_MIEDZY_POLAMI = 1
SZEROKOSC_OKNA = LICZBA_POL_W_POZIOMIE * (BOK_POLA + ODSTEP_MIEDZY_POLAMI) + ODSTEP_MIEDZY_POLAMI
WYSOKOSC_OKNA = LICZBA_POL_W_PIONIE * (BOK_POLA + ODSTEP_MIEDZY_POLAMI) + ODSTEP_MIEDZY_POLAMI
#
BOK_AGENTA1_W_POLACH = 1
BOK_AGENTA1 = BOK_AGENTA1_W_POLACH * (BOK_POLA + ODSTEP_MIEDZY_POLAMI) - ODSTEP_MIEDZY_POLAMI
#
DUZA_SZAFA = 1
#
BIALY = (255, 255, 255)
JASNOSZARY1 = (200, 200, 200)
SZARY1 = (150, 150, 150)
ZIELONY1 = (26, 122, 26)
CZARNY = (0, 0, 0)
CIEMNY_BRAZOWY1 = (60, 19, 33)
ZOLTY1 = (231, 213, 69)
NIEBIESKI1 = (65, 125, 225)
IKONA=pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'osoba2.png')),
                                               (BOK_AGENTA1, BOK_AGENTA1))
KALUZA=pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'kaluza.png')),
                                               (BOK_AGENTA1, BOK_AGENTA1))
DYWAN=pygame.transform.scale(pygame.image.load(os.path.join('Ikony', 'dywan.png')),
                                               (BOK_AGENTA1, BOK_AGENTA1))
###

###
GREY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (55, 55, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARKGREY = (150, 150, 150)
UGLY_PINK = (255, 0, 255)
BROWN = (153, 76, 0)
GOLD = (153, 153, 0)
DARKGREEN = (0, 102, 0)
DARKORANGE = (255, 128, 0)
#
# NUMBER_OF_BLOCKS_WIDE=8
# NUMBER_OF_BLOCKS_HIGH=8
# BLOCK_HEIGHT=round(SZEROKOSC_OKNA/NUMBER_OF_BLOCKS_HIGH)
# BLOCK_WIDTH=round(WYSOKOSC_OKNA/NUMBER_OF_BLOCKS_WIDE)
#
MAPFILE = "map.txt"
TITLE = "Gierka"
#
NUMBER_OF_BLOCKS_WIDE = LICZBA_POL_W_POZIOMIE
NUMBER_OF_BLOCKS_HIGH = LICZBA_POL_W_PIONIE
BLOCK_HEIGHT = BOK_POLA
BLOCK_WIDTH = BOK_POLA
