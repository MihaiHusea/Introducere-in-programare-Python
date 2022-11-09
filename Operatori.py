'''
Operatori:

Aritmetici: +,-,*,/,%

De comparare: <,>,==,!=,>=,<=

Logici: and, or, not
'''

a = 3
b = 5

print(a + b)
print((a + 3) - b)
print(a * b)
print((a + 7) / b)
print(12 % b)

print(a == b)  # a este egal cu b? => False
print(a != b)  # a este diferit de b? => True
print(b > a)  # a este mai mare decat b? => True
print(a < b)  # a este mai mic decat b? => True
print((a + 2) >= b)  # a+2 mai mare sau egal decat b? => True
print(a <= b)  # a este mai mic sau decat egal  b? => True

print(a < b and a < 4)  # True si True=>True
print(a < b or a < 2)  # True si False=>True
print(a < b and a < 2)  # True si False=>False

# exercitiu:
# La sedinta cu poti veni cu: mama sau tata sau cu bunicu si bunica


mama = True
tata = False
bunicu = False
bunica = False

print(mama or tata or (bunicu and bunica))  # True

mama = False
tata = False
bunicu = True
bunica = False

print(mama or tata or (bunicu and bunica))  # False
