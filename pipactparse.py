import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkinter import *
import os
import csv

class GUI:

    def __init__(self, master):
        window.title("Image Colorize Demo")
        window.geometry('650x400')
        window["bg"] = "green"
        master["bg"] = "grey"
        # Label
        self.lbl = Label(window, text="Select Image File:")
        self.lbl.grid(column=0, row=0)
        self.btn = Button(window, text=" Browse.. ", command=self.browse_file, bg="cyan")
        self.btn.grid(column=1, row=0)
        self.lbl_file = Label(window, text="")
        self.lbl_file.grid(column=2, row=0, columnspan=20)

        # go button
        self.color_btn = Button(window, text="plot >>", command=self.plot)
        self.color_btn.grid(row=1, column=11)

        for child in window.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def browse_file(self):
        filename = filedialog.askopenfilename(title="Select file",
                                              filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        if len(filename) == 0:
            messagebox.showinfo('File did not select....', 'Select a CSV File.....')
        else:
            print(filename)
            self.lbl_file.configure(text=filename)
            print(os.path.dirname(filename))

    def plot(self):
        filepath = self.lbl_file.cget("text")
        if len(filepath) == 0:
            messagebox.showinfo('File did not select....', 'Select a CSV File.....')
        else:
            filename = filepath.split("/")[-1]
            print(filepath)
            data=pd.read_csv('pipact.csv')
            data['RSSI'].plot(kind='hist')
            plt.show()
            plt.ylabel('Frequency')
            plt.xlabel('RSSI')

window = Tk()
GUI(window)
window.mainloop()