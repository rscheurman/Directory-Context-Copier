#!/usr/bin/env python3
import os
import pyperclip
import argparse
import tkinter as tk
from tkinter import filedialog

def is_text_file(file_path):
    text_extensions = {'.ts', '.js', '.html', '.css', '.json', '.md', '.txt', '.py', '.java', '.c', '.cpp', '.cs', '.go', '.rb', '.sh'}
    _, ext = os.path.splitext(file_path)
    return ext in text_extensions

def get_file_paths_and_contents(directory):
    file_data = []
    copied_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_text_file(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        file_content = f.read()
                    file_data.append(f"{file_path}\n{file_content}\n")
                    copied_files.append(file_path)
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")
    return file_data, copied_files

def copy_to_clipboard(data):
    pyperclip.copy(data)

def main():
    parser = argparse.ArgumentParser(description="Copy contents of text files in a directory to the clipboard.")
    parser.add_argument('directory', nargs='?', default=None, help="Directory to scan for text files")
    args = parser.parse_args()

    if args.directory:
        directory = os.path.abspath(args.directory)
    else:
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        directory = filedialog.askdirectory(title="Select Directory to Scan")

    if directory:
        file_data, copied_files = get_file_paths_and_contents(directory)
        combined_data = "\n".join(file_data)
        copy_to_clipboard(combined_data)
        print(f"All file paths and contents from {directory} have been copied to the clipboard.")
    else:
        print("No directory selected.")

if __name__ == "__main__":
    main()
