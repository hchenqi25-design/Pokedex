pokedex = {
    "Bulbasaur": {
        "tipos": ["Planta", "Veneno"],
        "daño_base": 45
    },
    "Charmander": {
        "tipos": ["Fuego"],
        "daño_base": 52
    },
    "Squirtle": {
        "tipos": ["Agua"],
        "daño_base": 48
    },
    "Pikachu": {
        "tipos": ["Eléctrico"],
        "daño_base": 55
    },
    "Jigglypuff": {
        "tipos": ["Normal"],
        "daño_base": 45
    },
    "Gengar": {
        "tipos": ["Fantasma", "Veneno"],
        "daño_base": 65
    },
    "Lapras": {
        "tipos": ["Agua", "Hielo"],
        "daño_base": 85
    },
    "Snorlax": {
        "tipos": ["Normal"],
        "daño_base": 110
    },
    "Dratini": {
        "tipos": ["Dragón"],
        "daño_base": 64
    },
    "Mewtwo": {
        "tipos": ["Psíquico"],
        "daño_base": 110
    },
}

#Consultar valor de una clave
salario = input("Ingresa el nombre del pokemon que quieras buscar => ")
print(pokedex[salario])

#Añadir pokemon
def añadir_pokemon():
    nombre = input("Nombre del nuevo Pokémon => ").capitalize()
    tipo = input("Tipo => ").capitalize()
    dano = int(input("Daño base => "))

    pokedex[nombre] = {
        "tipos": [tipo],
        "daño_base": dano
    }

    print(f"Los datos de {nombre} son {pokedex[nombre]}")

añadir_pokemon()

#Modificar valor
def modificar_pokemon():
    nombre = input("Nombre del Pokémon a modificar => ")

    if nombre in pokedex:
        tipo = input("Nuevo tipo => ")
        dano = int(input("Nuevo daño base => "))

        pokedex[nombre]["tipos"] = [tipo]
        pokedex[nombre]["daño_base"] = dano

        print(f"Los datos de {nombre} son {pokedex[nombre]}")
    else:
        print("Po kémon no encontrado")


modificar_pokemon()

#Cambiar valor de daño
def modificar_dano():
    nombre = input("Nombre del Pokémon a modificar => ")

    if nombre in pokedex:
        dano = int(input("Nuevo daño base => "))
        pokedex[nombre]["daño_base"] = dano
        print(f"El nuevo daño de {nombre} es {pokedex[nombre]['daño_base']}")
    else:
        print("Pokémon no encontrado")

modificar_dano()

#Eliminar pokemon
def eliminar_pokemon():
    nombre = input("Nombre del Pokémon a eliminar => ")

    if nombre in pokedex:
        del pokedex[nombre]
        print(f"{nombre} eliminado correctamente")
    else:
        print("Pokémon no encontrado")

eliminar_pokemon()

#Recorrer el diccionario
for p in pokedex:
    print(p)
    print(pokedex[p])

