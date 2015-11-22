import sys
import urllib2
import re
import urllib
import os
import time 
cookie = "NID_AUT=0lN0VjMOuJ4t9h7kiDy7Bq1L2cslCD8UYutM6Za8qkhiwVHOH4lSsVp59MCQ857J; NID_SES=AAABV+pX1z5o/uPMdH0tcyJa5nK2ihf074MSNncW1lm+79Tx4TYiEd1PwK1/ykmGEx3uuCS6bcQePl3DaycBQPYqHUmGytEO8owXmRrbsVB6wfNxcO75oMKkJgSj0cRK2cNARqiv8nzX8hTtLjVCCaKj38mOOaiApEYg2Qmn5cgVOXGJWM1A3IKjQN3rbDimVQxwUEhoZj2ULDnBfKEYn1onoF2CqD0D0qMBFYx4+6LvTNZZ4pcPCKsnxxvzn32Je2SJu55ZNRWChyIUO3bpbk+Zr0Ibq82jUgERJTdziEcWSXGvDCFhscXEJdyqdPHHRYv3+kOPihJrOUv23RvCUvI19iF1kDDmSkBdR9yY7OvTrT6DC29yvoBsjo/xO8uhqtAAqUSrJQnvX+IFzjDqkFmrTDup5IU1bXLuYrJCd7/YAlDx6XsRhGpGDFGTzxV3tzTXCiAWFbvLBRpr110M+z2xoag="

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
		print "Usage : fuckweb.py [url] [no] [name]"
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