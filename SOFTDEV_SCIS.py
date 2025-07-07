import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
import bcrypt

# Global references to windows
login_win = None
main_win = None
current_user = None
bg_image = None

# Create the login window
def open_login_window():
    global login_win, bg_image
    login_win = tk.Tk()
    login_win.geometry("1350x700+0+0")
    login_win.title("Barangay Dolores Senior Citizen Information System")

    # Load the image
    image = Image.open(r"C:\Users\Administrator\Downloads\brgy_dolores.png")
    bg_image = ImageTk.PhotoImage(image)

    # Create a label with the image as the background
    background_label = tk.Label(login_win, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = bg_image  # Keep a reference to the image

    # Title label
    title_label = tk.Label(
        login_win,
        text="Barangay Dolores Senior Citizen Information System",
        font=("Arial", 30, "bold"),
        foreground="white",
        border=12,
        relief=tk.GROOVE,
        bg="forestgreen"
    )
    title_label.pack(side=tk.TOP, fill=tk.X)

    # Frame for login fields
    frame = tk.Frame(login_win, bg='white')
    frame.place(relx=0.1, rely=0.5, anchor=tk.W)

    # Username and password fields
    username_label = tk.Label(frame, text="Username:", font=('Arial', 14, "bold"), bg='white')
    username_label.pack(pady=10)
    username_entry = tk.Entry(frame, bd=5, font=("Arial", 16))
    username_entry.pack(pady=10)

    password_label = tk.Label(frame, text="Password:", font=('Arial', 14, "bold"), bg='white')
    password_label.pack(pady=10)
    password_entry = tk.Entry(frame, show="*", bd=5, font=("Arial", 16))
    password_entry.pack(pady=10)

    def validate_login():
        global current_user
        username = username_entry.get()
        password = password_entry.get()

        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="senior_citizen_db"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            connection.close()

            if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
                current_user = username  # Save the logged-in user
                login_win.withdraw()  # Close the login window
                open_main_window()   # Open the main application window
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", str(e))

    # Login button
    login_button = tk.Button(frame, text="Login",
                             bd=7,
                             font=("Arial", 13),
                             width=14,
                             command=validate_login)
    login_button.pack(pady=10)

    # Register button
    def open_registration_window():
        register_win = tk.Toplevel()
        register_win.geometry("400x600")
        register_win.title("Register New User")

        tk.Label(register_win, text="Register New User", font=("Arial", 20, "bold")).pack(pady=10)

        # Registration fields
        tk.Label(register_win, text="Username:", font=("Arial", 14)).pack(pady=10)
        reg_username_entry = tk.Entry(register_win, font=("Arial", 14))
        reg_username_entry.pack(pady=5)

        tk.Label(register_win, text="Email:", font=("Arial", 14)).pack(pady=10)
        reg_email_entry = tk.Entry(register_win, font=("Arial", 14))
        reg_email_entry.pack(pady=5)

        tk.Label(register_win, text="Role:", font=("Arial", 14)).pack(pady=10)
        reg_role_combobox = ttk.Combobox(register_win, values=["Admin", "Staff", "User"], font=("Arial", 14), state="readonly")
        reg_role_combobox.pack(pady=5)
        reg_role_combobox.set("User")  # Default role

        tk.Label(register_win, text="Password:", font=("Arial", 14)).pack(pady=10)
        reg_password_entry = tk.Entry(register_win, show="*", font=("Arial", 14))
        reg_password_entry.pack(pady=5)

        tk.Label(register_win, text="Confirm Password:", font=("Arial", 14)).pack(pady=10)
        reg_confirm_password_entry = tk.Entry(register_win, show="*", font=("Arial", 14))
        reg_confirm_password_entry.pack(pady=5)

        # Register user
        def register_user():
            username = reg_username_entry.get()
            email = reg_email_entry.get()
            role = reg_role_combobox.get()
            password = reg_password_entry.get()
            confirm_password = reg_confirm_password_entry.get()

            if not username or not email or not password:
                messagebox.showerror("Error", "All fields are required")
                return
            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match")
                return

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            try:
                connection = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="senior_citizen_db"
                )
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO users (username, email, role, password) VALUES (%s, %s, %s, %s)",
                    (username, email, role, hashed_password.decode('utf-8'))
                )
                connection.commit()
                connection.close()
                messagebox.showinfo("Success", "User Registered Successfully")
                register_win.destroy()
            except pymysql.MySQLError as e:
                messagebox.showerror("Database Error", str(e))

        # Register button
        tk.Button(register_win, text="Register", font=("Arial", 14), command=register_user).pack(pady=20)

    # Register button on the login window
    register_button = tk.Button(frame, text="Register",
                                bd=7,
                                font=("Arial", 13),
                                width=14,
                                command=open_registration_window)
    register_button.pack(pady=10)

    login_win.mainloop()
    
# Function to open the main application window
def open_main_window():
    global main_win
    win = tk.Tk()
    win.geometry("1350x700+0+0")
    win.title("Barangay Dolores Senior Citizen Information System")
    title_label = tk.Label(
        win,
        text="Barangay Dolores Senior Citizen Information System",
        font=("Arial", 30, "bold"),
        border=12,
        relief=tk.GROOVE,
        bg="forestgreen"
    )
    title_label.pack(side=tk.TOP, fill=tk.X)

    detail_frame = tk.LabelFrame(win,text="Data Information",font=("Arial",15, "bold"),bd=12,relief=tk.GROOVE,bg="lightgreen")
    detail_frame.place(x=20,y=90,width=515,height=575)

    data_frame = tk.Frame(win,bd=12,bg="forestgreen",relief=tk.GROOVE)
    data_frame.place(x=570,y=90,width=740,height=575)

    #==============Variables========#
    osca_id = tk.StringVar()
    first_name = tk.StringVar()
    middle_name = tk.StringVar()
    last_name = tk.StringVar()
    birthdate = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    status = tk.StringVar()
    health_condition = tk.StringVar()
    sector = tk.StringVar()
    pensioner = tk.StringVar()
    educational_background = tk.StringVar()
    occupation = tk.StringVar()
    monthly_income = tk.StringVar()
    indigent = tk.StringVar()
    philhealth = tk.StringVar()
    contact_person = tk.StringVar()

    search_by = tk.StringVar()

    #==============Entry========#
    osca_id_lbl = tk.Label(detail_frame,text="OSCA ID ",font=('Arial',10,"bold"),bg="lightgreen")
    osca_id_lbl.grid(row=0,column=0,padx=2,pady=2)

    osca_id_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=osca_id)
    osca_id_ent.grid(row=0,column=1,padx=2,pady=2)

    first_name_lbl = tk.Label(detail_frame,text="FirstName ",font=('Arial',10,"bold"),bg="lightgreen")
    first_name_lbl.grid(row=1,column=0,padx=2,pady=2)

    first_name_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=first_name)
    first_name_ent.grid(row=1,column=1,padx=2,pady=2)

    middle_name_lbl = tk.Label(detail_frame,text="MiddleName ",font=('Arial',10,"bold"),bg="lightgreen")
    middle_name_lbl.grid(row=2,column=0,padx=2,pady=2)

    middle_name_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=middle_name)
    middle_name_ent.grid(row=2,column=1,padx=2,pady=2)

    last_name_lbl = tk.Label(detail_frame,text="LastName ",font=('Arial',10,"bold"),bg="lightgreen")
    last_name_lbl.grid(row=3,column=0,padx=2,pady=2)

    last_name_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=last_name)
    last_name_ent.grid(row=3,column=1,padx=2,pady=2)

    birthdate_lbl = tk.Label(detail_frame,text="Birthdate ",font=('Arial',10,"bold"),bg="lightgreen")
    birthdate_lbl.grid(row=4,column=0,padx=2,pady=2)

    birthdate_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=birthdate)
    birthdate_ent.grid(row=4,column=1,padx=2,pady=2)

    age_lbl = tk.Label(detail_frame,text="Age ",font=('Arial',10,"bold"),bg="lightgreen")
    age_lbl.grid(row=5,column=0,padx=2,pady=2)

    age_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=age)
    age_ent.grid(row=5,column=1,padx=2,pady=2)

    gender_lbl = tk.Label(detail_frame,text="Gender ",font=('Arial',10,"bold"),bg="lightgreen")
    gender_lbl.grid(row=6,column=0,padx=2,pady=2)

    gender_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=gender)
    gender_ent['values'] = ("Male","Female")
    gender_ent.grid(row=6,column=1,padx=2,pady=2)

    status_lbl = tk.Label(detail_frame,text="Status ",font=('Arial',10,"bold"),bg="lightgreen")
    status_lbl.grid(row=7,column=0,padx=0,pady=0)

    status_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=status)
    status_ent['values'] = ("Single","Married","Widow","Deceased")
    status_ent.grid(row=7,column=1,padx=2,pady=2)

    health_condition_lbl = tk.Label(detail_frame,text="Health Condition ",font=('Arial',10,"bold"),bg="lightgreen")
    health_condition_lbl.grid(row=8,column=0,padx=0,pady=0)

    health_condition_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=health_condition)
    health_condition_ent['values'] = ("Sick","Frail","Abandoned","Bedridden")
    health_condition_ent.grid(row=8,column=1,padx=2,pady=2)

    sector_lbl = tk.Label(detail_frame,text="Sector ",font=('Arial',10,"bold"),bg="lightgreen")
    sector_lbl.grid(row=9,column=0,padx=0,pady=0)

    sector_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=sector)
    sector_ent['values'] = ("4ps","PWD","Solo Parent","Family Head")
    sector_ent.grid(row=9,column=1,padx=2,pady=2)

    pensioner_lbl = tk.Label(detail_frame,text="Pensioner ",font=('Arial',10,"bold"),bg="lightgreen")
    pensioner_lbl.grid(row=10,column=0,padx=0,pady=0)

    pensioner_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=pensioner)
    pensioner_ent['values'] = ("SSS","GSIS","PVAO","Social Pension")
    pensioner_ent.grid(row=10,column=1,padx=2,pady=2)

    educational_background_lbl = tk.Label(detail_frame,text="Educational Background ",font=('Arial',10,"bold"),bg="lightgreen")
    educational_background_lbl.grid(row=11,column=0,padx=0,pady=0)

    educational_background_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=educational_background)
    educational_background_ent['values'] = ("Elementary","Elementary graduate","Highschool","Highschool graduate","College","College graduate","Vocational","Vocational graduate","None")
    educational_background_ent.grid(row=11,column=1,padx=2,pady=2)

    occupation_lbl = tk.Label(detail_frame,text="Occupation ",font=('Arial',10,"bold"),bg="lightgreen")
    occupation_lbl.grid(row=12,column=0,padx=2,pady=2)

    occupation_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=occupation)
    occupation_ent.grid(row=12,column=1,padx=2,pady=2)

    monthly_income_lbl = tk.Label(detail_frame,text="Monthly Income ",font=('Arial',10,"bold"),bg="lightgreen")
    monthly_income_lbl.grid(row=13,column=0,padx=2,pady=2)

    monthly_income_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=monthly_income)
    monthly_income_ent.grid(row=13,column=1,padx=2,pady=2)

    indigent_lbl = tk.Label(detail_frame,text="Indigent ",font=('Arial',10,"bold"),bg="lightgreen")
    indigent_lbl.grid(row=14,column=0,padx=0,pady=0)

    indigent_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=indigent)
    indigent_ent['values'] = ("Yes","No")
    indigent_ent.grid(row=14,column=1,padx=2,pady=2)

    philhealth_lbl = tk.Label(detail_frame,text="Philhealth ",font=('Arial',10,"bold"),bg="lightgreen")
    philhealth_lbl.grid(row=15,column=0,padx=0,pady=0)

    philhealth_ent = ttk.Combobox(detail_frame,font=('Arial',10),state="readonly",textvariable=philhealth)
    philhealth_ent['values'] = ("Yes","No")
    philhealth_ent.grid(row=15,column=1,padx=2,pady=2)

    contact_person_lbl = tk.Label(detail_frame,text="Contact Person ",font=('Arial',10,"bold"),bg="lightgreen")
    contact_person_lbl.grid(row=17,column=0,padx=2,pady=2)

    contact_person_ent = tk.Entry(detail_frame,bd=5,font=("arial",10),textvariable=contact_person)
    contact_person_ent.grid(row=17,column=1,padx=2,pady=2)


    #=======Function======#

    def fetch_data():
        try:
            # Connect to the database
            conn = pymysql.connect(host="localhost", user="root", password="", database="senior_citizen_db")
            curr = conn.cursor()
            # Fetch data from the 'data' table
            curr.execute("SELECT * FROM data")
            rows = curr.fetchall()
            
            # Populate the `barangay_table` widget
            if len(rows) != 0:
                barangay_table.delete(*barangay_table.get_children())
                for row in rows:
                    barangay_table.insert('', tk.END, values=row)
            
            conn.commit()  # Commit changes
        except Exception as e:
            messagebox.showerror("ERROR!", f"An error occurred: {e}")
        finally:
            conn.close()  # Ensure connection is closed


    def add_func():
        if osca_id.get() == "" or last_name.get() == "" or age.get() == "":
            messagebox.showerror("ERROR!","Please fill all the blank")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="senior_citizen_db")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (osca_id.get(),
                    first_name.get(),
                    middle_name.get(),
                    last_name.get(),
                    birthdate.get(),
                    age.get(),
                    gender.get(),
                    status.get(),
                    health_condition.get(),
                    sector.get(),
                    pensioner.get(),
                    educational_background.get(),
                    occupation.get(),
                    monthly_income.get(),
                    indigent.get(),
                    philhealth.get(),
                    contact_person.get()))
        conn.commit()
        conn.close()

        fetch_data()

    def get_cursor(event):
        ''' This function will fetch data of the selected row '''
        cursor_row = barangay_table.focus()
        content =  barangay_table.item(cursor_row)
        row = content['values']
        osca_id.set(row[0])
        first_name.set(row[1])
        middle_name.set(row[2])
        last_name.set(row[3])
        birthdate.set(row[4])
        age.set(row[5])
        gender.set(row[6])
        status.set(row[7])
        health_condition.set(row[8])
        sector.set(row[9])
        pensioner.set(row[10])
        educational_background.set(row[11])
        occupation.set(row[12])
        monthly_income.set(row[13])
        indigent.set(row[14])
        philhealth.set(row[15])
        contact_person.set(row[16])
        
    def clear():
        ''' This function will clear the entry boxes '''
        osca_id.set("")
        first_name.set("")
        middle_name.set("")
        last_name.set("")
        birthdate.set("")
        age.set("")
        gender.set("")
        status.set("")
        health_condition.set("")
        sector.set("")
        pensioner.set("")
        educational_background.set("")
        occupation.set("")
        monthly_income.set("")
        indigent.set("")
        philhealth.set("")
        contact_person.set("")
      

    def update_func():
        conn = pymysql.connect(host="localhost", user="root", password="", database="senior_citizen_db")
        curr = conn.cursor()
        query = """
            UPDATE data 
            SET first_name = %s, middle_name = %s, last_name = %s, birthdate = %s, age = %s, 
                gender = %s, status = %s, health_condition = %s, sector = %s, pensioner = %s, 
                educational_background = %s, occupation = %s, monthly_income = %s, 
                indigent = %s, philhealth = %s, contact_person = %s 
            WHERE osca_id = %s
        """
        values = (
            first_name.get(),
            middle_name.get(),
            last_name.get(),
            birthdate.get(),
            age.get(),
            gender.get(),
            status.get(),
            health_condition.get(),
            sector.get(),
            pensioner.get(),
            educational_background.get(),
            occupation.get(),
            monthly_income.get(),
            indigent.get(),
            philhealth.get(),
            contact_person.get(),
            osca_id.get()
        )
        curr.execute(query, values)
        conn.commit()
        curr.close()
        conn.close()
        fetch_data()
        clear()
        
    def delete_func():
        osca_id_to_delete = osca_id.get().strip()  # Assuming `osca_id` is the Entry widget for the OSCA ID

        if not osca_id_to_delete:
            messagebox.showerror("Error", "Please select a row to delete or enter a valid OSCA ID.")
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="senior_citizen_db")
            curr = conn.cursor()
            
            # Log the ID for debugging purposes (optional)
            print(f"Deleting OSCA ID: {osca_id_to_delete}")
            
            query = "DELETE FROM data WHERE osca_id = %s"
            curr.execute(query, (osca_id_to_delete,))
            
            # Check if any row was actually deleted
            if curr.rowcount == 0:
                messagebox.showerror("Error", f"No record found with OSCA ID: {osca_id_to_delete}")
            else:
                conn.commit()
                messagebox.showinfo('Success', 'The data was deleted successfully.')
                fetch_data()  # Refresh the data only if a record was deleted
                
        except pymysql.Error as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if curr:
                curr.close()
            if conn:
                conn.close()

    def search_func():
        search_value = search_ent.get()
        search_option = search_in.get()

        # Connect to the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="senior_citizen_db")
        cursor = conn.cursor()

        try:
            # Execute the search query based on the selected search option
            # OSCA ID","LastName","Gender","Age","Status","Occupation","Health Condition","Sector","Educational Background","Pensioner","Indigent","PhilHealth
            if search_option == "OSCA ID":
                query = "SELECT * FROM data WHERE osca_id = %s"
            elif search_option == "LastName":
                query = "SELECT * FROM data WHERE last_name LIKE %s"
                search_value = f"%{search_value}%"
            elif search_option == "Gender":
                query = "SELECT * FROM data WHERE gender = %s"
            elif search_option == "Status":
                query = "SELECT * FROM data WHERE status = %s"
            elif search_option == "Occupation":
                query = "SELECT * FROM data WHERE occupation = %s"
            elif search_option == "Health Condition":
                query = "SELECT * FROM data WHERE health_condition = %s"
            elif search_option == "Sector":
                query = "SELECT * FROM data WHERE sector = %s"
            elif search_option == "Educational Background":
                query = "SELECT * FROM data WHERE educational_background = %s"
            elif search_option == "Pensioner":
                query = "SELECT * FROM data WHERE pensioner = %s"
            elif search_option == "Indigent":
                query = "SELECT * FROM data WHERE indigent = %s"
            elif search_option == "PhilHealth":
                query = "SELECT * FROM data WHERE philhealth = %s"
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
        conn = pymysql.connect(host="localhost", user="root", password="", database="senior_citizen_db")
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

    #=====Settings=====#
    def open_settings():
        settings_window = tk.Toplevel()
        settings_window.title("Settings")
        settings_window.geometry("400x300")

        tk.Label(settings_window, text="Settings", font=("Arial", 14, "bold")).pack(pady=10)

        # Frame to hold user details
        details_frame = tk.Frame(settings_window, bg="white", bd=5, relief=tk.RIDGE)
        details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Fetch user data from the database
        try:
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="senior_citizen_db"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT username, email, role FROM users WHERE username = %s", (current_user,))
            user_data = cursor.fetchone()
            connection.close()

            if user_data:
                username, email, role = user_data

                # Display user credentials
                tk.Label(details_frame, text=f"Username: {username}", font=("Arial", 12), bg="white").pack(anchor="w", pady=5)
                tk.Label(details_frame, text=f"Email: {email}", font=("Arial", 12), bg="white").pack(anchor="w", pady=5)
                tk.Label(details_frame, text=f"Role: {role}", font=("Arial", 12), bg="white").pack(anchor="w", pady=5)
            else:
                tk.Label(details_frame, text="User details not found.", font=("Arial", 12), bg="white", fg="red").pack(pady=10)

        except pymysql.MySQLError as e:
            tk.Label(details_frame, text=f"Database Error: {e}", font=("Arial", 12), bg="white", fg="red").pack(pady=10)


    #========Button Frame=======#

    btn_frame = tk.Frame(detail_frame, bg="lightblue", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=340, y=200, width=140, height=200)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("Arial", 10, "bold" ), width=10,command=add_func)
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("Arial", 10, "bold"), width=10,command=update_func)
    update_btn.grid(row=1, column=0, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("Arial", 10, "bold"), width=10,command=delete_func)
    delete_btn.grid(row=2, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("Arial", 10, "bold"), width=10,command=clear)
    clear_btn.grid(row=3, column=0, padx=2, pady=2)

    #======= Total Frame=======#
    btn_frame = tk.Frame(detail_frame, bg="lightblue", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=340, y=400, width=140, height=100)

    total_btn = tk.Button(btn_frame,text=f"Total data: ", bd=7, font=('Arial',10, "bold"), width=10, bg="lightgrey",command=total_func)
    total_btn.grid(row=4,column=0,padx=2,pady=2)

    total_lbl = tk.Label(btn_frame,text="",font=('Arial',10, "bold"),bg="white")
    total_lbl.grid(row=5,column=0,padx=2,pady=2)

    #====== Search Frame  ======#
    search_frame = tk.Frame(data_frame, bg="lightblue", bd=10, relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP, fill=tk.X)

    search_lbl = tk.Label(search_frame, text="Search ", bg="lightblue", font=("Arial", 10, "bold"))
    search_lbl.grid(row=0, column=0, padx=12, pady=2)

    search_in = ttk.Combobox(search_frame, width=10, font=("Arial", 10), state="readonly", textvariable=search_by)
    search_in['values'] = ("OSCA ID", "LastName", "Gender", "Age", "Status", "Occupation", "Health Condition", 
                           "Sector", "Educational Background", "Pensioner", "Indigent", "PhilHealth")
    search_in.grid(row=0, column=1, padx=12, pady=2)

    search_ent = tk.Entry(search_frame, bd=5, font=("arial", 10))
    search_ent.grid(row=0, column=2, padx=12, pady=4)

    search_btn = tk.Button(search_frame, text="Search", font=("Arial", 8), bd=9, width=8, bg="lightgrey", command=search_func)
    search_btn.grid(row=0, column=3, padx=12, pady=2)

    showall_btn = tk.Button(search_frame, text="Show All", font=("Arial", 8), bd=9, width=8, bg="lightgrey", command=fetch_data)
    showall_btn.grid(row=0, column=4, padx=12, pady=2)

    # Add the Settings button
    settings_button = tk.Button(search_frame, text="Settings", font=("Arial", 8), bd=9, width=8, bg="lightgrey", command=open_settings)
    settings_button.grid(row=0, column=5, padx=12, pady=2)


    #=======Database Frame======#
    main_frame = tk.Frame(data_frame,bg="forestgreen",bd=13,relief=tk.GROOVE) 
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

    ''' OSCA ID, FirstName, MiddleName, LastName, BirthDate, Age, Gender, Status, Health Condition, Sector, Pensioner, Educational Background, Occupation, Monthly Income, Indigent, Philhealth, Contact Person '''
    barangay_table = ttk.Treeview(main_frame,columns=("OSCA ID",
                                                       "FirstName",
                                                       "MiddleName",
                                                       "LastName",
                                                       "BirthDate",
                                                       "Age",
                                                       "Gender",
                                                       "Status",
                                                       "Health Condition",
                                                       "Sector",
                                                       "Pensioner",
                                                       "Educational Background",
                                                       "Occupation",
                                                       "Monthly Income",
                                                       "Indigent",
                                                       "Philhealth",
                                                       "Contact Person"),
                                    yscrollcommand=y_scroll.set,
                                    xscrollcommand=x_scroll.set)
    y_scroll.config(command=barangay_table.yview)
    x_scroll.config(command=barangay_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    barangay_table.heading("OSCA ID",text="OSCA ID")
    barangay_table.heading("FirstName",text="FirstName")
    barangay_table.heading("MiddleName",text="MiddleName")
    barangay_table.heading("LastName",text="LastName")
    barangay_table.heading("BirthDate",text="BirthDate")
    barangay_table.heading("Age",text="Age")
    barangay_table.heading("Gender",text="Gender")
    barangay_table.heading("Status",text="Status")
    barangay_table.heading("Health Condition",text="Health Condition")
    barangay_table.heading("Sector",text="Sector")
    barangay_table.heading("Pensioner",text="Pensioner")
    barangay_table.heading("Educational Background",text="Educational Background")
    barangay_table.heading("Occupation",text="Occupation")
    barangay_table.heading("Monthly Income",text="Monthly Income")
    barangay_table.heading("Indigent",text="Indigent")
    barangay_table.heading("Philhealth",text="Philhealth")
    barangay_table.heading("Contact Person",text="Contact Person")

    barangay_table['show'] = 'headings'

    barangay_table.column("OSCA ID",width=100)
    barangay_table.column("FirstName",width=150)
    barangay_table.column("MiddleName",width=150)
    barangay_table.column("LastName",width=150)
    barangay_table.column("BirthDate",width=100)
    barangay_table.column("Age",width=100)
    barangay_table.column("Gender",width=100)
    barangay_table.column("Status",width=100)
    barangay_table.column("Health Condition",width=100)
    barangay_table.column("Sector",width=100)
    barangay_table.column("Pensioner",width=100)
    barangay_table.column("Educational Background",width=150)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Educational Background",width=100)
    barangay_table.column("Occupation",width=100)
    barangay_table.column("Monthly Income",width=100)
    barangay_table.column("Indigent",width=100)
    barangay_table.column("Philhealth",width=100)
    barangay_table.column("Contact Person",width=150)

    barangay_table.pack(fill=tk.BOTH,expand=True)

    fetch_data()

    barangay_table.bind("<ButtonRelease-1>",get_cursor)

    win.mainloop()
    
open_login_window()

