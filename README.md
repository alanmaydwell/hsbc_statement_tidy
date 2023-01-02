# Statement Tidy
Originally created to enable convenient copy/paste of details from own bank statements on the HSBC website into a LibreOffice spreadsheet.
However, this is no longer possible as from February 2021 the transactions are no longer available within the website, as statements are now only offered as PDF downloads.

When they were present the values are were tab-separated but they each had a descriptive prefix which I didn't want (Date, Description, Amount, Balance), e.g. a date is copied as **"Date17 Jan 20"** when I want just **"17 Jan 20"**.

This was a solution to this problem but no longer can be used. Now added:

- `bank_csv_file_to_clipboard.py`as alternative way to get the data by extracting from downloaded 'midata' csv file.
- `midata_export.py` as a newer more convenient way of processing the 'midata' file by beaking its contents into its constituent months and then adding the extracted details to the clipboard.

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

## midata_export.py
Another way of extracting details from 'midata' csv file.

- Either (a) specify the midata filename near the end of the file or (b) pass the filename as a command-line argument.
- When run, the details are separated by month, with heading and total for each, and placed all together as comma-separated text in the clipboard from where they can be pasted where you want.
