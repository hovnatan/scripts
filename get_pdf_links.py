# from http://stackoverflow.com/questions/6222911/how-can-i-grab-pdf-links-from-website-with-python-script/6223422#6223422 
# answer http://stackoverflow.com/a/6223422/2928970

# modules we're using (you'll need to download lxml)
import lxml.html, urllib2, urlparse, sys

# the url of the page you want to scrape
base_url = sys.argv[1]

# fetch the page
res = urllib2.urlopen(base_url)

# parse the response into an xml tree
tree = lxml.html.fromstring(res.read())

# construct a namespace dictionary to pass to the xpath() call
# this lets us use regular expressions in the xpath
ns = {'re': 'http://exslt.org/regular-expressions'}

# iterate over all <a> tags whose href ends in ".pdf" (case-insensitive)
for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):

    # print the href, joining it to the base_url
    print urlparse.urljoin(base_url, node.attrib['href'])
