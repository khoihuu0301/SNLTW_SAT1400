import tkinter as tk
from form_login_register import FormDangNhapDangKy
from ql_giaovien import QuanLyGiaoVien

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính ban đầu

    def start_app():
        root.deiconify()  # Hiện lại cửa sổ chính
        QuanLyGiaoVien(root)
    start_app()
    # FormDangNhapDangKy(tk.Tk(), on_success=start_app)  # Pass callback
    root.mainloop()
