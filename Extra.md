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

