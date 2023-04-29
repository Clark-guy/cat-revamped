
files = ["cat.txt",
         "cat0.txt",
         "cat1.txt",
         "cat2.txt",
         "cat3.txt",
         "cat4.txt",
         "cat5.txt",
         "cat6.txt",
         "cat7.txt",
         ]


for catFile in files:
    with open(catFile, "r") as file:
        read_data = file.read()
    lines = read_data.split("\n")
    print(read_data)

    print(catFile[:4]+"L.txt")
    newChars = ""
    for line in lines:
        for x in line[::-1]:
            match x:
                case "\\":
                    newChars+="/"
                case ">":
                    newChars+="<"
                case "<":
                    newChars+=">"
                case "\\":
                    newChars+="/"
                case ")":
                    newChars+="("
                case "(":
                    newChars+=")"
                case "/":
                    newChars+="\\"
                case _:
                    newChars+=x
        newChars+="\n"
    with open(catFile[:4]+"L.txt", "w") as writeFile:
        writeFile.write(newChars)
    file.close()
    writeFile.close()
    #print(line[::-1])

    print(newChars)
