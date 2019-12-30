import urllib

'''
Download pics from google after extracting the pics
'''

with open("/home/siddharth/vadaPav/url","r") as f:
    urls = f.readlines()
urls = [x.strip() for x in urls]
print urls 

ctr = 101
for url in urls:
    try :
        urllib.urlretrieve(url,'/home/siddharth/vadaPav/images/' + str(ctr) + '.jpg' )
        ctr += 1
        print ctr
    except:
        print "except"