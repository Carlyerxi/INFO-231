def decode(cipherText):
    '''解密'''
    length = findKeyLen(cipherText) #得到密钥长度
    key = findKey(cipherText,length) #找到密钥
    keyStr = ''
    for k in key:
        keyStr+=k
    print('the Key is:',keyStr)
    plainText = ''
    index = 0
    for ch in cipherText:
        c = chr((ord(ch)-ord(key[index%length]))%26+97)
        plainText += c
        index+=1
    return plainText
        
def openfile(fileName):
    '''读取文件'''
    file = open('vigenereCipherText.txt','r')
    text = file.read()
    file.close();
    text = text.replace('\n','')
    return text

def findKeyLen(cipherText):
    '''寻找密钥长度'''
    length = 1
    maxCount = 0
    for step in range(1,11):#假定密钥长度在1到10之间
        count = 0
        for i in range(step,len(cipherText)-step):
            if cipherText[i] == cipherText[i+step]:
                 count += 1
        print(count)
        if count>maxCount:
            maxCount = count
            length = step
    return length

def findKey(text,length):
    '''找出密钥'''
    key = []
    #定义字母表频率列表
    alphaRate =[0.08167,0.01492,0.02782,0.04253,0.12705,0.02228,0.02015,0.06094,0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.0009,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.0015,0.01974,0.00074]
    matrix =textToList(text,length)
    for i in range(length):
        w = [row[i] for row in matrix] #取出每组密文
        #print('w:',w)
        li = countList(w) #统计w中a-z出现的频率
        powLi = [] #算乘积
        for j in range(26):
            Sum = 0.0
            for k in range(26):
                Sum += alphaRate[k]*li[k]
            powLi.append(Sum)
            li = li[1:]+li[:1]#循环移位
        Abs = 100
        ch = ''
        for j in range(len(powLi)):
             if abs(powLi[j] -0.065546)<Abs:
                 Abs = abs(powLi[j] -0.065546)
                 ch = chr(j+97)
        key.append(ch)
    return key                

def countList(lis):
    '''统计列表中a-z出现的频率'''
    li = []
    alphabet = [chr(i) for i in range(97,123)]
    for c in alphabet:
        count = 0
        for ch in lis:
            if ch == c:
                count+=1
        li.append(count/len(lis))
    return li
        
def textToList(text,length):
    '''按密钥长度将text分组'''
    textMatrix = []
    row = []
    index = 0 
    for ch in text:
        row.append(ch)
        index += 1
        if index % length ==0:
            textMatrix.append(row)

            row = []
    return textMatrix


#按行输出矩阵
def printTextMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == '__main__':
    cipherText = openfile('vigenereCipherText.txt')
    print('cipherText:\n',cipherText)
    print('====================')
    plainText= decode(cipherText)
    print('====================')
    print('plainText:\n',plainText)
