# # if
#
# piesa_faina = True
# print('Pornim radioul!')
# if piesa_faina:
#     print('Dau radioul mai tare!')
#     print('Incep sa cant!')
# print('Oprim radioul!')
#
# # if else
# # daca numarul este par printam acest lucru
# # altfel printam impar
#
# nr = int(input('Numarul este: '))
# if nr % 2 == 0:
#     print('Numarul este par!')
# else:
#     print('Numarul este impar!')
#
# #Este un numar pozitiv?
#
# if nr >0:
#     print('Numarul este pozitiv!')
# else:
#     print('Numarul nu este pozitiv!')
#
# #daca utilizatorul are sub 18 ani , nu poate paria
#
# varsta=int(input('Introduceti varsta: '))
#
# if varsta >=18:
#     print('Puteti sa pariati!')
# else:
#     print('Ne pare rau! Nu puteti sa pariati!')
#
#
# # if, else if, if
# #cum ne saluta robotelul in functie de ora
#
# ora=int(input('Ora este: '))
# if ora <0:
#     print('Ora negativa!')
# elif ora <=11:
#     print('Buna dimineata!')
# elif ora<= 18:
#     print('Buna ziua!')
# elif ora <=22:
#     print('Buna seara!')
# elif ora <=24:
#     print('Noapte buna!')
# else:
#     print('ora mai mare decat 24!')

# robotel telefonic
optiune = int(input('Alegeti o optiune: '))
if optiune == 0:
    print('Meniu anterior')
elif optiune == 1:
    print('Ati ales limba romana!')
elif optiune == 2:
    print('Ati ales limba engleaza!')
else:
    print('Eroare! Nu am identificat optiunea! Mai incearca!')
