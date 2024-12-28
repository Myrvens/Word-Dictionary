import requests

while True:
    word = input("Enter your word: ")
    if word == "":
        break

    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        definitions = data[0]["meanings"][0]["definitions"]
        print(f"Definitions of {word}:")
        for i, definition in enumerate(definitions, start=1):
            print(f"{i}. {definition['definition']}")
    else:
        print("Word not found.")
