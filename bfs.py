from collections import deque

from krata import *


class Akcja(Enum):
    OBROT_W_LEWO = 0
    OBROT_W_PRAWO = 1
    KROK_W_PRZOD = 2


class Stan:
    def __init__(self, kierunek: Kierunek, poleStartoweGorne: PoleKraty):
        self.kierunek = kierunek
        self.poleStartoweGorne = poleStartoweGorne

    def skopiuj(self):
        return Stan(self.kierunek, self.poleStartoweGorne.skopiuj())


class Nastepnik:
    def __init__(self, akcja: Akcja or None, stan: Stan, poprzednik):
        self.akcja = akcja
        self.stan = stan
        self._poprzednik = poprzednik

    def getPoprzednik(self):
        return self._poprzednik

    def setPoprzednik(self, x):
        raise Exception

    poprzednik = property(getPoprzednik, setPoprzednik)

    def skopiuj(self):
        return Nastepnik(self.akcja, self.stan.skopiuj(), self.poprzednik)


def nastepnik_obrotu_w_lewo(nastepnik: Nastepnik):
    akcja = Akcja.OBROT_W_LEWO
    stan = Stan(nastepnik.stan.kierunek.kierunekNaLewo(), nastepnik.stan.poleStartoweGorne)
    return Nastepnik(akcja, stan, nastepnik)


def nastepnik_obrotu_w_prawo(nastepnik: Nastepnik):
    akcja = Akcja.OBROT_W_PRAWO
    stan = Stan(nastepnik.stan.kierunek.kierunekNaPrawo(), nastepnik.stan.poleStartoweGorne)
    return Nastepnik(akcja, stan, nastepnik)


def nastepnik_kroku_w_przod(nastepnik: Nastepnik):
    akcja = Akcja.KROK_W_PRZOD
    stan = Stan(nastepnik.stan.kierunek, nastepnik.stan.poleStartoweGorne)
    if stan.kierunek == Kierunek.POLNOC:
        stan.poleStartoweGorne.wiersz -= 1
    elif stan.kierunek == Kierunek.POLUDNIE:
        stan.poleStartoweGorne.wiersz += 1
    elif stan.kierunek == Kierunek.ZACHOD:
        stan.poleStartoweGorne.kolumna -= 1
    elif stan.kierunek == Kierunek.WSCHOD:
        stan.poleStartoweGorne.kolumna += 1
    return Nastepnik(akcja, stan, nastepnik)


def pole_w_granicach_kraty(pole: PoleKraty):
    if pole.wiersz not in range(0, pole.krata.liczbaPolPionowo):
        return False
    elif pole.kolumna not in range(0, pole.krata.liczbaPolPoziomo):
        return False
    else:
        return True


def pole_puste(pole: PoleKraty):
    if pole.krata.krata[pole.wiersz][pole.kolumna] in (ZawartoscPola.PUSTE, ZawartoscPola.CEL):
        return True
    else:
        return False


def mozna_zrobic_krok_w_przod(nastepnik: Nastepnik):
    nastepnik = nastepnik_kroku_w_przod(nastepnik)
    if pole_w_granicach_kraty(nastepnik.stan.poleStartoweGorne) and pole_puste(nastepnik.stan.poleStartoweGorne):
        return True
    else:
        return False


def succ(nastepnik: Nastepnik):
    wynik = []
    pom = nastepnik.skopiuj()
    wynik.append(nastepnik_obrotu_w_lewo(pom))
    pom = nastepnik.skopiuj()
    wynik.append(nastepnik_obrotu_w_prawo(pom))
    pom = nastepnik.skopiuj()
    if mozna_zrobic_krok_w_przod(pom):
        pom = nastepnik.skopiuj()
        wynik.append(nastepnik_kroku_w_przod(pom))
    return wynik


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


def stos_akcji(stan_koncowy: Nastepnik):
    stos = deque()
    while stan_koncowy.poprzednik is not None:
        stos.append(stan_koncowy.akcja)
        stan_koncowy = stan_koncowy.poprzednik
    return stos


def graphsearch(istate: Stan, cel: Stan):
    fringe = deque()
    explored = []
    fringe.append(Nastepnik(None, istate, None))
    while fringe:
        # for i in fringe:
        #     print("F",i.stan.kierunek,i.stan.poleStartoweGorne.wiersz,i.stan.poleStartoweGorne.kolumna,end=" ")
        # print()
        element: Nastepnik = fringe.popleft()
        if goaltest(element.stan, cel):
            return stos_akcji(element)
        explored.append(element)
        for nastepnik in succ(element):
            if not stan_w_liscie_nastepnikow(nastepnik.stan, fringe) and not stan_w_liscie_nastepnikow(nastepnik.stan,
                                                                                                       explored):
                fringe.append(nastepnik)
    return False
