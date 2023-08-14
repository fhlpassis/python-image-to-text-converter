# Image to text converter and extractor

## Installation

### Install python, pip and libs

sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip ipython3 tesseract-ocr tesseract-ocr-por libgl1 poppler-utils

pip install pytesseract opencv-python pdf2image flask requests

## Docker

### Container

docker build -t image-to-text-converter .

docker run --name pyser --rm -p 3000:3000 -d image-to-text-converter

### Compose

docker compose -f docker-compose.yaml up -d

## Help Links

[Base tutorial - Hashtag Programação](https://youtu.be/Wx3SyNwZtsA)

[Convert pdf to image](https://stackoverflow.com/questions/61832964/how-to-convert-pdf-into-image-readable-by-opencv-python)

[Convert pdf to image from url](https://stackoverflow.com/questions/51481200/convert-pdf-to-image-using-pdf-url-pdf2image)

[Install tesseract](https://linuxhint.com/install-tesseract-ocr-linux)

[Install tesseract tips](https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)
