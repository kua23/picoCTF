## information

It's a cute cat picture, AWWWWWW... but what's hidden sneakily in this picture? My first intuition is to use the `exiftool` command which returns the generic file properties of the picture. Upon using `exiftool cat.jpg`, we get all the details of the picture. 
```
ExifTool Version Number         : 12.65
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2023:11:18 15:54:35+05:30
File Access Date/Time           : 2023:11:20 21:55:14+05:30
File Inode Change Date/Time     : 2023:11:18 15:54:37+05:30
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```
The only thing that catches my eye is the license which looks like it has been encoded in some general code. Upon saving it in a license.txt file and using
`base64 -d license.txt` we get the flag.

### Flag
picoCTF{the_m3tadata_1s_modified}


## Matryoshka doll
By definition, a matryoshka doll is a Russian doll which contains smaller dolls inside it, which in turn contain smaller dolls. The title itself sounds like a hint to the ctf, trying to imply that there maybe hidden files inside the base `dolls.jpg`. Upon using `binwalk -e dolls.jpg `, the code returned is
```
                                 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378942, uncompressed size: 383937, name: base_images/2_c.jpg
651600        0x9F150         End of Zip archive, footer length: 22

```
which does show that there are hidden files inside the picture and we may just have to unzip it.

After using 
`unzip dolls.jpg` we get a directory named `_dolls.jpg.extracted` and upon changing the directory to that file, we can see upon using ls that it contains a sub directory called base_images, which contains `2_c.zip` and another `base_images` directory along with `3_c.zip` and upon changing the directory, and listing out its contents using `ls base_images` we get another `base_images` which we can navigate into to reveal another `base_images` directory along with `4_c.zip` and on finally navigating into that `base_images` directory, we ssee a `flag.txt` and on using `cat flag.txt`, we get the flag.

```
┌──(kali㉿kali)-[~/Downloads]
└─$ cd _dolls.jpg.extracted                                                                       
┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted]
└─$ ls
4286C.zip  base_images                                             
┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted]
└─$ cd base_images                                                                           
┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images]
└─$ ls
2_c.jpg  base_images                           
┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images]
└─$ cd base_images                                                   
┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images/base_images]
└─$ ls            
3_c.jpg  base_images                                                     
┌──(kali㉿kali)-[~/Downloads/_dolls.jpg.extracted/base_images/base_images]
└─$ cd base_images                                                   
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/base_images/base_images]
└─$ ls
4_c.jpg  flag.txt                                                     
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/base_images/base_images]
└─$ cat flag.txt  
picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}
```

### Flag
picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}    

