#!/usr/bin/env python3
"""
Can run this directly to process an "midata" file and export extracted details
to clipboard in csv format.

The csv filename to be imported can either be specified in the `if __name__ == "__main__"`
block at the end or passed as a command-line argument.
"""

import sys
import pyperclip
from bank_csv_file_to_clipboard import csv_read, to_date

class OrganisedValues:
    """
    Process values from "midata" CSV file with bank account transaction details
    downloaded from HSBC
    The file contains multiple months this can be used to split into months
    and also give a total +/- for all the transactions for that month.
    """
    def __init__(self, filename, date_format="%Y-%m-%d"):
        self.filename = filename
        self.date_format = date_format
        self.organised_values = []
        self.months_found = []
        headings, values = csv_read(filename)
        self.headings = headings
        self.organise_values(values)
        
    def organise_values(self, values):
        for row in values:
            date = to_date(row[0], self.date_format)
            month = f"{date.tm_year}-{date.tm_mon}"
            if month not in self.months_found:
                self.months_found.append(month)
            row_data = {"month": month, "date":date, "str_date": row[0], "type": row[1],
                        "description": row[2], "amount": row[3].replace("£", ""), "balance": row[4]}
            self.organised_values.append(row_data)
            
    def get_month_values(self, month):
        """
        Return all the rows that fall within the specified month
        Args:
            month: month within year in format like this: "2022-11"
        """
        wanted = [v for v in self.organised_values if v.get("month")==month]
        return wanted
    
    def get_sum(self, values):
        total = 0.00
        for row in values:
            total = total + float(row["amount"])
        return round(total, 2)
    
    def export_month(self, month):
        """
        Export specified month's transactions as a csv string
        Args:
            month: month within year in format like this: "2022-11"
        """
        wanted_values = self.get_month_values(month)
        total = self.get_sum(wanted_values)
        text = f"Transactions for:{month} Total:{total}\n"
        text += ",".join(self.headings) + "\n"
        for row in wanted_values:
            line = ",".join([str(v) for k, v in row.items() if k not in ("month", "date")])
            text += line+"\n"
        return text
    
    def export_all_months(self):
        """
        Return a single csv string containing transactions separated into
        all the months found within the imported values
        """
        text = f"Details extracted from: {self.filename}\n"
        for month in self.months_found:
            details = self.export_month(month)
            text += details + "\n"
        return text
            

if __name__ == "__main__":
    # Hard-coded filename replaced by command-line arg if supplied
    filename = "miDataTransactionsExample.csv"
    if sys.argv[1:2]:
        filename = sys.argv[1]
        
    values = OrganisedValues(filename)
    details = values.export_all_months()
    print(details)
    pyperclip.copy(details)
    print(f"Extracted details from '{filename}' and copied them to clipboard")
