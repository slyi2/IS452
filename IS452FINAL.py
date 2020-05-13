#!/usr/bin/env python
# coding: utf-8

# In[220]:


import requests #modules that loads html
from bs4 import BeautifulSoup #parse html
#bs4 is a library from BeautifulSoup used to parse the html codes
#loads the webpage, and creates Beautiful Soup objects
response = requests.get('https://www.onetonline.org/link/summary/11-3121.00')
soup = BeautifulSoup(response.content, 'html.parser')

#Job Zone Table ----

table = soup.find('table', {'summary':"Job Zone information for this occupation" }) 
#by using XPath helper, I first located the Job Zone info covering basic overall info about the position
#Even though locating html is a bit different, it was really helpful to understand the syntax that's used in this library.
#then, I used soup.find() to locate the table I wanted

data = [] #I created an empty list where this Job Zone information will be saved
for tr in table.find_all('tr'): #loop over all the tr tags 
    tds = list(tr.find_all('td')) #create a list of all the td tags
    column_name = tds[0].text #locate column names
    info = tds[1].text #locate column info
    data.append([column_name,info]) #append them into the empty data list for csv export
   
import csv    #typical outfile process we used in class for csv export.
outfile = open('Job_Summary.csv','w')
csv_out = csv.writer(outfile)
csv_out.writerow(['Infotype','information'])
csv_out.writerows(data)
outfile.close()

