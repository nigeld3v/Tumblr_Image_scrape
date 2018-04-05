# Tumblr_Image_scrape
This project employs Python3 and BeautifulSoup to scrape a Tumblr site (with the url provided by the user) to download, page by page, all the images and gifs from the site posts. This is an excellent tool for archiving other peoples' Tumblrs <3

HOW TO USE (for non-programmers)

Make sure you have room on your drive for what could be several Gigs of images and GIFs!!!

Okay,

***OPEN TERMINAL*** 
-or, for non-computery folks:
1) On your Mac keyboard, hit Command + [SPACEBAR]
2) type "terminal" and hit the enter key (you should now see a black field that allows you to type things)

```Install PIP3```
python get-pip.py

```Install the latest version of Python```
sudo apt-get python 3.6.1

```Install beautifulsoup```
sudo pip3 install beautifulsoup4

download Tumblr_Image_scrape.py file from ```https://github.com/nigeld3v/Tumblr_Image_scrape/blob/master/Tumblr_Image_scrape.py```

In Terminal, change your working directory to the folder where you have downloaded 'Tumblr_Image_scrape.py' type:
Python3 Tumblr_Image_scrape.py

You will be prompted to provide a Tumblr URL. Provide it in the format: 'http://www.<URL>.tumblr.com/' making sure that it begins with 'http://' and ends with '/'
  
Press Enter. The script should run and download the Tumblr site's images, page by page, and store them in a folder (title will be the Tumblr site's name) in the same directory where Tumblr_Image_scrape.py is kept.

<3 <3 <3 <3 <3
Features to look out for in the future:

Exception handling:
- accepts URL with no "http://"
- accepts URL with no "/" at end of url
- terminate/interrupt the script when there is no more image content to scrape
- meaningful image file naming (i.e. "FolderName_1" or "DDMMYY_FolderName_1")
