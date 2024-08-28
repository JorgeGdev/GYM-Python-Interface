import tkinter as tk
from tkinter import ttk

def create_help_screen(container, show_frame, frames):
    frame = tk.Frame(container, bg="pink")
    frame.grid(row=0, column=0, sticky="nsew")

    # Style for buttons with hover effect
    def on_enter(e):
        e.widget['background'] = 'lightblue'
        e.widget['font'] = ('Arial', 10, 'bold')

    def on_leave(e):
        e.widget['background'] = 'gray'
        e.widget['font'] = ('Arial', 10)
    
    # Help screen title
    title = tk.Label(frame, text="General Functions of the Application", fg="#92000a", font=("Arial", 25), bg="pink", bd=2, relief="solid",padx=50, pady=10)
    title.pack(pady=10)
    
    # Help text
    help_text = tk.Label(frame, text=(
        "Description:\n\n"
        "The City Gym Membership System is designed to manage gym memberships efficiently. "
        "The system offers various features including member registration, search, statistics viewing, and a user guide.\n\n"
        "Main Features:\n\n"
        "1. Membership Form: Register new members, input their details, and choose membership options.\n"
        "2. Member Search: Search for members by ID, last name, membership type, or a combination. You can also delete members.\n"
        "3. View Statistics: Display statistics like total members, membership types, and extra services selected.\n"
        "4. Help Screen: Provides a guide on how to use the system.\n\n"
        "Using the System:\n\n"
        "- Navigate through the Main Menu to access different features.\n"
        "- Register members through the Membership Form.\n"
        "- Search and manage members in the Search Member screen.\n"
        "- View overall gym statistics in the View Statistics screen.\n"
        "- Access this help guide anytime via the Help option.\n\n"
        "For more detailed instructions, ask to you Trainer Manager"
    ), wraplength=700, pady=10, padx=20, fg="#92000a", font=("Arial", 14), bg="pink", bd=2, relief="solid")
    help_text.pack(pady=20)
    
    # Button to return to the main menu
    btn_back = tk.Button(frame, text="Back to Main Menu", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["main_menu"]))
    btn_back.pack(pady=20)
    btn_back.bind("<Enter>", on_enter)
    btn_back.bind("<Leave>", on_leave)

    return frame
