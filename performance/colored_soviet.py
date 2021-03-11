from PIL import Image

img=Image.open("marx.jpeg")

pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
            if pixels[i,j][0]==0:
                pixels[i,j]=(255,0,0)
 

img.show()