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

