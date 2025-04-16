from library import *
def photo():
    global text1,pritext1
    win.file_name=filedialog.askopenfilename(initialdir="your directory path", title="file uploader",
                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    selected_image =Image.open(win.file_name)
    selected_image = selected_image.resize((400, 700), Image.ANTIALIAS)
    win.image = ImageTk.PhotoImage(selected_image)
    selected_image_label=Label(win,image=win.image).place(x=900,y=10)
    path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd=path
    text1=pytesseract.image_to_string(Image.open(win.file_name))
    pritext1=StringVar()
    pritext1.set(text1)
    show1=Label(win,textvariable=pritext1,bg="#4272a9",fg="#0e0d26",width=50,height=20,font=("Arial",10),highlightbackground='black',highlightthickness=2,bd=10).place(x=180,y=300)
def speak(tool):
    
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(tool)
    engine.runAndWait() 
def camera():
    global text,pritext
    cam=cv2.VideoCapture(0)       
    while True:
            _,image=cam.read()
            cv2.imshow('Camera',image)
            if cv2.waitKey(1)& 0xFF==ord('s'):
                cv2.imwrite('test.jpg',image)
                break
    cam.release()
    cv2.destroyAllWindows()
    path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    im_path='test.jpg'
    pytesseract.tesseract_cmd=path
    text=pytesseract.image_to_string(Image.open(im_path))
        
    pritext=StringVar()
    pritext.set(text)
    show=Label(win,textvariable=pritext,bg="#4272a9",fg="#0e0d26",width=50,height=20,font=("Arial",10),highlightbackground='black',highlightthickness=2).place(x=180,y=300)
win=Tk()
win.title("STR (Scan Text Reader)")
win.iconbitmap('icon.ico')
win.maxsize(width=1377,height=768)
#win.minsize(width=600,height=600)
bg_canvas=Canvas(win,bg="#FFFFFF",height=700,width=700)
filename=PhotoImage(file="strimagelow.png")
bg_label=Label(win, image=filename).place(x=0,y=0,relwidth=1,relheight=1)
bg_canvas.place(x=10,y=10)

lbl = Label(win,text="STR (Scan Text Reader)",font=("Arial","42"),fg="#0d344a",highlightbackground='black',highlightthickness=2).place(x=180,y=16)
frame1=Frame(win,width=200,background='#FFFFFF',highlightbackground='black',highlightthickness=2)
frame1.grid(row=120,column=300,padx=180,pady=115,ipadx=5,ipady=45)
radio1=IntVar()
radio=Radiobutton(win,text=("Photo"),variable=radio1,value=1,highlightbackground='black',highlightthickness=2).place(x=190,y=120)
radio=Radiobutton(win,text=("Camera"),variable=radio1,value=0,highlightbackground='black',highlightthickness=2).place(x=190,y=170)
def checkradio():
    if ((radio1.get())==0):
        camera()
     
    else:
        photo()
def tell():
    if ((radio1.get())==0):
        speak(text)
    else:
        speak(text1) 
tellme=Button(win,text="speak",fg="#0d344a",bg="#4272a9",font=("Arial","12"),width="10",height="2",command=tell,highlightbackground='black',highlightthickness=2).place(x=550,y=150)   
proceed=Button(win,text="Proceed",fg="#0d344a",bg="#4272a9",font=("Arial","12"),width="10",height="2",command=checkradio,highlightbackground='black',highlightthickness=2).place(x=420,y=150)
back=Label(win,text="Output",bg="#4272a9",fg="#0e0d26",width=50,height=20,font=("Arial"),highlightbackground='black',highlightthickness=2).place(x=180,y=300)
win.mainloop()