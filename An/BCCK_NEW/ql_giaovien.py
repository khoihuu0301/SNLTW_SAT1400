import tkinter as tk
from tkinter import ttk, messagebox
import json, os
from giaovien import GiaoVien

class QuanLyGiaoVien:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Giáo Viên")
        self.root.geometry("800x600")
        self.ten_file = "GV.json"
        self.GV = self.doc_file_json()
        print(self.GV)
        self.tao_giao_dien()

    def refresh(self):
        self.listbox.delete(0,tk.END)
        
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
        left = tk.Frame(self.root)
        left.pack(side="left", fill="y", padx=20, pady=20)

        self.listbox = tk.Listbox(self.root, width=100)
        self.listbox.pack(anchor="w")
        self.refresh()
        self.listbox.bind("<<ListboxSelect>>", self.hien_thi_thong_tin )
    
        ttk.Label(left, text="ID giáo viên:").pack(pady=5)
        self.id_entry = ttk.Entry(left)
        self.id_entry.pack()

        ttk.Label(left, text="Tên giáo viên:").pack(pady=5)
        self.ten_entry = ttk.Entry(left)
        self.ten_entry.pack()

        ttk.Button(left, text="Thêm", command=self.them_giao_vien).pack(pady=5)
        ttk.Button(left, text="Xoá", command=self.xoa_giao_vien).pack(pady=5)
        ttk.Button(left, text="Refresh", command=self.refresh).pack(pady=5)

        self.cb1 = ttk.Combobox(left, values=[gv.ID for gv in self.GV])
        self.cb1.pack(pady=10)
        self.cb1.bind("<<ComboboxSelected>>", self.hien_thi_thong_tin)

        right = tk.Frame(self.root)
        right.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.info_label = ttk.Label(right, text="Thông tin giáo viên", justify="left")
        self.info_label.pack(anchor="w")

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
        self.cap_nhat_combobox()
        self.id_entry.delete(0, tk.END)
        self.ten_entry.delete(0, tk.END)
        self.refresh()

    def xoa_giao_vien(self):
        selected = self.cb1.get()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Chọn giáo viên cần xoá.")
            return
        self.GV = [gv for gv in self.GV if gv.ID != selected]
        self.luu_file_json()
        self.cap_nhat_combobox()
        self.info_label.config(text="Thông tin giáo viên")

    def hien_thi_thong_tin(self, event=None):
        selected = self.get_selected_id()
        gv = next((gv for gv in self.GV if gv.ID == selected), None)
        if gv:
            self.info_label.config(text=f"ID: {gv.ID}\nTên: {gv.ten}")

    def kiem_tra_trung_ID(self, ID):
        return any(gv.ID == ID for gv in self.GV)

    def cap_nhat_combobox(self):
        self.cb1.set('')
        self.cb1['values'] = [gv.ID for gv in self.GV]

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
