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

## 13

This is again based on rot13. If we use the same code as shown in the first program, we get the answer.
![image](https://github.com/kua23/picoCTF/assets/61975172/656fdcc8-8105-4314-89d6-1b1f24fd61de)



### Flag

picoCTF{not_too_bad_of_a_problem}

## cipher

Here, the cipher is given as `picoCTF{ynkooejcpdanqxeykjrbdofgkq}`, and as the challenge name suggests is a caesar cipher. However, as the cipher given already has the word picoCTF it is very time consuming to bruteforce through every rot, so instead we can use an online decoder like (this website)[https://www.dcode.fr/caesar-cipher] which gives us the flag. 
![image](https://github.com/kua23/picoCTF/assets/61975172/9eebf85a-60ec-4606-a3a9-8e274bcf3f54)

### Flag
`picoCTF{crossingtherubiconvfhsjkou}`

## morse-code

On manually listening to the audio, we can compute the dits(.) and the das(_) and the pauses(/). On listening to it completely, we get
`.-- .... ....- --... / .... ....- --... .... / ----. ----- -.. / .-- ..--- ----- ..- ----. .... --...` which upon decoding using an online decoder like (this)[https://morsecode.world/international/translator.html].

### Flag
`picoCTF{wh47_h47h_90d_w20u9h7}`

## credstuff

Okay, here we are given two files `usernames.txt` and `passwords.txt`. Both of these contain the username and passwords of users and each line of one corresponds to the same in the other. So, here we can figure out which line the username `cultiris` is in and find the same line in the `passwords.txt`. The only problem is that both of them contain a lot of lines. So instead we can use the following commands:

![image](https://github.com/kua23/picoCTF/assets/61975172/c56d1b26-15ff-4ba7-bf61-4de45fa6d28e)

Here the -n is used to return the line of `cultiris`

In order to get the same line from the passwords.txt, we can use:
![image](https://github.com/kua23/picoCTF/assets/61975172/8a73a972-9b6e-4821-a529-fa3de6c9bc5a)
where the sed command is used to return the 378th line from passwords.txt

The returned password looks like it is in rot13 and hence can be decoded using the same Python program.

### Flag
`picoCTF{C7r1F_54V35_71M3}`

## RailFence

This is a different type of cipher which depends on arranging the letters in the form of a zigzag or a railtrack. Here, they have given that it has to be arranged in the form of 4 rails. On checking the Wikipedia page, we get to know more about this cipher. The rails repeat with a period of 2(N-1), where N is the number of rails, which is 6 in this case. L is the length of the string to be decrypted which in this case is `Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6`
is 56. K = L/(2N-1), which is almost 9 and that it how it has been split. 
This gives us
T    a           _     7     N     6     D     4     9 
 h   l g   : W   3 D   _ H   3 C   3 1   N _   _ A   9 7
  e f     s   H R   0 5   3 F   3 8   N 4   3 D   7 B   
         i     3     3     _     _     _     N     6    
which is the flag. `WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997`

### Flag
`picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}`



