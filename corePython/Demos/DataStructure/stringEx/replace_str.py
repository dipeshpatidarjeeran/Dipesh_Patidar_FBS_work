str1 = "FirstBit Solutions"
input_str = "Bit"
replace_str = "Byte"
str2 = ''
if input_str in str1:
    for i in str1:
        if i not in input_str:
            str2 += i
        else:
            if input_str[0] == i:
                str2 += replace_str
            # else:
            #     str2 += i
    print(str2)
else:
    print(str1)
