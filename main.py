import tkinter as tk
from tkinter import ttk
import sqlite3
import cv2
from PIL import Image, ImageTk
from membership_form import create_membership_form
from search_form import create_search_form
from statistics_form import create_statistics_form
from help_screen import create_help_screen

def show_frame(frame):
    frame.tkraise()

# Style for buttons with hover effect
def on_enter(e):
    e.widget['background'] = 'lightblue'
    e.widget['font'] = ('Arial', 10, 'bold')

def on_leave(e):
    e.widget['background'] = 'gray'
    e.widget['font'] = ('Arial', 10)

# Connect to the database
conn = sqlite3.connect("gym_database.db")
cursor = conn.cursor()

# Main window configuration
root = tk.Tk()
root.title("City Gym Membership System")
root.geometry("1260x750")

# Pink background for the main window
root.configure(bg="pink")

# Main container
container = tk.Frame(root, bg="pink")
container.pack(fill="both", expand=True)

# Dictionary to hold frames
frames = {}

# Create and store screens, passing show_frame, frames, cursor, and conn as arguments
frames["main_menu"] = tk.Frame(container, bg="pink")
frames["main_menu"].grid(row=0, column=0, sticky="nsew")

frames["membership_form"] = create_membership_form(container, show_frame, frames, cursor, conn)
frames["search_form"] = create_search_form(container, show_frame, frames, cursor, conn)
frames["statistics_form"] = create_statistics_form(container, show_frame, frames, cursor)
frames["help_screen"] = create_help_screen(container, show_frame, frames)

# Configure the main menu screen
title = tk.Label(frames["main_menu"], text="City Gym Membership System", fg="#92000a", font=("Arial", 30,), bg="pink", bd=2, relief="solid", padx=50, pady=10)
title.pack(pady=20)

# Buttons to navigate to other screens
btn_membership_form = tk.Button(frames["main_menu"], text="Membership Form", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["membership_form"]))
btn_membership_form.pack(pady=10)
btn_membership_form.bind("<Enter>", on_enter)
btn_membership_form.bind("<Leave>", on_leave)

btn_search_member = tk.Button(frames["main_menu"], text="Search Member", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["search_form"]))
btn_search_member.pack(pady=10)
btn_search_member.bind("<Enter>", on_enter)
btn_search_member.bind("<Leave>", on_leave)

btn_statistics = tk.Button(frames["main_menu"], text="View Statistics", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["statistics_form"]))
btn_statistics.pack(pady=10)
btn_statistics.bind("<Enter>", on_enter)
btn_statistics.bind("<Leave>", on_leave)

btn_help = tk.Button(frames["main_menu"], text="Help", bg="gray", fg="white", font=("Arial", 10), command=lambda: show_frame(frames["help_screen"]))
btn_help.pack(pady=10)
btn_help.bind("<Enter>", on_enter)
btn_help.bind("<Leave>", on_leave)

# Video Frame
video_label = tk.Label(frames["main_menu"])
video_label.pack(pady=20)

def play_video():
    cap = cv2.VideoCapture('video1.mp4')

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, _ = frame.shape
            new_width = int(width * 0.7)  # Adjust width to 50% of original size
            new_height = int(height * 0.5)  # Adjust height to 40% of original size
            frame = cv2.resize(frame, (new_width, new_height))
            frame = ImageTk.PhotoImage(Image.fromarray(frame))
            video_label.config(image=frame)
            video_label.image = frame
            video_label.after(10, update_frame)  # 10 ms delay for next frame
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart the video from the first frame
            update_frame()

    update_frame()

play_video()

# Initially show the main menu screen
show_frame(frames["main_menu"])

# Start the application
root.mainloop()

# Close the database connection when the application exits
conn.close()
