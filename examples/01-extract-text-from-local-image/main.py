import pytesseract
import cv2

# convert PDF to image then to array ready for opencv
# pages = convert_from_path('verse.jpg')
# img = np.array(pages[0])

# opencv code to view image
# img = cv2.resize(img, None, fx=0.5, fy=0.5)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image = cv2.imread('verse.jpg')

text = pytesseract.image_to_string(image, lang="por")

print(text)
