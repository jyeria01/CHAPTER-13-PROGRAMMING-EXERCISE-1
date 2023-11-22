# Import the tkinter module
import tkinter

# name_and_address_gui.py

import tkinter

class NameAndAddressGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Personal Information')

        self.info_var = tkinter.StringVar()
        self.info_label = tkinter.Label(self.main_window, textvariable=self.info_var, font=('Arial', 12))
        self.show_info_button = tkinter.Button(self.main_window, text='SHOW INFO', command=self.show_info)
        self.quit_button = tkinter.Button(self.main_window, text='QUIT', command=self.main_window.destroy)

        self.info_label.pack(pady=20)
        self.show_info_button.pack(side='left', padx=10)
        self.quit_button.pack(side='right', padx=10)

        tkinter.mainloop()

    def show_info(self):
        self.info_var.set('Santa Claus\n123 Elf Road \nNorth Pole, 88888')

if __name__ == '__main__':
    display_info_gui = NameAndAddressGUI()