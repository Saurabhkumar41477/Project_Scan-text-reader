from library import *
def camera():
    global text
    cam=cv2.VideoCapture(0)
    while True:
            _,image=cam.read()
            cv2.imshow('detection test',image)
            if cv2.waitKey(1)& 0xFF==ord('s'):
                cv2.imwrite('test.jpg',image)
                break
    cam.release()
    cv2.destroyAllWindows()
    path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    im_path='test.jpg'
    pytesseract.tesseract_cmd=path
    text=pytesseract.image_to_string(Image.open(im_path))
   