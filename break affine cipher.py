#set up a plaintext allow user to input message and change it to uppercase
#plaintext = input("Please enter your message:").upper()
#set up alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,. ;:!"
#2 keys A and B in affine cipher
#keyA = int(input("Please enter your key A:"))
#keyB = int(input("Please enter your key B:"))
#let user choice to encode or decode
#choice = input("Do you want to encode your message or decode?")
#create two empty list to store new message
encodeCipher = ""
#set an a^-1 to 0
keyAinverse = 0

plaintext = "CWF FSK AAC KHW JAO ZHA NGA THO ZUW ENC AKK MUA KJA HR"
##plaintext = "VYU XOX SJY YTS FXV OWM YFQ GCQ PPY CQP VQD OFP VQJ ODW PRT SEQ"
#plaintext = "KFM YGV VEM VHK AWK YZK FWG RKF MSJ JZG XOJ MEM DJZ MAM SCJ GKF EJK TSF GJI STM ZSW MKF MEJ KBS XGJ SFH PMJ JIK FME JKR MSZ"
decodeCipers = [] 
for keyA in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
    for keyB in range(0, 26):
        decodeCipher = ""
        for i in range(len(alphabet)):
            remain = (keyA * i)% len(alphabet)
            if remain == 1:
                keyAinverse = i
        
        for word in plaintext:
            if word in alphabet:
            #decryption function D(x)=a^-1(x-b) mod m
                decodeCipher += alphabet[(keyA * alphabet.index(word)+keyB)%(len(alphabet))]
        #print(decodeCipher)
        ##try on to be in the one as key word
        if("molly" in decodeCipher.lower()):
            decodeCipers.append(decodeCipher)
            
            print(decodeCipher.lower())
            print(keyA)
            print(keyB)
#print(len(decodeCipers))
#for d in decodeCipers:
#    print(d.lower())
    #    if "affine" in d.lower():
#        print(d)

