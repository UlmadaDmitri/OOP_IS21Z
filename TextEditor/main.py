from tkinter import filedialog
from tkinter import messagebox

from Font import *


class TextRedactor:

    def __init__(self):
        self.window = Tk()
        self.make_bind()
        self.window.title('zxc TextEditor pre-alpha')
        self.menu_bar = Menu(self.window)
        self.window.config(menu=self.menu_bar)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.format_menu = Menu(self.menu_bar, tearoff=0)
        self.display = Text()
        self.display.pack(fill=BOTH, expand=1)
        self.font = Font(self.window, self.display)
        self.font.change_font()
        self.path = None
        self.make_template()

    def make_template(self):
        self.file_menu.add_command(label='New (Ctrl+N)', command=self.new_document)
        self.file_menu.add_command(label='New window (Ctrl+B)', command=self.new_window)
        self.file_menu.add_command(label='Open (Ctrl+O)', command=self.open_file)
        self.file_menu.add_command(label='Save (Ctrl+S)', command=self.save_file)
        self.file_menu.add_command(label='Save As (Ctrl+Q)', command=self.save_file_as)
        self.file_menu.add_command(label='Exit (Ctrl+X)', command=self.window.destroy)

        self.help_menu.add_command(label='Help (Ctrl+H)', command=self.help_info)
        self.help_menu.add_command(label='About (Ctrl+I)', command=self.about_info)

        self.format_menu.add_command(label='Font (Ctrl+F)', command=self.font.open)

        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.menu_bar.add_cascade(label='Format', menu=self.format_menu)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

    def make_bind(self):
        self.window.bind('<Control-s>', lambda e: self.save_file())
        self.window.bind('<Control-q>', lambda e: self.save_file_as())
        self.window.bind('<Control-n>', lambda e: self.new_document())
        self.window.bind('<Control-b>', lambda e: self.new_window())
        self.window.bind('<Control-o>', lambda e: self.open_file())
        self.window.bind('<Control-f>', lambda e: self.font.open())
        self.window.bind('<Control-x>', lambda e: self.window.destroy())
        self.window.bind('<Control-H>', lambda e: self.help_info())
        self.window.bind('<Control-I>', lambda e: self.about_info())

    def open_file(self):
        file_name = filedialog.askopenfilename()
        try:
            with open(file_name) as f:
                self.display.delete('1.0', END)
                self.display.insert('1.0', f.read(), END)
                self.change_title(file_name)
                self.path = file_name
        except OSError:
            pass

    def save_file_as(self):
        files = [
            ('All Files', '*.*'),
            ('Python Files', '*.py'),
            ('Text Document', '*.txt')
        ]
        save_as = filedialog.asksaveasfilename(filetypes=files, defaultextension=".txt")
        try:
            with open(save_as, "w") as f:
                f.write(self.display.get(1.0, END))
                self.path = save_as
                self.change_title(self.path)
        except OSError:
            pass

    def save_file(self):
        if not self.path:
            self.save_file_as()
        else:
            with open(self.path, 'w') as f:
                f.write(self.display.get(1.0, END))

    def new_document(self):
        self.display.delete('1.0', END)
        self.change_title('This is a new file')

    def new_window(self):
        new_window = Toplevel()
        new_window.title('Test')
        new_window.config(menu=self.menu_bar)

    def change_title(self, title):
        self.window.title(title)

    def help_info(self):
        messagebox.showinfo('Help', 'No help')

    def about_info(self):
        messagebox.showinfo('About', 'TextEditor by me.')

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    redactor = TextRedactor()
    redactor.run()
