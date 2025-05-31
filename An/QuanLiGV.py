import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class GiaoVien:
    def __init__(self, ID, ten, mon, nam_sinh):
        self.ID = ID
        self.ten = ten
        self.mon = mon
        self.namsinh = nam_sinh

    def to_dict(self):
        return {"ID": self.ID, "ten": self.ten, "mon": self.mon, "nam_sinh": self.namsinh}


class QuanLyGiaoVien:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Giáo Viên")
        self.root.geometry("1500x800")

        self.ten_file = "GV.json"
        self.GV = self.doc_file_json()
        print(self.GV)

        self.tao_giao_dien()

    def tao_giao_dien(self):
        # Cập nhật font Times New Roman với cỡ chữ 20
        font_style = ("Times New Roman", 15)

        # Frame bên trái để nhập thông tin và các nút
        left_frame = tk.Frame(self.root)
        left_frame.pack(side="left", padx=20, pady=20)

        # Cập nhật danh sách giáo viên từ file JSON
        GV_id = [gv.ID for gv in self.GV]

        self.cb1 = ttk.Combobox(values=GV_id, width=40, font=font_style)  # Tạo Combobox
        self.cb1.place(x=50, y=50)
        self.cb1.bind("<<ComboboxSelected>>", self.hien_thi_thong_tin)

        # Nhập ID giáo viên
        tk.Label(left_frame, text="ID giáo viên:", font=font_style).pack(pady=5)
        self.id_entry = tk.Entry(left_frame, font=font_style)
        self.id_entry.pack()

        # Nhập tên giáo viên
        tk.Label(left_frame, text="Tên giáo viên:", font=font_style).pack(pady=5)
        self.ten_entry = tk.Entry(left_frame, font=font_style)
        self.ten_entry.pack()

        # Nhập năm sinh giáo viên
        tk.Label(left_frame, text="Năm sinh giáo viên:", font=font_style).pack(pady=5)
        self.namsinh_entry = tk.Entry(left_frame, font=font_style)
        self.namsinh_entry.pack()

        # Nhập môn dậy của giáo viên
        tk.Label(left_frame, text="Môn dạy giáo viên:", font=font_style).pack(pady=5)
        self.mon_entry = tk.Entry(left_frame, font=font_style)
        self.mon_entry.pack()

        # Nút Thêm và Xóa
        tk.Button(left_frame, text="Thêm giáo viên", command=self.them_giao_vien, font=font_style).pack(pady=5)
        tk.Button(left_frame, text="Xóa giáo viên", command=self.xoa_giao_vien, font=font_style).pack(pady=5)

        # Frame bên phải để hiển thị thông tin giáo viên
        right_frame = tk.Frame(self.root, relief="solid", bd=3, width=500, height=650)
        right_frame.pack(side="right", padx=50, pady=50)

        # Label hiển thị thông tin giáo viên
        self.info_label = tk.Label(right_frame, text="Thông tin giáo viên sẽ hiển thị tại đây", justify="left", font=font_style)
        self.info_label.place(x=130)
        # self.info_label.pack()

    def them_giao_vien(self):
        # Thêm giáo viên mới từ Entry widgets
        ID = self.id_entry.get()
        ten = self.ten_entry.get()
        mon = self.mon_entry.get()
        nam_sinh = self.namsinh_entry.get()

        if not ID or not ten:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ ID và tên giáo viên.")
            return

        if self.kiem_tra_trung_ID(ID):
            messagebox.showerror("Trùng ID", f"ID '{ID}' đã tồn tại.")
            return

        gv = GiaoVien(ID, ten, mon, nam_sinh)
        self.GV.append(gv)
        self.luu_file_json()
        self.cap_nhat_combobox()

        # Clear các trường nhập sau khi thêm
        self.id_entry.delete(0, tk.END)
        self.ten_entry.delete(0, tk.END)
        self.mon_entry.delete(0, tk.END)
        self.namsinh_entry.delete(0, tk.END)

    def xoa_giao_vien(self):
        # Xóa giáo viên được chọn trong combobox
        selected_gv = self.cb1.get()
        if not selected_gv:
            messagebox.showwarning("Chưa chọn giáo viên", "Vui lòng chọn giáo viên để xóa.")
            return

        # Xóa giáo viên trong danh sách
        self.GV = [gv for gv in self.GV if gv.ID != selected_gv]
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
        self.cb1.set('')
        self.cb1['values'] = [gv.ID for gv in self.GV]

    def hien_thi_thong_tin(self, event=None):
        # Lấy ID giáo viên được chọn trong combobox
        selected_gv = self.cb1.get()
        if selected_gv:
            # Truy tìm giáo viên từ danh sách GV dựa trên ID
            gv = next(gv for gv in self.GV if gv.ID == selected_gv)
            info = f"ID: {gv.ID}\n\nTên: {gv.ten}\n\nMôn: {gv.mon}\n\nNăm sinh: {gv.namsinh}"
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
                    GV = [GiaoVien(item["ID"], item["ten"], item["mon"], item["nam_sinh"]) for item in data]
                    print("GV:", GV)
                    return GV
                except json.JSONDecodeError:
                    messagebox.showerror("Lỗi", "File JSON bị lỗi hoặc trống.")
                    return []
        return []  # Nếu không có file, trả về danh sách trống


if __name__ == "__main__":
    root = tk.Tk()
    app = QuanLyGiaoVien(root)
    root.mainloop()
