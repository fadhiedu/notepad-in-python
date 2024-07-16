import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad_by_Fadhi")
        self.root.configure(bg="#333333")

        self.text_area = tk.Text(self.root, width=80, height=20, bg="#333333", fg="#FFFFFF", font=("Arial", 12))
        self.text_area.pack(fill="both", expand=True)

        self.menu_bar = tk.Menu(self.root, bg="#333333", fg="#FFFFFF")
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open...", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.root.config(menu=self.menu_bar)

    def new_file(self):
        self.text_area.delete(1.0, "end")

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, "end")
                self.text_area.insert("end", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title="Save File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end-1c"))

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(title="Save As", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end-1c"))

    def cut_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        self.text_area.delete("sel.first", "sel.last")

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste_text(self):
        self.text_area.insert("insert", self.text_area.clipboard_get())

    def select_all_text(self):
        self.text_area.tag_add("sel", "1.0", "end")

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()