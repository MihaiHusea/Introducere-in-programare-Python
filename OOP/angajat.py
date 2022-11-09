class Angajat():

    def __init__(self, nume, prenume, functie, vechime, salariu):
        self.nume = nume
        self.prenume = prenume
        self.functie = functie
        self.vechime = vechime
        self.salariu = salariu

    def descriere(self):
        print(f'-----------------------')
        print(f'Nume: {self.nume}')
        print(f'Prenume: {self.prenume}')
        print(f'Functie: {self.functie}')
        print(f'Vechime: {self.vechime}')
        print(f'Salariu: {self.salariu}')
        print(f'-----------------------')

    def actualizareVechime(self, noua_vechime):
        self.vechime += noua_vechime

    def marireSalariu(self):
        if self.vechime < 5:
            self.salariu += 300
            print(f'Marirea salariala este de 300 de lei. Noul salariu este: {self.salariu} de lei')
        elif self.vechime >= 5:
            self.salariu += 500
            print(f'Marirea salariala este de 500 de lei. Noul salariu este: {self.salariu} de lei')
