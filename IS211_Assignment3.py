#!/usr/bin/env python
# coding: utf-8

# In[19]:


import re
import argparse
import csv
import urllib2

url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

image_hits = 0
browser_hits = 0
columns = 0

IE = ['Internet Explorer', 0]
CHROME = ['Google Chrome', 0]
FIREFOX = ['Mozilla Firefox', 0]
SAFARI = ['Safari', 0]

for line in cr:
    columns += 1
    if re.search("Firefox", line[2], re.I):
        FIREFOX[1] += 1
    elif re.search(r"MSIE", line[2]):
        IE[1] += 1
    elif re.search(r"Chrome", line[2]):
        CHROME[1] += 1
    elif re.search(r"Safari", line[2]) and not re.search("Chrome", line[2]):
        SAFARI[1] += 1
    if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
        image_hits += 1
        
    image_hits_counter = (float(image_hits) / columns) * 100
    
    browser_hits = (CHROME, IE, SAFARI, FIREFOX)
    
    pop_count = 0
    
    pop_browser = ' '
    
    for b in browser_hits:
        if b[1] > pop_count:
            pop_count = b[1]
            pop_browser = b[0]
        else:
            continue
    stats = ('There were {} page hits today, image requests account for {}% of '
            'hits. \n{} has the most hits with {}.').format(columns, image_hits_counter, pop_browser, pop_count)
    

    print stats
            


# In[ ]:





# In[ ]:




