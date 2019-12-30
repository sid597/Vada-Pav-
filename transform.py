from PIL import Image
import os

'''
Rotate and flip the images present into the resized folder 
'''


ctr = len(os.listdir('/home/siddharth/vadaPav/resized/'))  # no of images 
image_path = '/home/siddharth/vadaPav/resized/'
nctr = 900


def rotate(img_path):
    l = [90,180,270]
    for degree in l:
        try:
            img = Image.open(img_path)
            img = img.rotate(degree, expand = 1)
            img.save('/home/siddharth/vadaPav/rotated/' + str(ctr) + str(degree) + '.jpg')
        except:
            print "I tried"
     



def flip(img_path):
    try:
        img = Image.open(img_path)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save('/home/siddharth/vadaPav/flip/' + str(nctr) + '.jpg')
    except: 
        print "I Tried"


for i in (os.listdir(image_path)):
    print i
    # rotate(image_path + i)
    flip(image_path + i)
    # ctr += 1
    nctr+=1


