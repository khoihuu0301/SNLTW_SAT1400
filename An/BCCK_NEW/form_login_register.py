import tkinter as tk
from tkinter import messagebox
import json
import os
from form_info_register import FormDangKy

class FormDangNhapDangKy:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success  # 💥 Save this to call later
        self.root.title("Đăng Nhập / Đăng Ký")
        self.root.geometry("300x250")

        tk.Label(root, text="Tên đăng nhập:").pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        tk.Label(root, text="Mật khẩu:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        tk.Button(root, text="Đăng Nhập", command=self.dang_nhap).pack(pady=10)
        tk.Button(root, text="Đăng Ký", command=self.dang_ky).pack()

    def dang_nhap(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.kiem_tra_nguoi_dung(username, password):
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            self.root.destroy()
            # Ở đây bạn có thể gọi app chính nếu muốn

                        # 💥 Call main app after login
            if self.on_success:
                self.on_success()

        else:
            messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu.")

    def dang_ky(self):
        root_dangky = tk.Tk()
        FormDangKy(root_dangky)
        root_dangky.mainloop()

    def kiem_tra_nguoi_dung(self, username, password):
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                try:
                    data = json.load(f)
                    return data.get(username) == password
                except:
                    return False
        return True
