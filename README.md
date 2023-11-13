# picoCTF

## 1. tunn3l v1s10n
A picture is given in the first file. Upon using
`exiftool tunn3l_v1s10n`
where exiftool is used for reading, writing and changing image and audio data
A file that can be read, written and executed is returned, its filetype being bitmap(.bmp)
As the file's name is just `tunn3l_v1s10n`, we change it to 
`mv tunn3l_v1s10n tunn3l_v1s10n.bmp`
Proceeding forward, we can open the file using an online app like [Photopea](https://www.photopea.com/). Upon doing so the file shows a picture showing text that reads
_'notaflag{sorry}'_ 
Opening the file in an hexeditor like [HexEd.it](https://hexed.it/), we can observe that the height of the .bmp file is very small.
The width of the file starts at offset 12 and goes on for a length of 4 bits, while the height starts at offset 16 and goes on for 4 bits too. On changing the height of the .bmp file to its width, by replacing _32 01_ with _16 6e_ and opening the file again with the text editor, we get the entire picture which contains the flag.

### Flag
`picoCTF{qu1t3_a_v13w_2020}`

## 2. Trivial FTP
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
to check if there is any hidden message in the three photos, the first two files, _'picture1.bmp' and 'picture2.bmp'_did not return anything but the third file _'picture3.bmp_ returned an embedded _'flag.txt'_
Using the command `steghide extract -sf picture3.bmp`, where sf stands for stegofile we get the flag.

### Flag
`picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`

## 3. MacroHard WeakEdge
This picoCTF is based on binwalk. Upon downloading the file _'Forensics is fun'_ , we can use binwalk on that file. This command is used for identifying and extracting embeddded files and code that is executable. In simpler words, it is used to extract the content of binary files. 

`binwalk 'Forensics is fun.pptm'`
Upon using this, we get a list of unzipped files
`binwalk -e ‘Forensics is fun.pptm’`
Doing this, we can use it to extract the unzipped files in the .pptm.
We get a new file called 'Forensics is fun.pptm.extracted' in our directory and upon navigating to it using 
``cd '_Forensics is fun.pptm.extracted'``
and using 
``ls -la *``
where * stands for all files and directories, we get a list of files.
```
rw-r--r-- 1 kali kali 100093 Nov 13 10:20  0.zip
-rw-r--r-- 1 kali kali  10660 Jan  1  1980 '[Content_Types].xml'

docProps:
total 20
drwxr-xr-x 2 kali kali 4096 Nov 13 10:20 .
drwxr-xr-x 5 kali kali 4096 Nov 13 10:20 ..
-rw-r--r-- 1 kali kali 3784 Jan  1  1980 app.xml
-rw-r--r-- 1 kali kali  666 Jan  1  1980 core.xml
-rw-r--r-- 1 kali kali 2278 Jan  1  1980 thumbnail.jpeg

ppt:
total 56
drwxr-xr-x 7 kali kali 4096 Nov 13 10:20 .
drwxr-xr-x 5 kali kali 4096 Nov 13 10:20 ..
-rw-r--r-- 1 kali kali 5197 Jan  1  1980 presentation.xml
-rw-r--r-- 1 kali kali  818 Jan  1  1980 presProps.xml
drwxr-xr-x 2 kali kali 4096 Nov 13 10:20 _rels
drwxr-xr-x 3 kali kali 4096 Nov 13 10:20 slideLayouts
drwxr-xr-x 3 kali kali 4096 Nov 13 10:20 slideMasters
drwxr-xr-x 3 kali kali 4096 Nov 13 10:20 slides
-rw-r--r-- 1 kali kali  182 Jan  1  1980 tableStyles.xml
drwxr-xr-x 2 kali kali 4096 Nov 13 10:20 theme
-rw-r--r-- 1 kali kali 7168 Jan  1  1980 vbaProject.bin
-rw-r--r-- 1 kali kali  811 Jan  1  1980 viewProps.xml

_rels:
total 12
drwxr-xr-x 2 kali kali 4096 Nov 13 10:20 .
drwxr-xr-x 5 kali kali 4096 Nov 13 10:20 ..
-rw-r--r-- 1 kali kali  738 Jan  1  1980 .rels
```
Then using,
``strings ppt/vbaProject.bin``
wew get a line saying
`sorry_this_isn 't_it`
Upon changing the directory using,
`cd slideMasters`
and using
`strings hidden`, we get a string
`Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q` and upon removing all the spaces and using base64 we can decode it. 

### Flag
`picoCTF{D1d_u_kn0w_ppts_r_z1p5}`

## 4. caas
Cowsay as a service is a program in which a cow tells a message which you input.
The server used here is node.js. This ctf was an example of a command injection which is basically when a program which takes in a user input is manipulated in such a way that the user who inputs the command can extract information from the program host's system.
Thus, our first task is to see if the cowsay works as it is intended to work. Hence, we first use (https://caas.mars.picoctf.net/cowsay/hi) which returns the cowsay as intended.
In order to use a command injection, we can use the same url and use
(https://caas.mars.picoctf.net/cowsay/hi;ls)
where the ; is used to end the first command and start a new command. This lists the files in the directory where the cowsay program is stored. This returns certain folders and files under which there is one .txt file and upon using (https://caas.mars.picoctf.net/cowsay/hi;ls;cat%20falg.txt), the flag is received.

### Flag
`picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}`

## 5. Forbidden Paths
Upon entering the website, (http://saturn.picoctf.net:64403/), there is a list of _.txt_ files and a '..' file.
The problem statement gives that there are four directories into which we need to navigate in order to get the _flag.txt_ file. On first trying to navigate through the directories by just pasting the path,
`/usr/share/nginx/html/ ` it did not work. Hence, instead of that I just used
`../../../../flag.txt` 
where it navigated into four directories and the flag file is provided. 

### Flag
picoCTF{7h3_p47h_70_5ucc355_e5fe3d4d}

## 6. Local Authority
The website which the user is directed to shows a username and a password which can be filled to get the flag, presumably... As there are no other elements present in the website, we can right click the page and go to the _**Inspect Source**_ option which shows an _index_ and a _style.css _ file. Upon entering any gibberish name and password, there pops a new file called _login.php_ which contains the code
```
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )

```
which we can use to get the flag

### Flag
picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb} 

## 7. Buffer Overflow
First, we connect to the server 
`nc saturn.picoctf.net 55984`
This CTF is based on buffer overflow. Buffer overflow occurs when the amount of data in a website exceeds it storage capacity. Smashing the stack which is provided in the problem statement also means overloading the program so it overflows. Upon seeing the code, we can deduce that if we find a fault in the segmentation, we get the flag. If the sig_sev handler detects a fault of an overflow, it is sent to the handler which then prints the flag

### Flag

## 8. Stonks
In this, the user has money from which a random share is picked after which the program asks the API token to the user. However, there exists a format string vulnerability as there are no quotes in the line 
`print (user_buf)` and there is no %x to accept the string.
On connecting to the server and choosing the connect to api token option, we can enter the api string as 
`%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x`
On doing this, we get a string in hexadecimal, which we convert to ASCII where we get a flag sort of looking file

### Flag


## 9. GDB Baby Step 0
GDB, which stands for the GNU Project debugger, allows us to debug a program step by step when it executes. You can disassemble your code and provide breakpoints in them and figure out the mistake using GDB.
After downloading the file and opening the file using 
`gdb debugger0_a`, we can use `info functions` to understand which functions do what. The command returns:
```
Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  __cxa_finalize@plt
0x0000000000001040  _start
0x0000000000001070  deregister_tm_clones
0x00000000000010a0  register_tm_clones
0x00000000000010e0  __do_global_dtors_aux
0x0000000000001120  frame_dummy
0x0000000000001129  main
0x0000000000001140  __libc_csu_init
0x00000000000011b0  __libc_csu_fini
0x00000000000011b8  _fini
```

The problem statement asks what is in the _eax function_ in the _main_ register. According to a source, the RAX registor is an accumulator register that is used for arithmetic and data manipulation generally. The GDB provides a function called _'disassemble'_ which can be used to, as the name suggests, disassemble a function. Hence, we use:
`disassemble main` that returns:
```
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   %rbp
   0x000000000000112e <+5>:     mov    %rsp,%rbp
   0x0000000000001131 <+8>:     mov    %edi,-0x4(%rbp)
   0x0000000000001134 <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000000000001138 <+15>:    mov    $0x86342,%eax
   0x000000000000113d <+20>:    pop    %rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
```
Thus, we get the value next to the eax register, but it is in hexadecimal. Upon converting the hexadecimal value to decimal, we get the value as 549698, which is the flag.

### Flag
`picoCTF{549698}`

## ARMssembly 0
What is an ARM first? It is a family of CPUs based on reduced instruction set computer(RISC) architecture. They have two main states where they can operate: Instructions state and Thumb state. According to a writeup which I followed, this ctf could have been used by either reading the assembly code or by cross compiling it.  This ctf is based on cross compiling ARM assembly on x86, where x86 is a damily of complex instruction set computer. Thus for cross compiling it, we need to install a cross compiler using 
``sudo apt install binutils-aarch64-linux-gnu`` and then from there, inn order to cross compile it, we use:
```
aarch64-linux-gnu-as -o chall.o chall.S
aarch64-linux-gnu-gcc -static -o chall chall.o
```
Upon then using
`file chall.o`
we find that it is compiled for ARM aarch64, which is a 64-bit extension of the ARM family. But this code cannot be run by a x86_64 cpu. In order to emulate it we use QEMU, which emulates using dynamic binary translation. We can install it using,
`sudo apt install qemu-user-static` and run it using 
`./chall 3854998744 915131509  ` where we get the answer as 
`Result: 3854998744`

WE CAN ALSO USE,
Upon using `cat chall.S`
we get a block of assembly code.
For func1,
```
func1:
        sub     sp, sp, #16
        str     w0, [sp, 12]
        str     w1, [sp, 8]
        ldr     w1, [sp, 12]
        ldr     w0, [sp, 8]
        cmp     w1, w0
        bls     .L2
        ldr     w0, [sp, 12]
        b       .L3
```
the sub command is for three components, where `#16` which denotes a constant, has to be subtracted from `sp` and be stored in ``sp``.
`sp` stands for stack pointer which is a place to store the memory address of the last elemnt added to the stack.
In 
```
str     w0, [sp, 12]
str     w1, [sp, 8]
```
`str` which stands for store, stores the value of `w0` and `w1` which are user inputted in sp. 
The number is used to denote the offset, where for 
`str     w0, [sp, 12]`
The number is stored in w0 on the stack at offset 12
```
ldr     w1, [sp, 12]
ldr     w0, [sp, 8]
```
Here, `ldr` stands for load register, which is used to load the offset value of 12 into the variable w1 in the stack point.
`cmp     w1, w0` is used to compare the values of w1 and w0.
`bls     .L2`
bls stands for branch if less, which says that if w0 is smaller than w1, branch to .L2.
```
ldr w0, [sp, 12] 
    b   .L3
```
This loads a value into w0 and branches to L3

L2:
`ldr     w0, [sp, 8]` - loads a value from stack at offset 8 and loads it into w0

L3:
`add     sp, sp, 16` - The stack is filled by adding 16 to sp

Thus, the flag will be the smaller number, that is: 3854998744 in 32 bit hex string.

### Flag
`picoctf{e5c69cd8}`




