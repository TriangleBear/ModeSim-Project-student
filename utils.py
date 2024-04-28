import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_students_from_csv(filename):
    students = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_info = {
                'age': row['Age'],
                'gender': row['Gender'],
                'year_level': row['Year level'],
                'status': row['Status']
            }
            students[row['Student no.']] = student_info
    return students

# Add this function to utils.py
def show_student_info(student_no, students, info_label, frame5_frame):
    """
    Display the information and attention span plot for a given student.

    Parameters:
    student_no (int): The student number.
    students (dict): The dictionary of student information.
    info_label (Label): The label to display student information.
    frame5_frame (Frame): The frame to display the attention span plot.

    Returns:
    None
    """
    info = students[student_no]
    info_text = f"Student No.: {student_no}\nAge: {info['age']}\nGender: {info['gender']}\nYear Level: {info['year_level']}\nStatus: {info['status']}"
    info_label.config(text=info_text)

    # Load the data from the CSV file
    data = pd.read_csv('SDF.csv')

    # Filter data for the selected student
    student_data = data[data['Student no.'] == student_no]

    # Extract attention span for each subject
    attention_span_columns = ['Intell Ag Attention Span', 'Chem Attention Span', 'Ethics Attention Span', 'Info Assurance Attention Span']
    attention_span_data = student_data[attention_span_columns].squeeze().values

    # Create the plot with a smaller size
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.bar(attention_span_columns, attention_span_data, color='skyblue')
    ax.set_xlabel('Subjects')
    ax.set_ylabel('Attention Span')
    ax.set_title(f'Attention Span for Student {student_no}')

    # Rotate x-axis labels to prevent overlapping
    plt.xticks(rotation=5, fontsize=6)

    # Clear previous plot from frame5
    for widget in frame5_frame.winfo_children():
        widget.destroy()

    # Embed the plot into frame5
    canvas = FigureCanvasTkAgg(fig, master=frame5_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=TOP, fill=BOTH, expand=True)