"""
This file ensures that the content in PDF file gets parsed faithfully
"""

import PyPDF2
import string

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
    except Exception as e:
      print(f"An error occurred during PDF processing: {e}")
      return None
    return text

def preprocess_text(text):
    if text is None:
      return ""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join(text.split()) # Removes extra whitespaces
    return text

pdf_file_path = "SampleLGBTTransformerCode/PDFParser/LGBTQmicroaggressions-webinar-transcript.pdf"  # Replace with your PDF path
extracted_text = extract_text_from_pdf(pdf_file_path)
    
if extracted_text:
    print("Text extracted successfully!")
    preprocessed_text = preprocess_text(extracted_text)
    print("Text preprocessed!")
    file = open('SampleLGBTTransformerCode/PDFParser/LGBTQmicroaggressions-webinar-transcript.txt', 'w')
    file.write(preprocessed_text)
    file.close()
else:
   print("Text extraction failed") 