import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

studata_files='baicuoikhoa.json'
with open(studata_files,'r',encoding='utf-8') as f:
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
    def __init__(self, filepath="baicuoikhoa.json"):
        self.filepath = filepath
        self.students = self.load_students()

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
        self.manager = StudentManager()

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Thêm", command=self.add_student).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Sửa", command=self.edit_student).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Xóa", command=self.delete_student).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Làm mới", command=self.refresh).grid(row=0, column=3, padx=5)

        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for s in self.manager.students:
            self.listbox.insert(tk.END, f"{s['id']} - {s['name']} - {s['age']} tuổi - Lớp {s['class']}")

    def get_selected_id(self):
        try:
            line = self.listbox.get(self.listbox.curselection())
            return int(line.split(" - ")[0])
        except:
            return None

    def add_student(self):
        student_id = simpledialog.askstring("id","nhập id học sinh")
        name = simpledialog.askstring("Tên", "Nhập tên học sinh:")
        age = simpledialog.askinteger("Tuổi", "Nhập tuổi học sinh:")
        student_class = simpledialog.askstring("Lớp", "Nhập lớp:")
        if name and age and student_class:
            self.manager.add_student(name, age, student_class)
            self.refresh()

    def edit_student(self):
        student_id = self.get_selected_id()
        if student_id is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn học sinh cần sửa.")
            return
        student = next((s for s in self.manager.students if s["id"] == student_id), None)
        if student:
            id = simpledialog.askstring("id", "Sửa id học sinh:", initialvalue=student["student_id"])
            name = simpledialog.askstring("Tên", "Sửa tên học sinh:", initialvalue=student["name"])
            age = simpledialog.askinteger("Tuổi", "Sửa tuổi:", initialvalue=student["age"])
            student_class = simpledialog.askstring("Lớp", "Sửa lớp:", initialvalue=student["class"])
            if name and age and student_class:
                self.manager.update_student(student_id, name, age, student_class)
                self.refresh()

    def delete_student(self):
        student_id = self.get_selected_id()
        if student_id is None:
            messagebox.showerror("Lỗi", "Chọn học sinh để xóa.")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa học sinh này?")
        if confirm:
            self.manager.delete_student(student_id)
            self.refresh()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.account_manager = AccountManager()

        tk.Label(root, text="Tên đăng nhập:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Mật khẩu:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Button(root, text="Đăng nhập", command=self.login).pack(pady=10)

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
    