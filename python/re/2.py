import re
def mult(pats,phrase):
    for pat in pats:
        print 'searching for pattern: {}'.format(pat)
        print re.findall(pat,phrase)
        print '\n'
p='sdsd..sdddss.sddssdds.sdsdsdsdsd.ssdddsssdddsssd'
mult(['sd+'],p)

