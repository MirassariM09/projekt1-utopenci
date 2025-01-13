"""Zadání pro mini-projekt.
Výstupem teamu je jeden kód.
Vždy jeden sdílí obrazovku a ostatní mu radí.
Po cca 20 minutách se prostřídáte.

Základ:
Hra, kde máte peníze - 100 Kč.
Je možné chodit mezi lokacemi (Hradčany, Václavák, Holešovice)
Při přechodu do jiné lokace se přičte počet dnů.
Po 14-ti dnech hra končí
Vypíše se finální počet peněz."""

print("Vítejte ve hře")

pocatecni_zustatek = 100
dny = 0

class Lokace():
    def __init__(self, Hradcany, Vaclavak, Holesovice):
        self.Hradcany = Hradcany
        self.Vaclavak = Vaclavak
        self.Holesovice = Holesovice



input("zadaj lokaci kam chces ist")



