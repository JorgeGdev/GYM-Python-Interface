import tkinter as tk
from tkinter import ttk

def create_statistics_form(container, show_frame, frames, cursor):
    frame = tk.Frame(container, bg="pink")
    frame.grid(row=0, column=0, sticky="nsew")

    # Style for buttons with hover effect
    def on_enter(e):
        e.widget['background'] = 'lightblue'
        e.widget['font'] = ('Arial', 10, 'bold')

    def on_leave(e):
        e.widget['background'] = 'gray'
        e.widget['font'] = ('Arial', 10)
    
    # Statistics screen title
    title = tk.Label(frame, text="View Statistics", fg="#92000a", font=("Arial", 30), bg="pink", bd=2, relief="solid", padx=50, pady=10)
    title.pack(pady=20)

    # Frame to hold the Treeview and scrollbar
    tree_frame = tk.Frame(frame)
    tree_frame.pack(pady=10)

    # Scrollbar for Treeview
    tree_scroll = tk.Scrollbar(tree_frame)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Treeview for displaying statistics
    tree = ttk.Treeview(tree_frame, columns=("Category", "Count"), show='headings', height=10, yscrollcommand=tree_scroll.set)
    tree.heading("Category", text="Category")
    tree.heading("Count", text="Count")
    
    tree.column("Category", width=200, anchor="center")
    tree.column("Count", width=100, anchor="center")
    
    tree.pack()

    # Configure the scrollbar
    tree_scroll.config(command=tree.yview)

    # Function to display statistics
    def show_statistics():
        # Clear previous results
        for item in tree.get_children():
            tree.delete(item)
        
        # Total members
        cursor.execute("SELECT COUNT(*) FROM Memberships")
        total_members = cursor.fetchone()[0]
        tree.insert("", tk.END, values=("Total Members", total_members))

        # Members by membership type
        cursor.execute("SELECT Membership_Type, COUNT(*) FROM Memberships GROUP BY Membership_Type")
        membership_types = cursor.fetchall()
        for row in membership_types:
            tree.insert("", tk.END, values=(f"Type: {row[0]}", row[1]))

        # Members by extras
        cursor.execute("SELECT SUM(Extra_1), SUM(Extra_2), SUM(Extra_3), SUM(Extra_4) FROM Memberships")
        extras = cursor.fetchone()
        tree.insert("", tk.END, values=("24/7 Access", extras[0]))
        tree.insert("", tk.END, values=("Personal Trainer", extras[1]))
        tree.insert("", tk.END, values=("Diet Consultation", extras[2]))
        tree.insert("", tk.END, values=("Access to Fitness Videos", extras[3]))

        # Total members with direct debit selected
        cursor.execute("SELECT COUNT(*) FROM Memberships WHERE Direct_Debit = 1")
        direct_debit_count = cursor.fetchone()[0]
        tree.insert("", tk.END, values=("Direct Debit Payment", direct_debit_count))

    # Button to display statistics
    btn_show_stats = tk.Button(frame, text="Show Statistics", bg="gray", fg="white", font=("Arial", 10), command=show_statistics)
    btn_show_stats.pack(pady=10)
    btn_show_stats.bind("<Enter>", on_enter)
    btn_show_stats.bind("<Leave>", on_leave)

    # Button to return to the main menu
    btn_back = tk.Button(frame, text="Back to Main Menu", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["main_menu"]))
    btn_back.pack(pady=20)
    btn_back.bind("<Enter>", on_enter)
    btn_back.bind("<Leave>", on_leave)

    return frame
