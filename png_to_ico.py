#Convert PNG files into ICO files using this python code: 
from PIL import Image
filename = r'images\image.png' #replace with the location of png file
img = Image.open(filename)
type=input("Do you Want to Change the Size of Image :")
if type==True:
    icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)] #change the size of the image
    img.save('logo.ico', sizes=icon_sizes)
else:
    img.save('file.ico') #save as default size
