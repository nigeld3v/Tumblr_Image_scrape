# works with Python3

# IMG_find_BS.py

# re stands for regular expressions
import re
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve

# Create a function that will scrape a tumblr account for images and download
# all of them into a folder
def tumblr_scrape(input_url):
    url = input_url

        # Print out the URL of the current page you're downloading from
    # print(url)

    # Send a "get" request to the URL the user provided, r is created as an
    # object
    r = requests.get(url)
    # Format the provided URL into text
    data = r.text
    # We're using BeautifulSoup with lxml as a parser
    soup = BeautifulSoup(data, 'lxml')
    # Give the title of the Tumblr site as name for the image folder
    title = soup.title.text

    dir_path = os.path.dirname(os.path.abspath(__file__))
    # Name the new folder with the title variable, taken from Tumblr site
    download_folder = os.path.join(dir_path, str(title))
    if os.path.exists(download_folder):
        pass
    else:
        os.mkdir(download_folder)
    # Track down the images and download them into the folder you just created
    for link in soup.find_all("img"):
        image = link.get("src")
        if re.search("78.media.tumblr.com/", image):
            img_name = image.split("/")[-1]
            img_path = os.path.join(download_folder, img_name)
            urlretrieve(image, img_path)
# Now we need to find the "next" button for this page

    print("Done downloading all images from " + title)
"""
This is very useful as an idea - XPATH
//li[@class="post"]//img/@src
"""
# Print Welcome message, request user input: TUMBLR URL
input_url = input("Welcome to Tumblr Image Scrape!\n\n\nPlease provide the URL "
"of a Tumblr from which you wish to download all the images, and then press "
"[ENTER]: ")
page_num = 1
while page_num:
    print("Downloaded: images from page "+ str(page_num))
    if page_num == 1:
        tumblr_scrape(input_url)
    else:
        tumblr_scrape(input_url + "page/" + str(page_num))
    page_num += 1
