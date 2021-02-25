# Mike McDonald
# CS361
# Content Generator - Sprint 4 implementation


import sys, csv, requests, re, tkinter, subprocess
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
    keywords = parseKeywords(str(input))
    keyword1 = keywords[0]
    keyword2 = keywords[1]
    life_generator_interface(keyword1,keyword2)
    wikipedia_search(keyword1, keyword2)


def parseKeywords(inputFile):
    # Read input keywords from passed CSV file, call search function and write results
    with open(inputFile, newline='') as csvfile:
        keywordReader = csv.reader(csvfile)
        row=next(keywordReader)
        row=next(keywordReader)
        keywords = row[0].split(';')
        return keywords

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

    # Content Output Field 
    outputlabel = ttk.Label(frame,text='Output: ').grid(column=2, row=9, columnspan=10, sticky=W)
    output = Text(frame, height=18, wrap=WORD)
    output.grid(column=2, row=10, columnspan=8, rowspan=5, sticky=W)
    scrollbar = Scrollbar(frame)
    output.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = output.yview)
    scrollbar.grid(column = 10, row = 10, rowspan = 5, sticky=N+S+W)

    # LifeGen Output Field 
    outputlabel = ttk.Label(frame,text='Top (Up to 10) Related Products: ').grid(column=2, row=16, columnspan=10, sticky=W)
    life_output = Text(frame, height=18, wrap=WORD)
    life_output.grid(column=2, row=17, columnspan=8, rowspan=5, sticky=W)
    scrollbar = Scrollbar(frame)
    life_output.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = life_output.yview)
    scrollbar.grid(column = 10, row = 17, rowspan = 5, sticky=N+S+W)

    # Submit Button
    ttk.Button(frame, text="Submit Request--->", command = lambda : gui_wiki(keyword1, keyword2, output, life_output)).grid(column=10, row=15, sticky=W)
    
    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    kw1_entry.focus()
    root.mainloop()

def gui_wiki(keyword1, keyword2, output,life_output):
    try:
        kw1=keyword1.get()
        kw2=keyword2.get()

        life_output.delete(1.0, END)
        result=life_generator_interface(kw1, kw2)
        resultString=life_generator_gui_parse(result)
        life_output.insert(1.0, resultString)

        output.delete(1.0, END)
        result=wikipedia_search(kw1, kw2)
        output.insert(1.0, result)
        
    except ValueError:
        pass

def wikipedia_search(keyword1, keyword2):
    response = requests.get(url="http://en.wikipedia.org/wiki/"+keyword1) 
    page = BeautifulSoup(response.content, 'html.parser')
    for pTag in page.find_all('p'):
        if search(keyword1, str(pTag), re.IGNORECASE) and search(keyword2, str(pTag), re.IGNORECASE):
            result = stripTags(str(pTag))
            break
        else:
            result = "No Content Found"
    with open('output.csv', 'w', newline='') as outputFile:
        writer = csv.writer(outputFile, quoting = csv.QUOTE_MINIMAL, escapechar='\t')
        writer.writerow(['input_keywords']+['output_content'])
        content = str(keyword1) + ';' + str(keyword2)
        writer.writerow([content] + [str(result)])
    return result

def stripTags(soupParagraph):
    strippedString=''
    tagLevel=0
    for character in soupParagraph:
        if character == "<" or character == "[":
            tagLevel+=1
        elif tagLevel==0 :
            strippedString+=character            
        elif character == ">" or character == "]":
            tagLevel-=1
    return strippedString

def life_generator_interface(keyword1, keyword2)-> str:
    # Create Input file for top 10 of that category  
    with open('life_generator_input.csv', 'w', newline='') as inputFile:
        writer = csv.writer(inputFile, quoting = csv.QUOTE_MINIMAL, escapechar='\t')
        writer.writerow(['input_type']+['input_item_category']+['input_number+to_generate'])
        writer.writerow([keyword1] + [keyword2]+[10])

    # Input File based call, rename output
    subprocess.run(['python3', 'life_generator/life_generator.py', 'life_generator_input.csv'])
    subprocess.run(['mv', 'output.csv', 'life_generator_output.csv'])

    # Delete created input file 
    subprocess.run(['rm', 'life_generator_input.csv'])
    return 'life_generator_output.csv'

def life_generator_gui_parse(filePath):
    # Read life gen output file and return string for GUI
    topTenProducts='Item Name\n-------------------------------------------------------\n'
    with open(filePath, newline='') as csvfile:
        resultsReader = csv.reader(csvfile)
        row=next(resultsReader)
        anyResults = False
        for item in range(10):
            try:
                row=next(resultsReader)
            except StopIteration:   
                break
            anyResults=True
            topTenProducts += row[3]+'\n' 
        if not anyResults:
            topTenProducts+= 'No Results Found'
         
    return topTenProducts

if __name__ == '__main__':
    interface_select()