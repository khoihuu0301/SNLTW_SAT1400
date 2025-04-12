import tkinter as tk
from tkinter import messagebox
import math

class QuadraticSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quadratic Equation Solver")

        # Predefined layout variables for consistent placement
        self.x = 10  # X-coordinate for labels
        self.Tx = 120  # Offset for entry fields
        self.Tlbly = 30  # Vertical spacing between rows
        self.widthEntry = 15  # Width of entry fields
        self.width = 10  # Button width

        # Title label
        self.label_title = tk.Label(self.master, text="Enter coefficients for ax² + bx + c = 0")
        self.label_title.place(x=self.x, y=self.Tlbly * 0)

        # Coefficient inputs
        self.label_a = tk.Label(self.master, text="a:")
        self.label_a.place(x=self.x, y=self.Tlbly * 1)
        self.entry_a = tk.Entry(self.master, width=self.widthEntry)
        self.entry_a.place(x=self.x + self.Tx, y=self.Tlbly * 1)

        self.label_b = tk.Label(self.master, text="b:")
        self.label_b.place(x=self.x, y=self.Tlbly * 2)
        self.entry_b = tk.Entry(self.master, width=self.widthEntry)
        self.entry_b.place(x=self.x + self.Tx, y=self.Tlbly * 2)

        self.label_c = tk.Label(self.master, text="c:")
        self.label_c.place(x=self.x, y=self.Tlbly * 3)
        self.entry_c = tk.Entry(self.master, width=self.widthEntry)
        self.entry_c.place(x=self.x + self.Tx, y=self.Tlbly * 3)

        # Solve button
        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve_quadratic, width=self.width)
        self.solve_button.place(x=self.x + 190, y=self.Tlbly * 4)

        # Result label
        self.result = tk.StringVar()
        self.result_label = tk.Label(self.master, textvariable=self.result, fg="blue")
        self.result_label.place(x=self.x, y=self.Tlbly * 5)

    def solve_quadratic(self):
        """Solve the quadratic equation and display the result."""
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            
            if a == 0:
                messagebox.showerror("Invalid Input", "Coefficient 'a' cannot be 0.")
                return
            
            discriminant = b**2 - 4*a*c
            
            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                self.result.set(f"Roots are real and different:\nRoot 1: {root1:.2f}, Root 2: {root2:.2f}")
            elif discriminant == 0:
                root = -b / (2 * a)
                self.result.set(f"Roots are real and the same:\nRoot: {root:.2f}")
            else:
                self.result.set("Roots do not exist.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuadraticSolverApp(root)
    root.mainloop()
