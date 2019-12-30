import urllib
file = open("/home/siddharth/vadaPav/bingUrls.txt", 'r')

'''
After extracting the url from bing save the images into bing folder 
'''

for line in file.readlines():
    fname = line.rstrip().split(',') #using rstrip to remove the \n
    ctr = 0
    for i in fname:
        try:
            urllib.urlretrieve(i,'/home/siddharth/vadaPav/bing_images/' + str(ctr) + '.jpg')
            ctr += 1
            print ctr
        except:
            print "except"
