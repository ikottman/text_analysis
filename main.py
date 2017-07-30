import os
from text_analyzer import TextAnalyzer

def title_case(string):
  return string.replace('_', ' ').title()

for author in os.listdir('text'):
  texts = os.listdir("text/{}".format(author))
  for book in texts:
    text = open("text/{}/{}".format(author, book)).read()
    title = title_case(book.replace('.txt', ''))
    csv = TextAnalyzer.analyze(text, title, title_case(author))
    print(csv)
