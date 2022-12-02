#exec(open('news_authors.py').read())

import json
import requests
from bs4 import BeautifulSoup
import re
from django.contrib.auth.models import User

hpen = "https://www.hamropatro.com/news"

lis={}

page = requests.get(hpen, verify=False)

soup = BeautifulSoup(page.content, "html.parser")
timediv = soup.findAll("div", class_ = "chip",attrs={'style':'display:block;cursor: pointer;background: none;border: none'})

for time_div in timediv:
    try:
        link=time_div.find_previous('a')['href']
        link=re.findall('(?<=&ss=).*&',link)[0][:-1]
        name=(time_div.find("span").text)
        img=(time_div.find("img")['src'])
        img=re.findall('(?<=images/).*',img)[0]
        imglink='http://storage.googleapis.com/hamropatro-storage/assets/hamropatro.com/images/'+img        
        lis[link]=[name,img] 
    except:
        pass
lis['hamropatro.com']=['Hamro Patro', 'a47db2bf-c3e3-4bde-bdb5-92f2129cc22e.png']

for comp in lis:
    user=User.objects.create_user(lis[comp][0], password="L|abadabadabbadwkwk!/.")
    # lis[comp].append(user.id)
    img_data = requests.get('http://storage.googleapis.com/hamropatro-storage/assets/hamropatro.com/images/'+lis[comp][1]).content
    with open('.\\media\\pfps\\'+comp.split('.')[0]+'.png', 'wb') as handler:
        handler.write(img_data)
    user.profile.image='pfps/'+comp.split('.')[0]+'.png'
    user.save()
    
# print(lis)