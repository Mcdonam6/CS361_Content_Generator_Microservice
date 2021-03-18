# Mike McDonald
# CS361
# Content Generator - Sprint 5 implementation


import sys, csv, requests, re, tkinter, subprocess
from bs4 import BeautifulSoup, NavigableString
from re import search
from tkinter import *
from tkinter import ttk
from gui_instructions import *

def interfaceSelect():
    if len(sys.argv)>1:
        contentGenerator(sys.argv[1])
    else:
        gui()


def contentGenerator(input):
    keywords = parseKeywords(str(input))
    lifeGeneratorInterface(keywords[0],keywords[1])
    wikipediaSearch(keywords[0], keywords[1])


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
    grid(root, frame)

    # Assemble initial Window elements
    ttk.Label(frame, text= introParagraph, wraplength=700).grid(column=1, row =1, columnspan=10, rowspan=3)
    keywords = keywordInputs(root, frame)
    contentCheck = tkinter.IntVar()
    contentCheckButton = ttk.Checkbutton(frame, text="Wiki Paragraph", variable=contentCheck, onvalue=1, offvalue=0)
    contentCheckButton.grid(column=2, row=4, columnspan = 3, sticky=W)
    ttk.Button(frame,text='(?)', command = lambda: openToolTip(contentOptionToolTip), width=3).grid(column=4, row=4)
    shoppingCheck = tkinter.IntVar()
    shoppingCheckButton = ttk.Checkbutton(frame, text="Top 10 Shopping", variable=shoppingCheck, onvalue=1, offvalue=0)
    shoppingCheckButton.grid(column=2, row=5, columnspan = 3, sticky=W)
    ttk.Button(frame,text='(?)', command = lambda: openToolTip(shoppingOptionToolTip), width=3).grid(column=4, row=5)

    output = None
    lifeGenOutput = None    
    guiElements = [keywords[0], keywords[1], contentCheck, shoppingCheck, output, lifeGenOutput, frame]

    
    # Submit Button and padding
    ttk.Button(frame, text="Submit Request--->", command = lambda : guiWiki(guiElements)).grid(column=9, row=9)
    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

def grid(root, frame):
    # Grid layout
    frame.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

def keywordInputs(root, frame):
    # Main Topic Keyword Entry and Tooltip button
    keyword1 = StringVar()
    kw1Entry = ttk.Entry(frame, width=16, textvariable=keyword1)
    kw1Entry.grid(column=2, row=7, columnspan = 3, sticky=W)
    ttk.Button(frame,text='(?)', command = lambda: openToolTip(mainTopicToolTip), width=3).grid(column=5, row=7, sticky=W)
    ttk.Label(frame,text='Main Topic').grid(column=4, row=7, sticky=E)

    # Sub-topic Keyword Entry and Tooltip button
    keyword2 = StringVar()
    kw2Entry = ttk.Entry(frame, width=16, textvariable=keyword2)
    kw2Entry.grid(column=2, row=8, columnspan = 3, sticky=W)
    ttk.Button(frame,text='(?)', command = lambda: openToolTip(subTopicToolTip), width=3).grid(column=5, row=8, sticky=W)
    ttk.Label(frame,text='Sub-Topic ').grid(column=4, row=8, sticky=E)
    return [keyword1, keyword2]

def openToolTip(tip):
    tipWindow = Tk()
    tipWindow.title = 'Content Generator Help'
    tipFrame = ttk.Frame(tipWindow, padding = "3 3 12 12")
    grid(tipWindow,tipFrame)
    ttk.Label(tipFrame, text= tip, wraplength=400).grid(column=1, row =1, columnspan=5, rowspan=3)
    tipWindow.mainloop()


def contentOutput(frame):
    # Content Output Field 
    global outputLabel
    outputLabel = ttk.Label(frame,text='Content Paragraph: ')
    outputLabel.grid(column=2, row=12, columnspan=10, sticky=W)
    global output
    output = Text(frame, height=18, wrap=WORD)
    output.grid(column=2, row=13, columnspan=8, rowspan=5, sticky=W)
    scrollbar = Scrollbar(frame)
    output.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = output.yview)
    scrollbar.grid(column = 10, row = 13, rowspan = 5, sticky=N+S+W)
    return output

def lifeOutput(frame):
    # LifeGen Output Field 
    global lifeLabel 
    lifeLabel= ttk.Label(frame,text='Top (Up to 10) Related Products: ')
    lifeLabel.grid(column=2, row=19, columnspan=10, sticky=W)
    global lifeGenOutput
    lifeGenOutput = Text(frame, height=18, wrap=WORD)
    lifeGenOutput.grid(column=2, row=20, columnspan=8, rowspan=5, sticky=W)
    scrollbar = Scrollbar(frame)
    lifeGenOutput.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = lifeGenOutput.yview)
    scrollbar.grid(column = 10, row = 20, rowspan = 5, sticky=N+S+W)
    return lifeGenOutput

def guiWiki(guiElements):

    keyword1 = guiElements[0]
    keyword2 = guiElements[1]
    contentCheck = guiElements[2]
    lifeGenCheck = guiElements[3]
    output = guiElements[4]
    lifeGenOutput = guiElements[5]
    frame = guiElements[6]

    try:
        keywords=[keyword1.get(),keyword2.get()]
        showHideContentParagraph(output, contentCheck, keywords, frame)
        showHideLifeGen(lifeGenOutput, lifeGenCheck, keywords, frame)
    except ValueError:
        pass

def showHideLifeGen(lifeGenOutput, lifeGenCheck, keywords, frame):
        # Create or destroy Life Gen Output
        if lifeGenOutput is None and lifeGenCheck.get():
            lifeGenOutput = lifeOutput(frame)
        elif isinstance(lifeGenOutput, tkinter.Text) and not lifeGenCheck.get():
            lifeGenOutput.grid_remove()
            lifeLabel.grid_remove()

        # Display Life Generator results
        if lifeGenOutput is not None:
            lifeGenOutput.delete(1.0, END)
            result=lifeGeneratorInterface(keywords[0], keywords[1])
            resultString=lifeGeneratorGuiParse(result)
            lifeGenOutput.insert(1.0, resultString)

def showHideContentParagraph(output, contentCheck, keywords, frame):
        # Create or destroy Content Output
        if output is None and contentCheck.get():
            output = contentOutput(frame)
        elif isinstance(output, tkinter.Text) and not contentCheck.get():
            output.grid_remove()
            outputLabel.grid_remove()

        # Display Content Generator results 
        if output is not None:
            output.delete(1.0, END)
            result=wikipediaSearch(keywords[0], keywords[1])
            output.insert(1.0, result)

def wikipediaSearch(keyword1, keyword2):
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

def lifeGeneratorInterface(keyword1, keyword2)-> str:
    # Create Input file for top 10 of that category  
    with open('lifeGeneratorInput.csv', 'w', newline='') as inputFile:
        writer = csv.writer(inputFile, quoting = csv.QUOTE_MINIMAL, escapechar='\t')
        writer.writerow(['input_type']+['input_item_category']+['input_number+to_generate'])
        writer.writerow([keyword1] + [keyword2]+[10])

    # Input File based call, rename output
    subprocess.run(['python3', 'life_generator/life_generator.py', 'lifeGeneratorInput.csv'])
    subprocess.run(['mv', 'output.csv', 'life_generator_output.csv'])

    # Delete created input file 
    subprocess.run(['rm', 'lifeGeneratorInput.csv'])
    return 'life_generator_output.csv'

def lifeGeneratorGuiParse(filePath):
    # Read life gen output file and return string for GUI
    topTenProducts='Item Name\n-------------------------------------------------------\n'
    with open(filePath, newline='') as csvfile:
        resultsReader = csv.reader(csvfile)
        row=next(resultsReader)
        anyResults = False
        for _ in range(10):
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
    interfaceSelect()