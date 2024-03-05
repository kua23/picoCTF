cipher = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
flag = ""
lowalpha = "abcdefghijklmnopqrstuvwxyz"
uppalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in cipher:
    if letter in lowalpha:
        flag += lowalpha[(lowalpha.index(letter) + 13) % 26]
    elif letter in uppalpha:
        flag += uppalpha[(uppalpha.index(letter) + 13) % 26]
    else:
        flag += letter
print(flag)



