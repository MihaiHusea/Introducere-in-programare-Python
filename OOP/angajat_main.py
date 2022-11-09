from OOP.angajat import Angajat

angajat1 = Angajat('Popescu', 'Ion', 'Contabil', 6, 4300)
angajat2 = Angajat('Ionescu', 'Adrian', 'Manager', 3, 5500)
angajat1.descriere()
angajat2.descriere()

angajat1.actualizareVechime(1)
angajat2.actualizareVechime(1)
angajat1.descriere()
angajat2.descriere()

angajat1.marireSalariu()
angajat2.marireSalariu()
angajat1.descriere()
angajat2.descriere()
