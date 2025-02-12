#backup
import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    """Backup files from source to destination, appending timestamp for duplicates."""
    
    # Validate source directory
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Create destination directory if it does not exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Created destination directory: {destination_dir}")

    # Iterate through files in source directory
    for file_name in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, file_name)

        # Ensure we only process files, not directories
        if os.path.isfile(source_file_path):
            destination_file_path = os.path.join(destination_dir, file_name)

            # Check if the file already exists in the destination
            if os.path.exists(destination_file_path):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                base_name, ext = os.path.splitext(file_name)
                new_file_name = f"{base_name}_{timestamp}{ext}"
                destination_file_path = os.path.join(destination_dir, new_file_name)

            # Copy the file
            try:
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Copied: {file_name} -> {destination_file_path}")
            except Exception as e:
                print(f"Error copying {file_name}: {e}")

if __name__ == "__main__":
    # Ensure correct number of arguments
    #if len(sys.argv) != 3:
     #   print("Usage: python backup.py <source_directory> <destination_directory>")
      #  sys.exit(1)

    source_directory = r"C:\Users\Admin\Github_Repo\python_assignments"
    destination_directory = r"C:\Users\Admin\Github_Repo\Backup"

    backup_files(source_directory, destination_directory)
