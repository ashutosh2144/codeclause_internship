import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import re


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.file_path = None

        self.create_menu()
        self.create_text_area()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Word Count", command=self.count_words)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def create_text_area(self):
        self.text_area = ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')
        self.text_area.bind("<KeyRelease>", self.syntax_highlight)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
                self.file_path = file_path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.file_path = file_path

    def exit(self):
        self.root.quit()

    def count_words(self):
        text = self.text_area.get(1.0, tk.END)
        words = text.split()
        word_count = len(words)
        messagebox.showinfo("Word Count", f"Total words: {word_count}")

    def syntax_highlight(self, event=None):
        text = self.text_area.get(1.0, tk.END)
        self.text_area.tag_remove("keyword", "1.0", tk.END)

        keywords = ("if", "else", "elif", "for", "while", "def", "class", "import", "from", "return")
        for keyword in keywords:
            matches = re.finditer(r"\b" + re.escape(keyword) + r"\b", text)
            for match in matches:
                start = "1.0 + {} chars".format(match.start())
                end = "1.0 + {} chars".format(match.end())
                self.text_area.tag_add("keyword", start, end)

        self.text_area.tag_config("keyword", foreground="blue")


def main():
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()