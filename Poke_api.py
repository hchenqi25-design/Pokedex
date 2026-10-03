import random
import requests

POKEMON = [
    (1, "Bulbasaur"), (4, "Charmander"), (7, "Squirtle"), (25, "Pikachu"),
    (39, "Jigglypuff"), (52, "Meowth"), (54, "Psyduck"), (94, "Gengar"),
    (133, "Eevee"), (143, "Snorlax"), (150, "Mewtwo"), (151, "Mew"),
    (152, "Chikorita"), (155, "Cyndaquil"), (158, "Totodile"), (249, "Lugia"),
    (250, "Ho-Oh"), (384, "Rayquaza"), (445, "Garchomp"), (448, "Lucario")
]

MODOS = ["sonido", "tipo", "movimientos"]

print("=== ¿Quién es ese Pokémon? ===")
print("Modos: sonido, tipo, movimientos")
modo = input("Elige modo: ").strip().lower()

if modo not in MODOS:
    print("Modo no válido.")
    exit()

pokemon_id, nombre_correcto = random.choice(POKEMON)
datos = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}").json()

intentos = 3

if modo == "sonido":
    sonido = datos["cries"].get("latest") or datos["cries"].get("legacy")
    print(f"\n🔊 Sonido del Pokémon: {sonido}")
    print("(Copia y pega la URL en tu navegador para escucharlo)")

elif modo == "tipo":
    tipos = [t["type"]["name"] for t in datos["types"]]
    print(f"\n🔥 Tipos: {', '.join(tipos)}")

elif modo == "movimientos":
    movimientos = [m["move"]["name"] for m in datos["moves"]]
    muestra = random.sample(movimientos, min(5, len(movimientos)))
    print(f"\n⚡ Movimientos: {', '.join(muestra)}")

print(f"\nTienes {intentos} intentos.\n")

for i in range(1, intentos + 1):
    respuesta = input(f"Intento {i}: ").strip().lower()
    if respuesta == nombre_correcto.lower():
        print(f"✅ ¡Correcto! Era {nombre_correcto}.")
        break
    else:
        restantes = intentos - i
        if restantes > 0:
            print(f"❌ Incorrecto. Te quedan {restantes} intento(s).")
        else:
            print(f"💀 Se acabaron los intentos. Era {nombre_correcto}.")