#!/usr/bin/env python3
"""
Simple Tkinter GUI for bank_csv_file_to_clipboard.py
"""

# Note tkinter module names are lower case with Python 3
import tkinter as tk
import tkinter.filedialog

from bank_csv_file_to_clipboard import date_range_to_clipboard

class StatementGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Statement data to clipboard")
        self.create_widgets()
        
    def create_widgets(self):
        # Label and entry for CSV file path
        self.filename_label = tk.Label(text="Filename")
        self.filename_label.grid()
        self.filename_field = tk.Entry()
        self.filename_field.grid(column=1, row=0)
        # Label and entry for start date
        self.start_date_label = tk.Label(text="Start Date")
        self.start_date_label.grid(column=0, row=1)
        self.start_date_entry = tk.Entry()
        self.start_date_entry.grid(column=1, row=1)
        # Label and entry for end date
        self.end_date_label = tk.Label(text="End Date")
        self.end_date_label.grid(column=0, row=2)
        self.end_date_entry = tk.Entry()
        self.end_date_entry.grid(column=1, row=2)
        # Button to use file selector to chose file
        self.file_button = tk.Button()
        self.file_button["text"] = "Select File"
        self.file_button["command"] = self.select_file
        self.file_button["fg"] = "Blue"
        self.file_button.grid(column=0, row=3)
        # Run button (defined more consisely than one above)
        self.run = tk.Button(text="Run", fg="green", command=self.process_file)
        self.run.grid(column=1, row=3)
        # Quit button
        self.quit = tk.Button(text="Quit", fg="red", command=self.master.destroy)
        self.quit.grid(column=2, row=3)

    def select_file(self):
        """Method called by file selector button
        Choose file and update displayed filename accordingly"""
        name= tkinter.filedialog.askopenfilename(title = "Select CSV file",
                                                 filetypes = (("csv files","*.csv"), ("all files","*.*")))
        print(name)
        self.filename_field.delete(0, -1)
        self.filename_field.insert(0, name)
        
    def process_file(self):
        """ Method called by Run button
        Process chosen filename using chosen dates"""
        filepath = self.filename_field.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        print(filepath, start_date, end_date)
        date_range_to_clipboard(filepath, start_date, end_date)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = StatementGui(root)
    root.mainloop()
