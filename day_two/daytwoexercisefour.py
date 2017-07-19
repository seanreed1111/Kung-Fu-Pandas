def caesarcypher():
    string = input("Please provide your message:\n")
    if type(string) != str:
        print("{} is not a string.".format(string))
    else:
        num = int(input("Please provide the shift amount as an integer:"))
        cypheredString = ""
        for character in string:
            if ord(character) in range(97, 97+26):
                characterNumber = ord(character)
                #print(characterNumber)
                #print(characterNumber + num)
                #there is also the condition of characterNumber being smaller than 97
                if (characterNumber + num) > 122:
                    difference = characterNumber + num - 122
                    newCharacter = chr(97 + difference - 1)
                    cypheredString += newCharacter
                elif (characterNumber + num) < 97:
                    difference = characterNumber + num -97
                    newCharacter = chr(122 + (difference+1))
                    cypheredString += newCharacter
                else:    
                    newCharacter = chr(characterNumber + num)
                    cypheredString += newCharacter
            elif ord(character) in range(65, 65+26):
                characterNumber = ord(character)
                if (characterNumber + num) > 90:
                    difference = characterNumber + num - 90
                    newCharacter = chr(65 + difference - 1)
                    cypheredString += newCharacter
                elif (characterNumber + num) < 65:
                    difference = characterNumber + num -65
                    newCharacter = chr(90 + (difference+1))
                    cypheredString += newCharacter
                else:    
                    newCharacter = chr(characterNumber + num)
                    cypheredString += newCharacter
            else:
                cypheredString += character
        print("\n")
        print("{} when ceasarfied is equal to {}.".format(string, cypheredString))
        print("\n")

caesarcypher()