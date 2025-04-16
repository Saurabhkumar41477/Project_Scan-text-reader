from library import *
from mainstream import win
def photo():
    global text1
    win.file_name=filedialog.askopenfilename(initialdir="your directory path", title="file uploader",
                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    selected_image =Image.open(win.file_name)
    selected_image = selected_image.resize((400, 700), Image.ANTIALIAS)
    win.image = ImageTk.PhotoImage(selected_image)
    selected_image_label=Label(win,image=win.image).place(x=900,y=10)
    path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd=path
    text1=pytesseract.image_to_string(Image.open(win.file_name))
    