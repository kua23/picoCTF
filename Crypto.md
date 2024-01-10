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

### Flag
`picoCTF{thenumbersmason}`

##

