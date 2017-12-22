import requests
import re

def getHTML():
    url = '''http://www.htqyy.com/genre/musicList/1?pageIndex=1&pageSize=20&order=hot'''
    html = requests.get(url)
    print(html.text)

    
if __name__ == '__main__':
    getHTML()