from collections import deque
from queue import PriorityQueue

from stan_nastepnik import *


class NastepnikZKosztemSciezki:
    def __init__(self, kosztSciezki: int, nastepnik: Nastepnik):
        self.kosztSciezki = kosztSciezki
        self.nastepnik = nastepnik

    def skopiuj(self):
        return NastepnikZKosztemSciezki(self.kosztSciezki, self.nastepnik.skopiuj())

    def __lt__(self, other):
        return self.kosztSciezki <= other.kosztSciezki


def goaltest(stan: Stan, cel: Stan):
    if stan.poleStartoweGorne.wiersz != cel.poleStartoweGorne.wiersz:
        return False
    elif stan.poleStartoweGorne.kolumna != cel.poleStartoweGorne.kolumna:
        return False
    else:
        return True


def stan_w_liscie_nastepnikow(stan: Stan, lista_nastepnikow):
    for i in lista_nastepnikow:
        if i.stan.kierunek != stan.kierunek:
            continue
        elif i.stan.poleStartoweGorne.wiersz != stan.poleStartoweGorne.wiersz:
            continue
        elif i.stan.poleStartoweGorne.kolumna != stan.poleStartoweGorne.kolumna:
            continue
        else:
            return True
    return False


def stan_w_kolejce_nastepnikow(stan: Stan, kolejka_nastepnikow: PriorityQueue):
    pom = []
    znaleziono = False
    while not kolejka_nastepnikow.empty():
        element = kolejka_nastepnikow.get()
        pom.append(element)
        nastepnik_z_kosztem_sciezki: NastepnikZKosztemSciezki = element[1]
        n = nastepnik_z_kosztem_sciezki.nastepnik
        if n.stan.kierunek != stan.kierunek:
            continue
        elif n.stan.poleStartoweGorne.wiersz != stan.poleStartoweGorne.wiersz:
            continue
        elif n.stan.poleStartoweGorne.kolumna != stan.poleStartoweGorne.kolumna:
            continue
        else:
            znaleziono = True
            break
    for e in pom:
        kolejka_nastepnikow.put(e)
    return znaleziono


def stos_akcji(stan_koncowy: Nastepnik):
    stos = deque()
    while stan_koncowy.poprzednik is not None:
        stos.append(stan_koncowy.akcja)
        stan_koncowy = stan_koncowy.poprzednik
    return stos


def heurystyka(z: Stan, cel: Stan):
    kroki_w_pionie = abs(cel.poleStartoweGorne.wiersz - z.poleStartoweGorne.wiersz)
    kroki_w_poziomie = abs(cel.poleStartoweGorne.kolumna - z.poleStartoweGorne.kolumna)
    return kroki_w_pionie + kroki_w_poziomie


def koszt_wjechania(z: Stan, do: Stan):
    z_wiersz = z.poleStartoweGorne.wiersz
    z_kolumna = z.poleStartoweGorne.kolumna
    do_wiersz = do.poleStartoweGorne.wiersz
    do_kolumna = do.poleStartoweGorne.kolumna
    krata = z.poleStartoweGorne.krata.krata
    if z_wiersz == do_wiersz and z_kolumna == do_kolumna and z.kierunek == do.kierunek:
        return 0
    elif z_wiersz == do_wiersz and z_kolumna == do_kolumna and z.kierunek != do.kierunek:
        return ZawartoscPolaNaKosztObrotu[krata[do_wiersz][do_kolumna]]
    elif z.kierunek == do.kierunek:
        krok_w_pionie = (abs(z_wiersz - do_wiersz) == 1 and z_kolumna == do_kolumna)
        krok_w_poziomie = (abs(z_kolumna - do_kolumna) == 1 and z_kolumna == z_kolumna)
        if krok_w_pionie or krok_w_poziomie:
            return ZawartoscPolaNaKosztWjechania[krata[do_wiersz][do_kolumna]]
        else:
            raise "Stany nie są połączone."


def priorytet(koszt_sciezki: int, z: Stan, do: Stan, cel: Stan):
    return koszt_sciezki + koszt_wjechania(z, do) + heurystyka(do, cel)


def graphsearch(istate: Stan, cel: Stan):
    fringe = PriorityQueue()
    explored = []
    pom = NastepnikZKosztemSciezki(0, Nastepnik(None, istate, None))
    fringe.put((priorytet(0, istate, istate, cel), pom))
    # fringe.append(Nastepnik(None, istate, None))
    while not fringe.empty():
        # for i in fringe:
        #     print("F",i.stan.kierunek,i.stan.poleStartoweGorne.wiersz,i.stan.poleStartoweGorne.kolumna,end=" ")
        # print()
        element: NastepnikZKosztemSciezki = fringe.get()[1]
        koszt_sciezki = element.kosztSciezki
        nastepnik = element.nastepnik
        if goaltest(nastepnik.stan, cel):
            return stos_akcji(nastepnik)
        explored.append(nastepnik)
        for nowy in succ(nastepnik):
            if not stan_w_kolejce_nastepnikow(nowy.stan, fringe) and not stan_w_liscie_nastepnikow(nowy.stan, explored):
                z = nastepnik.stan
                do = nowy.stan
                pom = NastepnikZKosztemSciezki(koszt_sciezki + koszt_wjechania(z, do), nowy)
                pom2 = (priorytet(koszt_sciezki, z, do, cel), pom)
                fringe.put(pom2)
                # print("dodano",pom.nastepnik.stan.kierunek,pom.nastepnik.stan.poleStartoweGorne.wiersz,pom.nastepnik.stan.poleStartoweGorne.kolumna)
    return False
