# bookbot

Small script that counts words and letters in a text file and prints a simple report.

Quick use
1. Put a .txt file in the repo (there are samples in the books/ folder).
2. Run:
   ```
   python3 main.py <path/to/book.txt>
   ```
   e.g. `python3 main.py books/frankenstein.txt`

What it does
- Prints total word count and a letter frequency list (letters lowercased and sorted by count).

Where the code is
- Main entry: [main.py](main.py) (calls the stats code)
- Counting logic: [stats.py](stats.py)