# def printGreeting():
#     print('Buna ziua! Bine ati venit!')
#
#
# def printGreetingBYName(prenume, nume):
#     print(f'Buna ziua {prenume} {nume}! Bine ati venit!')
#
#
# def mediaNr(a, b, c):
#     return (a + b + c) / 3
#
#
# def piValue():
#     return 3.14
#
#
# # exercitiu: daca persoana este majora, returnati true, altfel false
#
# def verificareMajor(varsta):
#     if varsta >= 18:
#         return True
#     else:
#         return False
#
#
# # zona de apelare(desktop)
# printGreeting()
# printGreeting()
# printGreetingBYName('James', 'Bond')
# printGreetingBYName('John', 'Wayne')
# print('Media este: ', mediaNr(4, 5, 8))
# print('Valoarea nr. Pi este: ', piValue())
# print('Verificare varsta persoana majora: ', verificareMajor(18))
# print('Verificare varsta persoana majora: ', verificareMajor(17))
# print('Verificare varsta persoana majora: ', verificareMajor(19))
#
# # se ia varsta utilizatorului
#
# age = int(input('Introduceti varsta: '))
# if verificareMajor(age):
#     print('Cont creat! Bun venit in aplicatie!')
# else:
#     print('Nu aveti varsta minima necesara(18) pentru a paria!')


# cel nr. maxim din 3 numere

def maxim(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(maxim(27, 45, 12))
