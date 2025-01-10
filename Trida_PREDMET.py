
print("Máš možnost si koupit tyto předměty: ")
class Predmet:
    def __init__(self, nazev, min_cena, max_cena):
        self.nazev = nazev
        self.min_cena = min_cena
        self.max_cena = max_cena

    def printit(self):
        print(f"Predmet {self.nazev} min.cena {self.min_cena} max_cena {self.max_cena}")

# pro kazdy predmet přiřadíme cenu
utopenec = Predmet("utopenec", 50, 100)
utopenec.printit()
med = Predmet("med", 100, 200)
med.printit()
palava = Predmet("palava", 200, 500)
palava.printit()