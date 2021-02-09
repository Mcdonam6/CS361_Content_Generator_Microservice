# Mike McDonald
# CS361
# Content Generator - Sprint 3 implementation

import sys, csv, requests, re
from bs4 import BeautifulSoup, NavigableString
from re import search

def interface_select():
    if len(sys.argv)>0:
        content_generator(sys.argv[1])
    else:
        gui_interface()


def content_generator(input):
    # When provided with an input file, this function Creates an Output file and write results
    with open('output.csv', 'w', newline='') as outputFile:
        writer = csv.writer(outputFile, delimiter='\t', quoting = csv.QUOTE_NONE, escapechar='\t')

        # Read input keywords from passed CSV file, call search function and write results
        with open(input, newline='') as csvfile:
            keywordReader = csv.reader(csvfile)
            row=next(keywordReader)
            row[0]=row[0]+', output_content'
            writer.writerow(row)
            row=next(keywordReader)
            keywords = row[0].split(';')
            keyword1 = keywords[0]
            keyword2 = keywords[1]
            content = [row[0] + ', ' + wikipedia_search(keyword1, keyword2)]
            writer.writerow(content)

def gui_interface():
    # TO-DO: implement tkinter GUI for application
    pass


def wikipedia_search(keyword1, keyword2):
    response = requests.get(url="http://en.wikipedia.org/wiki/"+keyword1) 
    page = BeautifulSoup(response.content, 'html.parser')
    for pTag in page.find_all('p'):
        if search(keyword1, str(pTag), re.IGNORECASE) and search(keyword2, str(pTag), re.IGNORECASE):
            return stripTags(str(pTag))
    return "No Content Found"

def stripTags(soupParagraph):
    strippedString=''
    inTag=False
    for character in soupParagraph:
        if character == "<" or character == "[":
            inTag=True
        if not inTag:
            strippedString+=character
        elif character == ">" or character == "]":
            inTag=False
    return strippedString


if __name__ == '__main__':
    interface_select()