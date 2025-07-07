import tkinter as tk
from tkinter import messagebox
import pymysql
from tkinter import ttk

# Create the login window
login_win = tk.Tk()
login_win.geometry("1350x700+0+0")
login_win.title("Barangay Dolores Information System")
title_label = tk.Label(login_win,text="Barangay Dolores Information System ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
title_label.pack(side=tk.TOP,fill=tk.X)

frame = tk.Frame(login_win)

# Create the username label
username_label = tk.Label(frame, text="Username:", font=('Arial', 14, "bold"))
username_label.pack(pady=10)
# Create the username entry
username_entry = tk.Entry(frame, bd=5, font=("Arial", 16))
username_entry.pack(pady=10)

# Create the password label
password_label = tk.Label(frame, text="Password:", font=('Arial', 14, "bold"))
password_label.pack(pady=10)
# Create the password entry
password_entry = tk.Entry(frame, show="*", bd=5, font=("Arial", 16))
password_entry.pack(pady=10)

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Check the username and password against the database or any other validation logic
    if username == "admin" and password == "admin123":
        login_win.destroy()  # Close the login window
        open_main_window()  # Open the main application window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

login_button = tk.Button(frame, text="Login", bd=7, font=("Arial", 13), width=14, command=validate_login)
login_button.pack(pady=10)


frame.pack(expand=True, padx=50, pady=50)

# Create the main application window
def open_main_window():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="Barangay Dolores Information System ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=300,y=90,width=810,height=575)
    

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Choose a Sitio  ",bg="lightgrey",font=("Arial",20,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    btn_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=100, y=110, width=605, height=390)
    
    centro1_btn = tk.Button(btn_frame, bg="lightgrey", text="Centro 1", bd=7, font=("Arial", 13,"bold"), width=27, height=3, command=main_window1)
    centro1_btn.grid(row=0, column=0, padx=2, pady=2)

    centro2_btn = tk.Button(btn_frame, bg="lightgrey", text="Centro 2", bd=7, font=("Arial", 13,"bold"), width=27, height=3, command=main_window2)
    centro2_btn.grid(row=0, column=1, padx=2, pady=2)

    ilaya1_btn = tk.Button(btn_frame, bg="lightgrey", text="Ilaya 1", bd=7, font=("Arial", 13,"bold"), width=27, height=3, command=main_window3)
    ilaya1_btn.grid(row=1, column=0, padx=2, pady=2)

    ilaya2_btn = tk.Button(btn_frame, bg="lightgrey", text="Ilaya 2", bd=7, font=("Arial", 13,"bold"), width=27, height=3, command=main_window4)
    ilaya2_btn.grid(row=1, column=1, padx=2, pady=2)

    mlknginlng_btn = tk.Button(btn_frame, bg="lightgrey", text="Malaking Inalang", bd=7, font=("Arial", 13,"bold"), width=27, height=3, command=main_window5)
    mlknginlng_btn.grid(row=2, column=0, padx=2, pady=2)

    galindo_btn = tk.Button(btn_frame, bg="lightgrey", text="Galindo", bd=7, font=("Arial", 13,"bold"), width=27, height=3, command=main_window6)
    galindo_btn.grid(row=2, column=1, padx=2, pady=2)

    ambulong_btn = tk.Button(btn_frame, bg="lightgrey", text="Ambulong", bd=7, font=("Arial", 13,"bold"), width=27, height=3, command=main_window7)
    ambulong_btn.grid(row=3, column=0, padx=2, pady=2)
    
#===========Centro 1===========#
def main_window1():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="CENTRO 1 Resident Information ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
    detail_frame.place(x=20,y=90,width=420,height=575)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=475,y=90,width=810,height=575)

#==============Variables========#

    idno = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    birthdate = tk.StringVar()
    status = tk.StringVar()
    occupation = tk.StringVar()
    contact = tk.StringVar()


    search_by = tk.StringVar()
    #==============Entry============#

    idno_lbl = tk.Label(detail_frame,text="ID No. ",font=('Arial',14,"bold"),bg="lightgrey")
    idno_lbl.grid(row=0,column=0,padx=2,pady=2)

    idno_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=idno)
    idno_ent.grid(row=0,column=1,padx=2,pady=2)

    name_lbl = tk.Label(detail_frame,text="Name ",font=('Arial',14,"bold"),bg="lightgrey")
    name_lbl.grid(row=1,column=0,padx=2,pady=2)

    name_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=name)
    name_ent.grid(row=1,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',14,"bold"),bg="lightgrey")
    age_lbl.grid(row=2,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=age)
    age_ent.grid(row=2,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',14,"bold"),bg="lightgrey")
    gender_lbl.grid(row=3,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female","Others")
    gender_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birth Date ",font=('Arial',14,"bold"),bg="lightgrey")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',14,"bold"),bg="lightgrey")
    status_lbl.grid(row=5,column=0,padx=2,pady=2)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Others")
    status_ent.grid(row=5,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',14,"bold"),bg="lightgrey")
    occupation_lbl.grid(row=6,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=occupation)
    occupation_ent.grid(row=6,column=1,padx=2,pady=2)

    contact_lbl = tk.Label(detail_frame,text="Contact ",font=('Arial',14,"bold"),bg="lightgrey")
    contact_lbl.grid(row=7,column=0,padx=2,pady=2)

    contact_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=contact)
    contact_ent.grid(row=7,column=1,padx=2,pady=2)

    #=======Function======#

    def fetch_data1():
        conn = pymysql.connect(host="localhost",user="root",password="",database="centro1")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data1")
        rows = curr.fetchall()
        if len(rows)!=0:
                     barangay_table.delete(*barangay_table.get_children())
                     for row in rows:
                         barangay_table.insert('',tk.END,values=row)
                     conn.commit()
        conn.close()

    def add_func():
        if idno.get() == "" or name.get() == "" or age.get() == "":
            messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="centro1")
        curr = conn.cursor()
        curr.execute("INSERT INTO data1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(idno.get(),name.get(),age.get(),gender.get(),birthdate.get(),status.get(),occupation.get(),contact.get()))
        conn.commit()
        conn.close()
    
        fetch_data1()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        birthdate.set(row[4])
        status.set(row[5])
        occupation.set(row[6])
        contact.set(row[7])

    def clear():
        ''' This function will clear the entry boxes '''
        idno.set("")
        name.set("")
        age.set("")
        gender.set("")
        birthdate.set("")
        status.set("")
        occupation.set("")
        contact.set("")


    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="centro1")
        curr = conn.cursor()
        query = "UPDATE data1 SET name = %s, age = %s, gender = %s, birthdate = %s, status = %s, occupation = %s, contact = %s WHERE idno = %s"
        values = (name.get(), age.get(), gender.get(), birthdate.get(), status.get(), occupation.get(), contact.get(), idno.get())
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data1()
        clear()

    def delete_func():
        id_to_delete = idno.get()  # Assuming idno is an Entry widget for entering the ID
    
        if id_to_delete == "":
            messagebox.showerror("Error", "Please select a row to delete.")
            return
    
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="centro1")
            curr = conn.cursor()
            query = "DELETE FROM data1 WHERE idno = %s"
            curr.execute(query, (id_to_delete,))
            conn.commit()
            messagebox.showinfo('Success', 'The data deleted successfully.')
            fetch_data1()  # Assuming you have a fetch_data() function to refresh the data
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        fetch_data1()

   
    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

    # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="centro1")
        cursor = conn.cursor()

        try:
        # Execute the search query based on the selected search option
            if search_option == "ID No.":
                query = "SELECT * FROM data1 WHERE idno = %s"
            elif search_option == "Name":
                query = "SELECT * FROM data1 WHERE name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data1 WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data1 WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data1 WHERE occupation = %s"
            else:
                messagebox.showerror("Error", "Invalid search option!")
                return

            cursor.execute(query, (search_value,))
            result = cursor.fetchall()

            if result:
            # Clear the existing data in the table
                barangay_table.delete(*barangay_table.get_children())

            # Insert the searched results into the table
                for row in result:
                    barangay_table.insert("", tk.END, values=row)

            # Commit the changes
                conn.commit()
            else:
                messagebox.showerror("Error", "No results found!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # Close the database connection
        conn.close()
#=========Total==========#

    def total_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="centro1")
        cursor = conn.cursor()

    # Execute the SQL query to get the total count from the 'data' table
        cursor.execute("SELECT COUNT(*) FROM data1")
        total_data = cursor.fetchone()[0]

    # Close MySQL connection
        cursor.close()
        conn.close()

    # Create a tkinter window
        total_lbl.config(text=f"Total data: {total_data1}")
    # Function to display the total data count

#========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=410, width=350, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=14, command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=14, command=update_func)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=14, command=delete_func)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=14, command=clear)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

#=======Total Frame=====#
    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=351, width=350, height=65)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',13), width=14, bg="lightgrey",command=total_func)
    total_btn.grid(row=12,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',14),bg="white")
    total_lbl.grid(row=12,column=1,padx=2,pady=2)

#============Search==========#

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    search_in = ttk.Combobox(search_frame,width=10,font=("Arial",13),state="readonly")
    search_in['values'] = ("ID No.","Name","Gender","Status","Occupation")
    search_in.grid(row=0,column=1,padx=12,pady=2)

    search_ent = tk.Entry(search_frame,bd=5,font=("arial",14))
    search_ent.grid(row=0,column=2,padx=12,pady=2)

    search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=search_func)
    search_btn.grid(row=0,column=3,padx=12,pady=2)

    showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=fetch_data1)
    showall_btn.grid(row=0,column=4,padx=12,pady=2)
   #=========Database Frame=====#

    main_frame = tk.Frame(data_frame,bg="lightgrey",bd=13,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

    ''' Name, Age, Gender, Birth Date, Status,Occupation, Contact '''
    barangay_table = ttk.Treeview(main_frame,columns=("ID No.","Name","Age","Gender","Birth Date","Status","Occupation","Contact"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("ID No.",text="ID No.")
    barangay_table.heading("Name",text="Name")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Birth Date",text="Birth Date")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Contact",text="Contact")

    barangay_table['show'] = 'headings'

    barangay_table.column("ID No.",width=100)
    barangay_table.column("Name",width=150)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Birth Date",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Contact",width=150)
    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data1()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)

    
#=======Centro 2=======#
def main_window2():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="CENTRO 2 Resident Information  ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
    detail_frame.place(x=20,y=90,width=420,height=575)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=475,y=90,width=810,height=575)

#==============Variables========#

    idno = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    birthdate = tk.StringVar()
    status = tk.StringVar()
    occupation = tk.StringVar()
    contact = tk.StringVar()


    search_by = tk.StringVar()
    #==============Entry============#

    idno_lbl = tk.Label(detail_frame,text="ID No. ",font=('Arial',14,"bold"),bg="lightgrey")
    idno_lbl.grid(row=0,column=0,padx=2,pady=2)

    idno_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=idno)
    idno_ent.grid(row=0,column=1,padx=2,pady=2)

    name_lbl = tk.Label(detail_frame,text="Name ",font=('Arial',14,"bold"),bg="lightgrey")
    name_lbl.grid(row=1,column=0,padx=2,pady=2)

    name_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=name)
    name_ent.grid(row=1,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',14,"bold"),bg="lightgrey")
    age_lbl.grid(row=2,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=age)
    age_ent.grid(row=2,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',14,"bold"),bg="lightgrey")
    gender_lbl.grid(row=3,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female","Others")
    gender_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birth Date ",font=('Arial',14,"bold"),bg="lightgrey")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',14,"bold"),bg="lightgrey")
    status_lbl.grid(row=5,column=0,padx=2,pady=2)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Others")
    status_ent.grid(row=5,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',14,"bold"),bg="lightgrey")
    occupation_lbl.grid(row=6,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=occupation)
    occupation_ent.grid(row=6,column=1,padx=2,pady=2)

    contact_lbl = tk.Label(detail_frame,text="Contact ",font=('Arial',14,"bold"),bg="lightgrey")
    contact_lbl.grid(row=7,column=0,padx=2,pady=2)

    contact_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=contact)
    contact_ent.grid(row=7,column=1,padx=2,pady=2)

    #=======Function======#

    def fetch_data():
        conn = pymysql.connect(host="localhost",user="root",password="",database="c2bis")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows)!=0:
                     barangay_table.delete(*barangay_table.get_children())
                     for row in rows:
                         barangay_table.insert('',tk.END,values=row)
                     conn.commit()
        conn.close()

    def add_func():
        if idno.get() == "" or name.get() == "" or age.get() == "":
           messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="c2bis")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(idno.get(),name.get(),age.get(),gender.get(),birthdate.get(),status.get(),occupation.get(),contact.get()))
        conn.commit()
        conn.close()
    
        fetch_data()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        birthdate.set(row[4])
        status.set(row[5])
        occupation.set(row[6])
        contact.set(row[8])

    def clear():
        ''' This function will clear the entry boxes '''
        idno.set("")
        name.set("")
        age.set("")
        gender.set("")
        birthdate.set("")
        status.set("")
        occupation.set("")
        contact.set("")


    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="c2bis")
        curr = conn.cursor()
        query = "UPDATE data SET name = %s, age = %s, gender = %s, birthdate = %s, status = %s, occupation = %s, contact = %s WHERE idno = %s"
        values = (name.get(), age.get(), gender.get(), birthdate.get(), status.get(), occupation.get(), contact.get(), idno.get())
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data()
        clear()

    def delete_func():
        id_to_delete = idno.get()  # Assuming idno is an Entry widget for entering the ID
    
        if id_to_delete == "":
            messagebox.showerror("Error", "Please select a row to delete.")
            return
    
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="c2bis")
            curr = conn.cursor()
            query = "DELETE FROM data WHERE idno = %s"
            curr.execute(query, (id_to_delete,))
            conn.commit()
            messagebox.showinfo('Success', 'The data deleted successfully.')
            fetch_data()  # Assuming you have a fetch_data() function to refresh the data
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        fetch_data()

   
    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

    # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="c2bis")
        cursor = conn.cursor()

        try:
        # Execute the search query based on the selected search option
            if search_option == "ID No.":
                query = "SELECT * FROM data WHERE idno = %s"
            elif search_option == "Name":
                query = "SELECT * FROM data WHERE name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data WHERE occupation = %s"
            else:
                messagebox.showerror("Error", "Invalid search option!")
                return

            cursor.execute(query, (search_value,))
            result = cursor.fetchall()

            if result:
            # Clear the existing data in the table
                barangay_table.delete(*barangay_table.get_children())

            # Insert the searched results into the table
                for row in result:
                    barangay_table.insert("", tk.END, values=row)

            # Commit the changes
                conn.commit()
            else:
                messagebox.showerror("Error", "No results found!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # Close the database connection
        conn.close()
#=========Total==========#

    def total_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="c2bis")
        cursor = conn.cursor()

    # Execute the SQL query to get the total count from the 'data' table
        cursor.execute("SELECT COUNT(*) FROM data")
        total_data = cursor.fetchone()[0]

    # Close MySQL connection
        cursor.close()
        conn.close()

    # Create a tkinter window
        total_lbl.config(text=f"Total data: {total_data}")
    # Function to display the total data count

#========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=410, width=350, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=14, command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=14, command=update_func)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=14, command=delete_func)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=14, command=clear)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

#=======Total Frame=====#
    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=351, width=350, height=65)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',13), width=14, bg="lightgrey",command=total_func)
    total_btn.grid(row=12,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',14),bg="white")
    total_lbl.grid(row=12,column=1,padx=2,pady=2)

#============Search==========#

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    search_in = ttk.Combobox(search_frame,width=10,font=("Arial",13),state="readonly")
    search_in['values'] = ("ID No.","Name","Gender","Status","Occupation")
    search_in.grid(row=0,column=1,padx=12,pady=2)

    search_ent = tk.Entry(search_frame,bd=5,font=("arial",14))
    search_ent.grid(row=0,column=2,padx=12,pady=2)

    search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=search_func)
    search_btn.grid(row=0,column=3,padx=12,pady=2)

    showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=fetch_data)
    showall_btn.grid(row=0,column=4,padx=12,pady=2)
   #=========Database Frame=====#

    main_frame = tk.Frame(data_frame,bg="lightgrey",bd=13,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

    ''' Name, Age, Gender, Birth Date, Status,Occupation, Contact '''
    barangay_table = ttk.Treeview(main_frame,columns=("ID No.","Name","Age","Gender","Birth Date","Status","Occupation","Contact"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("ID No.",text="ID No.")
    barangay_table.heading("Name",text="Name")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Birth Date",text="Birth Date")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Contact",text="Contact")

    barangay_table['show'] = 'headings'

    barangay_table.column("ID No.",width=100)
    barangay_table.column("Name",width=150)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Birth Date",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Contact",width=150)
    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)

    
#=========Ilaya 1==========#
def main_window3():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="ILAYA 1 Resident Information  ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
    detail_frame.place(x=20,y=90,width=420,height=575)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=475,y=90,width=810,height=575)

#==============Variables========#

    idno = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    birthdate = tk.StringVar()
    status = tk.StringVar()
    occupation = tk.StringVar()
    contact = tk.StringVar()


    search_by = tk.StringVar()
    #==============Entry============#

    idno_lbl = tk.Label(detail_frame,text="ID No. ",font=('Arial',14,"bold"),bg="lightgrey")
    idno_lbl.grid(row=0,column=0,padx=2,pady=2)

    idno_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=idno)
    idno_ent.grid(row=0,column=1,padx=2,pady=2)

    name_lbl = tk.Label(detail_frame,text="Name ",font=('Arial',14,"bold"),bg="lightgrey")
    name_lbl.grid(row=1,column=0,padx=2,pady=2)

    name_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=name)
    name_ent.grid(row=1,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',14,"bold"),bg="lightgrey")
    age_lbl.grid(row=2,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=age)
    age_ent.grid(row=2,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',14,"bold"),bg="lightgrey")
    gender_lbl.grid(row=3,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female","Others")
    gender_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birth Date ",font=('Arial',14,"bold"),bg="lightgrey")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',14,"bold"),bg="lightgrey")
    status_lbl.grid(row=5,column=0,padx=2,pady=2)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Others")
    status_ent.grid(row=5,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',14,"bold"),bg="lightgrey")
    occupation_lbl.grid(row=6,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=occupation)
    occupation_ent.grid(row=6,column=1,padx=2,pady=2)

    contact_lbl = tk.Label(detail_frame,text="Contact ",font=('Arial',14,"bold"),bg="lightgrey")
    contact_lbl.grid(row=7,column=0,padx=2,pady=2)

    contact_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=contact)
    contact_ent.grid(row=7,column=1,padx=2,pady=2)

    #=======Function======#

    def fetch_data():
        conn = pymysql.connect(host="localhost",user="root",password="",database="i1bis")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows)!=0:
                     barangay_table.delete(*barangay_table.get_children())
                     for row in rows:
                         barangay_table.insert('',tk.END,values=row)
                     conn.commit()
        conn.close()

    def add_func():
        if idno.get() == "" or name.get() == "" or age.get() == "":
            messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="i1bis")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(idno.get(),name.get(),age.get(),gender.get(),birthdate.get(),status.get(),occupation.get(),contact.get()))
        conn.commit()
        conn.close()
    
        fetch_data()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        birthdate.set(row[4])
        status.set(row[5])
        occupation.set(row[6])
        contact.set(row[8])

    def clear():
        ''' This function will clear the entry boxes '''
        idno.set("")
        name.set("")
        age.set("")
        gender.set("")
        birthdate.set("")
        status.set("")
        occupation.set("")
        contact.set("")


    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="i1bis")
        curr = conn.cursor()
        query = "UPDATE data SET name = %s, age = %s, gender = %s, birthdate = %s, status = %s, occupation = %s, contact = %s WHERE idno = %s"
        values = (name.get(), age.get(), gender.get(), birthdate.get(), status.get(), occupation.get(), contact.get(), idno.get())
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data()
        clear()

    def delete_func():
        id_to_delete = idno.get()  # Assuming idno is an Entry widget for entering the ID
    
        if id_to_delete == "":
            messagebox.showerror("Error", "Please select a row to delete.")
            return
    
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="i1bis")
            curr = conn.cursor()
            query = "DELETE FROM data WHERE idno = %s"
            curr.execute(query, (id_to_delete,))
            conn.commit()
            messagebox.showinfo('Success', 'The data deleted successfully.')
            fetch_data()  # Assuming you have a fetch_data() function to refresh the data
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        fetch_data()

   
    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

    # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="i1bis")
        cursor = conn.cursor()

        try:
        # Execute the search query based on the selected search option
            if search_option == "ID No.":
                query = "SELECT * FROM data WHERE idno = %s"
            elif search_option == "Name":
                query = "SELECT * FROM data WHERE name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data WHERE occupation = %s"
            else:
                messagebox.showerror("Error", "Invalid search option!")
                return

            cursor.execute(query, (search_value,))
            result = cursor.fetchall()

            if result:
            # Clear the existing data in the table
                barangay_table.delete(*barangay_table.get_children())

            # Insert the searched results into the table
                for row in result:
                    barangay_table.insert("", tk.END, values=row)

            # Commit the changes
                conn.commit()
            else:
                messagebox.showerror("Error", "No results found!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # Close the database connection
        conn.close()
#=========Total==========#

    def total_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="i1bis")
        cursor = conn.cursor()

    # Execute the SQL query to get the total count from the 'data' table
        cursor.execute("SELECT COUNT(*) FROM data")
        total_data = cursor.fetchone()[0]

    # Close MySQL connection
        cursor.close()
        conn.close()

    # Create a tkinter window
        total_lbl.config(text=f"Total data: {total_data}")
    # Function to display the total data count

#========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=410, width=350, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=14, command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=14, command=update_func)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=14, command=delete_func)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=14, command=clear)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

#=======Total Frame=====#
    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=351, width=350, height=65)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',13), width=14, bg="lightgrey",command=total_func)
    total_btn.grid(row=12,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',14),bg="white")
    total_lbl.grid(row=12,column=1,padx=2,pady=2)

#============Search==========#

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    search_in = ttk.Combobox(search_frame,width=10,font=("Arial",13),state="readonly")
    search_in['values'] = ("ID No.","Name","Gender","Status","Occupation")
    search_in.grid(row=0,column=1,padx=12,pady=2)

    search_ent = tk.Entry(search_frame,bd=5,font=("arial",14))
    search_ent.grid(row=0,column=2,padx=12,pady=2)

    search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=search_func)
    search_btn.grid(row=0,column=3,padx=12,pady=2)

    showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=fetch_data)
    showall_btn.grid(row=0,column=4,padx=12,pady=2)
   #=========Database Frame=====#

    main_frame = tk.Frame(data_frame,bg="lightgrey",bd=13,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

    ''' Name, Age, Gender, Birth Date, Status,Occupation, Contact '''
    barangay_table = ttk.Treeview(main_frame,columns=("ID No.","Name","Age","Gender","Birth Date","Status","Occupation","Contact"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("ID No.",text="ID No.")
    barangay_table.heading("Name",text="Name")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Birth Date",text="Birth Date")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Contact",text="Contact")

    barangay_table['show'] = 'headings'

    barangay_table.column("ID No.",width=100)
    barangay_table.column("Name",width=150)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Birth Date",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Contact",width=150)
    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)

#=========Ilaya 2==========#
def main_window4():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="ILAYA 2 Resident Information  ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
    detail_frame.place(x=20,y=90,width=420,height=575)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=475,y=90,width=810,height=575)

#==============Variables========#

    idno = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    birthdate = tk.StringVar()
    status = tk.StringVar()
    occupation = tk.StringVar()
    contact = tk.StringVar()


    search_by = tk.StringVar()
    #==============Entry============#

    idno_lbl = tk.Label(detail_frame,text="ID No. ",font=('Arial',14,"bold"),bg="lightgrey")
    idno_lbl.grid(row=0,column=0,padx=2,pady=2)

    idno_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=idno)
    idno_ent.grid(row=0,column=1,padx=2,pady=2)

    name_lbl = tk.Label(detail_frame,text="Name ",font=('Arial',14,"bold"),bg="lightgrey")
    name_lbl.grid(row=1,column=0,padx=2,pady=2)

    name_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=name)
    name_ent.grid(row=1,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',14,"bold"),bg="lightgrey")
    age_lbl.grid(row=2,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=age)
    age_ent.grid(row=2,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',14,"bold"),bg="lightgrey")
    gender_lbl.grid(row=3,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female","Others")
    gender_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birth Date ",font=('Arial',14,"bold"),bg="lightgrey")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',14,"bold"),bg="lightgrey")
    status_lbl.grid(row=5,column=0,padx=2,pady=2)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Others")
    status_ent.grid(row=5,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',14,"bold"),bg="lightgrey")
    occupation_lbl.grid(row=6,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=occupation)
    occupation_ent.grid(row=6,column=1,padx=2,pady=2)

    contact_lbl = tk.Label(detail_frame,text="Contact ",font=('Arial',14,"bold"),bg="lightgrey")
    contact_lbl.grid(row=7,column=0,padx=2,pady=2)

    contact_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=contact)
    contact_ent.grid(row=7,column=1,padx=2,pady=2)

    #=======Function======#

    def fetch_data():
        conn = pymysql.connect(host="localhost",user="root",password="",database="i2bis")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows)!=0:
                     barangay_table.delete(*barangay_table.get_children())
                     for row in rows:
                         barangay_table.insert('',tk.END,values=row)
                     conn.commit()
        conn.close()

    def add_func():
        if idno.get() == "" or name.get() == "" or age.get() == "":
            messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="i2bis")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(idno.get(),name.get(),age.get(),gender.get(),birthdate.get(),status.get(),occupation.get(),contact.get()))
        conn.commit()
        conn.close()
    
        fetch_data()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        birthdate.set(row[4])
        status.set(row[5])
        occupation.set(row[6])
        contact.set(row[8])

    def clear():
        ''' This function will clear the entry boxes '''
        idno.set("")
        name.set("")
        age.set("")
        gender.set("")
        birthdate.set("")
        status.set("")
        occupation.set("")
        contact.set("")


    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="i2bis")
        curr = conn.cursor()
        query = "UPDATE data SET name = %s, age = %s, gender = %s, birthdate = %s, status = %s, occupation = %s, contact = %s WHERE idno = %s"
        values = (name.get(), age.get(), gender.get(), birthdate.get(), status.get(), occupation.get(), contact.get(), idno.get())
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data()
        clear()

    def delete_func():
        id_to_delete = idno.get()  # Assuming idno is an Entry widget for entering the ID
    
        if id_to_delete == "":
            messagebox.showerror("Error", "Please select a row to delete.")
            return
    
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="i2bis")
            curr = conn.cursor()
            query = "DELETE FROM data WHERE idno = %s"
            curr.execute(query, (id_to_delete,))
            conn.commit()
            messagebox.showinfo('Success', 'The data deleted successfully.')
            fetch_data()  # Assuming you have a fetch_data() function to refresh the data
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        fetch_data()

   
    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

    # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="i2bis")
        cursor = conn.cursor()

        try:
        # Execute the search query based on the selected search option
            if search_option == "ID No.":
                query = "SELECT * FROM data WHERE idno = %s"
            elif search_option == "Name":
                query = "SELECT * FROM data WHERE name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data WHERE occupation = %s"
            else:
                messagebox.showerror("Error", "Invalid search option!")
                return

            cursor.execute(query, (search_value,))
            result = cursor.fetchall()

            if result:
            # Clear the existing data in the table
                barangay_table.delete(*barangay_table.get_children())

            # Insert the searched results into the table
                for row in result:
                    barangay_table.insert("", tk.END, values=row)

            # Commit the changes
                conn.commit()
            else:
                messagebox.showerror("Error", "No results found!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # Close the database connection
        conn.close()
#=========Total==========#

    def total_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="i2bis")
        cursor = conn.cursor()

    # Execute the SQL query to get the total count from the 'data' table
        cursor.execute("SELECT COUNT(*) FROM data")
        total_data = cursor.fetchone()[0]

    # Close MySQL connection
        cursor.close()
        conn.close()

    # Create a tkinter window
        total_lbl.config(text=f"Total data: {total_data}")
    # Function to display the total data count

#========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=410, width=350, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=14, command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=14, command=update_func)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=14, command=delete_func)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=14, command=clear)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

#=======Total Frame=====#
    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=351, width=350, height=65)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',13), width=14, bg="lightgrey",command=total_func)
    total_btn.grid(row=12,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',14),bg="white")
    total_lbl.grid(row=12,column=1,padx=2,pady=2)

#============Search==========#

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    search_in = ttk.Combobox(search_frame,width=10,font=("Arial",13),state="readonly")
    search_in['values'] = ("ID No.","Name","Gender","Status","Occupation")
    search_in.grid(row=0,column=1,padx=12,pady=2)

    search_ent = tk.Entry(search_frame,bd=5,font=("arial",14))
    search_ent.grid(row=0,column=2,padx=12,pady=2)

    search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=search_func)
    search_btn.grid(row=0,column=3,padx=12,pady=2)

    showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=fetch_data)
    showall_btn.grid(row=0,column=4,padx=12,pady=2)
   #=========Database Frame=====#

    main_frame = tk.Frame(data_frame,bg="lightgrey",bd=13,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

    ''' Name, Age, Gender, Birth Date, Status,Occupation, Contact '''
    barangay_table = ttk.Treeview(main_frame,columns=("ID No.","Name","Age","Gender","Birth Date","Status","Occupation","Contact"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("ID No.",text="ID No.")
    barangay_table.heading("Name",text="Name")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Birth Date",text="Birth Date")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Contact",text="Contact")

    barangay_table['show'] = 'headings'

    barangay_table.column("ID No.",width=100)
    barangay_table.column("Name",width=150)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Birth Date",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Contact",width=150)
    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)

#=========Malaking Inalang==========#
def main_window5():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="MALAKING INALANG Resident Information  ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
    detail_frame.place(x=20,y=90,width=420,height=575)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=475,y=90,width=810,height=575)

#==============Variables========#

    idno = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    birthdate = tk.StringVar()
    status = tk.StringVar()
    occupation = tk.StringVar()
    contact = tk.StringVar()


    search_by = tk.StringVar()
    #==============Entry============#

    idno_lbl = tk.Label(detail_frame,text="ID No. ",font=('Arial',14,"bold"),bg="lightgrey")
    idno_lbl.grid(row=0,column=0,padx=2,pady=2)

    idno_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=idno)
    idno_ent.grid(row=0,column=1,padx=2,pady=2)

    name_lbl = tk.Label(detail_frame,text="Name ",font=('Arial',14,"bold"),bg="lightgrey")
    name_lbl.grid(row=1,column=0,padx=2,pady=2)

    name_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=name)
    name_ent.grid(row=1,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',14,"bold"),bg="lightgrey")
    age_lbl.grid(row=2,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=age)
    age_ent.grid(row=2,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',14,"bold"),bg="lightgrey")
    gender_lbl.grid(row=3,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female","Others")
    gender_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birth Date ",font=('Arial',14,"bold"),bg="lightgrey")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',14,"bold"),bg="lightgrey")
    status_lbl.grid(row=5,column=0,padx=2,pady=2)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Others")
    status_ent.grid(row=5,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',14,"bold"),bg="lightgrey")
    occupation_lbl.grid(row=6,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=occupation)
    occupation_ent.grid(row=6,column=1,padx=2,pady=2)

    contact_lbl = tk.Label(detail_frame,text="Contact ",font=('Arial',14,"bold"),bg="lightgrey")
    contact_lbl.grid(row=7,column=0,padx=2,pady=2)

    contact_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=contact)
    contact_ent.grid(row=7,column=1,padx=2,pady=2)

    #=======Function======#

    def fetch_data():
        conn = pymysql.connect(host="localhost",user="root",password="",database="mibis")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows)!=0:
                     barangay_table.delete(*barangay_table.get_children())
                     for row in rows:
                         barangay_table.insert('',tk.END,values=row)
                     conn.commit()
        conn.close()

    def add_func():
        if idno.get() == "" or name.get() == "" or age.get() == "":
            messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="mibis")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(idno.get(),name.get(),age.get(),gender.get(),birthdate.get(),status.get(),occupation.get(),contact.get()))
        conn.commit()
        conn.close()
    
        fetch_data()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        birthdate.set(row[4])
        status.set(row[5])
        occupation.set(row[6])
        contact.set(row[8])

    def clear():
        ''' This function will clear the entry boxes '''
        idno.set("")
        name.set("")
        age.set("")
        gender.set("")
        birthdate.set("")
        status.set("")
        occupation.set("")
        contact.set("")


    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="mibis")
        curr = conn.cursor()
        query = "UPDATE data SET name = %s, age = %s, gender = %s, birthdate = %s, status = %s, occupation = %s, contact = %s WHERE idno = %s"
        values = (name.get(), age.get(), gender.get(), birthdate.get(), status.get(), occupation.get(), contact.get(), idno.get())
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data()
        clear()

    def delete_func():
        id_to_delete = idno.get()  # Assuming idno is an Entry widget for entering the ID
    
        if id_to_delete == "":
            messagebox.showerror("Error", "Please select a row to delete.")
            return
    
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="mibis")
            curr = conn.cursor()
            query = "DELETE FROM data WHERE idno = %s"
            curr.execute(query, (id_to_delete,))
            conn.commit()
            messagebox.showinfo('Success', 'The data deleted successfully.')
            fetch_data()  # Assuming you have a fetch_data() function to refresh the data
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        fetch_data()

   
    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

    # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="mibis")
        cursor = conn.cursor()

        try:
        # Execute the search query based on the selected search option
            if search_option == "ID No.":
                query = "SELECT * FROM data WHERE idno = %s"
            elif search_option == "Name":
                query = "SELECT * FROM data WHERE name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data WHERE occupation = %s"
            else:
                messagebox.showerror("Error", "Invalid search option!")
                return

            cursor.execute(query, (search_value,))
            result = cursor.fetchall()

            if result:
            # Clear the existing data in the table
                barangay_table.delete(*barangay_table.get_children())

            # Insert the searched results into the table
                for row in result:
                    barangay_table.insert("", tk.END, values=row)

            # Commit the changes
                conn.commit()
            else:
                messagebox.showerror("Error", "No results found!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # Close the database connection
        conn.close()
#=========Total==========#

    def total_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="mibis")
        cursor = conn.cursor()

    # Execute the SQL query to get the total count from the 'data' table
        cursor.execute("SELECT COUNT(*) FROM data")
        total_data = cursor.fetchone()[0]

    # Close MySQL connection
        cursor.close()
        conn.close()

    # Create a tkinter window
        total_lbl.config(text=f"Total data: {total_data}")
    # Function to display the total data count

#========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=410, width=350, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=14, command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=14, command=update_func)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=14, command=delete_func)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=14, command=clear)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

#=======Total Frame=====#
    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=351, width=350, height=65)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',13), width=14, bg="lightgrey",command=total_func)
    total_btn.grid(row=12,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',14),bg="white")
    total_lbl.grid(row=12,column=1,padx=2,pady=2)

#============Search==========#

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    search_in = ttk.Combobox(search_frame,width=10,font=("Arial",13),state="readonly")
    search_in['values'] = ("ID No.","Name","Gender","Status","Occupation")
    search_in.grid(row=0,column=1,padx=12,pady=2)

    search_ent = tk.Entry(search_frame,bd=5,font=("arial",14))
    search_ent.grid(row=0,column=2,padx=12,pady=2)

    search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=search_func)
    search_btn.grid(row=0,column=3,padx=12,pady=2)

    showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=fetch_data)
    showall_btn.grid(row=0,column=4,padx=12,pady=2)
   #=========Database Frame=====#

    main_frame = tk.Frame(data_frame,bg="lightgrey",bd=13,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

    ''' Name, Age, Gender, Birth Date, Status,Occupation, Contact '''
    barangay_table = ttk.Treeview(main_frame,columns=("ID No.","Name","Age","Gender","Birth Date","Status","Occupation","Contact"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("ID No.",text="ID No.")
    barangay_table.heading("Name",text="Name")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Birth Date",text="Birth Date")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Contact",text="Contact")

    barangay_table['show'] = 'headings'

    barangay_table.column("ID No.",width=100)
    barangay_table.column("Name",width=150)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Birth Date",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Contact",width=150)
    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)

#===========Galindo===========#
def main_window6():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="GALINDO Resident Information  ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
    detail_frame.place(x=20,y=90,width=420,height=575)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=475,y=90,width=810,height=575)

#==============Variables========#

    idno = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    birthdate = tk.StringVar()
    status = tk.StringVar()
    occupation = tk.StringVar()
    contact = tk.StringVar()


    search_by = tk.StringVar()
    #==============Entry============#

    idno_lbl = tk.Label(detail_frame,text="ID No. ",font=('Arial',14,"bold"),bg="lightgrey")
    idno_lbl.grid(row=0,column=0,padx=2,pady=2)

    idno_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=idno)
    idno_ent.grid(row=0,column=1,padx=2,pady=2)

    name_lbl = tk.Label(detail_frame,text="Name ",font=('Arial',14,"bold"),bg="lightgrey")
    name_lbl.grid(row=1,column=0,padx=2,pady=2)

    name_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=name)
    name_ent.grid(row=1,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',14,"bold"),bg="lightgrey")
    age_lbl.grid(row=2,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=age)
    age_ent.grid(row=2,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',14,"bold"),bg="lightgrey")
    gender_lbl.grid(row=3,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female","Others")
    gender_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birth Date ",font=('Arial',14,"bold"),bg="lightgrey")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',14,"bold"),bg="lightgrey")
    status_lbl.grid(row=5,column=0,padx=2,pady=2)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Others")
    status_ent.grid(row=5,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',14,"bold"),bg="lightgrey")
    occupation_lbl.grid(row=6,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=occupation)
    occupation_ent.grid(row=6,column=1,padx=2,pady=2)

    contact_lbl = tk.Label(detail_frame,text="Contact ",font=('Arial',14,"bold"),bg="lightgrey")
    contact_lbl.grid(row=7,column=0,padx=2,pady=2)

    contact_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=contact)
    contact_ent.grid(row=7,column=1,padx=2,pady=2)

    #=======Function======#

    def fetch_data():
        conn = pymysql.connect(host="localhost",user="root",password="",database="gbis")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows)!=0:
                     barangay_table.delete(*barangay_table.get_children())
                     for row in rows:
                         barangay_table.insert('',tk.END,values=row)
                     conn.commit()
        conn.close()

    def add_func():
        if idno.get() == "" or name.get() == "" or age.get() == "":
            messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="gbis")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(idno.get(),name.get(),age.get(),gender.get(),birthdate.get(),status.get(),occupation.get(),contact.get()))
        conn.commit()
        conn.close()
    
        fetch_data()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        birthdate.set(row[4])
        status.set(row[5])
        occupation.set(row[6])
        contact.set(row[8])

    def clear():
        ''' This function will clear the entry boxes '''
        idno.set("")
        name.set("")
        age.set("")
        gender.set("")
        birthdate.set("")
        status.set("")
        occupation.set("")
        contact.set("")


    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="gbis")
        curr = conn.cursor()
        query = "UPDATE data SET name = %s, age = %s, gender = %s, birthdate = %s, status = %s, occupation = %s, contact = %s WHERE idno = %s"
        values = (name.get(), age.get(), gender.get(), birthdate.get(), status.get(), occupation.get(), contact.get(), idno.get())
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data()
        clear()

    def delete_func():
        id_to_delete = idno.get()  # Assuming idno is an Entry widget for entering the ID
    
        if id_to_delete == "":
            messagebox.showerror("Error", "Please select a row to delete.")
            return
    
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="gbis")
            curr = conn.cursor()
            query = "DELETE FROM data WHERE idno = %s"
            curr.execute(query, (id_to_delete,))
            conn.commit()
            messagebox.showinfo('Success', 'The data deleted successfully.')
            fetch_data()  # Assuming you have a fetch_data() function to refresh the data
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        fetch_data()

   
    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

    # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="gbis")
        cursor = conn.cursor()

        try:
        # Execute the search query based on the selected search option
            if search_option == "ID No.":
                query = "SELECT * FROM data WHERE idno = %s"
            elif search_option == "Name":
                query = "SELECT * FROM data WHERE name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data WHERE occupation = %s"
            else:
                messagebox.showerror("Error", "Invalid search option!")
                return

            cursor.execute(query, (search_value,))
            result = cursor.fetchall()

            if result:
            # Clear the existing data in the table
                barangay_table.delete(*barangay_table.get_children())

            # Insert the searched results into the table
                for row in result:
                    barangay_table.insert("", tk.END, values=row)

            # Commit the changes
                conn.commit()
            else:
                messagebox.showerror("Error", "No results found!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # Close the database connection
        conn.close()
#=========Total==========#

    def total_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="gbis")
        cursor = conn.cursor()

    # Execute the SQL query to get the total count from the 'data' table
        cursor.execute("SELECT COUNT(*) FROM data")
        total_data = cursor.fetchone()[0]

    # Close MySQL connection
        cursor.close()
        conn.close()

    # Create a tkinter window
        total_lbl.config(text=f"Total data: {total_data}")
    # Function to display the total data count

#========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=410, width=350, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=14, command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=14, command=update_func)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=14, command=delete_func)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=14, command=clear)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

#=======Total Frame=====#
    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=351, width=350, height=65)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',13), width=14, bg="lightgrey",command=total_func)
    total_btn.grid(row=12,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',14),bg="white")
    total_lbl.grid(row=12,column=1,padx=2,pady=2)

#============Search==========#

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    search_in = ttk.Combobox(search_frame,width=10,font=("Arial",13),state="readonly")
    search_in['values'] = ("ID No.","Name","Gender","Status","Occupation")
    search_in.grid(row=0,column=1,padx=12,pady=2)

    search_ent = tk.Entry(search_frame,bd=5,font=("arial",14))
    search_ent.grid(row=0,column=2,padx=12,pady=2)

    search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=search_func)
    search_btn.grid(row=0,column=3,padx=12,pady=2)

    showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=fetch_data)
    showall_btn.grid(row=0,column=4,padx=12,pady=2)
   #=========Database Frame=====#

    main_frame = tk.Frame(data_frame,bg="lightgrey",bd=13,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

    ''' Name, Age, Gender, Birth Date, Status,Occupation, Contact '''
    barangay_table = ttk.Treeview(main_frame,columns=("ID No.","Name","Age","Gender","Birth Date","Status","Occupation","Contact"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("ID No.",text="ID No.")
    barangay_table.heading("Name",text="Name")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Birth Date",text="Birth Date")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Contact",text="Contact")

    barangay_table['show'] = 'headings'

    barangay_table.column("ID No.",width=100)
    barangay_table.column("Name",width=150)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Birth Date",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Contact",width=150)
    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)

    
#=========Ambulong==========#
def main_window7():
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Information System")
    title_label = tk.Label(win,text="AMBULONG Resident Information  ",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="silver")
    title_label.pack(side=tk.TOP,fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",20),bd=12,relief=tk.GROOVE,bg="lightgrey")
    detail_frame.place(x=20,y=90,width=420,height=575)

    data_frame = tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE)
    data_frame.place(x=475,y=90,width=810,height=575)

#==============Variables========#

    idno = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    birthdate = tk.StringVar()
    status = tk.StringVar()
    occupation = tk.StringVar()
    contact = tk.StringVar()


    search_by = tk.StringVar()
    #==============Entry============#

    idno_lbl = tk.Label(detail_frame,text="ID No. ",font=('Arial',14,"bold"),bg="lightgrey")
    idno_lbl.grid(row=0,column=0,padx=2,pady=2)

    idno_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=idno)
    idno_ent.grid(row=0,column=1,padx=2,pady=2)

    name_lbl = tk.Label(detail_frame,text="Name ",font=('Arial',14,"bold"),bg="lightgrey")
    name_lbl.grid(row=1,column=0,padx=2,pady=2)

    name_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=name)
    name_ent.grid(row=1,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',14,"bold"),bg="lightgrey")
    age_lbl.grid(row=2,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=age)
    age_ent.grid(row=2,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',14,"bold"),bg="lightgrey")
    gender_lbl.grid(row=3,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female","Others")
    gender_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birth Date ",font=('Arial',14,"bold"),bg="lightgrey")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',14,"bold"),bg="lightgrey")
    status_lbl.grid(row=5,column=0,padx=2,pady=2)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',16),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Others")
    status_ent.grid(row=5,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',14,"bold"),bg="lightgrey")
    occupation_lbl.grid(row=6,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=occupation)
    occupation_ent.grid(row=6,column=1,padx=2,pady=2)

    contact_lbl = tk.Label(detail_frame,text="Contact ",font=('Arial',14,"bold"),bg="lightgrey")
    contact_lbl.grid(row=7,column=0,padx=2,pady=2)

    contact_ent = tk.Entry(detail_frame,bd=5,font=("arial",16),textvariable=contact)
    contact_ent.grid(row=7,column=1,padx=2,pady=2)

    #=======Function======#

    def fetch_data():
        conn = pymysql.connect(host="localhost",user="root",password="",database="abis")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows)!=0:
                     barangay_table.delete(*barangay_table.get_children())
                     for row in rows:
                         barangay_table.insert('',tk.END,values=row)
                     conn.commit()
        conn.close()

    def add_func():
        if idno.get() == "" or name.get() == "" or age.get() == "":
            messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="abis")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(idno.get(),name.get(),age.get(),gender.get(),birthdate.get(),status.get(),occupation.get(),contact.get()))
        conn.commit()
        conn.close()
    
        fetch_data()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        birthdate.set(row[4])
        status.set(row[5])
        occupation.set(row[6])
        contact.set(row[8])

    def clear():
        ''' This function will clear the entry boxes '''
        idno.set("")
        name.set("")
        age.set("")
        gender.set("")
        birthdate.set("")
        status.set("")
        occupation.set("")
        contact.set("")


    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="abis")
        curr = conn.cursor()
        query = "UPDATE data SET name = %s, age = %s, gender = %s, birthdate = %s, status = %s, occupation = %s, contact = %s WHERE idno = %s"
        values = (name.get(), age.get(), gender.get(), birthdate.get(), status.get(), occupation.get(), contact.get(), idno.get())
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data()
        clear()

    def delete_func():
        id_to_delete = idno.get()  # Assuming idno is an Entry widget for entering the ID
    
        if id_to_delete == "":
            messagebox.showerror("Error", "Please select a row to delete.")
            return
    
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="abis")
            curr = conn.cursor()
            query = "DELETE FROM data WHERE idno = %s"
            curr.execute(query, (id_to_delete,))
            conn.commit()
            messagebox.showinfo('Success', 'The data deleted successfully.')
            fetch_data()  # Assuming you have a fetch_data() function to refresh the data
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()
        fetch_data()

   
    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

    # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="abis")
        cursor = conn.cursor()

        try:
        # Execute the search query based on the selected search option
            if search_option == "ID No.":
                query = "SELECT * FROM data WHERE idno = %s"
            elif search_option == "Name":
                query = "SELECT * FROM data WHERE name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data WHERE occupation = %s"
            else:
                messagebox.showerror("Error", "Invalid search option!")
                return

            cursor.execute(query, (search_value,))
            result = cursor.fetchall()

            if result:
            # Clear the existing data in the table
                barangay_table.delete(*barangay_table.get_children())

            # Insert the searched results into the table
                for row in result:
                    barangay_table.insert("", tk.END, values=row)

            # Commit the changes
                conn.commit()
            else:
                messagebox.showerror("Error", "No results found!")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # Close the database connection
        conn.close()
#=========Total==========#

    def total_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="abis")
        cursor = conn.cursor()

    # Execute the SQL query to get the total count from the 'data' table
        cursor.execute("SELECT COUNT(*) FROM data")
        total_data = cursor.fetchone()[0]

    # Close MySQL connection
        cursor.close()
        conn.close()

    # Create a tkinter window
        total_lbl.config(text=f"Total data: {total_data}")
    # Function to display the total data count

#========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=410, width=350, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 13), width=14, command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 13), width=14, command=update_func)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 13), width=14, command=delete_func)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 13), width=14, command=clear)
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

#=======Total Frame=====#
    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=24, y=351, width=350, height=65)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',13), width=14, bg="lightgrey",command=total_func)
    total_btn.grid(row=12,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',14),bg="white")
    total_lbl.grid(row=12,column=1,padx=2,pady=2)

#============Search==========#

    search_frame = tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text="Search ",bg="lightgrey",font=("Arial",14,"bold"))
    search_lbl.grid(row=0,column=0,padx=12,pady=2)

    search_in = ttk.Combobox(search_frame,width=10,font=("Arial",13),state="readonly")
    search_in['values'] = ("ID No.","Name","Gender","Status","Occupation")
    search_in.grid(row=0,column=1,padx=12,pady=2)

    search_ent = tk.Entry(search_frame,bd=5,font=("arial",14))
    search_ent.grid(row=0,column=2,padx=12,pady=2)

    search_btn = tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=search_func)
    search_btn.grid(row=0,column=3,padx=12,pady=2)

    showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",13),bd=9,width=10,bg="lightgrey",command=fetch_data)
    showall_btn.grid(row=0,column=4,padx=12,pady=2)
   #=========Database Frame=====#

    main_frame = tk.Frame(data_frame,bg="lightgrey",bd=13,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(data_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(data_frame,orient=tk.HORIZONTAL)

    ''' Name, Age, Gender, Birth Date, Status,Occupation, Contact '''
    barangay_table = ttk.Treeview(main_frame,columns=("ID No.","Name","Age","Gender","Birth Date","Status","Occupation","Contact"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("ID No.",text="ID No.")
    barangay_table.heading("Name",text="Name")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Birth Date",text="Birth Date")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Contact",text="Contact")

    barangay_table['show'] = 'headings'

    barangay_table.column("ID No.",width=100)
    barangay_table.column("Name",width=150)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Birth Date",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Contact",width=150)
    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)
login_win.mainloop()
