## How it works?

That script picks all images (except the logo image) and on the same 
directory, create a folder with the name 'wm'.
During the exection, for each image he create a watermarked copy and
write on 'wm' folder.

+ If 'wm' folder already exists with or without files the script 
continue your execution.
+ If has some non image file on the directory, the script just
ignores and jump for the next file.
+ If the image copy has alreay watermarked on the wm folder,
(a file with the same name), the script just ignores and jump
for the next file.