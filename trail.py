from tkinter import Tk, Label, Button, Entry, Frame, LEFT, RIGHT,Toplevel
from PIL import Image, ImageTk
from tkinter.ttk import *

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Laundry Management System - Login")

        # Admin Login Section
        self.admin_frame = Frame(master)
        self.admin_frame.pack(side=LEFT, padx=20, pady=20)

        # Load and resize admin image using Pillow
        admin_image_path = "admin_logo.jpg"  # Replace with the actual path
        admin_image = Image.open(admin_image_path)
        admin_image = admin_image.resize((150, 150), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        admin_image = ImageTk.PhotoImage(admin_image)

        self.admin_image_label = Label(self.admin_frame, image=admin_image)
        self.admin_image_label.image = admin_image
        self.admin_image_label.pack()

        self.admin_label = Label(self.admin_frame, text="Admin Login")
        self.admin_label.pack()

        self.admin_username_label = Label(self.admin_frame, text="Email:")
        self.admin_username_label.pack()

        self.admin_username_entry = Entry(self.admin_frame)
        self.admin_username_entry.pack()

        self.admin_password_label = Label(self.admin_frame, text="Password:")
        self.admin_password_label.pack()

        self.admin_password_entry = Entry(self.admin_frame, show="*")
        self.admin_password_entry.pack()

        self.admin_login_button = Button(self.admin_frame, text="Login", command=self.admin_login)
        self.admin_login_button.pack(side=LEFT, padx=5,pady = 10)  # Adjust padx as needed

        self.admin_register_button = Button(self.admin_frame, text="Register", command=self.admin_register)
        self.admin_register_button.pack(side=LEFT, padx=5,pady = 10)  # Adjust padx as needed

        # Student Login Section
        self.student_frame = Frame(master)
        self.student_frame.pack(side=RIGHT, padx=20, pady=20)

        # Load and resize student image using Pillow
        student_image_path = "student_logo.png"  # Replace with the actual path
        student_image = Image.open(student_image_path)
        student_image = student_image.resize((150, 150), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        student_image = ImageTk.PhotoImage(student_image)

        self.student_image_label = Label(self.student_frame, image=student_image)
        self.student_image_label.image = student_image
        self.student_image_label.pack()

        self.student_label = Label(self.student_frame, text="Student Login")
        self.student_label.pack()

        self.student_username_label = Label(self.student_frame, text="Email:")
        self.student_username_label.pack()

        self.student_username_entry = Entry(self.student_frame)
        self.student_username_entry.pack()

        self.student_password_label = Label(self.student_frame, text="Password:")
        self.student_password_label.pack()

        self.student_password_entry = Entry(self.student_frame, show="*")
        self.student_password_entry.pack()

        self.student_login_button = Button(self.student_frame, text="Login", command=self.student_login)
        self.student_login_button.pack(side=LEFT, padx=5,pady = 10)  # Adjust padx as needed

        self.student_register_button = Button(self.student_frame, text="Register", command=self.student_register)
        self.student_register_button.pack(side=LEFT, padx=5,pady = 10)  # Adjust padx as needed

    def admin_login(self):
        # Add logic for admin login
        admin_username = self.admin_username_entry.get()
        admin_password = self.admin_password_entry.get()
        # Perform authentication and open the admin window

    def admin_register(self):
        reg = Toplevel(self.master)
        reg.geometry('450x350+400+100')
        admin_reg = AdminReg(reg)
        # Add logic for admin registration
        # Open a registration window for admin

    def student_login(self):
        # Add logic for student login
        student_username = self.student_username_entry.get()
        student_password = self.student_password_entry.get()
        # Perform authentication and open the student window

    def student_register(self):
        pass
        # Add logic for student registration
        # Open a registration window for student
class AdminReg:
    def __init__(self, master):
        self.master = master
        master.title("Laundry Management System - Admin Registration")

        self.registration_frame = Frame(master)
        self.registration_frame.pack(padx=20, pady=20)

        self.registration_label = Label(self.registration_frame, text="Admin Registration")
        self.registration_label.pack()

        self.username_label = Label(self.registration_frame, text="Email:")
        self.username_label.pack()

        self.username_entry = Entry(self.registration_frame)
        self.username_entry.pack()

        self.password_label = Label(self.registration_frame, text="Password:")
        self.password_label.pack()

        self.password_entry = Entry(self.registration_frame, show="*")
        self.password_entry.pack()

        self.register_button = Button(self.registration_frame, text="Register", command=self.register)
        self.register_button.pack(pady=10)

    def register(self):
        # Add logic for admin registration
        admin_username = self.username_entry.get()
        admin_password = self.password_entry.get()


# Example usage
root = Tk()
root.geometry('450x350+400+100')
login_window = LoginWindow(root)
root.resizable(False,False)
root.mainloop()
