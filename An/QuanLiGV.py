import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class GiaoVien:
    def __init__(self, ID, ten):
        self.ID = ID
        self.ten = ten

    def to_dict(self):
        return {"ID": self.ID, "ten": self.ten}


class QuanLyGiaoVien:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Giáo Viên")
        self.root.geometry("600x400")
    
        self.GV = []
        with open("GV.json", "r") as file:
            GV_data = json.load(file)
            self.GV.extend(GV_data)

        GV_id = []
        for g in self.GV:
            GV_id.append(g["ID"])

        cb1 = ttk.Combobox(values = GV_id, width = 10)  # Tạo Combobox
        cb1.place(x=100, y =200)


    def tao_giao_dien(self):
        # Frame bên trái để nhập thông tin và các nút
        left_frame = tk.Frame(self.root)
        left_frame.pack(side="left", padx=20, pady=20)


        # Nhập ID giáo viên
        tk.Label(left_frame, text="ID giáo viên:").pack(pady=5)
        self.id_entry = tk.Entry(left_frame)
        self.id_entry.pack()

        # Nhập tên giáo viên
        tk.Label(left_frame, text="Tên giáo viên:").pack(pady=5)
        self.ten_entry = tk.Entry(left_frame)
        self.ten_entry.pack()

        # Nút Thêm và Xóa
        tk.Button(left_frame, text="Thêm giáo viên", command=self.them_giao_vien).pack(pady=5)
        tk.Button(left_frame, text="Xóa giáo viên", command=self.xoa_giao_vien).pack(pady=5)

        # Frame bên phải để hiển thị thông tin giáo viên
        right_frame = tk.Frame(self.root)
        right_frame.pack(side="right", padx=20, pady=20)

        # Label hiển thị thông tin giáo viên
        self.info_label = tk.Label(right_frame, text="Thông tin giáo viên sẽ hiển thị tại đây", justify="left")
        self.info_label.pack()

        # Khi chọn giáo viên trong combobox, hiển thị thông tin
        self.combobox.bind("<<ComboboxSelected>>", self.hien_thi_thong_tin)

        # Cập nhật Combobox với danh sách giáo viên từ file JSON
        self.cap_nhat_combobox()

    def them_giao_vien(self):
        # Thêm giáo viên mới từ Entry widgets
        ID = self.id_entry.get()
        ten = self.ten_entry.get()

        if not ID or not ten:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ ID và tên giáo viên.")
            return

        if self.kiem_tra_trung_ID(ID):
            messagebox.showerror("Trùng ID", f"ID '{ID}' đã tồn tại.")
            return

        gv = GiaoVien(ID, ten)
        self.GV.append(gv)
        self.luu_file_json()
        self.cap_nhat_combobox()

        # Clear các trường nhập sau khi thêm
        self.id_entry.delete(0, tk.END)
        self.ten_entry.delete(0, tk.END)

    def xoa_giao_vien(self):
        # Xóa giáo viên được chọn trong combobox
        selected_gv = self.combobox.get()
        if not selected_gv:
            messagebox.showwarning("Chưa chọn giáo viên", "Vui lòng chọn giáo viên để xóa.")
            return

        ID = selected_gv.split(" | ")[0].split(": ")[1]  # Lấy ID giáo viên từ chuỗi
        self.GV = [gv for gv in self.GV if gv.ID != ID]
        self.luu_file_json()
        self.cap_nhat_combobox()

    def kiem_tra_trung_ID(self, ID):
        # Kiểm tra ID có bị trùng không
        for gv in self.GV:
            if gv.ID == ID:
                return True
        return False

    def cap_nhat_combobox(self):
        # Cập nhật combobox với danh sách giáo viên
        self.combobox.set('')
        self.combobox['values'] = [f"ID: {gv.ID} | Tên: {gv.ten}" for gv in self.GV]

    def hien_thi_thong_tin(self, event=None):
        # Hiển thị thông tin giáo viên được chọn trong combobox
        selected_gv = self.combobox.get()
        if selected_gv:
            ID = selected_gv.split(" | ")[0].split(": ")[1]  # Lấy ID giáo viên từ chuỗi
            gv = next(gv for gv in self.GV if gv.ID == ID)
            info = f"ID: {gv.ID}\nTên: {gv.ten}"
            self.info_label.config(text=info)

    def luu_file_json(self):
        # Lưu danh sách giáo viên vào file JSON
        data = [gv.to_dict() for gv in self.GV]
        with open(self.ten_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def doc_file_json(self):
        # Đọc dữ liệu từ file JSON (GV.json)
        if os.path.exists(self.ten_file):
            with open(self.ten_file, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    # Xử lý dữ liệu từ JSON và tạo danh sách giáo viên
                    GV = [GiaoVien(item["ID"], item["ten"]) for item in data]
                    return GV
                except json.JSONDecodeError:
                    messagebox.showerror("Lỗi", "File JSON bị lỗi hoặc trống.")
                    return []
        else:
            return []  # Nếu không có file, trả về danh sách trống

if __name__ == "__main__":
    root = tk.Tk()
    app = QuanLyGiaoVien(root)
    root.mainloop()
