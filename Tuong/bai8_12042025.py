import tkinter as tk
from tkinter import messagebox

def window_giai_pt_b1():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if a == 0:
            if b == 0:
                ket_qua = "Phương trình có vô số nghiệm."
            else:
                ket_qua = "Phương trình vô nghiệm."
        else:
            x = -b / a
            ket_qua = f"Nghiệm của phương trình là x = {x:.2f}"
        label_ket_qua.config(text=ket_qua)
    except ValueError:
        messagebox.showerror("Lỗi", "nhập số hợp lệ!")


root = tk.Tk()
root.title("Giải phương trình bậc 1")
root.geometry("350x200")
root.resizable(False, True)

label_pt = tk.Label(root, text="Phương trình: ax + b = 0", font=("Time New Roman", 14), fg="light green")
label_pt.pack(pady=10)

label_a = tk.Label(root, text="a=")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="b=")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

btn_giai = tk.Button(root, text="Giải phương trình", command=window_giai_pt_b1)
btn_giai.pack(pady=10)

label_ket_qua = tk.Label(root, text="Đâyy là kết quả !!!!", fg="black")
label_ket_qua.pack()

root.mainloop()