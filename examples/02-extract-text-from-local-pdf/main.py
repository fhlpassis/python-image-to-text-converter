import numpy as np
import pdf2image
import cv2  # OpenCV library for python
import pytesseract

def convert_pdf_to_image(document, dpi):
    images = []
    images.extend(
                    list(
                        map(
                            lambda image: cv2.cvtColor(
                                np.asarray(image), code=cv2.COLOR_RGB2BGR
                            ),
                            pdf2image.convert_from_path(document, dpi=dpi),
                        )
                    )
                )
    return images

images = convert_pdf_to_image('path-to-pdf.pdf', 300)

# Number of pages in the pdf
print(len(images))

text = pytesseract.image_to_string(images[0], lang="por")

print(text)