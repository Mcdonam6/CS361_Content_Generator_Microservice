# Mike McDonald
# CS361
# Content Generator - Sprint 3 implementation


import sys, csv, requests, re, tkinter
from bs4 import BeautifulSoup, NavigableString
from re import search
from tkinter import *
from tkinter import ttk

def interface_select():
    if len(sys.argv)>1:
        content_generator(sys.argv[1])
    else:
        gui()


def content_generator(input):
    # When provided with an input file, this function Creates an Output file and write results
    with open('output.csv', 'w', newline='') as outputFile:
        writer = csv.writer(outputFile, quoting = csv.QUOTE_MINIMAL, escapechar = '\t')

        # Read input keywords from passed CSV file, call search function and write results
        with open(input, newline='') as csvfile:
            keywordReader = csv.reader(csvfile)
            row=next(keywordReader)
            writer.writerow([row[0]]+['output_content'])
            row=next(keywordReader)
            keywords = row[0].split(';')
            keyword1 = keywords[0]
            keyword2 = keywords[1]
            content = wikipedia_search(keyword1, keyword2)
            writer.writerow([row[0]]+[content])

def gui():
    # Main Window
    root = Tk()
    root.title("Kramaral Corporation Content Generator")
    frame = ttk.Frame(root, padding = "3 3 12 12")

    # Grid layout
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Introduction
    ttk.Label(frame, text='Welcome to the Kramaral Content Generator Service! Please use the options below to specify the type of content you require, and type the keywords for your request into the fields below.', wraplength=700).grid(column=1, row =1, columnspan=10, rowspan=3)

    # Main Topic Keyword Entry
    keyword1 = StringVar()
    kw1_entry = ttk.Entry(frame, width=7, textvariable=keyword1)
    kw1_entry.grid(column=2, row=7, sticky=(W, E))
    ttk.Label(frame,text='Main Topic').grid(column=3, row=7, sticky=W)

    # Sub-topic Keyword Entry
    keyword2 = StringVar()
    kw2_entry = ttk.Entry(frame, width=7, textvariable=keyword2)
    kw2_entry.grid(column=2, row=8, sticky=(W, E))
    ttk.Label(frame,text='Sub-Topic').grid(column=3, row=8, sticky=W)

    # Output Field 
    outputlabel = ttk.Label(frame,text='Output: ').grid(column=2, row=9, columnspan=10, sticky=W)
    output = Text(frame, height=18, wrap=WORD)
    output.grid(column=2, row=10, columnspan=8, rowspan=5, sticky=W)
    scrollbar = Scrollbar(frame)
    output.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = output.yview)
    scrollbar.grid(column = 10, row = 10, rowspan = 5, sticky=N+S+W)

    # Submit Button
    ttk.Button(frame, text="Submit Request--->", command = lambda : gui_wiki(keyword1, keyword2, output)).grid(column=10, row=15, sticky=W)
    
    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    kw1_entry.focus()
    root.mainloop()

def gui_wiki(keyword1, keyword2, output):
    try:
        output.delete(1.0, END)
        kw1=keyword1.get()
        kw2=keyword2.get()
        result=wikipedia_search(kw1, kw2)
        output.insert(1.0, result)
        with open('output.csv', 'w', newline='') as outputFile:
            writer = csv.writer(outputFile, quoting = csv.QUOTE_MINIMAL, escapechar='\t')
            writer.writerow(['input_keywords']+['output_content'])
            content = str(kw1) + ';' + str(kw2)
            writer.writerow([content] + [str(result)])
    except ValueError:
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