import tkinter as tk
from tkinter import messagebox
import json, os
from giaovien import GiaoVien

FONT = ("Times New Roman", 20)

class QuanLyGiaoVien:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Giáo Viên")
        self.root.geometry("1200x600")  # Tăng kích thước cửa sổ cho phù hợp với font lớn
        self.ten_file = "GV.json"
        self.GV = self.doc_file_json()
        print(self.GV)
        self.tao_giao_dien()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for t in self.GV:
            self.listbox.insert(tk.END, f'{t.ID} - {t.ten}')

    def get_selected_id(self):
        try:
            line = self.listbox.curselection()
            selected_text = self.listbox.get(line[0])
            return selected_text.split(" - ")[0]
        except:
            return None

    def tao_giao_dien(self):
        self.listbox = tk.Listbox(self.root, width=40, font=FONT)
        self.listbox.place(x=550, y=100)
        self.refresh()
        self.listbox.bind("<<ListboxSelect>>", self.hien_thi_thong_tin)

        # Labels và Entries
        tk.Label(self.root, text="Mã giáo viên:", font=FONT, bg="#f0f0f0").place(y=20, x=10)
        self.id_entry = tk.Entry(self.root, width=20, font=FONT)
        self.id_entry.place(x=10, y=70)

        tk.Label(self.root, text="Tên giáo viên:", font=FONT, bg="#f0f0f0").place(y=130, x=10)
        self.ten_entry = tk.Entry(self.root, width=20, font=FONT)
        self.ten_entry.place(x=10, y=180)

        # Buttons
        self.btn_them = tk.Button(self.root, text="Thêm", font=FONT, bg="green", command=self.them_giao_vien)
        self.btn_them.place(y=250, x=10)

        self.btn_xoa = tk.Button(self.root, text="Xoá", font=FONT, bg="red", command=self.xoa_giao_vien)
        self.btn_xoa.place(y=250, x=200)

        # Combobox (dùng tk.OptionMenu để dễ set font hơn ttk.Combobox)
        tk.Label(self.root, text="Chọn GV để xoá:", font=FONT).place(y=330, x=10)
        self.selected_gv = tk.StringVar(self.root)
        self.selected_gv.set('')
        self.option_menu = tk.OptionMenu(self.root, self.selected_gv, *[gv.ID for gv in self.GV])
        self.option_menu.config(font=FONT, width=15)
        self.option_menu.place(y=380, x=10)

        # Thông tin giáo viên
        self.info_label = tk.Label(self.root, text="Thông tin giáo viên", font=FONT, justify="left")
        self.info_label.place(x=550, y=20)

    def them_giao_vien(self):
        ID, ten = self.id_entry.get().strip(), self.ten_entry.get().strip()
        if not ID or not ten:
            messagebox.showwarning("Thiếu thông tin", "Điền đầy đủ ID và tên.")
            return
        if self.kiem_tra_trung_ID(ID):
            messagebox.showerror("Trùng ID", f"ID '{ID}' đã tồn tại.")
            return
        self.GV.append(GiaoVien(ID, ten))
        self.luu_file_json()
        self.cap_nhat_option_menu()
        self.id_entry.delete(0, tk.END)
        self.ten_entry.delete(0, tk.END)
        self.refresh()

    def xoa_giao_vien(self):
        selected = self.selected_gv.get()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Chọn giáo viên cần xoá.")
            return
        self.GV = [gv for gv in self.GV if gv.ID != selected]
        self.luu_file_json()
        self.cap_nhat_option_menu()
        self.info_label.config(text="Thông tin giáo viên")
        self.id_entry.delete(0, tk.END)
        self.ten_entry.delete(0, tk.END)
        self.refresh()

    def hien_thi_thong_tin(self, event=None):
        selected = self.get_selected_id()
        gv = next((gv for gv in self.GV if gv.ID == selected), None)
        if gv:
            self.info_label.config(text=f"ID: {gv.ID}\nTên: {gv.ten}")

    def kiem_tra_trung_ID(self, ID):
        return any(gv.ID == ID for gv in self.GV)

    def cap_nhat_option_menu(self):
        menu = self.option_menu["menu"]
        menu.delete(0, "end")
        for gv in self.GV:
            menu.add_command(label=gv.ID, command=lambda value=gv.ID: self.selected_gv.set(value))
        self.selected_gv.set('')

    def luu_file_json(self):
        with open(self.ten_file, "w", encoding="utf-8") as f:
            json.dump([gv.to_dict() for gv in self.GV], f, indent=4, ensure_ascii=False)

    def doc_file_json(self):
        if os.path.exists(self.ten_file):
            try:
                with open(self.ten_file, "r", encoding="utf-8") as f:
                    return [GiaoVien(item["ID"], item["ten"]) for item in json.load(f)]
            except:
                messagebox.showerror("Lỗi", "File JSON lỗi.")
        return []

# Nếu chạy file trực tiếp:
if __name__ == "__main__":
    root = tk.Tk()
    app = QuanLyGiaoVien(root)
    root.mainloop()
