from PIL import Image
import os

'''
Resize the downloaded images from bing and google to 300x300
'''

path_bing ='/home/siddharth/vadaPav/bing_images/' 
path_google = '/home/siddharth/vadaPav/google_images/'
ctr = 0       # No of images from bing used so that names don't overlap

def resize(img_path,i):
    img = Image.open(img_path)
    img = img.resize((300,300),Image.ANTIALIAS)
    try:
        img.save('/home/siddharth/vadaPav/transformed/'+str(i)+'.jpg')
    except:
        print "except"



for i in enumerate(os.listdir(path_bing)):
  resize(path_bing + i[1],i[0])
  ctr = i[0]
for j in enumerate(os.listdir(path_google),ctr+1):
    print j
    resize(path_google + j[1],j[0])
