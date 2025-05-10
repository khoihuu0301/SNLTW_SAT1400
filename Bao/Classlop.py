from tkinter import *
from tkinter import messagebox, filedialog  # Import filedialog for Save As functionality
from tkinter.ttk import Combobox
import json
import os  # Thêm thư viện để kiểm tra tệp

window = Tk()
window.title("Đăng Ký Tài khoản")
window.geometry("1024x600")  # Giảm kích thước cửa sổ
window.configure(background="light gray")

Label1 = Label(window, text="Quản lí lớp học", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=50, pady=10, justify='center', anchor='center')
Label1.pack(pady=20)  

label2 = Label(window, text="Lớp học", bg="light gray", font="Times 25")
label2.place(x=100, y=100)

Classes = []
if os.path.exists("Class.json"):  # Kiểm tra xem tệp có tồn tại không
    try:
        with open("Class.json", "r") as file:
            classes_data = json.load(file)
            Classes.extend(classes_data)
    except json.JSONDecodeError:
        messagebox.showerror("Lỗi", "Tệp Class.json không đúng định dạng JSON!")
else:
    messagebox.showerror("Lỗi", "Tệp Class.json không tồn tại!")

class_id = []
for c in Classes:
    class_id.append(c.get("I*d", "Unknown"))  # Sử dụng .get() để tránh lỗi nếu không có khóa "id"

cb1 = Combobox(window, values=class_id, width=10)  # Giảm chiều rộng từ 15 xuống 10
cb1.place(x=100, y=160)

label3 = Label(window, text="GV", bg="light gray", font="Times 25")
label3.place(x=720, y=100)

Label4 = Label(window, text="", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=100, pady=10, justify='center', anchor='center')  # Tăng giá trị padx để làm Label4 dài hơn
Label4.place(x=650, y=140)

label5 = Label(window, text="HS", bg="light gray", font="Times 25")
label5.place(x=720, y=230)

Label6 = Label(window, text="", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=100, pady=100, justify='center', anchor='center')  # Tăng giá trị pady để làm Label6 dài hơn nữa
Label6.place(x=650, y=280)

window.mainloop()
