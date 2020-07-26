import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkinter import *
import os
import csv

class GUI:

    def __init__(self, master):
        window.title("Histogram Maker")
        window.geometry('500x200')
        #window["bg"] = "green"
        #master["bg"] = "grey"
        # Label
        self.lbl = Label(window, text="Select CSV File:")
        self.lbl.grid(column=0, row=0)
        self.btn = Button(window, text=" Browse.. ", command=self.browse_file, bg="cyan")
        self.btn.grid(column=1, row=0)
        self.lbl_file = Label(window, text="")
        self.lbl_file.grid(column=0, row=1, columnspan=20)
        self.lbl_mean = Label(window, text="Mean:")
        self.lbl_mean.grid(column=0, row=2)
        self.lbl_median = Label(window, text="Median:")
        self.lbl_median.grid(column=0, row=3)
        # go button
        self.color_btn = Button(window, text="plot as histogram>>", command=self.plot)
        self.color_btn.grid(row=4, column=0)

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

            filepath = self.lbl_file.cget("text")
            filename = filepath.split("/")[-1]
            print(filepath)
            data = pd.read_csv(filepath)
            self.lbl_median.configure(text="Median: " + str(np.median(data['RSSI'])))
            self.lbl_mean.configure(text="Mean: " + str(np.mean(data['RSSI'])))

    def plot(self):
        filepath = self.lbl_file.cget("text")
        if len(filepath) == 0:
            messagebox.showinfo('File did not select....', 'Select a CSV File.....')
        else:
            filename = filepath.split("/")[-1]
            print(filepath)
            data=pd.read_csv(filepath)
            #data['RSSI'].plot(kind='hist')
            plt.figure(figsize=(20, 10))
            #plt.figure(figsize=(20, 10))
            plt.ylabel('Frequency')
            plt.xlabel('RSSI')
            plt.title(filename)
            bins=[x for x in range(min(data['RSSI']),max(data['RSSI'])+1)]
            plt.hist(data['RSSI'], bins, rwidth=.8)
            plt.xticks(bins)
            plt.show()

window = Tk()
GUI(window)
window.mainloop()