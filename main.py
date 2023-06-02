__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile

#1.
def clean_cache():
    cache_dir = os.path.join(os.getcwd(), 'cache')
    
    if os.path.exists(cache_dir) and not os.path.isfile(cache_dir):
  
        # Checking if the directory is empty or not
        if not os.listdir(cache_dir):
            print("Empty directory")
        else:
            print("Not empty directory")
    else:
        print("The path is either for a file or not valid")
clean_cache () 
 
#2.
def cache_zip(zip_file_path, cache_dir_path):
    print("Caching the zip file...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
        print(f"Extracted {zip_file_path} to {cache_dir_path}")
    print("Zip file cached.")
zip_file_path = r"C:\Users\walia\OneDrive\Winc\modules\files\data.zip"
cache_dir_path = r"C:\Users\walia\OneDrive\Winc\modules\files\cache"
cache_zip(zip_file_path, cache_dir_path)

#3.
def cached_files():
    parent_path = os.getcwd()
    file_dir_path = "files/cache"
    file_path_abs = os.path.abspath(os.path.join(parent_path, file_dir_path))
    print(file_path_abs)
    
    files = []
    for root, dirs, filenames in os.walk(file_path_abs):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                files.append(os.path.abspath(file_path))
    
    print("List of files:", files)
    return files
file_paths = cached_files() 

#4.
def find_password(file_paths):
    file_paths = cached_files()  # Get the list of file paths from cached_files()
    password = None
    print("Searching for the password...")
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            for line in file:
                if "password:" in line.lower():
                    password = line.split(":", 1)[1].strip()
                    break
    if password:
        print("Password found:", password)
    else:
        print("Password not found.")
    return password
password = find_password(file_paths)