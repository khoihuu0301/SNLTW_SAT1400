import tkinter as tk
from tkinter import messagebox
import math

# Function to solve the first degree equation (ax + b = 0)
def solve_first_degree(a, b):
    if a == 0:
        return "No solution" if b != 0 else "Infinite solutions"
    x = -b / a
    return x

# Function to solve the second degree equation (ax^2 + bx + c = 0)
def solve_second_degree(a, b, c):
    if a == 0:
        return "This is not a quadratic equation."
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:
        # One real solution
        x = -b / (2*a)
        return f"One real root: x = {x}"
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return f"Two complex roots: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i"

# Function to create the second window for solving the first degree equation
def open_first_degree_window():
    first_degree_window = tk.Toplevel(root)
    first_degree_window.title("First Degree Equation Solver")
    
    def solve_linear():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            result = solve_first_degree(a, b)
            result_label.config(text=f"Solution: {result}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
    
    tk.Label(first_degree_window, text="Enter value of a:").pack(pady=5)
    entry_a = tk.Entry(first_degree_window)
    entry_a.pack(pady=5)
    
    tk.Label(first_degree_window, text="Enter value of b:").pack(pady=5)
    entry_b = tk.Entry(first_degree_window)
    entry_b.pack(pady=5)
    
    solve_button = tk.Button(first_degree_window, text="Solve", command=solve_linear)
    solve_button.pack(pady=20)
    
    result_label = tk.Label(first_degree_window, text="Solution:")
    result_label.pack(pady=10)

# Function to create the second window for solving the second degree equation
def open_second_degree_window():
    second_degree_window = tk.Toplevel(root)
    second_degree_window.title("Second Degree Equation Solver")
    
    def solve_quadratic():
        try:
            a = float(entry_a2.get())
            b = float(entry_b2.get())
            c = float(entry_c2.get())
            result = solve_second_degree(a, b, c)
            result_label2.config(text=f"Solution: {result}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
    
    tk.Label(second_degree_window, text="Enter value of a:").pack(pady=5)
    entry_a2 = tk.Entry(second_degree_window)
    entry_a2.pack(pady=5)
    
    tk.Label(second_degree_window, text="Enter value of b:").pack(pady=5)
    entry_b2 = tk.Entry(second_degree_window)
    entry_b2.pack(pady=5)
    
    tk.Label(second_degree_window, text="Enter value of c:").pack(pady=5)
    entry_c2 = tk.Entry(second_degree_window)
    entry_c2.pack(pady=5)
    
    solve_button2 = tk.Button(second_degree_window, text="Solve", command=solve_quadratic)
    solve_button2.pack(pady=20)
    
    result_label2 = tk.Label(second_degree_window, text="Solution:")
    result_label2.pack(pady=10)

# Main window to select the type of equation to solve
root = tk.Tk()
root.title("Equation Solver")

tk.Label(root, text="Select the type of equation to solve", font=("Arial", 16)).pack(pady=20)

btn_linear = tk.Button(root, text="Solve First Degree (Linear) Equation", width=30, height=2, command=open_first_degree_window)
btn_linear.pack(pady=10)

btn_quadratic = tk.Button(root, text="Solve Second Degree (Quadratic) Equation", width=30, height=2, command=open_second_degree_window)
btn_quadratic.pack(pady=10)

root.mainloop()