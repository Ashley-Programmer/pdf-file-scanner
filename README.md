# Duplicate File Scanner

A simple GUI application that scans folders for duplicate files and allows you to delete them to free up disk space.

## Features

- Simple and intuitive graphical user interface
- Scans selected folder and all subfolders for duplicate files
- Uses MD5 hashing to identify duplicates (content-based comparison)
- Displays list of duplicate files with checkboxes
- Allows selective deletion of unwanted duplicates
- Confirmation dialog before deletion to prevent accidents

## How It Works

The application works by:
1. Calculating MD5 hash for each file in the selected directory and subdirectories
2. Identifying files with identical hashes as duplicates
3. Displaying found duplicates to the user
4. Allowing the user to select and delete unwanted copies

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/duplicate-file-scanner.git
```

2. Navigate to the project directory:
```
cd duplicate-file-scanner
```

3. Run the application:
```
python duplicate_scanner.py
```

## Usage

1. Click the "Scan for Duplicates" button
2. Select the folder you want to scan
3. Review the list of duplicate files
4. Check the boxes next to files you want to delete
5. Click "Delete Selected" to remove the selected duplicates

## Known Issues

- The current implementation only scans the top-level directory due to a bug in the `Find_Duplicates` function
- Variable naming inconsistency between `file_vars` and `File_Vars`

## Future Improvements

- Fix the recursive scanning to properly search all subdirectories
- Add file size information to help in decision making
- Group duplicates by content rather than showing a flat list
- Add ability to exclude certain file types or directories
- Implement file preview functionality

## License

MIT License - See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
