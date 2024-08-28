import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_membership_form(container, show_frame, frames, cursor, conn):
    frame = tk.Frame(container, bg="pink")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Make columns responsive
    for i in range(4):
        frame.grid_columnconfigure(i, weight=1)

    # Style for buttons with hover effect
    def on_enter(e):
        e.widget['background'] = 'lightblue'
        e.widget['font'] = ('Arial', 10, 'bold')
    
    def on_leave(e):
        e.widget['background'] = 'gray'
        e.widget['font'] = ('Arial', 10)

    # Function to update the background of the selected radiobutton
    def update_radiobutton_bg(selected_button, buttons):
        for button in buttons:
            if button == selected_button:
                button.config(bg="gray")
            else:
                button.config(bg="pink")

    # Function to update the background of the selected checkbutton
    def update_checkbutton_bg():
        checkbuttons = [check_24_7, check_trainer, check_diet, check_videos]
        for cb in checkbuttons:
            if cb.var.get():
                cb.config(bg="gray")
            else:
                cb.config(bg="pink")

    # Membership form title
    title = tk.Label(frame, text="Membership Form", fg="#92000a", font=("Arial", 30), bg="pink", bd=2, relief="solid", padx=50, pady=10)
    title.grid(row=0, column=0, columnspan=4, pady=10)

    # Left column
    tk.Label(frame, text="First Name:", bg="pink", bd=2, relief="solid").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    first_name_entry = tk.Entry(frame)
    first_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    tk.Label(frame, text="Last Name:", bg="pink", bd=2, relief="solid").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    last_name_entry = tk.Entry(frame)
    last_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    tk.Label(frame, text="Address:", bg="pink", bd=2, relief="solid").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    address_entry = tk.Entry(frame)
    address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    tk.Label(frame, text="Mobile Number:", bg="pink", bd=2, relief="solid").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    mobile_entry = tk.Entry(frame)
    mobile_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    # Right column
    tk.Label(frame, text="Membership Type:", bg="pink", bd=2, relief="solid").grid(row=1, column=2, padx=10, pady=5, sticky="e")
    membership_type = tk.StringVar()
    radiobutton_basic = tk.Radiobutton(frame, text="Basic", variable=membership_type, value="Basic", bg="pink", bd=2, relief="solid")
    radiobutton_basic.grid(row=1, column=3, padx=10, pady=5, sticky="w")
    radiobutton_regular = tk.Radiobutton(frame, text="Regular", variable=membership_type, value="Regular", bg="pink", bd=2, relief="solid")
    radiobutton_regular.grid(row=2, column=3, padx=10, pady=5, sticky="w")
    radiobutton_premium = tk.Radiobutton(frame, text="Premium", variable=membership_type, value="Premium", bg="pink", bd=2, relief="solid")
    radiobutton_premium.grid(row=3, column=3, padx=10, pady=5, sticky="w")

    # List of all radiobuttons for Membership Type
    radiobuttons_membership_type = [radiobutton_basic, radiobutton_regular, radiobutton_premium]

    # Set command to change background on selection for Membership Type
    radiobutton_basic.config(command=lambda: update_radiobutton_bg(radiobutton_basic, radiobuttons_membership_type))
    radiobutton_regular.config(command=lambda: update_radiobutton_bg(radiobutton_regular, radiobuttons_membership_type))
    radiobutton_premium.config(command=lambda: update_radiobutton_bg(radiobutton_premium, radiobuttons_membership_type))

    tk.Label(frame, text="Membership Duration:", bg="pink", bd=2, relief="solid").grid(row=4, column=2, padx=10, pady=5, sticky="e")
    membership_duration = tk.StringVar()
    radiobutton_3months = tk.Radiobutton(frame, text="3 Months", variable=membership_duration, value="3 Months", bg="pink", bd=2, relief="solid")
    radiobutton_3months.grid(row=4, column=3, padx=10, pady=5, sticky="w")
    radiobutton_12months = tk.Radiobutton(frame, text="12 Months", variable=membership_duration, value="12 Months", bg="pink", bd=2, relief="solid")
    radiobutton_12months.grid(row=5, column=3, padx=10, pady=5, sticky="w")
    radiobutton_24months = tk.Radiobutton(frame, text="24 Months", variable=membership_duration, value="24 Months", bg="pink", bd=2, relief="solid")
    radiobutton_24months.grid(row=6, column=3, padx=10, pady=5, sticky="w")

    # List of all radiobuttons for Membership Duration
    radiobuttons_membership_duration = [radiobutton_3months, radiobutton_12months, radiobutton_24months]

    # Set command to change background on selection for Membership Duration
    radiobutton_3months.config(command=lambda: update_radiobutton_bg(radiobutton_3months, radiobuttons_membership_duration))
    radiobutton_12months.config(command=lambda: update_radiobutton_bg(radiobutton_12months, radiobuttons_membership_duration))
    radiobutton_24months.config(command=lambda: update_radiobutton_bg(radiobutton_24months, radiobuttons_membership_duration))

    tk.Label(frame, text="Direct Debit Payment:", bg="pink", bd=2, relief="solid").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    direct_debit = tk.BooleanVar()
    radiobutton_yes = tk.Radiobutton(frame, text="Yes", variable=direct_debit, value=True, bg="pink", bd=2, relief="solid")
    radiobutton_yes.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    radiobutton_no = tk.Radiobutton(frame, text="No", variable=direct_debit, value=False, bg="pink", bd=2, relief="solid")
    radiobutton_no.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    # List of all radiobuttons for Direct Debit Payment
    radiobuttons_direct_debit = [radiobutton_yes, radiobutton_no]

    # Set command to change background on selection for Direct Debit Payment
    radiobutton_yes.config(command=lambda: update_radiobutton_bg(radiobutton_yes, radiobuttons_direct_debit))
    radiobutton_no.config(command=lambda: update_radiobutton_bg(radiobutton_no, radiobuttons_direct_debit))

    tk.Label(frame, text="Payment Frequency:", bg="pink", bd=2, relief="solid").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    payment_frequency = tk.StringVar()
    radiobutton_weekly = tk.Radiobutton(frame, text="Weekly", variable=payment_frequency, value="Weekly", bg="pink", bd=2, relief="solid")
    radiobutton_weekly.grid(row=7, column=1, padx=10, pady=5, sticky="w")
    radiobutton_monthly = tk.Radiobutton(frame, text="Monthly", variable=payment_frequency, value="Monthly", bg="pink", bd=2, relief="solid")
    radiobutton_monthly.grid(row=8, column=1, padx=10, pady=5, sticky="w")

    # List of all radiobuttons for Payment Frequency
    radiobuttons_payment_frequency = [radiobutton_weekly, radiobutton_monthly]

    # Set command to change background on selection for Payment Frequency
    radiobutton_weekly.config(command=lambda: update_radiobutton_bg(radiobutton_weekly, radiobuttons_payment_frequency))
    radiobutton_monthly.config(command=lambda: update_radiobutton_bg(radiobutton_monthly, radiobuttons_payment_frequency))

    tk.Label(frame, text="Extras:", bg="pink", bd=2, relief="solid").grid(row=8, column=2, padx=10, pady=5, sticky="e")
    extra_1 = tk.BooleanVar()
    check_24_7 = tk.Checkbutton(frame, text="24/7 Access", variable=extra_1, bg="pink", bd=2, relief="solid", command=update_checkbutton_bg)
    check_24_7.grid(row=8, column=3, padx=10, pady=5, sticky="w")

    extra_2 = tk.BooleanVar()
    check_trainer = tk.Checkbutton(frame, text="Personal Trainer", variable=extra_2, bg="pink", bd=2, relief="solid", command=update_checkbutton_bg)
    check_trainer.grid(row=9, column=3, padx=10, pady=5, sticky="w")

    extra_3 = tk.BooleanVar()
    check_diet = tk.Checkbutton(frame, text="Diet Consultation", variable=extra_3, bg="pink", bd=2, relief="solid", command=update_checkbutton_bg)
    check_diet.grid(row=10, column=3, padx=10, pady=5, sticky="w")

    extra_4 = tk.BooleanVar()
    check_videos = tk.Checkbutton(frame, text="Access to Fitness Videos", variable=extra_4, bg="pink", bd=2, relief="solid", command=update_checkbutton_bg)
    check_videos.grid(row=11, column=3, padx=10, pady=5, sticky="w")

    # Function to insert a new member into the database
    def insert_member():
        cursor.execute('''INSERT INTO Memberships (First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (first_name_entry.get(), last_name_entry.get(), address_entry.get(), mobile_entry.get(),
                        membership_type.get(), membership_duration.get(), direct_debit.get(),
                        extra_1.get(), extra_2.get(), extra_3.get(), extra_4.get(), payment_frequency.get()))
        conn.commit()
        # Clear fields after insertion
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        mobile_entry.delete(0, tk.END)
        membership_type.set(None)
        membership_duration.set(None)
        direct_debit.set(False)
        payment_frequency.set(None)
        extra_1.set(False)
        extra_2.set(False)
        extra_3.set(False)
        extra_4.set(False)
        update_radiobutton_bg(None, radiobuttons_membership_type)  # Reset the radiobutton background for Membership Type
        update_radiobutton_bg(None, radiobuttons_membership_duration)  # Reset the radiobutton background for Membership Duration
        update_radiobutton_bg(None, radiobuttons_direct_debit)  # Reset the radiobutton background for Direct Debit Payment
        update_radiobutton_bg(None, radiobuttons_payment_frequency)  # Reset the radiobutton background for Payment Frequency
        update_checkbutton_bg()  # Reset the checkbutton background
        messagebox.showinfo("Success", "Member added successfully!")

    # Button to insert the member
    btn_insert = tk.Button(frame, text="Add Member", bg="gray", fg="white", font=("Arial", 10), command=insert_member)
    btn_insert.grid(row=12, column=2, columnspan=2, pady=20, padx=10, sticky="e")

    # Button to return to the main menu
    btn_back = tk.Button(frame, text="Back to Main Menu", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["main_menu"]))
    btn_back.grid(row=12, column=0, columnspan=2, pady=20, padx=10, sticky="w")

    # Apply hover style to the buttons
    btn_insert.bind("<Enter>", on_enter)
    btn_insert.bind("<Leave>", on_leave)
    btn_back.bind("<Enter>", on_enter)
    btn_back.bind("<Leave>", on_leave)

    return frame
