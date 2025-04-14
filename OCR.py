from ocr_tamil.ocr import OCR
import langid
from googletrans import Translator

# Initialize OCR and translator once
ocr = OCR(detect=True)
translator = Translator()

def ocr_core(image_path):
    texts = ocr.predict(image_path)
    extracted_text = " ".join(texts[0])

    tamil_text = []
    for word in extracted_text.split():
        lang, _ = langid.classify(word)
        if lang == 'ta':
            tamil_text.append(word)

    return " ".join(tamil_text)

def translatee(tamil_text):
    translated = translator.translate(tamil_text, src='ta', dest='hi')
    return translated.text
