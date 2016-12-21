import urllib
url = raw_input()
encurl = urllib.urlencode({'url': url})
tinyurl = 'http://tinyurl.com/api-create.php?%s' % encurl
# print tinyurl
url = urllib.urlopen(tinyurl)
print url.read()
# print url.headers.items()
