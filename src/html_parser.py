from html.parser import HTMLParser
from urllib.request import urlopen, Request

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

def get_source(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    return html.decode()

html = get_source('https://techguide.sh/pt-BR/path/java/')

parser = MyParser()
print(parser.feed(html))

# # Retornar o número de polos de um curso da Univesp
#
# class MyParserPolosUnivesp(HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.n_polos = 0
#     def handle_starttag(self, tag, attrs):
#         if tag == 'p':
#             for attr in attrs:
#                 if attr[0] == 'class' and attr[1] == 'item-polos':
#                     self.n_polos += 1
#     def num_polos(self):
#         return self.n_polos
#
# html_univesp = get_source('https://univesp.br/cursos/engenharia-de-computacao')
# parser_univesp = MyParserPolosUnivesp()
# print(parser_univesp.feed(html_univesp))
# print(parser_univesp.num_polos())