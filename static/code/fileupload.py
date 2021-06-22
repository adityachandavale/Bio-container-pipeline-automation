import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
root.lift()
root.focus_force()
path = filedialog.askopenfilename(parent=root)