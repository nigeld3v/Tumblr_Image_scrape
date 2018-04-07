# Tumblr_Image_scrape
This project employs Python3 and BeautifulSoup to scrape a Tumblr site (with the url provided by the user) to download, page by page, all the images and gifs from the site posts. This is an excellent tool for archiving other peoples' Tumblrs <3

HOW TO USE (for non-programmers)

Make sure you have room on your drive for what could be several Gigs of images and GIFs!!!

Okay,

***OPEN TERMINAL*** 
-or, for non-computery folks:
1) On your Mac keyboard, hit Command + [SPACEBAR]
2) type "terminal" and hit the enter key (you should now see a black field that allows you to type things)

Install PIP3
```python get-pip.py```

Install the latest version of Python
```sudo apt-get python 3.6.1```

Install beautifulsoup
```sudo pip3 install beautifulsoup4```

download Tumblr_Image_scrape.py file from ```https://github.com/nigeld3v/Tumblr_Image_scrape/blob/master/Tumblr_Image_scrape.py```

In Terminal, you want to change your working directory to the folder where you have downloaded 'Tumblr_Image_scrape.py'
If you do not know how to navigate the files on your computer using Terminal, here is a good resource:
https://www.digitalocean.com/community/tutorials/how-to-use-cd-pwd-and-ls-to-explore-the-file-system-on-a-linux-server
You should easily be able to find the right file using "pwd", "cd", and "ls" commands in terminal.

Once you have changed your directory to the file where Tumblr_Image_scrape.py was saved, type:
Python3 Tumblr_Image_scrape.py
and then press the [Enter] key on your keyboard.

You will be prompted to provide a Tumblr URL. Type or paste the address of the Tumblr, then press the [Enter] key on your keyboard.
  
Press Enter. The script should run and download the Tumblr site's images, page by page, and store them in a folder (title will be the Tumblr site's name) in the same directory where Tumblr_Image_scrape.py is kept.

Note: if it works, this script will continue to run until you make it stop. The easiest way to do this in Terminal is to hit the [Control]+[C] keys on your keyboard.

<3 <3 <3 <3 <3
Features to look out for in the future:

> Exception handling:
- terminate/interrupt the script when there is no more image content to scrape

> Turning this whole thing into a browser plugin
