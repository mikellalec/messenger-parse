import numpy as np
import pandas as pd
import datetime
from bs4 import BeautifulSoup

messages_index=BeautifulSoup(open("messages/messages.htm"),"html5lib")
print("Opened messages/mesages.htm")

df=pd.DataFrame([], columns=['friend', 'date', 'contents'], index=[])
count=0

for a in messages_index.find_all('a', href=True):
    if(a['href'][:2]=="me"):##message file, parse it
        message_file=BeautifulSoup(open(a['href']),"html5lib")
        print(a['href'])
        friend=
        for message in message_file.find_all("div", {"class": "message"}):
            df.append
            count=count+1

print(count)
