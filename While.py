# problema: masina merge cat timp are benzina

litri_benzina = 10

while litri_benzina > 0:
    # acceleram
    print('Masina accelereaza!')
    # scadem benzina
    litri_benzina -= 1
    if litri_benzina <= 3:
        print('Se aprinde becul rosu!')
print('STOP!')
