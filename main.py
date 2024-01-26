from tkinter import Tk, Label, Button, Entry, Frame, LEFT, RIGHT,Toplevel,messagebox,Checkbutton,Radiobutton,IntVar, Spinbox, StringVar
from PIL import Image, ImageTk
from tkinter.ttk import *
import mysql.connector

#database connection
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Praneetha@1'    
)
cursor = conn.cursor()
cursor.execute('create database if not exists LMS')
cursor.execute('use LMS')


class MainPageLogin:
    def __init__(self, master):
        self.master = master
        master.title("Laundry Management System - Login")

        # Admin Login Section
        self.admin_frame = Frame(master)
        self.admin_frame.pack(side=LEFT, padx=20, pady=20)

        self.admin_label = Label(self.admin_frame, text="Admin Login")
        self.admin_label.pack()

        # Load and resize admin image using Pillow
        admin_image_path = "admin_logo.jpg"  # Replace with the actual path
        admin_image = Image.open(admin_image_path)
        admin_image = admin_image.resize((140, 140), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        admin_image = ImageTk.PhotoImage(admin_image)

        self.admin_image_label = Label(self.admin_frame, image=admin_image)
        self.admin_image_label.image = admin_image
        self.admin_image_label.pack()


        self.admin_email_label = Label(self.admin_frame, text="Email:")
        self.admin_email_label.pack()

        self.admin_email_entry = Entry(self.admin_frame)
        self.admin_email_entry.pack()

        self.admin_password_label = Label(self.admin_frame, text="Password:")
        self.admin_password_label.pack()

        self.admin_password_entry = Entry(self.admin_frame, show="*")
        self.admin_password_entry.pack()

        self.admin_login_button = Button(self.admin_frame, text="Login", command=self.admin_login)
        self.admin_login_button.pack(side=LEFT, padx=5,pady = 10)  

        self.admin_register_button = Button(self.admin_frame, text="Register", command=self.admin_register)
        self.admin_register_button.pack(side=LEFT, padx=5,pady = 10) 

        # Student Login Section
        self.student_frame = Frame(master)
        self.student_frame.pack(side=RIGHT, padx=20, pady=20)

        self.student_label = Label(self.student_frame, text="Student Login")
        self.student_label.pack()

        # Load and resize student image using Pillow
        student_image_path = "student_logo.png"  
        student_image = Image.open(student_image_path)
        student_image = student_image.resize((140, 140), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        student_image = ImageTk.PhotoImage(student_image)

        self.student_image_label = Label(self.student_frame, image=student_image)
        self.student_image_label.image = student_image
        self.student_image_label.pack()


        self.student_email_label = Label(self.student_frame, text="Email:")
        self.student_email_label.pack()

        self.student_email_entry = Entry(self.student_frame)
        self.student_email_entry.pack()

        self.student_password_label = Label(self.student_frame, text="Password:")
        self.student_password_label.pack()

        self.student_password_entry = Entry(self.student_frame, show="*")
        self.student_password_entry.pack()

        self.student_login_button = Button(self.student_frame, text="Login", command=self.student_login)
        self.student_login_button.pack(side=LEFT, padx=5,pady = 10)  

        self.student_register_button = Button(self.student_frame, text="Register", command=self.student_register)
        self.student_register_button.pack(side=LEFT, padx=5,pady = 10)  

    def admin_login(self):
        admin_email = self.admin_email_entry.get()
        admin_password = self.admin_password_entry.get()
        # Performing authentication
        cursor = conn.cursor()
        query = "SELECT * FROM admin_reg WHERE email = %s AND password = %s"
        cursor.execute(query, (admin_email, admin_password))

        result = cursor.fetchone()
        cursor.close()

        if result:
            messagebox.showinfo('Login Successful', 'Admin login successful')
        else:
            messagebox.showerror('Login Failed', 'Invalid credentials')


    def admin_register(self):
        ad_reg = Toplevel(self.master)
        ad_reg.geometry('450x350+400+100')
        admin_reg = AdminReg(ad_reg)
        

    def student_login(self):
        student_email = self.student_email_entry.get()
        student_password = self.student_password_entry.get()
        cursor = conn.cursor()
        query = "SELECT * FROM student_reg WHERE email = %s AND password = %s"
        cursor.execute(query, (student_email, student_password))

        result = cursor.fetchone()
        cursor.close()
        if result:
            dash = Toplevel(self.master)
            dash.geometry('450x350+400+100')
            dashb = StudentDashboard(dash)
        else:
            messagebox.showerror('Login Failed', 'Invalid credentials')


    def student_register(self):
        st_reg = Toplevel(self.master)
        st_reg.geometry('450x350+400+100')
        student_reg = StudentReg(st_reg)

#class for admin registration page
class AdminReg:
    def __init__(self, master):
        self.master = master
        master.title("Laundry Management System - Admin Registration")

        self.registration_frame = Frame(master)
        self.registration_frame.pack(padx=20, pady=20)

        self.registration_label = Label(self.registration_frame, text="Admin Registration")
        self.registration_label.grid(row=0, column=0, columnspan=2,pady = 10)

        self.email_label = Label(self.registration_frame, text="Email:")
        self.email_label.grid(row=1, column=0,pady=5)

        self.email_entry = Entry(self.registration_frame)
        self.email_entry.grid(row=1, column=1,pady =5)

        self.username_label = Label(self.registration_frame, text="Username:")
        self.username_label.grid(row=2, column=0,pady=5)

        self.username_entry = Entry(self.registration_frame)
        self.username_entry.grid(row=2, column=1,pady =5)

        self.password_label = Label(self.registration_frame, text="Password:")
        self.password_label.grid(row=3, column=0,pady =5)

        self.password_entry = Entry(self.registration_frame, show="*")
        self.password_entry.grid(row=3, column=1,pady =5)

        self.hostel_label = Label(self.registration_frame, text="Hostel:")
        self.hostel_label.grid(row=4, column=0,pady=5)

        self.hostel_entry = Entry(self.registration_frame)
        self.hostel_entry.grid(row=4, column=1,pady =5)

        self.mobile_label = Label(self.registration_frame, text="Mobile Number:")
        self.mobile_label.grid(row=5, column=0,pady =5)

        self.mobile_entry = Entry(self.registration_frame)
        self.mobile_entry.grid(row=5, column=1,pady =5)
    
        self.register_button = Button(self.registration_frame, text="Register", command=self.save_admin_data)
        self.register_button.grid(row=6, column=0, columnspan=2, pady=10)
    def save_admin_data(self):
        #capturing the data entered by admin to send to DB
        admin_email = self.email_entry.get()
        admin_password = self.password_entry.get()
        admin_mobno = self.mobile_entry.get()
        admin_username = self.username_entry.get()
        admin_hostel = self.hostel_entry.get()
        self.query = f"insert into admin_reg values('{admin_username}','{admin_email}','{admin_password}','{admin_mobno}','{admin_hostel}')"
        cursor.execute(self.query)
        conn.commit()
        messagebox.showinfo('SAVED','Registration Successful')
        self.master.destroy()

#class for student registration page
class StudentReg:
    def __init__(self, master):
        self.master = master
        master.title("Laundry Management System - Student Registration")

        self.registration_frame = Frame(master)
        self.registration_frame.pack(padx=20, pady=20)

        self.registration_label = Label(self.registration_frame, text="Student Registration")
        self.registration_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.email_label = Label(self.registration_frame, text="Email:")
        self.email_label.grid(row=1, column=0, pady=5)

        self.email_entry = Entry(self.registration_frame)
        self.email_entry.grid(row=1, column=1, pady=5)

        self.username_label = Label(self.registration_frame, text="Username:")
        self.username_label.grid(row=2, column=0,pady=5)

        self.username_entry = Entry(self.registration_frame)
        self.username_entry.grid(row=2, column=1,pady =5)

        self.password_label = Label(self.registration_frame, text="Password:")
        self.password_label.grid(row=3, column=0, pady=5)

        self.password_entry = Entry(self.registration_frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=5)

        self.mobile_label = Label(self.registration_frame, text="Mobile Number:")
        self.mobile_label.grid(row=4, column=0, pady=5)

        self.mobile_entry = Entry(self.registration_frame)
        self.mobile_entry.grid(row=4, column=1, pady=5)

        self.hostel_label = Label(self.registration_frame, text="Hostel Name:")
        self.hostel_label.grid(row=5, column=0, pady=5)

        self.hostel_entry = Entry(self.registration_frame)
        self.hostel_entry.grid(row=5, column=1, pady=5)

        self.room_label = Label(self.registration_frame, text="Room Number:")
        self.room_label.grid(row=6, column=0, pady=5)

        self.room_entry = Entry(self.registration_frame)
        self.room_entry.grid(row=6, column=1, pady=5)

        self.register_button = Button(self.registration_frame, text="Register", command=self.save_student_data)
        self.register_button.grid(row=7, column=0, columnspan=2, pady=10)

    def save_student_data(self):
        #capturing the data entered by student to send to DB
        student_email = self.email_entry.get()
        student_password = self.password_entry.get()
        student_mobile = self.mobile_entry.get()
        student_hostel = self.hostel_entry.get()
        student_room = self.room_entry.get()
        student_username = self.username_entry.get()
        self.query = f"insert into student_reg values('{student_username}','{student_email}','{student_password}','{student_mobile}','{student_hostel}','{student_room}')"
        cursor.execute(self.query)
        conn.commit()
        messagebox.showinfo('SAVED','Registration Successful')

        self.master.destroy()


class StudentDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Dashboard")
        
        # self.student_username = student_username

        # Creating buttons
        self.place_order_button = Button(self.master, text="Place Order", command=self.place_order)
        self.place_order_button.pack(pady=10)

        self.support_button = Button(self.master, text="Support", command=self.support)
        self.support_button.pack(pady=10)

    def place_order(self):
        pla = Toplevel(self.master)
        pla.geometry('450x350+400+100')
        place = PlaceOrder(pla)
        

    def support(self):
        pass


class PlaceOrder:
    def __init__(self, master):
        self.master = master
        self.master.title("Place Order - Laundry Management System")
        #self.username = username

        self.order_frame = Frame(master)
        self.order_frame.pack(padx=20, pady=20)

        # Number of Clothes
        self.clothes_label = Label(self.order_frame, text="Number of Clothes:")
        self.clothes_label.grid(row=0, column=0, pady=5)

        self.clothes_entry = Entry(self.order_frame)
        self.clothes_entry.grid(row=0, column=1, pady=5)

        # Services Required
        self.services_label = Label(self.order_frame, text="Services Required:")
        self.services_label.grid(row=1, column=0, pady=5)

        self.dry_clean_var = IntVar()
        self.wash_fold_var = IntVar()
        self.iron_required_var = IntVar()

        self.dry_clean_cb = Checkbutton(self.order_frame, text="Dry Clean", variable=self.dry_clean_var)
        self.dry_clean_cb.grid(row=1, column=1, pady=5)

        self.wash_fold_cb = Checkbutton(self.order_frame, text="Wash and Fold", variable=self.wash_fold_var)
        self.wash_fold_cb.grid(row=2, column=1, pady=5)

        self.iron_required_cb = Checkbutton(self.order_frame, text="Iron Required", variable=self.iron_required_var)
        self.iron_required_cb.grid(row=3, column=1, pady=5)

        # Preferred Time
        self.time_label = Label(self.order_frame, text="Preferred Time:")
        self.time_label.grid(row=4, column=0, pady=5)

        self.time_entry = Entry(self.order_frame)
        self.time_entry.grid(row=4, column=1, pady=5)

        # Mode of Payment
        self.payment_label = Label(self.order_frame, text="Mode of Payment:")
        self.payment_label.grid(row=5, column=0, pady=5)

        self.payment_var = StringVar()
        self.cod_rb = Radiobutton(self.order_frame, text="COD", variable=self.payment_var, value="COD")
        self.cod_rb.grid(row=5, column=1, pady=5)

        # Place Order Button
        self.place_order_button = Button(self.order_frame, text="Place Order", command=self.place_order)
        self.place_order_button.grid(row=6, column=1, columnspan=2, pady=10)

    def place_order(self):
        # Get values from widgets and process the order
        num_of_clothes = self.clothes_entry.get()
        services_required = []
        if self.dry_clean_var.get():
            services_required.append("Dry Clean")
        if self.wash_fold_var.get():
            services_required.append("Wash and Fold")
        if self.iron_required_var.get():
            services_required.append("Iron Required")
        preffered_time = self.time_entry.get()
        mode_of_payment = self.payment_var.get()


#usage
root = Tk()
root.geometry('450x350+400+100')
login_window = MainPageLogin(root)
#disabling the maximize/resize option
root.resizable(False,False)
root.mainloop()
