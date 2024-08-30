import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# Function to split the CSV file
def split_csv(file_path, max_lines):
    """
    Splits the CSV file into smaller files with the specified maximum number of lines.
    
    Parameters:
    - file_path: str - The path to the input CSV file.
    - max_lines: int - The maximum number of lines per output file.
    
    Returns:
    None
    """
    df = pd.read_csv(file_path)  # Read the CSV file
    
    total_rows = len(df)  # Total number of rows in the original file
    num_chunks = (total_rows // max_lines) + (1 if total_rows % max_lines else 0)  # Calculate the number of files needed
    
    base_name = os.path.splitext(os.path.basename(file_path))[0]  # Get the base name of the file without the extension
    
    save_dir = os.getcwd()  # Directory where the script is run
    
    for i in range(num_chunks):
        chunk = df[i*max_lines:(i+1)*max_lines]  # Get the chunk of data
        chunk.to_csv(os.path.join(save_dir, f"{base_name}_{max_lines}_part{i+1}.csv"), index=False)  # Save the chunk
    
    # Display the result information
    messagebox.showinfo("Success", f"CSV file successfully split!\n\nTotal number of lines in the original file: {total_rows}\nNumber of files created: {num_chunks}")

# Function to open file dialog and select CSV file
def select_file():
    """
    Opens a file dialog to select a CSV file and inserts the file path into the entry widget.
    
    Returns:
    None
    """
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Function to start splitting process
def start_splitting():
    """
    Starts the CSV splitting process by calling split_csv() with the selected file and max lines.
    
    Returns:
    None
    """
    file_path = file_entry.get()
    try:
        max_lines = int(lines_entry.get())
        if file_path and max_lines > 0:
            split_csv(file_path, max_lines)
        else:
            messagebox.showerror("Error", "Please provide a valid file and number of lines.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for maximum lines.")

# Setting up the GUI
root = tk.Tk()
root.title("CSV Splitter")

# File selection
tk.Label(root, text="Select CSV File:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

# Max lines input
tk.Label(root, text="Max Lines per File:").grid(row=1, column=0, padx=10, pady=10)
lines_entry = tk.Entry(root, width=10)
lines_entry.grid(row=1, column=1, padx=10, pady=10)

# Start button
tk.Button(root, text="Split CSV", command=start_splitting).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()