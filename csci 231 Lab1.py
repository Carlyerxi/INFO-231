####additive cipher
##
##def additive_code(word,num):
##    word = str(word)
##    num = int(num)
##    new_message = []
##    for i in range(len(word)):
##        new_message.append(chr(ord(word[i])+num))
##    return "".join(new_message)
##
##
###main
##additive_code("the essence of the free press is the reliable reasonable and moral nature of freedom the character of the censored press is the nondescript confusion of tyranny",6)
##


#For multiplicative cipher&affine cipher
plaintext = input("Please enter your message:").upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyA = int(input("Please enter your key A:"))
keyB = int(input("Please enter your key B:"))
multipleKey =int(input("Please enter your m key:"))
choice = input("Do you want to encode your message or decode?")
encodeCipher = ""
decodeCipher = ""
keyAinverse = 0


if choice == "encode":
    for word in plaintext:
        if word in alphabet:
            encodeCipher += alphabet[((keyA*(alphabet.index(word)))+keyB)%(len(alphabet))]

    print(encodeCipher)
    
elif choice == "multiplicative":
    for word in plaintext:
        if word in alphabet:
            encodeCipher += alphabet[(multipleKey*alphabet.index(word))%(len(alphabet))]
            
    print(encodeCipher)
    
else:
    for i in range(len(alphabet)):
        flag = (keyA * i)% len(alphabet)
        if flag == 1:
            keyAinverse = i
        
    for word in plaintext:
        if word in alphabet:
            decodeCipher += alphabet[keyAinverse*(alphabet.index(word)-keyB)%(len(alphabet))]
    print(decodeCipher)

