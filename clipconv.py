#!/usr/bin/env python3

"""
Use statement_tidy to process text from clipboard
then copy the processed text back to the clipboard.
"""

import pyperclip
from statement_tidy import hsbc_tidy

clip_content = pyperclip.paste()

if clip_content:
    revised_content = hsbc_tidy(clip_content)
    if revised_content:
        pyperclip.copy(revised_content)
        print("{} characters copied to clipboard.".format(len(revised_content)))
    else:
        print("Clipboard has content but response empty.")
else:
    print("Nothing found in clipboard")
