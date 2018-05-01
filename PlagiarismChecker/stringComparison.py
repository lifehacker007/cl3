import string 

def PlagiarismChecker(text1 , text2) :
    cleanCharacters = string.letters + string.digits + "- " 

    cleanString1 = filter(lambda c: c in cleanCharacters, text1)
    cleanString2 = filter(lambda c: c in cleanCharacters, text2)

    cleanWords1 = cleanString1.split() 
    cleanWords2 = cleanString2.split()

    if "is" in cleanWords1 : cleanWords1.remove("is")
    if "the" in cleanWords1 : cleanWords1.remove("the")
    if "a" in cleanWords1 : cleanWords1.remove("a")
    if "in" in cleanWords1 : cleanWords1.remove("in")

    if "is" in cleanWords2 : cleanWords2.remove("is")   
    if "the" in cleanWords2 : cleanWords2.remove("the")
    if "a" in cleanWords2 : cleanWords2.remove("a")
    if "in" in cleanWords2 : cleanWords2.remove("in")

    kitneWordsCopyKiye = len(set(cleanWords1) & set(cleanWords2)) 
    similarityFlag = False
    smallerLength = 0

    if len(cleanWords1) <= len(cleanWords2) :
        smallerLength = len(cleanWords1)
    else :
        smallerLength = len(cleanWords2)

    if kitneWordsCopyKiye >= (0.5 * smallerLength) :
        similarityFlag = True

    return similarityFlag

if __name__ == "__main__":
    print("")
