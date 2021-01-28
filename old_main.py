import calendar
import os
import time
from urllib.request import urlopen

import requests
import zipfile
from bs4 import BeautifulSoup


def main():
    epochlist = [0, 0]

    date_time = "2019_11_08_14_42_08"  # random initiation

    while True:

        link = "http://mbd.hu/uris/"
        f = urlopen(link)
        html = f.read()

        soup = BeautifulSoup(html)  #raises warning for some reason
        table = soup.find("table")

        try:
            date_time = open_dir(table)
        except:
            print("file not found")

        if create_epoch(date_time) != epochlist[1]: #if folder has been replaced, grab data and download it
            epochlist[0] = epochlist[1]
            epochlist[1] = create_epoch(date_time)
            listlink = grab_list(date_time, epochlist[0])
            print(epochlist)
        else:
            print("File Unchanged!")

        time.sleep(10) #sleep time to allow zip file to fully download, otherwise it gets corrupted


def open_dir(table):
    for row in table.find_all("tr")[1:]:

        for td in row.find_all("td"):

            data = td.get_text()

            if data.startswith("201" or "202"):
                filename = data
                date_time = filename[:-2]

    print(date_time)
    return date_time


def grab_list(date_time, pw):
    ziplink = "http://mbd.hu/uris/" + date_time + "/urilist.zip"

    pw = str(pw) #convert pwd to string as .encode doesnt accept int

    if os.path.isfile("urilist.txt"):
        os.remove("urilist.txt")
    if os.path.isfile("urilist.zip"): #delete previous file if it exists to replace it
        os.remove("urilist.zip")

    try: #estalish connection and get data
        target_path = "urilist.zip"
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

        response = s.get(ziplink, stream=True, allow_redirects=True)
        handle = open(target_path, "wb")
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)
        handle.close()
    except:
        print("Unable to download file")

    try:
        with zipfile.ZipFile("urilist.zip") as zf:
            zf.extractall(pwd=pw.encode())
    except:
        print("password incorrect")

    try: #open list, read content from global list to dict; compare, count and add content back to global file
        with open("urilist.txt", "r") as f:
            lines = f.read()
            for url in lines.split():
                get_message(url)
    except:
        print("problem opening file")

    return


def create_epoch(date_time): #convert name to epoch time
    pattern = '%Y_%m_%d_%H_%M_%S'
    epoch = int(calendar.timegm(time.strptime(date_time, pattern)))
    return epoch


def get_message(link): #open global list, import to dict to analyse most occuring url
    try:
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

        response = s.get(link)
        if len(response.content) < 100:
            print('\n\nLink & Message:\n', link, '\n', response.content, '\n')
    except:
        pass
    return


if __name__ == '__main__':
    main()
