from email.charset import add_alias
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import json
import os

window = Tk()
window.title("Đăng Ký Tài khoản")
window.geometry("1500x800")  # Tăng kích thước cửa sổ
window.configure(background="light gray")

class Lop:
    def __init__(self, id, name, time_start, end_time, teachers, students):
        self.id = id
        self.name = name
        self.time_start = time_start
        self.end_time = end_time
        self.teachers = teachers
        self.students = students

    def __str__(self):
        info = (
            f"\033[96mId: {self.id}\n"
            f"Name: {self.name}\n"
            f"Time start: {self.time_start}\n"
            f"Time end: {self.end_time}\n"
            f"GV: {', '.join(self.teachers)}\n"
            f"HS: {', '.join(self.students)}\033[0m"
        )
        return info

    @staticmethod
    def load_all(filepath):
        classes = []
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    for c in data:
                        classes.append(
                            Lop(
                                c.get("Id", ""),
                                c.get("Name", ""),
                                c.get("Time start", ""),
                                c.get("Time end", ""),
                                c.get("GV", []),
                                c.get("HS", []),
                            )
                        )
            except Exception:
                messagebox.showerror("Lỗi", f"Tệp {filepath} không đúng định dạng JSON!")
        else:
            messagebox.showerror("Lỗi", f"Tệp {filepath} không tồn tại!")
        return classes

    @staticmethod
    def save_all(classes, filepath):
        data = []
        for c in classes:
            data.append({
                "Id": c.id,
                "Name": c.name,
                "Time start": c.time_start,
                "Time end": c.end_time,
                "GV": c.teachers,
                "HS": c.students
            })
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def add_class(new_class, filepath):
        classes = Lop.load_all(filepath)
        classes.append(new_class)
        Lop.save_all(classes, filepath)

    @staticmethod
    def delete_class(class_id, filepath):
        classes = Lop.load_all(filepath)
        new_classes = [c for c in classes if str(c.id) != str(class_id)]
        if len(new_classes) == len(classes):
            return False
        Lop.save_all(new_classes, filepath)
        classes=new_classes
        return True

    @staticmethod
    def open_add_class_window():
        add_window = Toplevel(window)
        add_window.title("Thêm lớp học mới")
        add_window.geometry("900x600")  # Tăng kích thước cửa sổ thêm lớp
        add_window.configure(background="light gray")
        Label(add_window, text="Add class", font="Times 20", bg="light gray").grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

        frame = Frame(add_window, bg="light gray")
        frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        Label(frame, text="Id", bg="light gray", font="Times 15").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        entry1 = Entry(frame, width=40, font=("Arial", 15))
        entry1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        Label(frame, text="Name", bg="light gray", font="Times 15").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        entry2 = Entry(frame, width=40, font=("Arial", 15))
        entry2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        Label(frame, text="Time start", bg="light gray", font="Times 15").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        entry3 = Entry(frame, width=40, font=("Arial", 15))
        entry3.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        Label(frame, text="Time end", bg="light gray", font="Times 15").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        entry4 = Entry(frame, width=40, font=("Arial", 15))
        entry4.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        Label(frame, text="GV", bg="light gray", font="Times 15").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        entry5 = Entry(frame, width=40, font=("Arial", 15))
        entry5.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        Label(frame, text="HS", bg="light gray", font="Times 15").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        entry6 = Entry(frame, width=40, font=("Arial", 15))
        entry6.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        def add_to_json():
            id_val = entry1.get().strip()
            name_val = entry2.get().strip()
            time_start_val = entry3.get().strip()
            time_end_val = entry4.get().strip()
            gv_val = entry5.get().strip()
            hs_val = entry6.get().strip()

            if not id_val or not name_val or not time_start_val or not time_end_val or not gv_val or not hs_val:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                return
            if not id_val.isdigit():
                messagebox.showerror("Lỗi", "Id phải là số!")
                return

            new_class = Lop(
                id_val,
                name_val,
                time_start_val,
                time_end_val,
                [i.strip() for i in gv_val.split(",") if i.strip()],
                [i.strip() for i in hs_val.split(",") if i.strip()]
            )
            Lop.add_class(new_class, r"C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\Class.json")
            messagebox.showinfo("Thành công", "Đã thêm lớp học mới!")
            add_window.destroy()

        button1 = Button(add_window, text="Add", bg="light gray", font="Times 20", command=add_to_json)
        button1.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")

    @staticmethod
    def open_delete_class_window():
        delete_window = Toplevel(window)
        delete_window.title("Xóa lớp học")
        delete_window.geometry("500x250")  # Tăng kích thước cửa sổ xóa lớp
        delete_window.configure(background="light gray")
        Label(delete_window, text="Nhập Id lớp cần xóa:", font="Times 15", bg="light gray").grid(row=0, column=0, padx=20, pady=20, sticky="w")
        entry_id = Entry(delete_window, width=35, font=("Arial", 15))
        entry_id.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        def delete_class():
            id_to_delete = entry_id.get().strip()
            if not id_to_delete:
                messagebox.showerror("Lỗi", "Vui lòng nhập Id lớp!")
                return
            result = Lop.delete_class(id_to_delete, r"C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\Class.json")
            if not result:
                messagebox.showerror("Lỗi", "Không tìm thấy lớp với Id này!")
                return
            messagebox.showinfo("Thành công", f"Đã xóa lớp có Id {id_to_delete}!")
            delete_window.destroy()

        Button(delete_window, text="Delete", font="Times 15", bg="light gray", command=delete_class).grid(row=2, column=0, pady=20, sticky="ew")

# Main window layout using grid
window.grid_rowconfigure(0, minsize=80)
window.grid_columnconfigure(0, minsize=300)
window.grid_columnconfigure(1, minsize=300)
window.grid_columnconfigure(2, minsize=300)
window.grid_columnconfigure(3, minsize=300)

Label1 = Label(window, text="               Quản lí lớp học", bg="light gray", fg="Black", font="Times 36",  justify='center', anchor='center')
Label1.grid(row=0, column=0, columnspan=4, pady=30, sticky="ew")

label2 = Label(window, text="Lớp học", bg="light gray", font="Times 28")
label2.grid(row=1, column=0, padx=20, pady=20, sticky="w")

# Load data
Classes = Lop.load_all(r"C:\Users\ASUS\OneDrive\Máy tính\Code\SNLTW_SAT1400\Bao\Class.json")
class_id = [str(c.id) for c in Classes]

cb1 = Combobox(window, values=class_id, width=18, font=("Arial", 22), state="readonly")
cb1.grid(row=1, column=1, padx=20, pady=20, sticky="w")

lbl_id = Label(window, text="Class ID",bg = "light gray", font=("Times", 28))
lbl_id.grid(row=2, column=0, padx=20, pady=20, sticky="w")
entry_id = Text(window, width=25, height=1, font=("Arial", 22))
entry_id.grid(row=2, column=1, padx=20, pady=20, sticky="w")

lbl_ten = Label(window, text="Class Name", bg= "light gray", font=("Times", 28))
lbl_ten.grid(row=3, column=0, padx=20, pady=20, sticky="w")
entry_ten = Text(window, width=25, height=1, font=("Arial", 22))
entry_ten.grid(row=3, column=1, padx=20, pady=20, sticky="w")

label3 = Label(window, text="GV:    ", bg="light gray", font="Times 28")
label3.grid(row=2, column=2, padx=(20,0), pady=20, sticky="e")
Label4 = Label(window, text="", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 22", padx=20, pady=20, justify='center', anchor='center')
Label4.grid(row=2, column=3, padx=(0,20), pady=20, sticky="w")

label5 = Label(window, text="HS:    ", bg="light gray", font="Times 28")
label5.grid(row=3, column=2, padx=(20,0), pady=20, sticky="e")
HS_HEIGHT = 5  # Số dòng tối đa hiển thị

hs_frame = Frame(window, bg="light gray")
hs_frame.grid(row=3, column=3, padx=(0,20), pady=20, sticky="w")
HSBox = scrolledtext.ScrolledText(hs_frame, width=25, height=HS_HEIGHT, font=("Times", 22), wrap=WORD)
HSBox.pack(fill=BOTH, expand=True)
HSBox.config(state=DISABLED, borderwidth=2, relief="solid", bg="light gray", fg="Black")

button1 = Button(window, text="Add Class", bg="light gray", font="Times 28", command=Lop.open_add_class_window)
button1.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

button2 = Button(window, text="Delete Class", bg="light gray", font="Times 28", command=Lop.open_delete_class_window)
button2.grid(row=4, column=1, padx=20, pady=20, sticky="ew")

# button3 = Button(window, text="Fix Class", bg="light gray", font="Times 22")
# button3.grid(row=4, column=2, padx=20, pady=20, sticky="ew")

def hien_thi_thong_tin(id):
    entry_id.delete("1.0", "end")
    entry_ten.delete("1.0", "end")  # Thêm dòng này để xóa nội dung cũ của class name
    for c in Classes:
        if str(c.id) == str(id):
            entry_id.insert("1.0", c.id)
            entry_ten.insert("1.0", c.name)  # Thêm dòng này để hiển thị class name
            Label4.config(text=", ".join(c.teachers))
            HSBox.config(state=NORMAL)
            HSBox.delete("1.0", END)
            HSBox.insert(END, ",\n".join(c.students))
            HSBox.config(state=DISABLED)
            break
    else:
        entry_id.insert("1.0", "")
        entry_ten.delete("1.0", "end")  # Đảm bảo xóa class name nếu không tìm thấy
        Label4.config(text="")
        HSBox.config(state=NORMAL)
        HSBox.delete("1.0", END)
        HSBox.config(state=DISABLED)

cb1.bind("<<ComboboxSelected>>", lambda event: hien_thi_thong_tin(cb1.get()))

window.mainloop()
