# pdf-file-scanner

Duplicate File Scanner
A simple Python application that helps you find and manage duplicate files on your computer.
Show Image
Features

Easy-to-use graphical interface - No command line knowledge required
Fast scanning - Uses MD5 hashing algorithm to efficiently identify duplicates
Selective deletion - Choose which duplicate files to remove
Safe operation - Confirmation dialog before any deletion occurs

# Requirements

- Python3 or higher
- Tkinter (usually comes pre-installed with Python)

# Installation

- Clone this repository or download the script:

- bashgit clone https://github.com/Ashley-Programmer/duplicate-file-scanner.git

- No additional packages are required as this application uses only Python standard libraries.

# Usage

- Run the script:

bashpython duplicate_file_scanner.py

Click the "Scan for Duplicates" button and select a folder to scan.
The application will recursively search through the selected folder and all its subfolders.
Any duplicate files found will be displayed as a list of checkboxes.
Select the files you want to delete and click the "Delete Selected" button.
Confirm the deletion when prompted.

# How It Works

The application walks through the directory tree of the selected folder.
For each file, it calculates an MD5 hash of the file contents.
It keeps track of files with identical hashes in a dictionary.
Files with matching hashes are identified as duplicates.
The user can then select which duplicates to remove.

# Known Limitations

Very large files might take longer to hash.
The application does not compare file names or dates, only content.
There's currently no way to export the list of duplicates.

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

- No duplicates found: Make sure you're scanning a folder that might contain duplicates.
- Error hashing file: This usually occurs with system files or files that are currently in use.
- Cannot delete file: The file might be in use by another program. Close the program and try again.

# Future Improvements

- Add ability to export list of duplicates
- Implement more hash algorithms for comparison
- Add file preview capability
- Create portable executable versions for Windows/Mac
