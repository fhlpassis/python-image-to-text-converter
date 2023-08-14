FROM python

WORKDIR /app

COPY ./app .

RUN apt update && apt upgrade -y

RUN apt install python3 python3-pip ipython3 tesseract-ocr tesseract-ocr-por libgl1 poppler-utils -y

RUN pip install pytesseract opencv-python pdf2image flask requests

EXPOSE 3000

CMD ["python", "main.py"]