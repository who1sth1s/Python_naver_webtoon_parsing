import sys
import urllib2
import re
import urllib
import os
import time 
cookie = "NID_AUT=7eZ7OnxUeGjCygDRKnwQGZT2hdpnH3Qk+eMy6LDRpnGAT9xEVaN5Ba4fK3XUMXZ9; NID_SES=AAABVavXcril8wD3Gdr2tt4eI7TrlNJIkJLfWwHf4zDudV/uRQ9IgdQ/MFvBOHvfhRYPEa8kSmizguNHeyqicBnn62jknwgW73MvV18cARuQhLpvBZ8aXlL9+p6GwzMIMz1UkQ7+IhZ7pPwCM7J2JPb3mZYL2xNTNzxvfqZtZWI8q0EcAt4vrTejdPAtRrghHzRunzvrWLODvxSj/VzK3Y5aQiH7taRRFsuJL+hbK8S6eJFdrIAJF95mg2NtM/Jkkr7TyPsn4qpcAedwiJ3gyUVUMigOw+vCRcMx3AWC9GgD3grItRoPTQ/nPeDjxA4F6KRDcUUQZAFOT7Hj6xmwZ5o9sSp7ln3WOIk7YJuroBPsrOJH8kGM22m3PKCguHMllLTiGdHL7q+SWByTFLw3YJS3ZHTBS/t5erU38btYyryI/acp/tk3alfmaVY6sCxNStdwdBhypuf8JIoxmKAnZ/sBwK8="

def parsing(html):
	exp = re.compile(r'<img.+?src="(http://imgcomic\.naver\.net/webtoon/[0-9]+/[0-9]+/(.+?\.(jpg|png|gif|JPG|PNG|GIF)))".*?')
	img = exp.findall(html)
	return img

def gethtml(url):
	user_agent = "Mozila/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36\r\n"
	Referer = url
	req = urllib2.Request(url)
	req.add_header("User-Agent", user_agent)
	req.add_header("Referer", url)
	req.add_header("Cookie", cookie)
	response = urllib2.urlopen(req) 
	the_page = response.read()
	return the_page

def main(argv):
	if len(argv) != 4:
		print "Usage : webtoon.py [url] [no] [name]"
		return 1
	url = argv[1]
	no = argv[2]
	os.system("mkdir " + argv[3])
	for i in range(1, int(no)+2):
		url2 = url[0:31] + "detail.nhn?" + url[40:] + "&no=" + str(i)
		print url2
		html = gethtml(url2)
		imgs = parsing(html)
		cnt = 1
		os.system("mkdir " + "/Users/gwonsejung/Desktop/webtoon/" + argv[3] + "/" + argv[3] + str(i))
		for img in imgs:
			print img[0]
			Referer = img[0]
			req = urllib2.Request(img[0])
			req.add_header("Referer", Referer)
			response = urllib2.urlopen(req) 
			the_page = response.read()
			f = open("/Users/gwonsejung/Desktop/webtoon" + "/" + argv[3] + "/" + argv[3] + str(i) + "/" + str(cnt), "wb")
			f.write(the_page)
			f.close()
			cnt += 1
		print "[*]Save complete"

if __name__ == '__main__':
    sys.exit(main(sys.argv))
