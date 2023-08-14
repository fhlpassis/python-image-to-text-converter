import requests, pdf2image, pytesseract
pdf = requests.get('https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', stream=True)
images = pdf2image.convert_from_bytes(pdf.content)

text = pytesseract.image_to_string(images[0], lang="por")

print(text)