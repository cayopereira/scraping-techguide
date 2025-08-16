from urllib.request import Request, urlopen

def get_source(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = get_source('https://www.uol.com.br/')
#print(html)

# Evitando o erro HTTP Error 403: Forbidden
req = Request(url='https://sofifa.com', headers={'User-Agent': 'Mozilla/5.0'})

html_sofifa = urlopen(req).read()
print(html_sofifa)



