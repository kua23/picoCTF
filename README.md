# picoCTF

# title
## subtitle
### subsubtitle
`code one line`
```
code 2 lines
code 2 lines
```
> for flagging
* for bullets
[google](https://www.google.com/)

## tunn3l v1s10n
A picture is given in the first file. Upon using
`exiftool tunn3l_v1s10n`
a file that can be read, written and executed is returned, its filetype being bitmap(.bmp)
As the file's name is just `tunn3l_v1s10n`, we change it to 
`mv tunn3l_v1s10n tunn3l_v1s10n.bmp`
Proceeding forward, we can open the file using an online app like [Photopea](https://www.photopea.com/). Upon doing so the file shows a picture showing text that reads
_'sorry, not a flag'_ 
Opening the file in an hexeditor like [HexEd.it](https://hexed.it/), we can observe that the height of the .bmp file is very small.
The width of the file starts at offset 12 and goes on for a length of 4 bits, while the height starts at offset 16 and goes on for 4 bits too. On changing the height of the .bmp file to its width, by replacing _32 01_ with _16 6e_ and opening the file again with the text editor, we get the entire picture which contains the flag.

### Flag
`picoCTF{qu1t3_a_v13w_2020}`

## Trivial FTP
First, a directory called _**tftp.pcanpng**_ is downloaded, which hosts a Trivil File Transfer Protocol. Upon opening the directory using [Wireshark](https://www.wireshark.org/), and navigating to _File>Export Objects>TFTP_, all the files in the directory can be saved. There exists a file called _**instructions.txt**_ which can be opened using
`cat instructions.txt`
from which we get a cipher:
_GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA_
This did look like a caesar cipher, and upon bruteforcing it using [this tool](https://www.dcode.fr/caesar-cipher), it was encoded as a _rot13_ file. Upon decoding the key, it returned
`TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
`
_'I will check back for the plan'_ must actually mean deciphering the plan file which upon doing so using [rot13](https://www.dcode.fr/caesar-cipher) gave 
`IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
`
Upon using the command 
'steghide info'
to check if there is any hidden message in the three photos, the first two did not return anything but the third one returned an embedded _'flag.txt'_
Using the command `steghide extract -sf picture3.bmp`, where sf stands for stegofile 
where we get the flag

### Flag
`picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`

## MacroHard WeakEdge
This picoCTF is based on binwalk. Upon downloading the file _'Forensics is fun'_ , we can use binwalk on that file. This command is used for identifying and extracting embeddded files and code that is executable. In simpler words, it is used to extract the content of binary files. 
```
binwalk 'Forensics is fun.pptm'
binwalk -e ‘Forensics is fun.pptm’
cd '_Forensics is fun.pptm.extracted'
ls -la * 
string ppt/vbaProject.bin
```
Okay, here is the block of code which was used. First, upon using the first line, we get certain unzipped files and upon using the second command we can extract the files in the .pptm
Upon changing the directory to the extracted pptm and listing all the files, we get a list of files and where * where stands for all files and directories.
Upon using the string command, we get a line which returns
`sorry_this_isn 't_it`
Upon changing the directory using,
`cd slideMasters`
and using
`string ppt/slideMasters/hidden`, we get a string
`Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q` and upon removing all the spaces and using base64 we can decode it. 

### Flag
`picoCTF{D1d_u_kn0w_ppts_r_z1p5}`

## caas
Cowsay as a service is a program in which a cow tells a message which you input.
The server used here is node.js. This ctf was an example of a command injection which is basically when a program which takes in a user input and is manipulated in such way that the user who inputs the command can extract information from the program's host's system.
Thus, our first task is to see if the cowsay works as it is intended to work. Hence, we first use (https://caas.mars.picoctf.net/cowsay/hi) which returns the cowsay as intended.
In order to use a command injection, we can use the same url and use
(https://caas.mars.picoctf.net/cowsay/hi;ls)
where the ; is used to end the first command and start a new command. This lists the files in the directory where the cowsay program is stored. This returns certain folders and files under which there is one .txt file and upon using (https://caas.mars.picoctf.net/cowsay/hi;ls;cat%20falg.txt), the flag is received.

### Flag
`picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}`

## Forbidden Paths
Upon entering the website, (http://saturn.picoctf.net:64403/), there is a list of _.txt_ file and a '..' file.
The problem statement gives that there are four directories into which we need to navigate in order to get the _flag.txt_ file. On first trying to navigate through the directories by just pasting the path, it did not work. Hence, instead of that I just used
`../../../../flag.txt` which navigated into four directories and the flag file is provided. 

### Flag
picoCTF{7h3_p47h_70_5ucc355_e5fe3d4d}

## Local Authority
The website which the user is directed to shows a username and a passwor which can be filled to get the flag, presumably... As there are no other elements present in the website, we can right click the page and go to the _**Inspect Source**_ option which shows a _index_ and a _style.css _ file. Upon entering any gibberish name and password, there pops a new file called _login.php_ which contains the code
```
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )

```
which we can use to get the flag

### Flag
picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb} 


