import bs4
import requests
import lxml

link="https://timesofindia.indiatimes.com/business"
try:
    listoflinks = []
    source = requests.get(link)
    soup = bs4.BeautifulSoup(source.text, 'lxml')
    try:
        span = soup.find_all('span', class_="w_tle")
        for x in span:
            y = x.find('a').get('href')
            listoflinks.append(y)
    except:
        print("Error")

    for x in listoflinks:
        if x[0] == "/" and x[1] == "b":
            urll = "https://timesofindia.indiatimes.com/"+x
            source = requests.get(urll)
            soup = bs4.BeautifulSoup(source.text, 'lxml')
            # print(urll)
            try:
                # prints the title
                title = soup.find_all('h1', class_="_23498")
                # for x in title:
                # print("Title = ",x.get_text())
                x = title[0].get_text()
                y = ".txt"
                z = x +y
                if ":" in z:
                    z=z.replace(":","")
                # if "Had no" in z:
                #     print(urll)
                f=open(z,"w")
                f.write(title[0].get_text())
                f.write("\n")
                f.write("\n")
                # print()

                date = soup.find_all('div', class_="_3Mkg- byline")
                # for x in date:
                # print("Date = ",x.get_text())
                f.write(date[0].get_text())
                f.write("\n")
                f.write("\n")
                # print()

                # prints the body
                body = soup.find('div', class_="_1_Akb clearfix")
                for x in body:
                # print(body.get_text())
                # print("--------------------------------------------------------------------------------------------------")
                    f.write(x.get_text())
                    f.write("\n")
                    f.write("\n")
                    f.write("--------------------------------------------------------------------------------------------------")
                    f.write("\n")
                    f.write("\n")
            except:
                print("ERROR")
            finally:
                f.close()
except:
    print("ERROR")
