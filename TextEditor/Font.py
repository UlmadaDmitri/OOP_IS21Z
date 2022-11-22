from tkinter import *
from tkinter import font


class Font:
    window = None
    inputs = []
    font_size = None
    fonts = None
    current_settings = {
        'font': 'System',
        'size': '10',
        'style': 'normal'
    }

    def __init__(self, window, display):
        self.main_window = window
        self.families = list(font.families())
        self.radio_var = StringVar()
        self.display = display

    def open(self):
        self.window = Toplevel(self.main_window)
        self.window.title('Font')
        self.window.resizable(False, False)
        self.window.grab_set()
        self.window.focus_set()

        self.make_font_select()
        self.make_font_style()
        self.make_font_size()
        self.make_buttons()

    def make_font_select(self):
        frame = Frame(self.window)
        self.fonts = Listbox(frame, width=35, font=('System', 10))
        label = Label(frame, text='Font-Family:', font=('System', 10))

        for i in self.families:
            self.fonts.insert(END, i)
        label.pack(side=TOP)
        index = self.families.index(self.current_settings['font'])
        self.fonts.select_set(index)
        self.fonts.see(index)
        self.fonts.pack(side=TOP)
        frame.pack(side=LEFT, fill=Y, padx=10)

    def make_font_style(self):
        frame = Frame(self.window)
        label = Label(frame, text='Font-Style:', font=('System', 10))
        label.pack(side=TOP)
        self.radio_var.set(self.current_settings['style'])
        font_styles = ['normal', 'bold', 'italic']
        radio = []

        for i in font_styles:
            radio.append(Radiobutton(frame, variable=self.radio_var, text=i.title(), value=i, font=('System', 10)))
            radio[-1].pack(side=TOP)
        frame.pack(side=LEFT, fill=Y, padx=10)

    def make_font_size(self):
        var = StringVar()
        frame = Frame(self.window)
        label = Label(frame, text='Font-Size:', font=('System', 10))
        self.font_size = Spinbox(frame, textvariable=var, from_=1, to=100, font=('System', 10))
        var.set(self.current_settings['size'])
        label.pack(side=TOP)
        self.font_size.pack(side=TOP)
        frame.pack(side=LEFT, fill=Y, padx=10)

    def make_buttons(self):
        frame = Frame(self.window)
        save = Button(frame, text='Save', command=self.save_font, font=('System', 11))
        cancel = Button(frame, text='Cancel', command=self.window.destroy, font=('System', 11))
        save.pack(side=LEFT, padx=5, pady=5)
        cancel.pack(side=LEFT, padx=5, pady=5)
        frame.pack(side=BOTTOM, fill=Y)

    def save_font(self):
        self.current_settings['font'] = self.fonts.get(ACTIVE)
        self.current_settings['size'] = self.font_size.get()
        self.current_settings['style'] = self.radio_var.get()
        self.change_font()
        self.window.destroy()

    def change_font(self):
        self.display.configure(
            font=(self.current_settings['font'], self.current_settings['size'], self.current_settings['style']))
