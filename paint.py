import tkinter as tk
import math

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Paint bằng OOP")
        self.root.geometry("900x700")

        # Canvas để vẽ
        self.canvas = tk.Canvas(root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Tool hiện tại: draw, line, rect, circle
        self.current_tool = "draw"
        self.current_color = "black"
        self.start_x = None
        self.start_y = None
        self.current_shape = None  # Đối tượng shape đang vẽ tạm thời

        self.setup_ui()
        self.bind_events()

    def setup_ui(self):
        # Thanh công cụ
        tool_frame = tk.Frame(self.root)
        tool_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Màu
        colors = ["black", "red", "green", "blue", "orange", "purple"]
        for color in colors:
            tk.Button(tool_frame, text=color.capitalize(), bg=color, fg="white",
                      command=lambda c=color: self.set_color(c)).pack(side=tk.LEFT, padx=2)

        # Công cụ vẽ
        tk.Button(tool_frame, text="Vẽ tự do", command=lambda: self.set_tool("draw")).pack(side=tk.LEFT, padx=5)
        tk.Button(tool_frame, text="Đường thẳng", command=lambda: self.set_tool("line")).pack(side=tk.LEFT)
        tk.Button(tool_frame, text="Chữ nhật", command=lambda: self.set_tool("rect")).pack(side=tk.LEFT)
        tk.Button(tool_frame, text="Hình tròn", command=lambda: self.set_tool("circle")).pack(side=tk.LEFT)

        # Xóa
        tk.Button(tool_frame, text="Xóa màn hình", command=self.clear_canvas).pack(side=tk.RIGHT, padx=10)

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def set_tool(self, tool):
        self.current_tool = tool

    def set_color(self, color):
        self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.current_tool == "draw":
            self.current_shape = self.canvas.create_line(event.x, event.y, event.x+1, event.y+1,
                                                         fill=self.current_color, width=2, capstyle=tk.ROUND, smooth=True)

    def on_mouse_drag(self, event):
        if self.current_tool == "draw":
            # Nối thêm điểm vào đường vẽ
            coords = self.canvas.coords(self.current_shape)
            coords.extend([event.x, event.y])
            self.canvas.coords(self.current_shape, *coords)

        elif self.current_tool in ("line", "rect", "circle"):
            if self.current_shape:
                self.canvas.delete(self.current_shape)

            if self.current_tool == "line":
                self.current_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                                             fill=self.current_color, width=2)

            elif self.current_tool == "rect":
                self.current_shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y,
                                                                  outline=self.current_color, width=2)

            elif self.current_tool == "circle":
                # Tính bán kính từ đường chéo
                # r = math.hypot(event.x - self.start_x, event.y - self.start_y)
                # self.current_shape = self.canvas.create_oval(self.start_x - r, self.start_y - r,
                #                                              self.start_x + r, self.start_y + r,
                #                                              outline=self.current_color, width=2)
                self.current_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y,
                                                             outline=self.current_color, width=2)

    def on_button_release(self, event):
        self.current_shape = None  # Hoàn tất vẽ


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()



#Class PaintApp:
    #Init
        #Setup_UI
        #Setup_Canvas
        #Setup_BindSuKien
#SetTool
#SetColor
#OnButtonPress
#OnMouseDrag
#OnButtonRelease