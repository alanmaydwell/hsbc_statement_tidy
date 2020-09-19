#!/usr/bin/env python3

"""
Removes descriptive prefixes from bank statement details copied
from HSBC website.

e.g. Changes "Amount-10.00" to "-10.00"

Use a follows:
1. Copy/paste statment contents from web page to a text file
2. Give the filename a .tsv extension and NOT "new" at start.
3. Save the file to same directory as statement_tidy.py
4. Run statement_tidy.py. It will process any .tsv files in
same directory that don't start "new".
5. A new version of the file is created with "new_" at start
of its name and the content has prefixes removed. 
"""

import os

def hsbc_tidy(content):
    """
    Tidy up and return statement details that have been copied
    to clipboard from HSBC website.

    Pasted values are tab-separated (useful) but have
    annoying prefixes (e.g. dates have "Date" in front).
    This function strips the prefixes and returns the modified
    text.
    
    Args:
        content: text to be processed
    Returns:
        Tidied text
    """
    # Holder for tidied text
    tidied_text = ""
    # Unwanted prefixes for each tsv column, in order
    unwanted_prefixes = ["Date", "Description", "Amount", "Balance"]
    # Examine each line in turn from original content
    for line in content.splitlines():
        # Convert from tsv str to list
        items = line.split("\t")
        # Skip any single-value text lines and the initial "blank" lines 
        if len(items) > 2:
            # Remove unwanted prefix from each item in list
            for i, (item, prefix) in enumerate(zip(items, unwanted_prefixes)):
                items[i] = item.lstrip(prefix)
            # Add modified line to tidied text
            tidied_text += "\t".join(items) + "\n"
    return tidied_text


def read_file(filename):
    with open(filename, "r") as infile:
        text = infile.read()
    return text

def save_text(filename, content, new_prefix="new_"):
    newfilename = new_prefix + filename
    with open(newfilename, "w") as outfile:
        outfile.write(content)
    print("Created:", newfilename)


if __name__ == "__main__":
    #Process whole directory
    files = [f for f in os.listdir(os.getcwd())
             if f.endswith(".tsv")
             and not f.startswith("new")]
    for f in files:
        file_content = read_file(f)
        new_text = hsbc_tidy(file_content)
        save_text(f, new_text)
