# interencdec

Points: 50

## Challenge

Can you get the real meaning from this file.

`YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg==`

## Hints

Engaging in various decoding processes is of utmost importance

## Solution

Decode the text from base 64, a byte string is obtained containing another base64 text.  
`b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='`  
Decode the text again using base64,  
`wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}`  
It looks like a substitution or caesar cipher,
On using [dcode.fr](https://www.dcode.fr/caesar-cipher), we can bruteforce.

### Flag
`	picoCTF{caesar_d3cr9pt3d_86de32d2}`



