# https://refactoring.guru/pl/design-patterns/observer/python/example

from __future__ import annotations

from abc import ABC, abstractmethod


class Obserwowany(ABC):
    obserwatorzy = []

    def dolaczObserwatora(self, obserwator: Obserwator):
        self.obserwatorzy.append(obserwator)

    def odlaczObserwatora(self, obserwator: Obserwator):
        self.obserwatorzy.remove(obserwator)

    @abstractmethod
    def powiadomObserwatorow(self):
        """
        Notify all observers about an event.
        """
        pass


class Obserwator(ABC):
    @abstractmethod
    def odbierzPowiadomienie(self, obserwowany: Obserwowany):
        """
        Receive update from subject.
        """
        pass
