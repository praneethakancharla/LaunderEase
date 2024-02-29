from tkinter import Tk, Label, Button, Entry, Frame,Toplevel,messagebox,Checkbutton,Radiobutton,IntVar,RAISED, StringVar,Text,X,W
from PIL import Image, ImageTk
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
        self.master.title("Laundry Management System - Login")
        self.master.configure(bg="lightblue")

       
        # Admin Login Section
        self.admin_frame = Frame(master, width=300, height=300, bg="lightblue")
        self.admin_frame.grid(row=0, column=0, padx=20, pady=20)

        self.admin_label = Label(self.admin_frame, text="Admin Login" , font=("Times New Roman", 16,"bold"),bg ="lightblue")
        self.admin_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        admin_image_path = "admin_logo.jpg"
        admin_image = Image.open(admin_image_path)
        admin_image = admin_image.resize((140, 140),Image.BICUBIC)
        admin_image = ImageTk.PhotoImage(admin_image)

        self.admin_image_label = Label(self.admin_frame, image=admin_image)
        self.admin_image_label.image = admin_image
        self.admin_image_label.grid(row=1, column=0, columnspan=2)

        self.admin_email_label = Label(self.admin_frame, text="Email:", font=("Bookman Old Style ", 12),bg = "lightblue")
        self.admin_email_label.grid(row=2, column=0, pady=(10, 0))

        self.admin_email_entry = Entry(self.admin_frame)
        self.admin_email_entry.grid(row=2, column=1, pady=(10, 0))

        self.admin_password_label = Label(self.admin_frame, text="Password:", font=("Bookman Old Style ", 12),bg ="lightblue")
        self.admin_password_label.grid(row=3, column=0, pady=(10, 0))

        self.admin_password_entry = Entry(self.admin_frame, show="*")
        self.admin_password_entry.grid(row=3, column=1, pady=(10, 0))

        self.admin_login_button = Button(self.admin_frame, text="  Login ", command=self.admin_login,)
        self.admin_login_button.grid(row=4, column=0,padx=(0,5),pady=(20,0))

        self.admin_register_button = Button(self.admin_frame, text="Register", command=self.admin_register)
        self.admin_register_button.grid(row=4, column=1,padx=(5,0),pady=(20,0))

        # Student Login Section
        self.student_frame = Frame(master, width=300, height=300, bg="lightblue")
        self.student_frame.grid(row=0, column=1, padx=70, pady=20)

        self.student_label = Label(self.student_frame, text="Student Login", font=("Times New Roman", 16,"bold"),bg = "lightblue")
        self.student_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        student_image_path = "student_logo.png"  
        student_image = Image.open(student_image_path)
        student_image = student_image.resize((140, 140), Image.BICUBIC)
        student_image = ImageTk.PhotoImage(student_image)

        self.student_image_label = Label(self.student_frame, image=student_image)
        self.student_image_label.image = student_image
        self.student_image_label.grid(row=1, column=0, columnspan=2)

        self.student_email_label = Label(self.student_frame, text="Email:", bg="lightblue", font=("Bookman Old Style ", 12))
        self.student_email_label.grid(row=2, column=0, pady=(10, 0))

        self.student_email_entry = Entry(self.student_frame)
        self.student_email_entry.grid(row=2, column=1, pady=(10, 0))

        self.student_password_label = Label(self.student_frame, text="Password:", bg="lightblue", font=("Bookman Old Style ", 12))
        self.student_password_label.grid(row=3, column=0, pady=(10, 0))

        self.student_password_entry = Entry(self.student_frame, show="*")
        self.student_password_entry.grid(row=3, column=1, pady=(10, 0))

        self.student_login_button = Button(self.student_frame, text="  Login ", command=self.student_login)
        self.student_login_button.grid(row=4, column=0,padx=(0,5),pady=(20,0))

        self.student_register_button = Button(self.student_frame, text="Register", command=self.student_register)
        self.student_register_button.grid(row=4, column=1,padx=(5,0),pady=(20,0))
        
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
            admin_username = result[0] 
            a_dash = Toplevel(self.master)
            a_dash.geometry('550x350+550+150')
            dasha = AdminDashboard(a_dash,admin_username)
            
        else:
            messagebox.showerror('Login Failed', 'Invalid credentials')


    def admin_register(self):
        ad_reg = Toplevel(self.master)
        ad_reg.geometry('550x350+550+150')
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
            student_username = result[0]
            dash = Toplevel(self.master)
            dash.geometry('550x350+550+150')
            dashb = StudentDashboard(dash,student_username)
        else:
            messagebox.showerror('Login Failed', 'Invalid credentials')


    def student_register(self):
        st_reg = Toplevel(self.master)
        st_reg.geometry('550x350+550+150')
        student_reg = StudentReg(st_reg)

#class for admin registration page
class AdminReg:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False,False)
        self.master.title("Laundry Management System - Admin Registration")
        self.master.configure(bg="lightblue")


        self.registration_frame = Frame(master,bg="lightblue")
        self.registration_frame.pack(padx=20, pady=20)

        self.registration_label = Label(self.registration_frame, text="Admin Registration",font=("Times New Roman", 16,"bold"),bg ="lightblue")
        self.registration_label.grid(row=0, column=0, columnspan=2,pady = 10)

        self.email_label = Label(self.registration_frame, text="Email:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.email_label.grid(row=1, column=0,pady=5)

        self.email_entry = Entry(self.registration_frame)
        self.email_entry.grid(row=1, column=1,pady =5)

        self.username_label = Label(self.registration_frame, text="Username:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.username_label.grid(row=2, column=0,pady=5)

        self.username_entry = Entry(self.registration_frame)
        self.username_entry.grid(row=2, column=1,pady =5)

        self.password_label = Label(self.registration_frame, text="Password:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.password_label.grid(row=3, column=0,pady =5)

        self.password_entry = Entry(self.registration_frame, show="*")
        self.password_entry.grid(row=3, column=1,pady =5)

        self.hostel_label = Label(self.registration_frame, text="Hostel:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.hostel_label.grid(row=4, column=0,pady=5)

        self.hostel_entry = Entry(self.registration_frame)
        self.hostel_entry.grid(row=4, column=1,pady =5)

        self.mobile_label = Label(self.registration_frame, text="Mobile Number:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.mobile_label.grid(row=5, column=0,pady =5)

        self.mobile_entry = Entry(self.registration_frame)
        self.mobile_entry.grid(row=5, column=1,pady =5)
    
        self.register_button = Button(self.registration_frame, text="Register", command=self.save_admin_data)
        self.register_button.grid(row=6, column=0, columnspan=2, pady=20)
    def save_admin_data(self):
        #capturing the data to send into database
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
        master.resizable(False,False)
        master.title("Laundry Management System - Student Registration")
        master.configure(bg="lightblue")

        self.registration_frame = Frame(master,background="lightblue")
        self.registration_frame.pack(padx=20, pady=20)
        

        self.registration_label = Label(self.registration_frame, text="Student Registration",font=("Times New Roman", 16,"bold"),bg ="lightblue")
        self.registration_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.email_label = Label(self.registration_frame, text="Email:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.email_label.grid(row=1, column=0, pady=5)

        self.email_entry = Entry(self.registration_frame)
        self.email_entry.grid(row=1, column=1, pady=5)

        self.username_label = Label(self.registration_frame, text="Username:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.username_label.grid(row=2, column=0,pady=5)

        self.username_entry = Entry(self.registration_frame)
        self.username_entry.grid(row=2, column=1,pady =5)

        self.password_label = Label(self.registration_frame, text="Password:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.password_label.grid(row=3, column=0, pady=5)

        self.password_entry = Entry(self.registration_frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=5)

        self.mobile_label = Label(self.registration_frame, text="Mobile Number:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.mobile_label.grid(row=4, column=0, pady=5)

        self.mobile_entry = Entry(self.registration_frame)
        self.mobile_entry.grid(row=4, column=1, pady=5)

        self.hostel_label = Label(self.registration_frame, text="Hostel Name:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.hostel_label.grid(row=5, column=0, pady=5)

        self.hostel_entry = Entry(self.registration_frame)
        self.hostel_entry.grid(row=5, column=1, pady=5)

        self.room_label = Label(self.registration_frame, text="Room Number:",bg="lightblue", font=("Bookman Old Style ", 12))
        self.room_label.grid(row=6, column=0, pady=5)

        self.room_entry = Entry(self.registration_frame)
        self.room_entry.grid(row=6, column=1, pady=5)

        self.register_button = Button(self.registration_frame, text="Register", command=self.save_student_data)
        self.register_button.grid(row=7, column=0, columnspan=2, pady=20)

    def save_student_data(self):
        #capturing the data to send into database
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

#student dash board page
class StudentDashboard:
    def __init__(self, master, student_username):
        self.master = master
        master.resizable(False,False)
        self.master.title("Student Dashboard")
        self.student_username = student_username
        self.cursor = cursor
        self.master.configure(bg="lightblue")
        self.master.geometry('550x350+550+150')

        self.main_frame = Frame(self.master, bg="lightblue")
        self.main_frame.pack()

        self.welcome_frame = Frame(self.main_frame, bg="lightblue")
        self.welcome_frame.pack(side="top", pady=20)

        self.welcome_label = Label(self.welcome_frame, text="Hi! Welcome, ", font=("Times New Roman", 16), bg="lightblue")
        self.welcome_label.pack(side="left")

        self.username_label = Label(self.welcome_frame, text=self.student_username, font=("Times New Roman", 20, "bold"), bg="lightblue")
        self.username_label.pack(side="left")

        self.button_frame = Frame(self.main_frame, bg="lightblue")
        self.button_frame.pack(side="top", pady=20)

        self.place_order_button = Button(self.button_frame, text="Place Order", command=self.place_order)
        self.place_order_button.pack(side="left", padx=(0, 10))  # Add right padding to the left button

        self.space_frame = Frame(self.button_frame, width=20, bg="lightblue")
        self.space_frame.pack(side="left")

        self.support_button = Button(self.button_frame, text="Support", command=self.support)
        self.support_button.pack(side="left", padx=(10, 0))

        self.space_frame = Frame(self.button_frame, width=20, bg="lightblue")
        self.space_frame.pack(side="left")

        self.support_button = Button(self.button_frame, text="Instructions", command=self.instructions)
        self.support_button.pack(side="left", padx=(10, 0))

        

    def place_order(self):
        pla = Toplevel(self.master)
        pla.geometry('550x350+550+150')
        place = PlaceOrder(pla,self.student_username)
        

    def support(self):
        query = "SELECT username, mobilenumber, hostel FROM admin_reg"
        self.cursor.execute(query)
        admins = self.cursor.fetchall()

        support_window = Toplevel(self.master)
        support_window.geometry('550x350+550+150')
        support_window.title("Admin Contact Details")
        support_window.resizable(False,False)
        support_window.configure(bg="lightblue")

        # Displaying admin contact details
        for admin in admins:
                admin_frame = Frame(support_window, relief=RAISED, borderwidth= 2)
                admin_frame.pack(pady=10, fill=X, padx=10) 

                admin_name_label = Label(admin_frame, text=f"Admin Name: {admin[0]}", font=("Bookman Old Style", 12))
                admin_name_label.pack(anchor=W)

                admin_mobile_label = Label(admin_frame, text=f"Mobile Number: {admin[1]}", font=("Bookman Old Style", 12))
                admin_mobile_label.pack(anchor=W)

                admin_hostel_label = Label(admin_frame, text=f"Hostel: {admin[2]}", font=("Bookman Old Style", 12))
                admin_hostel_label.pack(anchor=W)

    def instructions(self):
        instructions_text = """
        INSTRUCTIONS:

        1. Operating Hours: Monday to Saturday, 9:00 AM to 7:00 PM.
        2. Closed on Sundays and Public Holidays.
        3. For any queries or support, contact the admin using 
        the 'Support' button.
        """

        instructions_window = Toplevel(self.master)
        instructions_window.geometry('550x350+550+150')
        instructions_window.resizable(False,False)
        instructions_window.title("Instructions")
        instructions_window.configure(bg="lightblue")

        instructions_label = Label(instructions_window, text=instructions_text, justify="left", bg="lightblue", fg="black", font=("Bookman Old Style", 12))
        instructions_label.pack(pady=10)
        

class PlaceOrder:
    def __init__(self, master, username):
        self.master = master
        master.resizable(False,False)
        self.master.title("Place Order - Laundry Management System")
        self.student_username = username
        master.configure(bg="lightblue")

        self.order_frame = Frame(master, bg="lightblue")
        self.order_frame.pack(padx=20, pady=20)
        self.master.geometry('550x350+550+150')

        
        self.clothes_label = Label(self.order_frame, text="Number of Clothes:", font=("Bookman Old Style", 11), bg="lightblue")
        self.clothes_label.grid(row=0, column=0, pady=5)

        self.clothes_entry = Entry(self.order_frame)
        self.clothes_entry.grid(row=0, column=1, pady=5)

        
        self.services_label = Label(self.order_frame, text="Services Required:", font=("Bookman Old Style", 11), bg="lightblue")
        self.services_label.grid(row=1, column=0, pady=5)

        self.dry_clean_var = IntVar()
        self.wash_fold_var = IntVar()
        self.iron_required_var = IntVar()

        self.dry_clean_cb = Checkbutton(self.order_frame, text="Dry Clean", variable=self.dry_clean_var, bg="lightblue",font=("Bookman Old Style", 9))
        self.dry_clean_cb.grid(row=1, column=1, pady=5)

        self.wash_fold_cb = Checkbutton(self.order_frame, text="Wash and Fold", variable=self.wash_fold_var, bg="lightblue",font=("Bookman Old Style",9))
        self.wash_fold_cb.grid(row=2, column=1, pady=5)

        self.iron_required_cb = Checkbutton(self.order_frame, text="Iron Required", variable=self.iron_required_var, bg="lightblue",font=("Bookman Old Style", 9))
        self.iron_required_cb.grid(row=3, column=1, pady=5)

        self.time_label = Label(self.order_frame, text="Preferred Time:", font=("Bookman Old Style", 11), bg="lightblue")
        self.time_label.grid(row=4, column=0, pady=5)

        self.time_entry = Entry(self.order_frame)
        self.time_entry.grid(row=4, column=1, pady=5)

        self.payment_label = Label(self.order_frame, text="Mode of Payment:", font=("Bookman Old Style", 11), bg="lightblue")
        self.payment_label.grid(row=5, column=0, pady=5)

        self.payment_var = StringVar()
        self.cod_rb = Radiobutton(self.order_frame, text="COD", variable=self.payment_var, value="COD", bg="lightblue",font=("Bookman Old Style", 9))
        self.cod_rb.grid(row=5, column=1, pady=5)

        self.requirements_label = Label(self.order_frame, text="Any Other Requirements:", font=("Bookman Old Style", 11), bg="lightblue")
        self.requirements_label.grid(row=6, column=0, pady=5)

        self.requirements_text = Text(self.order_frame, height=2, width=30)
        self.requirements_text.grid(row=6, column=1, pady=5)

        self.place_order_button = Button(self.order_frame, text="Place Order", command=self.place_order, font=("Bookman Old Style", 10))
        self.place_order_button.grid(row=7, column=1, columnspan=2, pady=10)
    def place_order(self):
        num_of_clothes = self.clothes_entry.get()
        services_required = []
        if self.dry_clean_var.get():
            services_required.append("Dry Clean")
        if self.wash_fold_var.get():
            services_required.append("Wash and Fold")
        if self.iron_required_var.get():
            services_required.append("Iron Required")
        preferred_time = self.time_entry.get()
        mode_of_payment = self.payment_var.get()
        other_requirements = self.requirements_text.get("1.0", "end-1c")
        query = '''
            INSERT INTO stu_requests (student_username, num_of_clothes, services_required, preferred_time, mode_of_payment, other_requirements)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (self.student_username, num_of_clothes, ', '.join(services_required), preferred_time, mode_of_payment, other_requirements))
        conn.commit()

        messagebox.showinfo('Order Placed', 'Your order has been placed successfully.')
        self.master.destroy()


class AdminDashboard:
    def __init__(self, master, admin_username):
        self.master = master
        self.master.title("Student Dashboard")
        self.admin_username = admin_username

        self.master.configure(bg="lightblue")
        self.master.geometry('550x350+550+150')

        self.welcome_frame = Frame(self.master, bg="lightblue")
        self.welcome_frame.pack(side="top", pady=20)

        self.welcome_label =Label(self.welcome_frame, text="Hi! Welcome, ", font=("Times New Roman", 16), bg="lightblue")
        self.welcome_label.pack(side="left")

        self.username_label = Label(self.welcome_frame, text=self.admin_username, font=("Times New Roman", 20, "bold"), bg="lightblue")
        self.username_label.pack(side="left")

        self.display_requests()

    def display_requests(self):
        query1 = "SELECT * FROM stu_requests"
        cursor.execute(query1)
        requests = cursor.fetchall()

        # Displaying all requests
        for request in requests:
            request_frame = Frame(self.master,padx=20,pady=10, relief=RAISED, borderwidth=2, bg="lightblue")
            request_frame.pack(pady=10, fill=X, padx=10)  

            query2 = "SELECT mobilenumber, hostel FROM student_reg WHERE username = %s"
            cursor.execute(query2, (request[1],))
            details = cursor.fetchone()

            student_label = Label(request_frame, text=f"Student: {request[1]}", bg="lightblue",font=("Bookman Old Style", 10))
            student_label.pack(anchor=W)

            student_mobile_label = Label(request_frame, text=f"Mobile number: {details[0]}", bg="lightblue", font=("Bookman Old Style", 10))
            student_mobile_label.pack(anchor=W)

            student_hostel_label = Label(request_frame, text=f"Hostel: {details[1]}", bg="lightblue", font=("Bookman Old Style", 10))
            student_hostel_label.pack(anchor=W)

            num_clothes_label = Label(request_frame, text=f"Number of Clothes: {request[2]}", bg="lightblue", font=("Bookman Old Style", 10))
            num_clothes_label.pack(anchor=W)

            services_label = Label(request_frame, text=f"Services Required: {request[3]}", bg="lightblue", font=("Bookman Old Style", 10))
            services_label.pack(anchor=W)

            time_label = Label(request_frame, text=f"Preferred Time: {request[4]}", bg="lightblue", font=("Bookman Old Style", 10))
            time_label.pack(anchor= W)

            payment_label = Label(request_frame, text=f"Mode of Payment: {request[5]}", bg="lightblue", font=("Bookman Old Style", 10))
            payment_label.pack(anchor=W)

            requirements_label = Label(request_frame, text=f"Other Requirements: {request[6]}", bg="lightblue", font=("Bookman Old Style", 10))
            requirements_label.pack(anchor=W)

            
            completed_button = Button(request_frame, text="Completed", command=lambda req_id=request[0], frame=request_frame: self.mark_as_completed(req_id, frame))
            completed_button.pack(anchor=W)

    def mark_as_completed(self, request_id,request_frame):
        # Removing the request from the database
        query = "DELETE FROM stu_requests WHERE request_id = %s"
        cursor.execute(query, (request_id,))
        conn.commit()
       
        request_frame.destroy()



root = Tk()
root.geometry('550x350+550+150')
login_window = MainPageLogin(root)
root.resizable(False,False)
root.mainloop()
