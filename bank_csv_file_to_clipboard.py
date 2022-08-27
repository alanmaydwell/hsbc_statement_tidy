#!/usr/bin/env python3
"""
Extract values between date range from bank statement csv file and convert them
to tsv values in clipboard. Idea is for convenient pasting into spreadsheet.
"""

import time
import pyperclip

def csv_read(filename="midata7885.csv", separator=","):
    """Read data from CSV file. Return list of headings and
    list of lists of values.
    Assumes first non-empty row contains headings.
    Intended to use with CSV file downloaded from HSBC"""
    headings = []
    values = []    
    # encoding value used below to remove "byte order mark" (\ufeff) from file
    with open(filename, "r", encoding='utf-8-sig') as csv_file:
        for row in csv_file:
            row_values = [r.strip() for r in row.strip().split(separator)]
            if row_values:
                if not headings:
                    headings = row_values
                else:
                    values.append(row_values)
    print("Values read from file:", len(values))
    return headings, values
    

def to_date(value, format="%d/%m/%Y"):
    """Convert date from string to date as time.struct_time.
    Defaults to 01/01/1900 if value error encountered on conversion.
    """
    try:
        date = time.strptime(value, format)
    except ValueError:
        date = time.strptime("01/01/1900", "%d/%m/%Y")
    return date


def date_range_values(values, start="15/01/2021", end="15/02/2021"):
    """Extract and return values between start and end date limits
    Relies on date being 1st element in each list.
    """
    start_date = to_date(start)
    end_date = to_date(end)
    filtered = [v for v in values
                if to_date(v[0]) >= start_date
                and to_date(v[0]) <= end_date]
    return filtered


def values_to_string(values):
    """Convert list of lists to tsv string"""
    text = ""
    for row in values:
        text = text + "\t".join(row) + "\n"
    return text

def date_range_to_clipboard(filename, start_date, end_date, reverse=True):
    headings, values = csv_read(filename)
    if reverse:
        values.reverse()
    drv = date_range_values(values, start_date, end_date)
    drvstr = values_to_string(drv)
    pyperclip.copy(drvstr)
    print("Copied {} items from {} to {} to clipboard.".format(len(drv), start_date, end_date))



class BankCSVExtract:
    def __init__(self, filename, file_date_format=""):
        """
        Extract parts of "MI Data" CSV file from a bank over chosed date ranges
        Args:
            filename: filename of the csv file
            file_date_format: optional format of dates in the csv file. Will try to auto
                              detect if no value supplied.
        """
        self.filename = filename
        self.headings, self.values = csv_read(self.filename)
        
        # Find date position in file (default to leftmost)
        date_index = 0
        if "Date" in self.headings:
            date_index = self.headings.index("Date")
        self.date_index = date_index
        # Use supplied date format, otherwise detect it
        if file_date_format:
            self.file_date_format = file_date_format
        else:
            self.file_date_format = self.auto_set_date_format()

    def auto_set_date_format(self):
        """
        Automatically set the file date format by examining a date from the file
        Looks for first date in imported values and try to detect its format as either
        "%Y/%m/%d" or "%d/%m/%Y" and return the result. Note also auto detects separator,
        so not necessarily "/"
        Home made - could try dateutil.parser as alternative
        """
        eg_date = self.values[0][self.date_index]
        # Extract each numerical part of the date
        separator = [c for c in eg_date if not (c.isdigit() or c.isalpha())][0]
        date_components = eg_date.split(separator)
        # Set either "%d/%m/%Y" or %Y/%m/%d" based on possition of 4 character element
        if len(date_components[0]) == 4:
            date_format = f"%Y{separator}%m{separator}%d"
        else:
            date_format = f"%d{separator}%m{separator}%Y"
        return date_format   
        
    def extract(self, start_date, end_date, range_date_format="%d/%m/%Y"):
        """Extract and return values within chosen date range
        Args:
            start_date: start of date range (str)
            end_date: end of date range (str)
            range_date_format: optional date format for both the above,
                               defaults to %d/%m/%Y
        """
        # Do something here. Need date format setting
        start_date = to_date(start_date, range_date_format)
        end_date = to_date(end_date, range_date_format)
        filtered = [v for v in self.values
                    if to_date(v[self.date_index], self.file_date_format) >= start_date
                    and to_date(v[self.date_index], self.file_date_format) <= end_date]        
        return filtered


if __name__ == "__main__":
    #filename = "midata7885.csv"
    #start_date = "15/01/2021"
    #end_date = "15/02/2021"
    #date_range_to_clipboard(filename, start_date, end_date)
    thing = BankCSVExtract("miDataTransactions(31Jul22).csv")
    bog = thing.extract("01/06/2022", "01/07/2022")
