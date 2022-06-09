while True:
    # Creature and location variables to store name and place
    creature = input("What is the creature? ")
    # If, instead of introducing a valid creature, 'stop' is introduced, then program exists
    if creature == "stop":
        exit()
    location = input("What is the location? ")
    # Conditionals to print the correct phrase
    if (creature == "Kraken" or creature == "Hipocampo" or creature == "Pulpo") and (location == "babor" or location == "estribor"):
        print(f"¡Ahoy! capitán, un {creature} a {location}")        
    elif (creature == "Kraken" or creature == "Hipocampo" or creature == "Pulpo") and (location == "proa" or location == "popa"):
        print(f"¡Ahoy! capitán, un {creature} por la {location}")
    elif (creature == "Ballena" or creature == "Macaraprono") and (location == "babor" or location == "estribor"):
        print(f"¡Ahoy! capitán, una {creature} a {location}")
    elif (creature == "Ballena" or creature == "Macaraprono") and (location == "proa" or location == "popa"):
        print(f"¡Ahoy! capitán, un {creature} por la {location}")
    elif creature == "Leviatanes" and (location == "babor" or location == "estribor"):
        print(f"¡Ahoy! capitán, unos {creature} a {location}")
    elif creature == "Leviatanes" and (location == "proa" or location == "popa"):
        print(f"¡Ahoy! capitán, unos {creature} por la {location}")
    elif (creature == "Sirenas" or creature == "Hidras") and (location == "babor" or location == "estribor"):
        print(f"¡Ahoy! capitán, unas {creature} a {location}")
    elif (creature == "Sirenas" or creature == "Hidras") and (location == "proa" or location == "popa"):
        print(f"¡Ahoy! capitán, unas {creature} por la {location}")