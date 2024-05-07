from tkinter import *
from utils import read_students_from_csv, show_student_info
from clustering import cluster_students, display_cluster_graph
from tkinter import ttk
import os

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

students = read_students_from_csv(os.path.join(os.path.dirname(__file__), 'SDF.csv'))

info_label = Label(frame3, text="", bg="gray", fg="black", justify=LEFT)
info_label.place(relx=0.5, rely=0.5, anchor=CENTER)

data = os.path.join(os.path.dirname(__file__), 'SDF.csv')
X = data[['Intell Ag Attention Span', 'Chem Attention Span', 'Ethics Attention Span', 'Info Assurance Attention Span']]
clusters = cluster_students(X)

# Create the dropdown box
student_var = StringVar(a)  # To store the selected student number
student_dropdown = ttk.Combobox(frame4_frame, textvariable=student_var, values=list(students.keys()))  # List of student numbers
student_dropdown.pack(pady=10)  # Add padding

# Function to handle selection changes
def handle_selection(event):
  selected_student = student_var.get()
  show_student_info(selected_student, students, info_label, frame5_frame)

# Bind the selection event to the dropdown box
student_dropdown.bind("<<ComboboxSelected>>", handle_selection)

a.mainloop()
