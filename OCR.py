try:  
    from PIL import Image
    from googletrans import Translator
except ImportError:  
    import Image
import pytesseract


def ocr_core(filename):  
    """
    This function will handle the core OCR processing of images.
    """
    
    text= pytesseract.image_to_string(Image.open(filename), lang='eng')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

def translatee(filename):
    translator = Translator()

   
    text1= pytesseract.image_to_string(Image.open(filename), lang='eng')
    translation_text=translator.translate( text1 , dest='tamil')
    return translation_text

