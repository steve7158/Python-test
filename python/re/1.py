import re
patterns =['term1', 'term2']
text='This is a string with term1 but not the other'
for obj in patterns:
    print 'I am searching for '+obj
    if re.search(obj, text):
        print 'match'
    else:
        print 'not match'
