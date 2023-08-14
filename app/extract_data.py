import pdf2image
import pytesseract
import requests


def convert_pdf_from_url(url):
    doc = requests.get(url, stream=True)
    images = pdf2image.convert_from_bytes(doc.content)
    text = pytesseract.image_to_string(images[0], lang="por")
    return text
