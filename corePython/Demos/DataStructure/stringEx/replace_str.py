str1 = "FirstBit Solutions"
input_str = "irs"
replace_str = "Byte"
count = 0
str2 = ''
ex = ''
li =[]

#just to check position of old string
for i in range(len(str1)):
    if str1[i] == input_str[count]:
        ex += str1[i]
        li.append(i)
        count += 1
        if ex == input_str:
            break
    else:
        ex = ''
        li = []
        count = 0

#to replace new string with old string
for i in range(len(str1)):
    if i == li[0]:
        str2 += replace_str
    if i not in li:
        str2 += str1[i]

print(str2)
