import requests
import re
from requests.exceptions import RequestException

def get_one_page(url):
    
    headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'deflate',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }

    try:
        response = requests.get(url,headers=headers)
        
        if response.status_code == 200:
            return response.text
        return None

    except RequestException as e:
        print("出错了:%s"%(e.message))
        return None

def html_parser(html):
    pattern = re.compile("<dd>\s*(<i\s*class=.*>.*</i>).*</dd>",re.S)
    item = re.findall(pattern,html)
    print(item)


def main():
    url ='http://maoyan.com/board/4?'
    html = get_one_page(url)
    html_parser(html)

if __name__ == '__main__':
    main()

