from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word (press Enter to exit): ")
    if word == "":
        print("Exiting the program.")
        break
    
    meaning = dictionary.meaning(word)
    if meaning:
        print(f"Meaning of '{word}':")
        for key, value in meaning.items():
            print(f"{key}: {', '.join(value)}")
    else:
        print(f"Sorry, the meaning of '{word}' could not be found.")
