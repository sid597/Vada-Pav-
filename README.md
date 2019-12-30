# Vada Pav 
My implementation to Build and train a system to detect if a given image is of a Vada-pav or not!

Project started : 29 dec 2019

## Steps I took to scrape data :
- Searched for dataset in kaggle and google but did not find there  
- Checked out the following platforms for images but did not find good results :
  - Instagram : search #Vadapav but results were not very meaningful
  - Facebook : same as Instagram did not find good results
  - ShutterStock : Paid service so did not use it
-  Checked Google and Bing for image searches and there found much better results

### How did I get images from google and Bing ? 
I did it in 2 parts :
 - Get urls of all the pics in search result 
 - Go to the links and download them 
 
 1) To get the list of urls I went to the image search results and scrolled till the results which came were revelent.
 I did this manully could have also done through selenium by scrolling the document but I took this approach
 Then in the developer consolse I wrote script to extract all these urls and download them in a text file 
 the script is in [get_urls.txt](./get_urls.txt) and the urls from Bing and Google can be found in 
 [bingUrls.txt](./bingUrls.txt) and [googleUrls](./googleUrls).
 
 2) Wrote scripts to download images from bing and google and saved them in 
 [bing_images](./bing_images) and [google_images](./google_images). The scripts are in [download_from_bing.py]
 (./download_from_bing.py) and [download_from_google.py](./download_from_google.py)
 
 
 ** After I did this proces I found out an extension called Fatkun Batch Download Image which makes this process very easy
    Searched for plugins before also but don't know how this one skipped from me 

Found about 800 images combined from both google and bing. Then I manually checked and discarded the images 
now have ~500 meaningful images overall. Kept 80 images for test and ~420 for training.

Images obtained were of different sizes so wrote a script to make the resolution smalland same for all 
which can be found inside [resize.py](./resize.py). Used PIL library to resize the images in 300x300 resolution
docker run -it tensorflow/tensorflow:1.1.0 bash

## Augumentation 


Augumented the images to have rotated and flipped images scripts for them are in [transform.py](./transform.py)
Now have a total of ~2000 images for training


## For model training
For training I am going to use retrain.py provided by google tenserflow
Steps I am going to follow :
- Create a folder named 'images' and Inside it will have 2 folders one for trainigs images and the other with test images 
- Download and retrain the Inception V3 net by google
- Run the following command 

  python retrain.py \
  --bottleneck_dir=bottlenecks \
  --model_dir=inception \
  --summaries_dir=training_summaries/long \
  --output_graph=retrained_graph.pb \
  --output_labels=retrained_labels.txt \
  --image_dir=images
- This will generate my own image classifier for Vada pav.
