import tkinter as t


class PaintApp :
    def __init__(self, root):
        self.root = root
        self.root.title("Paint app")
        
        self.color = "black"
        self.brush_size = 4
        
        self.canvas = t.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack()
        
        self.canvas.bind("<B1-Motion>", self.Paint)
        
        self.Setup_Canvas
        
    def Paint(self, event):
        x1 = event.x 
    
    

        
        
        
        
            
        
        



sc = t.Tk()
sc.mainloop()