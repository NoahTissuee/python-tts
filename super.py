import pyttsx3
import PyPDF2
import time

words_per_minute = 150 
save_audio = True
pdf_name = 'sample.pdf'

with open(pdf_name, 'rb') as path:
    pdfReader = PyPDF2.PdfReader(path)
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty('voice', voices[1].id) 
    speak.setProperty('rate', words_per_minute) 
    full_text = ""
    for page in pdfReader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    if save_audio is True:
        speak.save_to_file(full_text, 'output_audio.mp3')
        speak.runAndWait()


                      
