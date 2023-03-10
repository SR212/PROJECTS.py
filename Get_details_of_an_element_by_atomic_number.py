from periodictable import*

# Get details of an element by atomic number
Z=int(input("entre le numero atomique:"))
element=elements[Z]
print(f"Z= {element.number}")
print(f"Symbole: {element.symbol}")
print(f"Nom: {element.name}")
print(f"Masse_Atomique: {element.mass}")
print(f"Densite: {element.density}")
