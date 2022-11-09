class ContBancar:
    # constructor
    def __init__(self, titularCont, iban):
        # atribute,fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    # metode

    def descriere(self):
        print(f'Titular cont: {self.titularCont}')
        print(f'IBAN: {self.iban}')
        print(f'Sold: {self.sold}')
        print(f'Activ: {self.activ}')
        print(f'Numar de incercari: {self.incercari_activare}')
        print(f'---------------------------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            self.activ = True
            print(f'Contul a fost activat!')
            print(f'---------------------------------------------')
        else:
            print(f'PIN gresit!')
            print(f'---------------------------------------------')
            self.incercari_activare += 1

    def alimentareCont(self, suma):
        self.sold += suma
        self.salut()
        print(f'Ati depus suma de: {suma} lei. Soldul actual este: {self.sold}')
        print(f'---------------------------------------------')

    def debitareCont(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            self.salut()
            print(f'Ati retras cu succes suma de: {suma} lei. Soldul actual este: {self.sold}')
            print(f'---------------------------------------------')
        else:
            self.salut()
            print(f'Suma de {suma}, nu poate fi debitata! Fonduri insuficiente! Sold actual:{self.sold}')
            print(f'---------------------------------------------')

    def salut(self):
        print(f'Buna ziua {self.titularCont}!')
