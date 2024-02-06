import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.text_area = tk.Text(root, wrap="word", undo=True)
        self.text_area.pack(expand="yes", fill="both")
