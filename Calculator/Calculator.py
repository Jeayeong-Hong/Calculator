
import tkinter as tk

class CalCulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for (text, row, col) in buttons:
            button =tk.Button(self.root, text=text, font=("Areal",18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
    
    def on_button_click(self, button_text):
        current = self.display.get()

        if button_text == "=":
            try:
                result = str(eval(current))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "error")
        elif button_text == "C":
            self.display.delete(0,tk.END)
        else:
            self.display.insert(tk.END, button_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = CalCulator(root)
    root.mainloop()
