from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


##  Scrape data from NACCRR

base_url = 'http://naccrrapps.naccrra.org/navy/directory/programs.php?program=omcc&state=CA&pagenum='

max_pages = 50

appended_data = []

for page in range(1, max_pages + 1):
    url = base_url+str(page)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    td_all = soup.find('table').find_all('td')
    
    td_all_list = []
    for td in soup.find('table').find_all('td'):
        td_all_list.append(td.get_text())
        
    df = pd.DataFrame(np.array(td_all_list).reshape(int((len(td_all_list)/8)),8), # Split data into 8 columns
                  columns=['provider_name','type_of_care',
                           'address','city','state','zip','phone','email'])
    appended_data.append(df)
    
    if len(df) < 25:  # Fewer than 25 records means it's the last page, therefore terminate.
       break

appended_data = pd.concat(appended_data)


output_file = 'outputs/scraped_data.csv'
appended_data.to_csv(output_file, index=None)


print('Total rows scraped : ' + str(len(appended_data)))
print('Saved to: ' + output_file)
