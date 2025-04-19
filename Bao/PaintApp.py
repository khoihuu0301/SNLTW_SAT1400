import tkinter as tk
from tkinter import colorchooser

class PaintApp:
     def __init__(self, root):
          self.root = root
          self.root.title("Paint App")
          self.root.geometry("900x700")

          self.color = "black"
          self.fill_color = "white"  # Default fill color
          self.brush_size = 5
          self.draw_mode = "free"  # Default mode is free drawing

          self.canvas = tk.Canvas(root, bg="white", width=800, height=500)
          self.canvas.pack(pady=20)

          self.canvas.bind("<B1-Motion>", self.paint)
          self.canvas.bind("<ButtonPress-1>", self.start_draw)
          self.canvas.bind("<ButtonRelease-1>", self.end_draw)

          self.controls_frame = tk.Frame(root)
          self.controls_frame.pack()

          self.color_button = tk.Button(self.controls_frame, text="Choose Outline Color", command=self.choose_color)
          self.color_button.grid(row=0, column=0, padx=10)

          self.fill_color_button = tk.Button(self.controls_frame, text="Choose Fill Color", command=self.choose_fill_color)
          self.fill_color_button.grid(row=0, column=1, padx=10)

          self.size_label = tk.Label(self.controls_frame, text="Brush Size:")
          self.size_label.grid(row=0, column=2, padx=10)

          self.size_slider = tk.Scale(self.controls_frame, from_=1, to=20, orient="horizontal", command=self.change_brush_size)
          self.size_slider.set(self.brush_size)
          self.size_slider.grid(row=0, column=3, padx=10)

          self.clear_button = tk.Button(self.controls_frame, text="Clear Canvas", command=self.clear_canvas)
          self.clear_button.grid(row=0, column=4, padx=10)

          self.free_draw_button = tk.Button(self.controls_frame, text="Free Draw", command=lambda: self.set_draw_mode("free"))
          self.free_draw_button.grid(row=0, column=5, padx=10)

          self.circle_button = tk.Button(self.controls_frame, text="Draw Circle", command=lambda: self.set_draw_mode("circle"))
          self.circle_button.grid(row=0, column=6, padx=10)

          self.rect_button = tk.Button(self.controls_frame, text="Draw Rectangle", command=lambda: self.set_draw_mode("rectangle"))
          self.rect_button.grid(row=0, column=7, padx=10)

          self.start_x = None
          self.start_y = None
          self.temp_shape = None  # Temporary shape ID

     def paint(self, event):
          if self.draw_mode == "free":
               x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
               x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
               self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
          elif self.draw_mode in ["circle", "rectangle"] and self.start_x and self.start_y:
               if self.temp_shape:
                    self.canvas.delete(self.temp_shape)  # Remove previous temporary shape

               x1, y1 = self.start_x, self.start_y
               x2, y2 = event.x, event.y

               if self.draw_mode == "circle":
                    self.temp_shape = self.canvas.create_oval(x1, y1, x2, y2, outline=self.color, width=self.brush_size, fill=self.fill_color)
               elif self.draw_mode == "rectangle":
                    self.temp_shape = self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.color, width=self.brush_size, fill=self.fill_color)

     def start_draw(self, event):
          if self.draw_mode in ["circle", "rectangle"]:
               self.start_x, self.start_y = event.x, event.y

     def end_draw(self, event):
          if self.temp_shape:
               self.canvas.delete(self.temp_shape)  # Remove temporary shape
               self.temp_shape = None

          if self.draw_mode == "circle" and self.start_x and self.start_y:
               x1, y1 = self.start_x, self.start_y
               x2, y2 = event.x, event.y
               self.canvas.create_oval(x1, y1, x2, y2, outline=self.color, width=self.brush_size, fill=self.fill_color)
          elif self.draw_mode == "rectangle" and self.start_x and self.start_y:
               x1, y1 = self.start_x, self.start_y
               x2, y2 = event.x, event.y
               self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.color, width=self.brush_size, fill=self.fill_color)

     def choose_color(self):
          self.color = colorchooser.askcolor(color=self.color)[1]

     def choose_fill_color(self):
          self.fill_color = colorchooser.askcolor(color=self.fill_color)[1]

     def change_brush_size(self, value):
          self.brush_size = int(value)

     def clear_canvas(self):
          self.canvas.delete("all")

     def set_draw_mode(self, mode):
          self.draw_mode = mode

if __name__ == "__main__":
     root = tk.Tk()
     app = PaintApp(root)
     root.mainloop()