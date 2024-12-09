import tkinter as tk
from tkinter import messagebox
import random

class NormalCalculator:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return self.num1 / self.num2

class BooleanCalculator(NormalCalculator):
    def __init__(self, bit1, bit2):
        if bit1 not in [0, 1] or bit2 not in [0, 1]:
            raise ValueError("Bits must be 0 or 1!")
        super().__init__(bit1, bit2)

    def add(self):
        result = super().add()
        return 1 if result == 2 else result

    def subtract(self):
        result = super().subtract()
        return 1 if result == -1 else result

    def divide(self):
        raise NotImplementedError("Division not supported in Boolean Calculator!")

def calculate():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        operation = operation_var.get()

        if calc_type_var.get() == "Boolean":
            calc = BooleanCalculator(num1, num2)
        else:
            calc = NormalCalculator(num1, num2)

        if operation == "Add":
            result = calc.add()
        elif operation == "Subtract":
            result = calc.subtract()
        elif operation == "Multiply":
            result = calc.multiply()
        elif operation == "Divide":
            result = calc.divide()

        result_label.config(text=f"Result: {result}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Calculator")

tk.Label(app, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

tk.Label(app, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar(app)
operation_var.set("Add")
tk.OptionMenu(app, operation_var, "Add", "Subtract", "Multiply", "Divide").grid(row=2, column=1)

calc_type_var = tk.StringVar(app)
calc_type_var.set("Normal")
tk.Radiobutton(app, text="Normal", variable=calc_type_var, value="Normal").grid(row=3, column=0)
tk.Radiobutton(app, text="Boolean", variable=calc_type_var, value="Boolean").grid(row=3, column=1)

tk.Button(app, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2)

result_label = tk.Label(app, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

app.mainloop()