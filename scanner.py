import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

# scan_folder() opens a folder selection dialog
def scan_folder():
    folder = filedialog.askdirectory() # ask user to choose folder
    if not folder:
        return
    duplicates = Find_Duplicates(folder) # find duplicate files within selected folder
    display_duplicates(duplicates) # display duplicate files

# function to search for duplicates
def Find_Duplicates(folder):
    
    files_hashes = {} # dictionary to store file hashes
    duplicates = [] # list to store duplicate files

    # traverse the folder and get file hashes
    for Root, dirs, files in os.walk(folder): # os.walk() to traverse/iterate through all files in the folder
        
        for file in files:
            file_path = os.path.join(Root, file)
            file_hash = hash_file(file_path)

            if file_hash in files_hashes:
                duplicates.append(file_path) # found duplicate
            else:
                files_hashes[file_hash] = file_path

    return duplicates


def hash_file(file_path):
    hash_md5 = hashlib.md5() # return the hash of the file md5
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except Exception as e:
        print(f"Error hashing file {file_path}")
    return hash_md5.hexdigest()


def display_duplicates(duplicates):
    global file_vars
    
    # display duplicates as checkboxes for selection
    for widget in frame.winfo_children():
        widget.destroy()
    if duplicates:
        file_Vars = [] # store checkbox variables

        for file in duplicates:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(frame, text=file, variable=var, anchor="w")
            chk.pack(fill="x")
            file_Vars.append((var, file)) # store checkbox and file path
        delete_button.pack(pady=10)
    else:
        messagebox.showinfo("No duplicates", "No duplicate files found.")

def delete_selected():
    # deletes selected duplicate files after user confirm
    selected_files = [file for var, file in file_vars if var.get()]

    if not selected_files:
        messagebox.showwarning("No Selection", "Please select at least one file to delete!")
        return

    confirm = messagebox.askyesno("Confirm deletion", f"Are you sure you want to delete {len(selected_files)} files?")
    if confirm:
        for file in selected_files:
            try:
                os.remove(file)
            except Exception as e:
                messagebox.showinfo("Error", f"Could not delete {file}: {e}")

        messagebox.showinfo("Deletion Complete", "Selected files have been deleted successfully!")
        scan_folder() # refresh results after deletion

# set up Tkinter UI
root = tk.Tk()
root.title("Duplicate File Scanner")
root.geometry("800x500+300+200")
root.resizable(False, False)

label = tk.Label(root, text="File Scanner", font=('Arial', 20, "bold"))
label.pack(pady=5)

scan_button = tk.Button(root, text="Scan for Duplicates", command=scan_folder)
scan_button.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

delete_button = tk.Button(root, text="Delete Selected", command=delete_selected)

root.mainloop()