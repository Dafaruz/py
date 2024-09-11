import PyPDF2
import pyttsx3


# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    # Open the PDF file in binary mode
    with open(pdf_file, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize text variable
        text = ""

        # Loop through all the pages and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


# Function to convert text to speech
def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Start speaking the extracted text
    engine.say(text)
    engine.runAndWait()


# Main function
def pdf_to_speech(pdf_file):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_file)

    # If text is not empty, convert it to speech
    if text:
        print("Converting to speech...")
        text_to_speech(text)
    else:
        print("No text found in the PDF.")


# Input the PDF file path
pdf_file = input("Enter the path to your PDF file: ")

# Convert the PDF to speech
pdf_to_speech(pdf_file)
