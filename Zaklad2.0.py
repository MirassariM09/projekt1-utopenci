


"""Základ:
Hra, kde máte peníze - 100 Kč.
Je možné chodit mezi lokacemi (Hradčany, Václavák, Holešovice)
Při přechodu do jiné lokace je přičte počet dnů.
Po 14-ti dnech hra končí
Vypíše se finální počet peněz.

Rozšíření 1:
V každé lokace je možné kupovat předměty:
Utopenec (50-100kč)
Med (100-200kč)
Láhev pálavy (200-500kč)
"""

"""Pozn.
Úloha slouží k procvičení objektového programování - tzn:
Předmět je třída - pamatujeme si min a max cenu. Pamatuje si aktuální cenu.
Lokace je třída - v lokacích jsou uložené přeměty
Osoba je třída - pamatujeme si počet předmětů, kolik máme peněz, jestli máme kabát...

Každá třída bude v jiném souboru - procvičíme importy.
"""
print("vitejte ve hře")

penize = 100

pocet_dnu = 0

class Lokace:
    def __init__(self, nazev):
        self.nazev = nazev

    def __repr__(self):
        return f"cast mesta {self.nazev}"
"""
        #když přesun, tak se přičte den
    for a in range(14):
        pocet_dnu += 1
        if pocet_dnu >= 14:
            print("skončil jsi")
        elif pocet_dnu < 14:
            input("Zadej lokaci kam chces jit")
        else:
            print("neplatna lokace")
"""


lokace = [Lokace("Holesovice"), Lokace("Hradcany"), Lokace("Vaclavak")]

aktualni_lokace = lokace[0]


while pocet_dnu < 14:
    for i in lokace:
        print(i)

    print(f"dnes je pocet dnu {pocet_dnu}")
    odpoved_uzivatele = input("Zadej kam chces jít(muzes zadat 0,1,2)")
    aktualni_lokace = lokace[int(odpoved_uzivatele)]
    print(f"uzivatel jde do lokace {lokace[int(odpoved_uzivatele)]}")
    pocet_dnu += 1


