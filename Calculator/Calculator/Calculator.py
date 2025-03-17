
import tkinter as tk

class CalCulator:
    def __init__(self, root):
        self.root = root
        self.root.title("°è»ê±â")
        self.root.geometry("400x600")

        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)