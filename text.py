input1 = input ("Enter text ")
l = len(input1)

print("Original text : " + input1)
for x in range(0, l):
    c = input1[x]
    c = c.upper()
    if (c == "A"):
        print(".- |  a")
    elif (c == "B"):
        print("-... | b")
    elif (c == "C"):
        print(" -.-. | c")
    elif (c == "D"):
        print("-.. | d")
    elif (c == "E"):
        print(". | e")
    elif (c == "F"):
        print("..-. | f")
    elif (c == "G"):
        print("--. | g")
    elif (c == "H"):
        print(".... | h")
    elif (c == "I"):
        print(".. | i")
    elif (c == "J"):
        print(".--- | j")
    elif (c == "K"):
        print("-.- | k")
    elif (c == "L"):
        print(".-.. | l")
    elif (c == "M"):
        print("-- | m")
    elif (c == "N"):
        print("-. | n")
    elif (c == "O"):
        print("--- | o")
    elif (c == "P"):
        print(".--. | p")
    elif (c == "Q"):
        print(" --.- | q")
    elif (c == "R"):
        print(".-. | r")
    elif (c == "S"):
        print("... | s")
    elif (c == "T"):
        print("- | t")
    elif (c == "U"):
        print("..- | u")
    elif (c == "V"):
        print("...- | v")
    elif (c == "W"):
        print(".-- | w")
    elif (c == "X"):
        print("-..- | x")
    elif (c == "Y"):
        print("-.-- | y")
    elif (c == "Z"):
        print("--.. | z")
    elif (c == " "):
        print(" ")
    elif (c == "!"):
        print("Not existing/translatable in morse code. | !\n")
    elif (c == "?"):
        print("..--.. | ?")
    elif (c == "@"):
        print(".--.-. | @")
    elif (c == "/"):
        print("-..-. | /")
    elif (c == "."):
        print(".-.-.- | .")
    elif (c == ","):
        print("--..-- | ,]")
    elif (c == "1"):
        print(".---- | 1")
    elif (c == "2"):
        print("..--- | 2")
    elif (c == "3"):
        print("...-- | 3")
    elif (c == "4"):
        print("....- | 4")
    elif (c == "5"):
        print("..... | 5")
    elif (c == "6"):
        print("-.... | 6")
    elif (c == "7"):
        print("--... | 7")
    elif (c == "8"):
        print("---.. | 8")
    elif (c == "9"):
        print("----. | 9")
    elif (c == "0"):
        print("----- | 0")

