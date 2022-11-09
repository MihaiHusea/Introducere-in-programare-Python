# Listele in Python pot sa cuprinda elemente de tipuri diferite
# Au dimensiune dinamica

fructe = ["mar", "banana", "portocala", 3, True, 3]

# Afisam o lista:
print(fructe)

# Accesam un element in functie de index

print(fructe[1])

# Adaugam un element nou

fructe.append('rosie')
print(fructe)

# Suprascriem un element

fructe[0] = "para"
print(fructe)

# Dimensiunea listei

print(len(fructe))

# Scoate si ne returneaza ultimul element

last = fructe.pop()
print('ultimul element este: ', last)
print('noua lista este: ', fructe)

# De cate ori apare un element
print('elementul "3" apare de: ', fructe.count(3), 'ori')

# extindem lista
fructe_exotice = ["ananas", "kiwi"]
fructe.extend(fructe_exotice)
print(fructe)
