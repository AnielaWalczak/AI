from collections import deque

from stan_nastepnik import *


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
