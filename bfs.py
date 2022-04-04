from krata import *

def bfs(Krata: Krata, start: PoleKraty, cel: PoleKraty):
    wierzcholek_sciezka = [["start", start], [["start", start]]]
    bfs_kolejka = [wierzcholek_sciezka]
    odwiedzone = set()
    while bfs_kolejka:
        elem = bfs_kolejka.pop(0)
        odwNowe = str(elem[0][1].wiersz) + "/" + str(elem[0][1].kolumna)
        odwiedzone.add(odwNowe)
        polaObok = succ(Krata,elem[0][1])
        for neighbor in polaObok:
            sciezka = elem[1].copy()
            sprOdw = str(neighbor[1].wiersz) + "/" + str(neighbor[1].kolumna)
            if sprOdw not in odwiedzone:
                if neighbor[1].wiersz == cel.wiersz and neighbor[1].kolumna == cel.kolumna:
                    sciezka.append(neighbor)
                    return sciezka
                else:
                    sciezka.append([neighbor])
                    bfs_kolejka.append([neighbor, sciezka])

def succ(Krata: Krata, poleKraty: PoleKraty):
    polaDostepneObok = list()
    if poleKraty.kolumna - 1 >= 0:  # nie poza kratę
        if Krata.krata[poleKraty.wiersz][poleKraty.kolumna - 1] != ZawartoscPola.SCIANA:  # nie szafka (szafka to ściana)
            poleLewe = PoleKraty(Krata, poleKraty.wiersz, poleKraty.kolumna - 1)
            naLewo = ["Kierunek.LEWO", poleLewe]
            polaDostepneObok.append(naLewo)
    if poleKraty.wiersz - 1 >= 0:  # nie poza kratę
        if Krata.krata[poleKraty.wiersz - 1][poleKraty.kolumna] != ZawartoscPola.SCIANA:
            poleGorne = PoleKraty(Krata, poleKraty.wiersz - 1, poleKraty.kolumna)
            naGore = ["Kierunek.GORA", poleGorne]
            polaDostepneObok.append(naGore)
    if poleKraty.kolumna + 1 < LICZBA_POL_W_POZIOMIE:  # nie poza kratę
        if Krata.krata[poleKraty.wiersz][poleKraty.kolumna + 1] != ZawartoscPola.SCIANA:
            polePrawe = PoleKraty(Krata, poleKraty.wiersz, poleKraty.kolumna + 1)
            naPrawo = ["Kierunek.PRAWO", polePrawe]
            polaDostepneObok.append(naPrawo)
    if poleKraty.wiersz + 1 < LICZBA_POL_W_PIONIE:  # nie poza kratę
        if Krata.krata[poleKraty.wiersz + 1][poleKraty.kolumna] != ZawartoscPola.SCIANA:
            poleDolne = PoleKraty(Krata, poleKraty.wiersz + 1, poleKraty.kolumna)
            naDol = ["Kierunek.DOL", poleDolne]
            polaDostepneObok.append(naDol)
    return polaDostepneObok