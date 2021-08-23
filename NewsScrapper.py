import os
import bs4
import requests
import lxml

# getting the cwd
cwd=os.getcwd()+"\\"

news=["india","business","world"]

for typeNews in news:
    # making directory for each typeNews
    path=os.path.join(cwd,typeNews)
    try:
        os.mkdir(path)
    except Exception as e:
        print(e)
    # changing cwd to newly made directory
    os.chdir(path)

    link = f"https://timesofindia.indiatimes.com/{typeNews}"
    try:
        listoflinks = []
        source = requests.get(link)
        soup = bs4.BeautifulSoup(source.text, 'lxml')
         # getting the links
        try:
            span = soup.find_all('span', class_="w_tle")
            for x in span:
                y = x.find('a').get('href')
                listoflinks.append(y)
        except Exception as e:
            print(e)

        for x in listoflinks:
            if x[0] == "/" and x[1] == typeNews[0]:
                urll = "https://timesofindia.indiatimes.com"+x
                source = requests.get(urll)
                soup = bs4.BeautifulSoup(source.text, 'lxml')
                # printing the news
                try:
                    # prints the title
                    title = soup.find_all('h1', class_="_1Y-96")
                    z = title[0].get_text() +".txt"
                    # replacing to get a valid file name
                    if ":" in z:
                        z=z.replace(":","")
                    if "/" in z:
                        z=z.replace("/","")
                    if "*" in z:
                        z=z.replace("*","")
                    if "?" in z:
                        z=z.replace("?","")
                    if "<" in z:
                        z=z.replace("<","")
                    if ">" in z:
                        z=z.replace(">","")
                    if "|" in z:
                        z=z.replace("|","")
                    if '"' in z:
                        z=z.replace('"',"\"")
                    f=open(z,"w",encoding='utf-8')
                    f.write(title[0].get_text())
                    f.write("\n")
                    f.write("\n")

                    # printing the date
                    date = soup.find_all('div', class_="yYIu- byline")
                    f.write(date[0].get_text())
                    f.write("\n")
                    f.write("\n")

                    # prints the body
                    body = soup.find_all('div', class_="_3YYSt clearfix")
                    for x in body:
                        f.write(x.get_text())
                        f.write("\n")
                        f.write("\n")
                        f.write("--------------------------------------------------------------------------------------------------")
                except Exception as e:
                    print(e)
                finally:
                    f.close()
    except Exception as e:
        print(e)