#Install the 'PyPDF2', 'textract' and 'nltk' libraries using following commands inside the terminal
pip install PyPDF2
pip install textract
pip install nltk

#Import all the libraries
import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Enter the name of the file here
file_name = "Experience.pdf"

#Open allows to read the file
pdf_file_obj = open(file_name, 'rb')

#Now the 'pdf_reader' variable is a readable object that will be parsed
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

#Discerning the no. of pages will allow us to parse throug all the pages
num_pages = pdf_reader.numPages
count = 0
text = ""

#The while loop will read each page
while count<num_pages:
    page_obj = pdf_reader.getPage(count)
    count +=1
    text += page_obj.extractText()
    
#If statement is to check if the above library returned words, as PyPDF2 can't read scanned files
if text != "":
    text = text
   
#If the above returns as false, we run the OCR library 'textract' to convert scanned/image based PDF files into text

else:
    text = textract.process(C:/Users/Chinmaya/Downloads/Experience.pdf, method='textract', language='eng')

#Now we got a text variable which contains all the text derived from the PDF file
#Type print(text)to see what it contains.
#It might contains a lot of spaces, possibly junk such as '\n,' etc

#Now clean the text variable and return it as a list of keywords
#The word_tokenize() function will break the text phrases into individual words
tokens = word_tokenize(text)

#Creating a new list that contains punctuation we needed to clean
punctuations = ['(',')',';',':','[',']',',']

#initializing the stopwords variable, which is a list of words, that don't hold much values as keywords
stop_words = stopwords.words('english')

#creating a list comprehension that only returns a list of words that are not in 'stop_words' and not in 'punctuations'
#we get word for word in tokens if not word in stop_words and not in punctuations
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]