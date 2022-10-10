import cv2
import pytesseract


img = cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img)

print(text)
