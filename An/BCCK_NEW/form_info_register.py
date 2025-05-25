import tkinter as tk
from tkinter import ttk, messagebox

class FormDangKy:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Đăng kí Thông Tin")
        self.root.geometry("600x400")

        self.build_form()

    def build_form(self):
        tk.Label(self.root, text="Form Đăng kí Thông Tin", font=("Arial", 16, "bold")).grid(row=0, column=1, pady=10)

        labels = ["Họ và tên", "Ngày sinh", "Quốc tịch", "Địa chỉ", "Email", "Số điện thoại"]
        self.entries = {}

        for idx, label in enumerate(labels):
            tk.Label(self.root, text=label + ":").grid(row=idx + 1, column=0, padx=10, pady=5, sticky="e")
            if label == "Quốc tịch":
                self.entries[label] = ttk.Combobox(self.root, values=["Việt Nam", "Mỹ", "Anh", "Pháp"])
                self.entries[label].set("Việt Nam")
            else:
                self.entries[label] = tk.Entry(self.root)

            self.entries[label].grid(row=idx + 1, column=1)

        tk.Button(self.root, text="Register", command=self.register).grid(row=8, column=0, pady=20)
        tk.Button(self.root, text="Thoát", command=self.root.quit).grid(row=8, column=2)

    def register(self):
        values = {label: widget.get().strip() for label, widget in self.entries.items()}
        for field, value in values.items():
            if not value:
                messagebox.showwarning("Thiếu thông tin", f"Vui lòng nhập {field}.")
                return

        messagebox.showinfo("Đăng kí", f"Đăng kí thành công cho {values['Họ và tên']}")
        self.root.quit()
