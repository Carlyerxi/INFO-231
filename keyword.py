import re

secretkey = raw_input("Please Enter Keywords: ")
str(secretkey) = ''.join(x for i, x in enumerate(secretkey)
            if secretkey.index(x) == i)
print str(secretkey)


def Keyword_Encryption(txt):
    number = input("Please Enter Number: ")
    (alphabet)str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,. ;:!"
    str6 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    (new1alphabet)str2 = str(secretkey) + str1(alphabet)
    ()str3 = ''.join(x for i, x in enumerate(str2) if str2.index(x) == i)
    str4 = str3[(len(str3)-number):len(str3)] + str3[:(len(str3)-number)]
    str5 = ""

    for i in txt:
        if re.match(r"[a-z]", i):
            str5 = str5 + str4[str1.index(i)]
        elif re.match(r'[A-Z]',i):
            str5 = str5 + str4[str6.index(i)].upper()
        else:
            str5 = str5 + i
    print("Ciphertext：%s" % str5)


if __name__ == '__main__':
    txt = raw_input("Please Enter Plaintext: ")
    Keyword_Encryption(txt)
