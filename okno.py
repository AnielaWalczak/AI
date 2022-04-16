from krata import *


class Okno(Obserwator):
    def __init__(self, krata, agent):
        self.krata = krata
        self.agent = agent
        self.krata.dolaczObserwatora(self)
        self.agent.dolaczObserwatora(self)
        self.klatkaz = pygame.time.Clock()

    def wyswietlOkno(self):
        self.klatkaz.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # print("Użytkownik spróbował zamknąć okno.")
                pygame.quit()
        self.krata.narysujKrate()
        self.agent.narysujAgenta()
        pygame.display.update()

    def odbierzPowiadomienie(self, obserwowany: Obserwowany):
        self.wyswietlOkno()
