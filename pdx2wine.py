import os
import shutil
import sys

def organize_files(base_dir):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if '\\' in file:
                # Split the filename based on the Windows path separator
                parts = file.split('\\')
                *dirs, filename = parts
                
                # Create the target directory structure
                target_dir = os.path.join(root, *dirs)
                os.makedirs(target_dir, exist_ok=True)
                
                # Move the file to the new directory
                src_path = os.path.join(root, file)
                dst_path = os.path.join(target_dir, filename)
                
                print(f"Moving '{src_path}' to '{dst_path}'")
                shutil.move(src_path, dst_path)
def process_directories(base_dir):
    # Walk through the top-level subdirectories
    for entry in os.scandir(base_dir):
        if entry.is_dir():
            print(f"Processing directory: {entry.path}")
            organize_files(entry.path)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>")
        sys.exit(1)

    base_dir = sys.argv[1]
    if not os.path.isdir(base_dir):
        print(f"Error: '{base_dir}' is not a directory.")
        sys.exit(1)

    process_directories(base_dir)

if __name__ == "__main__":
    main()