# web scraping script to tell the meaning of a word
import urllib2
from bs4 import BeautifulSoup

url = "https://www.merriam-webster.com/dictionary/"
word=raw_input("Enter Word:")
while(word!="-1"):
	wiki=url+word
	try:
		page = urllib2.urlopen(wiki)
		soup = BeautifulSoup(page,"html.parser")
		#find the html tag and class name by using inspect element 
		a=soup.find('span',class_='dt ')
		a.find('strong').decompose()
		t=a.text.strip()
		print t
	except urllib2.HTTPError, e:
	    print "Couldn't find the meaning of the word \'%s\'"%(word)
	except urllib2.URLError, e:
	    print "Couldn't find the meaning of the word \'%s\'"%(word)
	word=raw_input("Enter Word:")
