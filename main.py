import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2 as cv
import face_recognition

filepath = None

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CU Attendance Monitoring")
        self.geometry("700x400")

        #create a container to hold all the pages in this app
        self.container = tk.Frame(self)
        self.container.pack()

        #create a dictionary to hold the each page and the information the page contains
        self.frames = {}

        for frame in (Welcome, Admin, TakePicture, showPicture, Register):
            page = frame(self.container,self) #container is the window while self is the controller
            self.frames[frame] = page
            page.grid(row=0, column = 0, sticky = 'nsew')

        self.show_page(Welcome)#show welcome page first

    #function to be able to navigate to all the pages
    def show_page(self,page):
        frame_info = self.frames[page]
        frame_info.tkraise()

    def open_page(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("Take Attendance")
        self.new_window.geometry("700x400")

        self.webcam_label = tk.Label(self.new_window,  text ="webcam", width= 30, height=20, bg="white")
        self.webcam_label.pack(side="left", padx= 50)

        self.frame = tk.Frame(self.new_window)
        self.frame.pack(pady=30)
        self.label = tk.Label(self.frame,text="Welcome...", font=("Arial", 15, 'bold'))
        self.label.pack(pady=20)


    def open_file(self):
        global filepath

        filepath = filedialog.askopenfilename(title="Choose a nice picture")
        
        picture = cv.imread(filepath)
        print(picture.shape, filepath)
        myapp.show_page(showPicture)
        # self.show_page(showPicture)
        # self.display_image(filepath, showPicture)
        

    def display_image(self, window):
        self.path = image_path
        self.image = Image.open(self.path) 
        self.image = self.image.resize((200, 200))
        self.tk_image = ImageTk.PhotoImage(self.image) 
        self.label = tk.Label(window, image=self.tk_image, width=400, height=400)
        self.label.pack()

    def register(self):
        # username = self.entry.get()

        messagebox.showinfo(message="User Registered Successfully", title="Alert!")

        self.show_page(Welcome)


        

class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.label = tk.Label(self, text = "Student Attendance Monitoring System", font = ("Arial", 20, "bold"))
        self.label.pack(pady= 20)

        self.frame = tk.Frame(self)
        self.frame.pack(pady=70)

        self.admin_btn = tk.Button(self.frame, text="Admin", width=25, bg="blue" , fg="white", pady=10, command=lambda:controller.show_page(Admin))
        self.admin_btn.pack(side='left', padx=30)

        self.begin_btn = tk.Button(self.frame, text="Begin Student Attendance", bg="blue", fg="white", width=25, pady=10, command=controller.open_page)
        self.begin_btn.pack(padx=30)


class Admin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.label = tk.Label(self, text="Admin Page", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.frame = tk.Frame(self)
        self.frame.pack(pady=90)

        self.new_btn = tk.Button(self.frame, text="Register New Student", width=30, pady=10, bg="blue", fg="white", command=lambda: controller.show_page(TakePicture))
        self.new_btn.pack(side="left", padx=30)

        self.download_btn = tk.Button(self.frame, text="Download Student Attendance", width=30,pady=10, bg="blue", fg="white")
        self.download_btn.pack(padx=30)

        self.back_btn = tk.Button(self, text="<- Go Back", width=10, bg="black", fg="white", command=lambda: controller.show_page(Welcome))
        self.back_btn.place(x=0, y=290)



class TakePicture(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.webcam_label = tk.Label(self, text ="webcam", width= 30, height=20, bg="white")
        self.webcam_label.pack(side='left', pady=30)

        self.frame = tk.Frame(self)
        self.frame.pack(padx=20)

        self.label = tk.Label(self.frame, text="Smile!", font=("Arial", 20, "bold"))
        self.label.pack(pady=60)
        self.take_pic = tk.Button(self.frame, text="Take Picture", bg="blue", fg="white", width=20, pady=10, command=lambda: controller.show_page(Register))
        self.take_pic.pack()
        self.upload_btn = tk.Button(self.frame, text="^ Upload Picture", bg="green", fg="white", width=20, pady=10, command=controller.open_file)
        self.upload_btn.pack(pady=10)

        self.back_btn = tk.Button(self, text="<- Go Back", width=10, bg="black", fg="white", command=lambda: controller.show_page(Admin))
        self.back_btn.place(x=0, y=340)

class showPicture(tk.Frame):
    def __init__(self, parent, controller):
        global filepath

        super().__init__(parent)

        self.button = tk.Button(self, text="Register", bg="blue", fg="white", width=20, pady=10, command=lambda: controller.show_page(Register))
        self.button.pack()

        self.path = filepath
        print(filepath)
        self.image = Image.open(self.path) 
        self.image = self.image.resize((200, 200))
        self.tk_image = ImageTk.PhotoImage(self.image) 
        self.label = tk.Label(self, image=self.tk_image, width=400, height=400)
        self.label.pack()
        
        
        

class Register(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.webcam_label = tk.Label(self , text ="webcam", width= 30, height=20, bg="white")
        self.webcam_label.pack(side="left")

        self.frame = tk.Frame(self)
        self.frame.pack(pady=70)
        self.entry_label = tk.Label(self.frame, text="Enter the student's full name", font=("Arial", 10))
        self.entry_label.pack(pady=10)
        self.entry = tk.Entry(self.frame, width=20, font=("Arial",15))
        self.entry.pack()
        self.regist = tk.Button(self.frame, text="Register", bg="blue", fg="white", width=20, pady=10, command=controller.register)
        self.regist.pack(pady=20)
        self.retry = tk.Button(self.frame, text="Try Again", bg="red", fg="white", width=20, pady=10, command=lambda: controller.show_page(TakePicture))
        self.retry.pack()

myapp = app()
myapp.mainloop()