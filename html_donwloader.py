import requests

def take_html(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Unable to access the site: {response.status_code}")
    for order in range(0, 255):
        html_content = html_content.replace(chr(order), "")
    return html_content

if __name__ == "__main__":
    print(take_html("https://www.setn.com/"))