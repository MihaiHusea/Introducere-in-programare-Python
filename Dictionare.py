dict_gol = {}

# Declaram si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# Adaugam elemente
note_elevi['Sebi'] = 7
print(note_elevi)

# Aflam elemente din dict

print(note_elevi['Gigel'])
# sau
print(note_elevi.get("Gigel"))

# Actualizam valori

note_elevi['Costel'] = 10
print(note_elevi)

# Aflam dimensiunea

print(len(note_elevi))

# Stergem valori

note_elevi.pop('Gigel')
print(note_elevi)
print(note_elevi.get('Gigel', 'Acest elev nu mai este'))

# returneaza doar cheile
print(note_elevi.keys())
