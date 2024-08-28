import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_search_form(container, show_frame, frames, cursor, conn):
    frame = tk.Frame(container, bg="pink")
    frame.grid(row=0, column=0, sticky="nsew")

    # Style for buttons with hover effect
    def on_enter(e):
        e.widget['background'] = 'lightblue'
        e.widget['font'] = ('Arial', 10, 'bold')

    def on_leave(e):
        e.widget['background'] = 'gray'
        e.widget['font'] = ('Arial', 10)

    # Search form title
    title = tk.Label(frame, text="Search Member", fg="#92000a", font=("Arial", 30), bg="pink", bd=2, relief="solid", padx=50, pady=10)
    title.pack(pady=20)
    
    # Member ID Search
    tk.Label(frame, text="Search by Member ID:", bg="pink", bd=2, relief="solid").pack(pady=5)
    id_entry = tk.Entry(frame)
    id_entry.pack(pady=5)

    # Last Name Search
    tk.Label(frame, text="Search by Last Name:", bg="pink", bd=2, relief="solid").pack(pady=5)
    last_name_entry = tk.Entry(frame)
    last_name_entry.pack(pady=5)

    # Membership Type Search
    tk.Label(frame, text="Search by Membership Type:", bg="pink", bd=2, relief="solid").pack(pady=5)
    membership_type_combo = ttk.Combobox(frame, values=["Basic", "Regular", "Premium"])
    membership_type_combo.pack(pady=5)

    # Result area
    tree_frame = tk.Frame(frame)
    tree_frame.pack(padx=10, pady=20)

    tree_scroll = tk.Scrollbar(tree_frame)
    tree_scroll.pack(side="right", fill="y")

    tree = ttk.Treeview(tree_frame, columns=("ID", "First Name", "Last Name", "Membership Type", "Mobile", "Address"), show='headings', height=10, yscrollcommand=tree_scroll.set)
    tree.pack(padx=10, pady=10)

    tree_scroll.config(command=tree.yview)

    tree.heading("ID", text="ID")
    tree.heading("First Name", text="First Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Membership Type", text="Membership Type")
    tree.heading("Mobile", text="Mobile")
    tree.heading("Address", text="Address")

    # Function to search members in the database
    def search_member():
        tree.delete(*tree.get_children())  # Clear previous results
        member_id = id_entry.get()
        last_name = last_name_entry.get()
        membership_type = membership_type_combo.get()

        query = "SELECT * FROM Memberships WHERE 1=1"
        params = []

        if member_id:
            query += " AND MemberID = ?"
            params.append(member_id)
        
        if last_name:
            query += " AND Last_Name LIKE ?"
            params.append(f"%{last_name}%")

        if membership_type:
            query += " AND Membership_Type = ?"
            params.append(membership_type)

        cursor.execute(query, params)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("No Results", "No members found matching your criteria.")

    # Function to delete the selected member
    def delete_member():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a member to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected member?")
        if confirm:
            member_id = tree.item(selected_item)["values"][0]
            cursor.execute("DELETE FROM Memberships WHERE MemberID = ?", (member_id,))
            conn.commit()
            tree.delete(selected_item)
            messagebox.showinfo("Deleted", f"Member ID {member_id} has been deleted successfully.")

    # Search button
    btn_search = tk.Button(frame, text="Search", bg="gray", fg="white", font=("Arial", 10), command=search_member)
    btn_search.pack(pady=10)
    btn_search.bind("<Enter>", on_enter)
    btn_search.bind("<Leave>", on_leave)

    # Delete button
    btn_delete = tk.Button(frame, text="Delete Member", bg="gray", fg="white", font=("Arial", 10), command=delete_member)
    btn_delete.pack(pady=10)
    btn_delete.bind("<Enter>", on_enter)
    btn_delete.bind("<Leave>", on_leave)

    # Button to return to the main menu
    btn_back = tk.Button(frame, text="Back to Main Menu", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["main_menu"]))
    btn_back.pack(pady=20)
    btn_back.bind("<Enter>", on_enter)
    btn_back.bind("<Leave>", on_leave)

    return frame
