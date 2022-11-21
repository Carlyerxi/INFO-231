##additive cipher

def additive_code(word,num):
    word = str(word)
    num = int(num)
    new_message = []
    for i in range(len(word)):
        new_message.append(chr(ord(word[i])+num))
    return "".join(new_message)


#main
additive_code("the essence of the free press is the reliable reasonable and moral nature of freedom the character of the censored press is the nondescript confusion of tyranny",6)




