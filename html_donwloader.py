import requests
import time

def take_html(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return
    for order in range(0, 255):
        html_content = html_content.replace(chr(order), "")
    return html_content

    

if __name__ == "__main__":
    t1 = time.time()
    print(take_html("https://zh.wikipedia.org/zh-tw/Wikipedia:%E9%A6%96%E9%A1%B5"))
    t2 = time.time()
    print(t2-t1)