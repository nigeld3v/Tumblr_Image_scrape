# works with Python3

# Tumblr_Image_scrape.py

# re stands for regular expressions
import re
import requests
# BeautifulSoup is for parsing html as a tree
from bs4 import BeautifulSoup
import os
# URLLIB is for requests in general, sends and accepts text
from urllib.request import urlretrieve

# Create a function that will scrape a tumblr account for images and download
# all of them into a folder
def tumblr_scrape(input_url):
    url = input_url
    # Send a "get" request (I want "this" page) to the URL the user provided, r
    # is created as an object (which is a Python object)
    r = requests.get(url)
    # Format the provided URL into text
    data = r.text
    # We're feeding "data" to BeautifulSoup with lxml as a parser
    soup = BeautifulSoup(data, 'lxml')
    # Give the title of the Tumblr site as name for the image folder
    title = soup.title.text
    # Find where this .py file sits on the device, points to the file, dir name
    # points at the directory that containt this file - on level above
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # Name the new folder with the title variable, taken from Tumblr site
    # dir_path + what folder I want the new folder to live in
    download_folder = os.path.join(dir_path, str(title))
    if os.path.exists(download_folder):
        pass
    else:
        os.mkdir(download_folder)
    # Track down the images and download them into the folder you just created
    # Also we will give the images slightly meaningful filenames
    # Filename will be tumblrtitle_page#_image#
    imgnum = 0
    for link in soup.find_all("img"):
        image = link.get("src")
        if re.search("78.media.tumblr.com/", image):
            file_format = image.split("/")[-1].split(".")[-1]
            img_name = soup.title.text + "_" + str(page_num)+"_"+ str(imgnum)
            img_path = os.path.join(download_folder, img_name + "." +
                file_format)
            urlretrieve(image, img_path)
            imgnum += 1
# Now we need to find the "next" button for this page

    print("Done downloading all images from " + title)

"""
This is very useful as an idea - XPATH
//li[@class="post"]//img/@src
"""

# Print Welcome message, request user input: TUMBLR URL
input_url = input("Welcome to Tumblr Image Scrape!\n\n\nThis script is a quick "
"and easy way to archive all the images from posts on a Tumblr site of your "
"choice.\n\n\nATTENTION: this script does not automatically stop when all "
"images from the Tumblr have been downloaded. To stop this script in terminal "
"you need to press [control]+[C] on your keyboard.\n\n\nPlease provide the URL "
"of a Tumblr from which you wish to download all the images, and then press "
"[ENTER]: ")
# ensure there is a slash at the end of URL so page advance works
if input_url[-1] != "/":
    input_url = input_url + "/"
else:
    # pass means do nothing
    pass
# ensure there is a http:// at the start of the URL so script works
if input_url[0:6] != "http://":
    input_url = "http://" + input_url
else:
    pass
page_num = 1
while page_num:
    print("Downloaded: images from page "+ str(page_num))
    if page_num == 1:
        tumblr_scrape(input_url)
    else:
        tumblr_scrape(input_url + "page/" + str(page_num))
    page_num += 1
