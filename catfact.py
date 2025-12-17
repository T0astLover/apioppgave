import requests

def meow():
    url = "https://catfact.ninja/fact"
    svar = requests.get(url)

    if svar.status_code == 200:
        data = svar.json()
        print("Kattefakta:")
        print(data["fact"])