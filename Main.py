from tkinter import *
from utils import read_students_from_csv, show_student_info
from clustering import cluster_students, display_cluster_graph
import pandas as pd
from tkinter import ttk

# Add this function to main.py
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    win.geometry(f"{width}x{height}+{x}+{y}")

# Main program
a = Tk()
a.geometry("900x700")
a.resizable(0, 0)

center_window(a)

# Set a theme for the application
style = ttk.Style(a)
style.theme_use('clam')  # You can choose other themes like 'alt', 'default', 'classic'

frame3 = Frame(a, bg="#D3D3D3", highlightbackground="black", highlightthickness=1, bd=10, width=300, height=400)
frame3.place(x=0, y=0)

# Use ttk.Button for a styled button
button1 = ttk.Button(frame3, text="Cluster Graph General", command=lambda: display_cluster_graph(X, clusters))
button1.place(relx=0.5, y=20, anchor=N)

frame4_frame = Frame(a, bg="#E0FFFF")  # A light cyan background for a fresher look
frame4_frame.place(x=300, y=0, width=600, height=400, anchor=NW)

frame5_frame = Frame(a, bg="#E0FFFF", highlightthickness=1, bd=10)
frame5_frame.place(x=450, y=400, width=900, height=300, anchor=N)

label_attention = Label(frame5_frame, text="Attention Span:", bg="gray", fg="black")
label_attention.place(relx=0.5, rely=0.1, anchor=N)

students = read_students_from_csv('SDF.csv')

info_label = Label(frame3, text="", bg="gray", fg="black", justify=LEFT)
info_label.place(relx=0.5, rely=0.5, anchor=CENTER)

data = pd.read_csv('SDF.csv')
X = data[['Intell Ag Attention Span', 'Chem Attention Span', 'Ethics Attention Span', 'Info Assurance Attention Span']]
clusters = cluster_students(X)

# Create a scrollbar
scrollbar = Scrollbar(frame4_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a canvas to hold the frame
canvas = Canvas(frame4_frame, bg="#E0FFFF", highlightthickness=0, yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Configure the scrollbar to work with the canvas
scrollbar.config(command=canvas.yview)

# Create a new frame inside the canvas
inner_frame = Frame(canvas, bg="#E0FFFF")
canvas.create_window((0, 0), window=inner_frame, anchor=NW)  # Move this line after creating the canvas

# Update the canvas scroll region
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

canvas.create_window((0, 0), window=inner_frame, anchor=NW)

for i, student_no in enumerate(students.keys()):
    # Calculate row and column positions using integer division and modulo
    row = int(i / 6)  # Integer division for row (floor)
    col = i % 6  # Modulo for column (remainder)

    # Create circular button and button object
    canvas = Canvas(inner_frame, width=70, height=70, bg="light blue", highlightthickness=0)
    canvas.grid(row=row, column=col, padx=5, pady=5)
    canvas.create_oval(5, 5, 65, 65, fill="light green", outline="black")

    button = Button(canvas, text=student_no, bg="light green", fg="black", bd=0, relief="flat",
                    command=lambda no=student_no: show_student_info(no, students, info_label, frame5_frame))
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

a.mainloop()