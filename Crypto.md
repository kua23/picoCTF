## mod 26

We can use the following code to decode this
![image](https://github.com/kua23/picoCTF/assets/61975172/e8138814-dbd2-4888-9a15-6e8c156229ab)
`lowalpha= "abcdefghijklmnopqrstuvwxyz"
uppalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = str(input("Enter the cipher"))
flag = ""
for letter in cipher:
    if letter in lowalpha:
        flag += lowalpha[(lowalpha.index(letter) + 13) % len(lowalpha) ]
    elif letter in uppalpha:
        flag += uppalpha[(uppalpha.index(letter) + 13) % len(uppalpha)]
    else:
        flag += letter
print(flag)`
In this, we first have 2 variables lowalpha and uppalpha consisting of the lowercase and uppercase letters. The cipher is inputted by the user, while the flag is an empty string. 
In the for loop, first each letter is taken from the cipher string and is compared to see if it is a lowercase or uppercase. If it is a letter, then taking the index of the letter, the number 13 is added to it. Thus, the letter's position is shifted by 13. However, if the number exceeds 26, then the remainder of that number is taken with 26 so that it forms a loop basically.

This is how rot13 works and this is how we get the flag.

### Flag
picoCTF{next_time_I'll_try_2_rounds_of_rot13_wqWOSBKW}

## The Numbers

Here, the image consists of a code of numbers and we need to dedcipher the flag from them. 
![image](https://github.com/kua23/picoCTF/assets/61975172/97b5986e-9c46-4346-ab07-d830cf5fb57a)
Here, as the starting part of every flag starts with picoCTF{}, even this flag must start with it. Here, each numbers does look like it just corresponds to its own letter in the alphabet. It is basically a substitution cipher. Hence upon decoding it, we get the flag
We can use this code to decode it,
![image](https://github.com/kua23/picoCTF/assets/61975172/43c2a843-b701-4611-93b4-ff11f227f6f5)

Here, every space counts as a separator, so each of the elements in the string `string` before each space is considered as one element and appended into the list `cipher`. The flag is initialized as an empty string. Now, iterating through the string, we first check if the element in the list is a number. If it is a number, it is converted into its corresponding letter based on the ASCII numbers. It is finally appended into the flag. If it is not a number it is directly appended into the flag as is the case with the `{}`


### Flag
`picoCTF{thenumbersmason}`

## easy 1

Here, they have given the decrypted flag(even though they've mentioned encrypted) and the key and have given a decryption table. This is first of all a classic example of Vigenere cipher. As the table is a decryption table, in order for it to work as a decription table, we need to use it in reverse. As the decrypted flag is `UFJKXQZQUNB ` and the key is `SOLVECRYPTO`. Thus in the given table,
![image](https://github.com/kua23/picoCTF/assets/61975172/ff1278cf-0d4b-43ec-84d0-5c11d727c733)

We will get the encryption if we check the column or row of S containing U corresponds to which row or column. Here this corresponds to C. Similarly, for another example, if we take the letter O in the column and move down the same column till we find F, the row corresponding to the letter F is R. And if we continue to solve it, we get the flag. 

### Flag
`picoCTF{CRYPTOISFUN}`

## 




