import requests

def pikachu():
    svar = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    data = svar.json()

    hoyde = data["height"] / 10
    vekt = data["weight"] / 10

    print("Pikachu:")
    print("Høyde:", hoyde, "meter")
    print("Vekt:", vekt, "kg")