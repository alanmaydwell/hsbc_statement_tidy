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


if __name__ == "__main__":
    filename = "midata7885.csv"
    start_date = "15/01/2021"
    end_date = "15/02/2021"
    date_range_to_clipboard(filename, start_date, end_date)

