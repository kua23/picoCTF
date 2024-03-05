cipher = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
cipher = cipher.split()
flag = ""
for x in cipher:
    if x.isnumeric() == True:
        number = int(x)
        flag += str(chr(64 + int(number)))
    else:
        flag += x
print(flag)

