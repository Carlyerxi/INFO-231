import collections
keyword = print ("请输入关键词：")
key = keyword
letter = print ("从哪个字母开始：")
char = letter
plaintext = print ("请输入明文：")
cle = plaintext
cip = []
table1 = list("abcdefghijklmnopqrstuvwxyz")
#给定26个空格用于后边的判断
table2 = list("                          ")
#去除重复字母
key_res = ''.join(collections.OrderedDict.fromkeys(key))
#判断给定字母的下标
for i in range(len(table1)):
       if char == table1[i]:
              k = i
#先将关键词放入列表
for j in key_res:
       table2[k] = j
       k = k + 1
#放入剩余字母
for j in table2:
       for i in table1:
              if i not in key_res and ' ' in table2:
                     table2[k] = i
                     k = (k + 1) % 26
#字符比对生成密文
for i in cle:
       for j in range(len(table1)):
              if i == table1[j]:
                     cip.append(table2[j])
print ("加密后的内容为：%s") % ''.join(cip)
