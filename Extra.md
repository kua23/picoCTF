## 1. information

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


## 2. Matryoshka doll
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

## 3. Glory of the Garden
![image](https://github.com/kua23/picoCTF/assets/61975172/e505a2fd-0839-41b0-919b-b5cca0ab4c15)

The hint given for this ctf is what iss a hexeditor, which seems pretty obvious that we need to open the pictures using (a hexeditor)[https://hexed.it/]
Upon opening the picture and scrolling to the bottom, you do find a line saying `Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"` which is the flag

### Flag
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}


## 4. Wireshark doo dooo do doo...

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

## 5. Enhance!

The given file from where we need to get the flag is a Scalable Vector Graphic. This type of image file can typically zoomed in more and more without affecting the quality of the image too much. However, we can only zoom in on the file a little bit.
On opening the file using ghex, we see that it is a file of `xml`(Extensible Markup Language) type.
![image](https://github.com/kua23/picoCTF/assets/61975172/f53afa5b-e091-45ea-bab0-9d88874bc379)

Thus we can create a copy of the file and change the file formatting to `xml` to see if there are any other hidden details. Opening the file in any text editor like Visual Studio Code, we can see the contents of the xml file.

![image](https://github.com/kua23/picoCTF/assets/61975172/72d649cc-b779-4ba6-9ca0-f544daba4320)

Along with the circle, ellipse, there is a text layer in the xml file whose size is just 0.00352781 pixel. If we further scroll down, we can see the flag which is typed in different rows, On combining all of them, we get the flag. 
![image](https://github.com/kua23/picoCTF/assets/61975172/9425f054-84f0-4e43-940d-3ea97f64de29)

### Flag
`picoCTF{3nh4nc3d_24374675}`

## 6. Lookey here

This is one of the easiest. It just is a text file containing a lot of text. Based on the hint given, if we just use the `grep` command we get the flag
![image](https://github.com/kua23/picoCTF/assets/61975172/d842fdb9-e84b-4738-a49a-c499993ddb70)

### Flag
picoCTF{gr3p_15_@w3s0m3_2116b979}

## 7. Extensions

Trying to open it with the default text editor, it shows that the user does not have permissions to do so. If we `cat` the file too, it shows a bunch of nonsensical characters. However, at the top of the file it says PNG which means that it may actually be a picture encoded as a text file. Opening the text file using GHex to get its hex dump, we can see the first few magic bytes to determine what type of file it actually is.

![image](https://github.com/kua23/picoCTF/assets/61975172/d49d10f9-cb42-4554-add6-0fc593371189)

If we use `file flag.txt` it shows that it is actually PNG.
![image](https://github.com/kua23/picoCTF/assets/61975172/dd02a70d-4812-4db5-ba70-ec2cd6edc78a)

If we go to the list of file signatures too, it shows the same thing that it is a .png. Now, if we change the extension to .png, we can view the flag.

![image](https://github.com/kua23/picoCTF/assets/61975172/b49077e8-5167-4c52-a30e-3cdedc1157b9)

### Flag
picoCTF{now_you_know_about_extensions}

##8.  Packet Primer

Another simple challenge... In this, we are given a `pcap` file which can be opened in WireShark. It contains a list of 9 IP addresses, and if you just scroll through the hexdumps of the packets sent over the IP addresses, you get the flag in one of the addresses.
![image](https://github.com/kua23/picoCTF/assets/61975172/1ab5c300-262e-4aac-8bd7-0610fc4de490)


### Flag
`picoCTF{p4ck37_5h4rk_01b0a0d6}`

## 9. Redaction gone wrong

Here, certain parts of the pdf have been bloocked out, and it looks like one part of it contains the flag. Hence we can use the following command
![image](https://github.com/kua23/picoCTF/assets/61975172/b8284b7c-169d-4339-96bf-51fc9977c33e) to convert the pdf document to a .txt document. 
Then we can use the `grep` command
![image](https://github.com/kua23/picoCTF/assets/61975172/c53df197-61d5-4bb9-b411-1b262d6ae19d) to get the flag.

For an easier but cheesy way, we can just open it using the default pdf viewer of the system, and then select the text using the cursor which highlights the text.
![image](https://github.com/kua23/picoCTF/assets/61975172/e5bfd53d-e9f1-4a87-a69b-461186c7fdb1)

### Flag
picoCTF{C4n_Y0u_S33_m3_fully}

## 10. So Meta
The title of the CTF itself gives the hint towards the flag. Metadata is basically the information about the data we want. Thus, in order to find the data about the image given in the CTF, we can use 
![image](https://github.com/kua23/picoCTF/assets/61975172/b5b611ff-917d-49aa-9841-65832c358a82)

In which the artist of the image is the flag.

### Flag
picoCTF{s0_m3ta_eb36bf44}

## 11. What Lies Within

For this, we are given a `buildings.png` and we need to find out how to extract the flag from the given image file. We can use the `zsteg -a buildings.png` command in order to try and extract any information hiding in the image. However, it gives a very long line of text output which is difficult to search through. Instead we can use 
![image](https://github.com/kua23/picoCTF/assets/61975172/8102c359-95b5-4db4-86be-19b0736721bb)
the grep command to extract the flag

### Flag
`picoCTF{h1d1ng_1n_th3_b1t5}`

## 12. Sleuthkit Intro

In this we are given a file of the .gz file and are asked to find out the sectors that it occupies in a new disk partition. First, in order to check the amount of space it takes up we have to unzip the file as it is compressed. This can be done using

![image](https://github.com/kua23/picoCTF/assets/61975172/22e68eca-18ef-4243-8266-0964c977899d)

Then, upon using the `mmls` command we can figure out the length of the sector.
![image](https://github.com/kua23/picoCTF/assets/61975172/36fb4962-df94-44c9-b1b2-7030e8164a80)

In order to get the flag, we need to input this in the netcat link which the challenge has provided.

![image](https://github.com/kua23/picoCTF/assets/61975172/11e76441-c336-4ac4-b02d-30fc1b35f965)
Thus, we get the flag.

### Flag
picoCTF{mm15_f7w!}




















