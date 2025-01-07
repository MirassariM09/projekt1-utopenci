"""Zadání pro mini-projekt.
Výstupem teamu je jeden kód.
Vždy jeden sdílí obrazovku a ostatní mu radí.
Po cca 20 minutách se prostřídáte.

Základ:
Hra, kde máte peníze - 100 Kč.
Je možné chodit mezi lokacemi (Hradčany, Václavák, Holešovice)
Při přechodu do jiné lokace je přičte počet dnů.
Po 14-ti dnech hra končí
Vypíše se finální počet peněz."""

print("Vítejte ve hře")

pocatecni_zustatek = 100

class Lokace():
    def __init__ (self,lokace):

        Hradčany = Lokace
        Václavák = Lokace
        Holešovice = Lokace

input("zadaj lokace kam chceš isť")
print(f"zadal si lokace {Lokace}")

