import os

from klasy import *

from agenci import *

OKNO = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Okno1")
Krata = Krata(OKNO)


def wyswietl_agentow():
    for a in Agent1.Agenci:
        OKNO.blit(a.tekstura, (a.hitbox.x, a.hitbox.y))
        if a.droga == 0:
            a.obierzNowyKierunek()
            a.okreslDlugoscDrogi()
        # a.ruszSie(Agenci1)
    pygame.display.update()


def czy_wylosowane_dla_agenta_pola_sa_puste(pole_lewe_gorne):
    wynik = True
    for wiersz in range(pole_lewe_gorne.wiersz, pole_lewe_gorne.wiersz + BOK_AGENTA1_W_POLACH):
        for kolumna in range(pole_lewe_gorne.kolumna, pole_lewe_gorne.kolumna + BOK_AGENTA1_W_POLACH):
            if Krata.krata[wiersz][kolumna] != POLE.PUSTE:
                wynik = False
                break
        if wynik == False:
            break
    return wynik


def dodaj_agenta1():
    los = None
    if len(Agent1.Agenci) in range(0, 40):
        los = random.randint(1, 150)
    elif len(Agent1.Agenci) in range(40, 50):
        los = random.randint(1, 15)
    if los != None:
        pom = None
        if los in (1, 2) or len(Agent1.Agenci) == 0:
            pom = 'wozek.png'
        elif los in (3, 4):
            pom = 'wozek_ze_skrzynka.png'
        elif los == 5 and len(Agent1.Agenci) > 6:
            pom = 'traktor_ikona.png'
        if pom != None:
            pole_lewe_gorne = Pole(random.randint(0, LICZBA_POL_W_PIONIE - BOK_AGENTA1_W_POLACH),
                                   random.randint(0, LICZBA_POL_W_POZIOMIE - BOK_AGENTA1_W_POLACH))
            if len(Agent1.Agenci) == 0:
                pole_lewe_gorne = Pole(0, 0)
            if czy_wylosowane_dla_agenta_pola_sa_puste(pole_lewe_gorne):
                pom = 'test1_ikona.png'
                ikona = pygame.transform.scale(pygame.image.load(os.path.join('Ikony', pom)),
                                               (BOK_AGENTA1, BOK_AGENTA1))
                nowy_agent = Agent1(pole_lewe_gorne, ikona, KIERUNEK.GORA, 0)
                nowy_agent.zaznacz_zajmowane_pola_na_kracie(Krata)
                Agent1.Agenci.append(nowy_agent)
        # print(Krata)


def main():
    klatkaz = pygame.time.Clock()
    warunek_dzialania = True
    while warunek_dzialania:
        klatkaz.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                warunek_dzialania = False
                break
        Krata.wyswietl_krate()
        wyswietl_agentow()
        dodaj_agenta1()
    pygame.quit()


main()
