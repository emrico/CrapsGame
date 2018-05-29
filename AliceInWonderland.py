# First Read File
# Variable LetterOf Interest

file = open("alice_in_wonderland.dat","r")
filecontents = file.read()
number_of_e = 0
letter_count = 0

for character in filecontents:
    letter = ord(character)
    if((letter > 64 and letter < 91) or (letter > 96 and letter < 123)):
        letter_count += 1
        if((letter == 69) or (letter == 101)):
            number_of_e += 1
file.close()


print("\nTotal Number Of Letters: {}".format(letter_count))
print("Number of e's: {}".format(number_of_e))
print("{:.1f}% of all the letters are e's\n".format((number_of_e / letter_count)*100))
