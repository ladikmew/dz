import pytesseract
import pyautogui
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

old_msg = 0
msg = 0

for i in range(1000):
    pil_img = pyautogui.screenshot(region=(1167,919, 30, 20)).save('filename.png')
    #exit()
    pil_img = pyautogui.screenshot(region=(1167,919, 30, 20))#.save('filename.png')

    #exit()
    open_cv_image = np.array(pil_img)
    open_cv_image = open_cv_image[:, :, ::-1].copy() # Convert RGB to BGR
    img = open_cv_image
    text = pytesseract.image_to_string(img)
    try:
        msg = int(text.strip())
    except ValueError:
        pass
    msg = str(msg) + "\n"
    print(msg, end="")
    with open("file.txt", "w") as f:
        f.write(msg)