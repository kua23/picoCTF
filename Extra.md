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

## Glory of the Garden
![image](https://github.com/kua23/picoCTF/assets/61975172/e505a2fd-0839-41b0-919b-b5cca0ab4c15)

The hint given for this ctf is what iss a hexeditor, which seems pretty obvious that we need to open the pictures using (a hexeditor)[https://hexed.it/]
Upon opening the picture and scrolling to the bottom, you do find a line saying `Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"` which is the flag

### Flag
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}


## Wireshark doo dooo do doo...

This is based on packet capture, which basically means capturing the traffic going across the network. As we transfer data, first a segment header(transport) is added to the data, then a packet header(network) followed by a frame header and a frame trailer(data link).

Now, there are 937 packets to choose the flag from and we have no idea where to start. Thus we can start from going to the Statistics drop down and clicking on Conversations in order to determine the communication between the system sending the packets and the system receiving the packets. 
![image](https://github.com/kua23/picoCTF/assets/61975172/a833c973-59d3-46eb-ac83-9b935fe1e609)
This does provide some data, but not very important.

In the same Statistics drop down, we can go to the Protocol Hierarchy menu to see the most used protocols in sending these packets.
![image](https://github.com/kua23/picoCTF/assets/61975172/6b77aa67-f44c-4b36-ac20-55a4f49e4aed)

We can see that most of the bytes are occurring in HTTP, which looks like an ideal place to start looking for the flag. 

Thus, we can go back to the Conversations page and click on the IPv4 filter where we get a bunch of IP addresses. If we go to to any one of these addresses, right click and click 'Appy as filter to A <--> B. This is basically done to filter only those IP addresses from the given host to the destination.
![image](https://github.com/kua23/picoCTF/assets/61975172/fba21481-39ff-4d45-b778-907cd6351d71)

Once this is done, we can go back to the main panel, right click any IP address following the HTTP protocol and follow the HTTP stream.
![image](https://github.com/kua23/picoCTF/assets/61975172/bce2e643-cb3e-4ec1-9424-1099f9dfd0c5)

![image](https://github.com/kua23/picoCTF/assets/61975172/e55e552f-c9fa-49f6-98e8-7f1b0c735b8d)
We basically get the information corresponding to the data sent through the corresponding packet, and at the end it looks suspiciously like a flag. 

This is basically rot 13 encoded, which gives the flag. 

### Flag
`picoCTF{p33kab00_1_s33_u_deadbeef}`

## Enhance!

The given file from where we need to get the flag is a Scalable Vector Graphic. This type of image file can typically zoomed in more and more without affecting the quality of the image too much. However, we can only zoom in on the file a little bit.
On opening the file using ghex, we see that it is a file of `xml`(Extensible Markup Language) type.
![image](https://github.com/kua23/picoCTF/assets/61975172/f53afa5b-e091-45ea-bab0-9d88874bc379)

Thus we can create a copy of the file and change the file formatting to `xml` to see if there are any other hidden details. Opening the file in any text editor like Visual Studio Code, we can see the contents of the xml file.

![image](https://github.com/kua23/picoCTF/assets/61975172/72d649cc-b779-4ba6-9ca0-f544daba4320)

Along with the circle, ellipse, there is a text layer in the xml file whose size is just 0.00352781 pixel. If we further scroll down, we can see the flag which is typed in different rows, On combining all of them, we get the flag. 
![image](https://github.com/kua23/picoCTF/assets/61975172/9425f054-84f0-4e43-940d-3ea97f64de29)

### Flag
`picoCTF{3nh4nc3d_24374675}`

## Lookey here

This is one of the easiest. It just is a text file containing a lot of text. Based on the hint given, if we just use the `grep` command we get the flag
![image](https://github.com/kua23/picoCTF/assets/61975172/d842fdb9-e84b-4738-a49a-c499993ddb70)

### Flag
picoCTF{gr3p_15_@w3s0m3_2116b979}

## Extensions

Trying to open it with the default text editor, it shows that the user does not have permissions to do so. If we `cat` the file too, it shows a bunch of nonsensical characters. However, at the top of the file it says PNG which means that it may actually be a picture encoded as a text file. Opening the text file using GHex to get its hex dump, we can see the first few magic bytes to determine what type of file it actually is.

![image](https://github.com/kua23/picoCTF/assets/61975172/d49d10f9-cb42-4554-add6-0fc593371189)

If we use `file flag.txt` it shows that it is actually PNG.
![image](https://github.com/kua23/picoCTF/assets/61975172/dd02a70d-4812-4db5-ba70-ec2cd6edc78a)

If we go to the list of file signatures too, it shows the same thing that it is a .png. Now, if we change the extension to .png, we can view the flag.

![image](https://github.com/kua23/picoCTF/assets/61975172/b49077e8-5167-4c52-a30e-3cdedc1157b9)

### Flag
picoCTF{now_you_know_about_extensions}














