from email.charset import add_alias
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
import json
import os



window = Tk()
window.title("Đăng Ký Tài khoản")
window.geometry("1024x600")
window.configure(background="light gray")

def open_add_class_window():
    add_window = Toplevel(window)
    add_window.title("Thêm lớp học mới")
    add_window.geometry("800x700")
    add_window.configure(background="light gray")
    Label(add_window, text="Add class", font="Times 20", bg="light gray").pack(pady=20)

    frame = Frame(add_window, bg="light gray")
    frame.pack(pady=10)

    Label(frame, text="Id", bg="light gray", font="Times 15").grid(row=0, column=0, padx=5, pady=10, sticky="w")
    entry1 = Entry(frame, width=30)
    entry1.grid(row=0, column=1, padx=5, pady=10)

    Label(frame, text="Name", bg="light gray", font="Times 15").grid(row=1, column=0, padx=5, pady=10, sticky="w")
    entry2 = Entry(frame, width=30)
    entry2.grid(row=1, column=1, padx=5, pady=10)

    Label(frame, text="Time start", bg="light gray", font="Times 15").grid(row=2, column=0, padx=5, pady=10, sticky="w")
    entry3 = Entry(frame, width=30)
    entry3.grid(row=2, column=1, padx=5, pady=10)
    Label(frame, text="Time end", bg="light gray", font="Times 15").grid(row=3, column=0, padx=5, pady=10, sticky="w")
    entry4 = Entry(frame, width=30)
    entry4.grid(row=3, column=1, padx=5, pady=10)
    Label(frame, text="GV", bg="light gray", font="Times 15").grid(row=4, column=0, padx=5, pady=10, sticky="w")
    entry5 = Entry(frame, width=30)
    entry5.grid(row=4, column=1, padx=5, pady=10)
    Label(frame, text="HS", bg="light gray", font="Times 15").grid(row=5, column=0, padx=5, pady=10, sticky="w")
    entry6 = Entry(frame, width=30)
    entry6.grid(row=5, column=1, padx=5, pady=10)

    def add_to_json():
        # Lấy dữ liệu từ các entry
        id_val = entry1.get().strip()
        name_val = entry2.get().strip()
        time_start_val = entry3.get().strip()
        time_end_val = entry4.get().strip()
        gv_val = entry5.get().strip()
        hs_val = entry6.get().strip()

        # Kiểm tra dữ liệu
        if not id_val or not name_val or not time_start_val or not time_end_val or not gv_val or not hs_val:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        if not id_val.isdigit():
            messagebox.showerror("Lỗi", "Id phải là số!")
            return

        new_class = {
            "Id": id_val,
            "Name": name_val,
            "Time start": time_start_val,
            "Time end": time_end_val,
            "GV": [i.strip() for i in gv_val.split(",") if i.strip()],
            "HS": [i.strip() for i in hs_val.split(",") if i.strip()]
        }
        # Đọc dữ liệu cũ
        try:
            with open("Class.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
        # Thêm dữ liệu mới
        data.append(new_class)
        # Ghi lại file
        with open("Class.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Thành công", "Đã thêm lớp học mới!")
        add_window.destroy()

    button1 = Button(add_window, text="Add", bg="light gray", font="Times 20", command=add_to_json)
    button1.pack(pady=20)

def open_delete_class_window():
    delete_window = Toplevel(window)
    delete_window.title("Xóa lớp học")
    delete_window.geometry("400x200")
    delete_window.configure(background="light gray")
    Label(delete_window, text="Nhập Id lớp cần xóa:", font="Times 15", bg="light gray").pack(pady=10)
    entry_id = Entry(delete_window, width=30)
    entry_id.pack(pady=10)

    def delete_class():
        id_to_delete = entry_id.get().strip()
        if not id_to_delete:
            messagebox.showerror("Lỗi", "Vui lòng nhập Id lớp!")
            return
        try:
            with open("Class.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            messagebox.showerror("Lỗi", "Không đọc được file Class.json!")
            return
        new_data = [c for c in data if str(c.get("Id")) != id_to_delete]
        if len(new_data) == len(data):
            messagebox.showerror("Lỗi", "Không tìm thấy lớp với Id này!")
            return
        with open("Class.json", "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Thành công", f"Đã xóa lớp có Id {id_to_delete}!")
        delete_window.destroy()

    Button(delete_window, text="Delete", font="Times 15", bg="light gray", command=delete_class).pack(pady=10)

Label1 = Label(window, text="Quản lí lớp học", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=50, pady=10, justify='center', anchor='center')
Label1.pack(pady=20)  

label2 = Label(window, text="Lớp học", bg="light gray", font="Times 25")
label2.place(x=100, y=100)

# Tạo các widget hiển thị thông tin lớp học ngay từ đầu
lbl_id = Label(window, text="Class ID", font=("Arial", 20))
lbl_id.place(x=350, y=100)
entry_id = Text(window, width=20, height=1, font=("Arial", 20))
entry_id.place(x=500, y=100)

lbl_ten = Label(window, text="Class Name", font=("Arial", 20))
lbl_ten.place(x=350, y=150)
entry_ten = Text(window, width=20, height=1, font=("Arial", 20))
entry_ten.place(x=500, y=150)

def hien_thi_thong_tin(id):
    # Xóa nội dung cũ
    entry_id.delete("1.0", "end")
    entry_ten.delete("1.0", "end")
    # Tìm lớp học theo id
    for c in Classes:
        if str(c.get("Id", "")) == str(id):
            entry_id.insert("1.0", c.get("Id", ""))
            entry_ten.insert("1.0", c.get("Name", ""))
            # Hiển thị GV và HS
            Label4.config(text=", ".join(c.get("GV", [])))
            Label6.config(text=", ".join(c.get("HS", [])))
            break
    else:
        entry_id.insert("1.0", "")
        entry_ten.insert("1.0", "")
        Label4.config(text="")
        Label6.config(text="")

cb1 = Combobox(window, width=50, font=("Arial", 35), state="readonly")
cb1.grid(row=0, column=1, padx=10, pady=10, sticky="w")
# Load data
Classes = []
if os.path.exists("Class.json"):
    try:
        with open("Class.json", "r") as file:
            classes_data = json.load(file)
            Classes.extend(classes_data)
    except json.JSONDecodeError:
        messagebox.showerror("Lỗi", "Tệp Class.json không đúng định dạng JSON!")
else:
    messagebox.showerror("Lỗi", "Tệp Class.json không tồn tại!")

cb1["values"] = [str(c.get("Id", "")) for c in Classes]  # Populate the combobox with class IDs
cb1.bind("<<ComboboxSelected>>", lambda event: hien_thi_thong_tin(cb1.get()))  # Bind selection event

class_id = []
for c in Classes:
    class_id.append(str(c.get("Id", "Unknown")))  # Sửa "I*d" thành "Id"

cb1 = Combobox(window, values=class_id, width=10)
cb1.place(x=100, y=160)

label3 = Label(window, text="GV", bg="light gray", font="Times 25")
label3.place(x=720, y=100)

Label4 = Label(window, text="", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=100, pady=10, justify='center', anchor='center')
Label4.place(x=650, y=140)

label5 = Label(window, text="HS", bg="light gray", font="Times 25")
label5.place(x=720, y=230)

Label6 = Label(window, text="", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=100, pady=100, justify='center', anchor='center')
Label6.place(x=650, y=280)

button1 = Button(window, text="Add Class", bg="light gray", font="Times 20", command=open_add_class_window)
button1.place(x=80, y=200)

button2 = Button(window, text="Delete Class", bg="light gray", font="Times 20", command=open_delete_class_window)
button2.place(x=70, y=260)

button3 = Button(window, text="Fix Class", bg="light gray", font="Times 20")
button3.place(x=90, y=320)

window.mainloop()
