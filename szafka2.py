import miejsce


class Szafka:
    def __init__(self, numerSzafki, rozmiar, iloscPolek, iloscMiejscNaPolce):
        self.numer = numerSzafki
        # np. A
        self.rozmiarMiejsc = rozmiar
        # średni, duży, mały
        # self.iloscWolnychMiejsc = iloscPolek*iloscMiejscNaPolce
        self.iloscPolek = iloscPolek
        self.iloscMiejscNaPolce = iloscMiejscNaPolce
        self.listaMiejsc = []
        self.listaWolnychMiejsc = []
        self.stworzMiejsca()

    def stworzMiejsca(self):
        j = 0  # półka
        k = 0
        while j < self.iloscPolek:
            name = self.numer + "/" + str(j) + "/" + str(k)
            nowe_miejsce = miejsce.Miejsce(name, j, k)
            self.listaMiejsc.append(nowe_miejsce)
            k = k + 1
            if k > self.iloscMiejscNaPolce - 1:
                j = j + 1
                k = 0

        self.listaWolnychMiejsc = self.listaMiejsc.copy()

    def polozPaczke(self, numerPaczki):
        if len(self.listaWolnychMiejsc) != 0:
            self.listaWolnychMiejsc[0].numerUmieszczonejPaczki = numerPaczki
            self.listaWolnychMiejsc[0].status = "zajęte"
            self.listaWolnychMiejsc.pop(0)
