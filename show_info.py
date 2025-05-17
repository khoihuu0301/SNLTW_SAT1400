from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import json
from tkinter import Menu



class Lop:
    def __init__(self, id, name, start_time, end_time, teachers, students):
        self.id = id
        self.name = name
        self.start_time = ""
        self.end_time = ""
        self.teachers = []
        self.students = []
window = Tk()
window.title("Chinh Sua Lop Hoc")
window.geometry("1920x1080")  # Set the size of the window
window.configure(background="light gray")

# Configure grid layout
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
with open("d:\\Teky\\sat_1400\\GithubRepo\\SNLTW_SAT1400\\LH.json", "r", encoding="utf-8") as file:
    class_list = [Lop(item["Id"], item["Ten"], item["Thoi gian bat dau"], item["Thoi gian ket thuc"], item["GV"], item["HS"]) for item in json.load(file)]

def hien_thi_thong_tin(id):
    lbl_id = Label(window, text="Class ID", font=("Arial", 35))
    lbl_id.grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_id = Text(window, width=50, height=2, font=("Arial", 35), name="class_id")  # Font size 35
    entry_id.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    entry_id.insert("1.0", class_list[class_list.index(next(item for item in class_list if item.id == id))].id)
    lbl_ten = Label(window, text="Class Name", font=("Arial", 35))
    lbl_ten.grid(row=4, column=0, padx=10, pady=10, sticky="e")
    entry_ten = Text(window, width=50, height=2, font=("Arial", 35), name="class_name")  # Font size 35
    entry_ten.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    entry_ten.insert("1.0", class_list[class_list.index(next(item for item in class_list if item.id == id))].name)

cb1 = Combobox(window, width=50, font=("Arial", 35), state="readonly")
cb1.grid(row=0, column=1, padx=10, pady=10, sticky="w")
cb1["values"] = [item.id for item in class_list]  # Populate the combobox with class IDs
cb1.bind("<<ComboboxSelected>>", lambda event: hien_thi_thong_tin(cb1.get()))  # Bind selection event
  # Load data
window.mainloop()