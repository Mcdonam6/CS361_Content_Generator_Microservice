CS361_Content_Generator_Microservice
Mike McDonald

############################
Running content-generator.py
############################
1. First, ensure python 3 is installed by running one of the following commands in the terminal of your operating system:
    Windows:    "python --version"
    MacOS:      "python3 --version"
    Linux:      "python3 --version"

    If you do not have Python3 installed, please install the most recent release of Python3

2. Prior to running the program you must ensure the required beautifulSoup4 python package is installed. If you have python 3.4 or later based on the results of step 1, you can install the required package with the pip package manager. Run the command "pip install beautifulsoup4" to do so. If you have another version of Python you can install beautiful soup with an alternative method outlined in the installation docs at the following web address: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup 

3. Once the required non-standard library package is installed, you may run the program with either a .csv file or by using the GUI. For running the program with the GUI, navigate to the directory containing the content-generator.py file and enter the command "python3 content-generator.py" into the terminal. To run the program with a .csv input file, place the input file into the same directory as the content-generator.py file, navigate to that directory in the termainal and run the command "python3 content-generator.py {inputfile.csv}" where the {inputfile.csv} is replaced with the name of your input file name. 

4. Upon running that command, if you have not entered an input file name the GUI will launch and prompt for keywords to perform the content generation service with. Provide the keywords and click the submit button to generate content. The output content will then be displayed in the output field of the GUI as well as be provided in an output .csv file. To run a new content generation request, simply update the keywords and press Submit again. If you have provided an input file with keywords, the program will run automatically without GUI and create or update an output.csv file to the same directory as the program and input files.
