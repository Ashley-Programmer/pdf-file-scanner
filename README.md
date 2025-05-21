# Duplicate File Scanner

A Python-based GUI application that efficiently scans folders for duplicate files using MD5 hash comparison and provides an easy interface to delete unnecessary duplicates, helping you free up valuable disk space.

## Features

- Clean, simple and intuitive graphical user interface
- **Full recursive scanning** of selected folder and all subfolders for duplicate files
- Uses MD5 cryptographic hashing for efficient content-based comparison
- Handles large files efficiently by reading in chunks
- Employs O(1) time complexity lookups for optimal performance
- Displays list of duplicate files with convenient checkboxes for selection
- Allows selective deletion of unwanted duplicates
- Confirmation dialog before deletion to prevent accidental data loss
- Error handling for file access issues
- Window size configured for better visibility (800x500 pixels)

## How It Works

The application works by:
1. Calculating MD5 hash for each file in the selected directory and subdirectories
2. Using dictionary data structures for O(1) time complexity lookups
3. Identifying files with identical hashes as duplicates (true content comparison)
4. Displaying found duplicates to the user in a scrollable list
5. Allowing the user to select and delete unwanted copies

## Technical Implementation

### Core Algorithms
- **Recursive Directory Traversal**: Uses `os.walk()` to efficiently scan the entire directory tree with proper recursion
- **Content-Based Comparison**: Implements MD5 hashing for robust duplicate detection regardless of filename
- **Memory-Efficient Chunking**: Processes large files in 4KB chunks to maintain low memory footprint
- **O(1) Lookup Performance**: Employs Python dictionaries for constant-time hash lookups

### Data Structures Used
- **Dictionary (Hash Table)**: Maps file hashes to file paths for O(1) time complexity lookups
- **Lists**: Stores duplicate file paths and tracks user selections
- **Tkinter Widgets**: Manages the GUI components including frames, buttons, and checkboxes

## Requirements

- Python
- Tkinter (usually comes pre-installed with Python)
- No external dependencies required

## Installation

1. Clone this repository:
```
git clone https://github.com/Ashley-Programmer/pdf-file-scanner.git
```

2. Navigate to the project directory:
```
cd files
```

3. Run the application:
```
python scanner.py
```

## Usage

1. Click the "Scan for Duplicates" button
2. Select the folder you want to scan in the directory selection dialog
3. Wait while the application recursively scans all files in the selected folder and subfolders
4. Review the list of duplicate files that appears
5. Check the boxes next to files you want to delete (keeping at least one copy of files you need)
6. Click "Delete Selected" to remove the selected duplicates
7. Confirm the deletion when prompted

## Code Structure

```
duplicate_scanner.py
├── scan_folder() - Opens folder selection dialog and initiates scanning
├── Find_Duplicates(folder) - Recursively finds duplicates using hash comparison
│   └── Properly indented return statement for complete directory traversal
├── hash_file(file_path) - Creates MD5 hash of file contents in chunks
├── display_duplicates(duplicates) - Shows duplicates as selectable checkboxes
├── delete_selected() - Handles deletion of selected duplicates
└── Main GUI setup - Creates the application window and controls
```

## Known Issues

- Variable naming inconsistency between `file_vars` and `file_Vars` may cause reference errors
- Large file lists may be difficult to navigate without a scrollbar
- No visual indication of scanning progress for large directories
- No file size information displayed to assist in decision making

## Future Improvements

### Functionality Enhancements
- Fix the variable naming inconsistency between `file_vars` and `file_Vars`
- Add a scrollbar to navigate through large lists of duplicates
- Implement progress indicator for scanning large directories
- Display file sizes, dates, and preview thumbnails to aid decision making
- Add search and filtering capabilities for large result sets
- Implement grouping of duplicates by content rather than showing a flat list
- Add ability to exclude specific file types, directories, or size ranges
- Create an option to automatically select all duplicates except the oldest/newest copy

### Technical Improvements
- Implement SHA-256 as an alternative hash option for higher security
- Add multi-threading to improve scanning performance
- Create a persistent configuration system for user preferences
- Implement logging for better debugging and error tracking
- Add unit tests to ensure reliability
- Package the application as a standalone executable

## How to Contribute

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Python community for the powerful standard libraries
- Inspired by the need to manage duplicate files efficiently

---

*This project was created to demonstrate effective file handling, GUI development, and data structure usage in Python.*
