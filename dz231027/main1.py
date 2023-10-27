import pytesseract
import pyautogui
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\pronina2\\teseract\\tesseract.exe'

old_msg = 0
msg = 0
my_file = open("file.txt", "w")

for i in range(1000):
    # pil_img = pyautogui.screenshot(region=(1314,946, 40, 25)).save('filename.png')
    #exit()
    pil_img = pyautogui.screenshot(region=(1314,946, 40, 25))#.save('filename.png')

    #exit()
    open_cv_image = np.array(pil_img)
    #open_cv_image = open_cv_image[:, :, ::-1].copy() # Convert RGB to BGR
    img = open_cv_image
    text = pytesseract.image_to_string(img)
    try:
        msg = int(text.strip())
    except ValueError:
        pass
    msg = str(msg) + "\n"
    print(msg, end="")
    my_file.write(msg)