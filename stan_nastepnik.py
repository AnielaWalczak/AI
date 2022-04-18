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


def mozna_wjechac_na_pole(pole: PoleKraty):
    if pole.krata.krata[pole.wiersz][pole.kolumna] != ZawartoscPola.SCIANA:
        return True
    else:
        return False


def mozna_zrobic_krok_w_przod(nastepnik: Nastepnik):
    nastepnik = nastepnik_kroku_w_przod(nastepnik)
    if pole_w_granicach_kraty(nastepnik.stan.poleStartoweGorne) and mozna_wjechac_na_pole(
            nastepnik.stan.poleStartoweGorne):
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
