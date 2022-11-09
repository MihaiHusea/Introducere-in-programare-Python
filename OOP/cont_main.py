from OOP.cont_bancar import ContBancar

cont1 = ContBancar('John Wayne', 'RO0001')
cont2 = ContBancar('Mary Wayne', 'RO0002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.descriere()
cont2.descriere()

cont1.alimentareCont(700)
cont2.alimentareCont(500)
cont2.alimentareCont(700)

cont1.debitareCont(750)
cont1.debitareCont(700)

cont2.debitareCont(300)
cont2.debitareCont(200)
