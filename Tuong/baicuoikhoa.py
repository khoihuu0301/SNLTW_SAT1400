import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

studata_files = 'baicuoikhoa.json'
with open(studata_files, 'r', encoding='utf-8') as f:
    list_studata = json.load(f)

class AccountManager:
    def __init__(self, filepath="baicuoikhoa.json"):
        self.filepath = filepath
        self.load_users()

    def load_users(self):
        with open(self.filepath, "r") as f:
            self.users = json.load(f)

    def authenticate(self, username, password):
        return self.users.get(username) == password


class StudentManager:
    def __init__(self, filepath=r"C:\Users\Phucd\OneDrive\Máy tính\snltw\snltw 2\__pycache__\snltw 3\baicuoikhoa.json"):
        self.filepath = filepath
        self.students = self.load_students()
        print(self.students)

    def load_students(self):
        with open(self.filepath, "r") as f:
            return json.load(f)

    def save_students(self):
        with open(self.filepath, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, name, age, student_class):
        student_id = max([s["id"] for s in self.students], default=0) + 1
        self.students.append({
            "id": student_id,
            "name": name,
            "age": age,
            "class": student_class
        })
        self.save_students()

    def update_student(self, student_id, name, age, student_class):
        for s in self.students:
            if s["id"] == student_id:
                s["name"] = name
                s["age"] = age
                s["class"] = student_class
        self.save_students()

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s["id"] != student_id]
        self.save_students()


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý học sinh")
        self.root.geometry("1500x800")
        self.manager = StudentManager()

        font_setting = ("Times New Roman", 28)

        self.listbox = tk.Listbox(root, width=80, font=font_setting)
        self.listbox.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Danh sách", font=font_setting, command=self.refresh).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Thêm", font=font_setting, command=self.add_student).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Sửa", font=font_setting, command=self.edit_student).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Xóa", font=font_setting, command=self.delete_student).grid(row=0, column=3, padx=10)
        tk.Button(btn_frame, text="Làm mới", font=font_setting, command=self.refresh).grid(row=0, column=4, padx=10)

        self.form_frame = tk.Frame(root)
        self.form_frame.pack(pady=20)
        self.id_label = tk.Label(self.form_frame, text="ID học sinh:", font=font_setting)
        self.id_label.grid(row=0, column=0, sticky="e")
        self.id_entry = tk.Entry(self.form_frame, font=font_setting)
        self.id_entry.grid(row=0, column=1)

        self.name_label = tk.Label(self.form_frame, text="Tên học sinh:", font=font_setting)
        self.name_label.grid(row=1, column=0, sticky="e")
        self.name_entry = tk.Entry(self.form_frame, font=font_setting)
        self.name_entry.grid(row=1, column=1)

        self.age_label = tk.Label(self.form_frame, text="Tuổi:", font=font_setting)
        self.age_label.grid(row=2, column=0, sticky="e")
        self.age_entry = tk.Entry(self.form_frame, font=font_setting)
        self.age_entry.grid(row=2, column=1)

        self.class_label = tk.Label(self.form_frame, text="Lớp:", font=font_setting)
        self.class_label.grid(row=3, column=0, sticky="e")
        self.class_entry = tk.Entry(self.form_frame, font=font_setting)
        self.class_entry.grid(row=3, column=1)

        self.refresh()


        self.refresh()
    def refresh(self):
        self.listbox.delete(0, tk.END)
        for s in self.manager.students:
            self.listbox.insert(tk.END, f'{s["id"]} - {s["name"]} - {s["age"]} tuổi - Lớp {s["class"]}')
    def get_selected_id(self):
        try:
            line = self.listbox.get(self.listbox.curselection())
            return int(line.split(" - ")[0])
        except:
            return None
    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)
    def add_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        student_class = self.class_entry.get()
        if name and age and student_class:
            self.manager.add_student(name, int(age), student_class)
            self.clear_form()
            self.refresh()
        else:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin.")
    def edit_student(self):
        student_id = self.get_selected_id()
        if student_id is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn học sinh cần sửa.")
            return
        student = next((s for s in self.manager.students if s["id"] == student_id), None)
        if student:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, student["name"])

            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, student["age"])

            self.class_entry.delete(0, tk.END)
            self.class_entry.insert(0, student["class"])

            def confirm_edit():
                name = self.name_entry.get()
                age = self.age_entry.get()
                student_class = self.class_entry.get()
                if name and age and student_class:
                    self.manager.update_student(student_id, name, int(age), student_class)
                    self.clear_form()
                    self.refresh()
                else:
                    messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin.")

            confirm_button = tk.Button(self.form_frame, text="Cập nhật", command=confirm_edit)
            confirm_button.grid(row=3, column=0, columnspan=2)
    def delete_student(self):
        student_id = self.get_selected_id()
        if student_id is None:
            messagebox.showerror("Lỗi", "Chọn học sinh để xóa.")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa học sinh này?")
        if confirm:
            self.manager.delete_student(student_id)
            self.clear_form()
            self.refresh()
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.root.geometry("1500x800")  

        self.account_manager = AccountManager()

        tk.Label(root, text="Tên đăng nhập:", font=("Times New Roman", 40)).pack()
        self.username_entry = tk.Entry(root, font=("Times New Roman", 40))
        self.username_entry.pack()

        tk.Label(root, text="Mật khẩu:", font=("Times New Roman", 40)).pack()
        self.password_entry = tk.Entry(root, show="*", font=("Times New Roman", 40))
        self.password_entry.pack()

        tk.Button(root, text="Đăng nhập", font=("Times New Roman", 40), command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.account_manager.authenticate(username, password):
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            self.root.destroy()
            root = tk.Tk()
            app = StudentApp(root)
            root.mainloop()
        else:
            messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu.")


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()