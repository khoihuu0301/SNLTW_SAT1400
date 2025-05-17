from tkinter import *
from tkinter import messagebox, filedialog  # Import filedialog for Save As functionality
from tkinter.ttk import Combobox
import json
import os  # Thêm thư viện để kiểm tra tệp

# Khởi tạo cửa sổ chính
window = Tk()
window.title("Quản lí lớp học")
window.geometry("1024x600")  # Giảm kích thước cửa sổ
window.configure(background="light gray")

# Tiêu đề
Label1 = Label(window, text="Quản lí lớp học", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=50, pady=10, justify='center', anchor='center')
Label1.pack(pady=20)  

# Nhãn "Lớp học"
label2 = Label(window, text="Lớp học", bg="light gray", font="Times 25")
label2.place(x=100, y=100)

# Kiểm tra xem file `Class.json` có tồn tại không
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
    Classes = []  # Danh sách lớp học trống nếu tệp không tồn tại

# Lấy danh sách ID lớp học
class_id = []
for c in Classes:
    class_id.append(c.get("ID", "Unknown"))  # Sử dụng .get() để tránh lỗi nếu không có khóa "ID"

# Combobox để chọn lớp học
cb1 = Combobox(window, values=class_id, width=10)
cb1.place(x=100, y=160)

# Nhãn "Giáo viên"
label3 = Label(window, text="GV", bg="light gray", font="Times 25")
label3.place(x=720, y=100)

# Label để hiển thị thông tin giáo viên
Label4 = Label(window, text="", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=100, pady=10, justify='center', anchor='center')
Label4.place(x=650, y=140)

# Nhãn "Học sinh"
label5 = Label(window, text="HS", bg="light gray", font="Times 25")
label5.place(x=720, y=230)

# Label để hiển thị thông tin học sinh
Label6 = Label(window, text="", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 32", padx=100, pady=100, justify='center', anchor='center')
Label6.place(x=650, y=280)

# Hàm khi thay đổi lớp học trong Combobox
def update_info(event):
    selected_class_id = cb1.get()  # Lấy lớp học đã chọn
    selected_class = next((cls for cls in Classes if cls["ID"] == selected_class_id), None)
    
    if selected_class:
        # Cập nhật thông tin giáo viên và học sinh
        Label4.config(text=selected_class["Teacher"])
        Label6.config(text="\n".join(selected_class["Students"]))
    else:
        # Nếu không tìm thấy lớp học
        Label4.config(text="")
        Label6.config(text="")

# Gắn sự kiện khi thay đổi lựa chọn trong Combobox
cb1.bind("<<ComboboxSelected>>", update_info)

# Khởi chạy ứng dụng
window.mainloop()
