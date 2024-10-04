from PIL import Image
import PIL.ImageOps 
import os

#make the list of path form the ./image folder
path = "image/"

ls = os.listdir(path)

#open the first image
for i in ls:
    img = Image.open(path + i)
    #display the image
    #reverse the image to have a white background
    img = img.convert('RGB')
    img = PIL.ImageOps.invert(img)
    img = img.save(path + i)
    