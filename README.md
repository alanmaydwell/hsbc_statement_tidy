# Statement Tidy
I want to be able to conveniently copy/paste details from my bank statements on the HSBC website into a LibreOffice spreadsheet.

The values are tab-separated, so this works but they each have a descriptive prefix which I don't want (Date, Description, Amount, Balance), e.g. a date is copied as **"Date17 Jan 20"** when I want just **"17 Jan 20"**.

This is a solution to this problem.

However, from February 2021 it no longer seems possible to even access these values as there's no longer an option to display the statement values on the web page (only option is PDF download).  Now added `bank_csv_file_to_clipboard.py`as alternative way to get the data by extracting from downloaded csv file.

## statement_tidy.py
- Written in Python 3 but might work with Python 2
- Uses only standard library.

### How to use

1. Create an empty text file in the same directory as **statement_tidy.py**. The filename needs to have a .tsv extension and should not start with "new".
2. Copy/paste statement contents from web page into the text file and save the file.For an example see `example.tsv`.
3. Run statement_tidy.py. It will process any .tsv files in
same directory that don't start "new". If there are multiple files it will process all of them.
4. A new version of each qualifying file is created with "new_" at the start
of its name and content with the prefixes removed. Its contents can be copy/pasted into a spreadsheet.

## clipconv.py
- Written in Python 3 but might work with Python 2
- Requires **pyperclip** module.

### How to use

More convenient way of removing the prefixes that works directly with the clipboard.

1. Copy statement contents from web page to clipboard.
2. Run clipconv.py. This reads data from clipboard, processes it and then writes the modified text back to the clipboard. If successful there is a message confirming the number of characters copied to the clipboard.
3. Paste modified values directly into spreadsheet.

## `bank_csv_file_to_clipboard.py`
- Copies data from downloaded CSV file to clipboard as tab-separated values.
- Values extracted between specified start and end date range 
- Written in Python 3 but might work with Python 2
- Requires **pyperclip** module.

### How to use
1. Download "midata" CSV file and place it in same directory as `bank_csv_file_to_clipboard.py`
2. Within `bank_csv_file_to_clipboard.py` set the filename and start date/ end date in the `if __name__ == "__main__"` block at its end.
3. Run ``bank_csv_file_to_clipboard.py`
4. Values should now be in clipboard in tab-separated format for pasting into spreadsheet.
5. Note `bank_csv_file_to_clipboard.py` (below) can help with the above.

## `bank_csv_gui.py`
Simple Tkinter GUI which can be used to run `bank_csv_file_to_clipboard.py`.
Note this lacks any checking for invalid values.
