from tkinter import *
from utils import read_students_from_csv, show_student_info
from clustering import cluster_students, display_cluster_graph
import pandas as pd

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

frame3 = Frame(a, bg="gray", highlightbackground="black", highlightthickness=1, bd=10, width=300, height=700)
frame3.place(x=0, y=0)

button1 = Button(frame3, text="Cluster Graph General", bg="white", fg="black", command=lambda: display_cluster_graph(X, clusters))
button1.place(relx=0.5, y=20, anchor=N)

frame4_frame = Frame(a, bg="light blue")
frame4_frame.place(x=300, y=0, width=600, height=400, anchor=NW)

frame5_frame = Frame(a, bg="light blue", highlightthickness=1, bd=10)
frame5_frame.place(x=300, y=400, width=600, height=300, anchor=NW)

label_attention = Label(frame5_frame, text="Attention Span:", bg="gray", fg="black")
label_attention.place(relx=0.5, rely=0.1, anchor=N)

students = read_students_from_csv('SDF.csv')

info_label = Label(frame3, text="", bg="gray", fg="black", justify=LEFT)
info_label.place(relx=0.5, rely=0.5, anchor=CENTER)

data = pd.read_csv('SDF.csv')
X = data[['Intell Ag Attention Span', 'Chem Attention Span', 'Ethics Attention Span', 'Info Assurance Attention Span']]
clusters = cluster_students(X)

for i, student_no in enumerate(students.keys()):
    row = i // 6
    col = i % 6

    # Create circular button
    canvas = Canvas(frame4_frame, width=70, height=70, bg="light blue", highlightthickness=0)
    canvas.grid(row=row, column=col, padx=5, pady=5)
    canvas.create_oval(5, 5, 65, 65, fill="light green", outline="black")

    button = Button(canvas, text=student_no, bg="light green", fg="black", bd=0, relief="flat",
                    command=lambda no=student_no: show_student_info(no, students, info_label, frame5_frame))
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

a.mainloop()