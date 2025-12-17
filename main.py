import catfact
import pokeapi
import weather

def main():
    print("Velg program:")
    print("1 - Catfact")
    print("2 - Pikachu info")
    print("3 - Vær i Oslo")

    valg = input("Skriv 1, 2 eller 3: ")

    if valg == "1":
        catfact.meow()
    elif valg == "2":
        pokeapi.pikachu()
    elif valg == "3":
        weather.oslo()
    else:
        print("Ugyldig valg")

if __name__ == "__main__":
    main()
