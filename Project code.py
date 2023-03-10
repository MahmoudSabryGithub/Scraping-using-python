# importing required libraries
import requests
from bs4 import BeautifulSoup
from pandas import *

#The number of pages for search
page_num=input("inter the number of pages:")
f=[]

#looping over all pages to extract jobs from specified pages
for i in range(int(page_num)):
    #get connect with the page
    page = requests.get("https://wuzzuf.net/search/jobs/?a=hpb&q=Data%20analyst&start=" + str(i))

    #extracting the source of the page
    def main(page):
        src = page.content
        soup = BeautifulSoup(src, "lxml")
        jobs = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
        d = []
        #Extracting required knowledge from the page
        def main_features(jobs):
            title = jobs.contents[0].find("h2").text.strip()
            description = jobs.contents[0].find("div", {"class": "css-d7j1kk"}).find("a").text.strip("-")
            location = jobs.contents[0].find("span", {"class": "css-5wys0k"}).text.strip()
            time = jobs.contents[0].find("span", {"class": "css-1ve4b75 eoyjyou0"}).text.strip()
            d.append({"Job title": title, "Job description": description, "Location": location,
                      "Job time": time})

        for i in range(1, len(jobs)):
            main_features(jobs[i])
        f.extend(d)



    main(page)


#Creating a DataFrame and Csv file 
data=DataFrame(f)
print(data)
data.to_csv("C:\\Users\\DELL\\Documents\\Python\\Scraping using python\\result file.csv",index=False)














