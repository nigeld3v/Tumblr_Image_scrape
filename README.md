# Tumblr_Image_scrape
This project employs Python3 and BeautifulSoup to scrape a Tumblr site (with the url provided by the user) to download, page by page, all the images and gifs from the site posts. This is an excellent tool for archiving other peoples' Tumblrs <3

HOW TO USE (for non-programmers)

Make sure you have room on your drive for what could be several Gigs of images and GIFs!!!

Okay,

***OPEN TERMINAL*** 
-or, for non-computery folks:
1) On your Mac keyboard, hit Command + [SPACEBAR]
2) type "terminal" and hit the enter key (you should now see a black field that allows you to type things)

***Install PIP3***
python get-pip.py
***Install the latest version of Python***
sudo apt-get python 3.6.1
***Install beautifulsoup***
sudo pip3 install beautifulsoup4

<3 <3 <3 <3 <3
Future features to look out for in the future:

Exception handling:
- accepts URL with no "http://"
- accepts URL with no "/" at end of url
- terminate/interrupt the script when there is no more image content to scrape
- meaningful image file naming (i.e. "FolderName_1" or "DDMMYY_FolderName_1")
