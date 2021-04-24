import wikipediaapi


def printArticle(description_size):
    print('Titel des Wikipedia Artikels: {}'.format(page_py.title))
    print('Link zum Artikel: {}'.format(page_py.fullurl))
    print('Beschreibung: \n{}'.format(page_py.summary[0:description_size]))


wiki_api = wikipediaapi.Wikipedia('de')
page_py = wiki_api.page(input('Wikipedia Artikel: '))

if page_py.exists() is False:
    print('Dieser Wikipedia Artikel konnte nicht gefunden werden.')
    pass

description_size_string = input('Wie viele Zeichen soll die Beschreibung von Wikipedia dir ausgeben? ')

try:
    printArticle(int(description_size_string))
except ValueError as _:
    print("Bitte gib eine Zahl an.")
