#Password Data Encryption Using Method of Overloading
import base64

def vernamE(key,message) :
    cipherTextCharacters = []
    for i in range(len(message)) :
        keyForCurrentCharacter = key[(i % len(key))]
        currentCipherTextCharacter = chr(ord(message[i]) + ord(keyForCurrentCharacter) % 256)
        cipherTextCharacters.append(currentCipherTextCharacter)
    cipherText = "".join(cipherTextCharacters)
    return cipherText
   

def vernamD(key,cipherText) :
    decryptedTextCharacters = []
    for i in range(len(cipherText)) :
        keyForCurrentCharacter = key[(i % len(key))]
        currentDecryptedTextCharacter = chr((256 + ord(cipherText[i]) - ord(keyForCurrentCharacter)) % 256) 
        decryptedTextCharacters.append(currentDecryptedTextCharacter)
    decryptedText = "".join(decryptedTextCharacters)
    return decryptedText   

def MethodOverloading(text1,text2,flag) :
    if flag is True : 
        output = vernamE(text1,text2)
        return output
    else :
        output = vernamD(text1,text2)
        return output


print("Enter your password (i.e. key) - ")
key = raw_input()
print("")
print("Enter your message to be encrypted - ")
message = raw_input()
print("")
print("This is the cipher text generated - which can totally not be cracked ;) - ")
cipherText = MethodOverloading(key,message,True)
gibberish = base64.urlsafe_b64encode(cipherText)
print(gibberish)
print("")
print("This is the decrypted message using your password which is supposed to match your original message - ")
decryptedText = MethodOverloading(key,cipherText,False)
print(decryptedText)
print("")
