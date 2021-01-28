import bs4
import requests
import lxml

link="https://timesofindia.indiatimes.com/business"
try:
    listoflinks=[]
    source=requests.get(link)
    soup=bs4.BeautifulSoup(source.text,'lxml')
    try:
        span=soup.find_all('span', class_="w_tle")
        for x in span:
            y=x.find('a').get('href')
            listoflinks.append(y)
    except:
        print("Error")

    
    for x in listoflinks:
        if x[0]=="/" and x[1]=="b":
            urll="https://timesofindia.indiatimes.com/"+x
            source=requests.get(urll)
            soup=bs4.BeautifulSoup(source.text,'lxml')
            print(urll)
            try:
                # prints the title
                title=soup.find_all('h1',class_="_23498")
                for x in title:
                    print("Title = ",x.get_text())
                    print()
                date=soup.find_all('div',class_="_3Mkg- byline")
                for x in date:
                    print("Date = ",x.get_text())
                    print()
                # prints the body
                body=soup.find('div',class_="_1_Akb clearfix")
                for x in body:
                    print(body.get_text())
                    print("--------------------------------------------------------------------------------------------------")
            except:
                print("ERROR")
except:
    print("ERROR")