__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile
import shutil

parent_path = os.getcwd()
cache_path = os.path.join(parent_path, "cache")
data_path = os.path.join(parent_path, "data_zip")

# #1.
#import os
def clean_cache():
    if  os.path.exists(cache_path): #Cleans the cache directory by removing/empty its contents or creating a new empty directory if it doesn't exist.
        shutil.rmtree(cache_path)
    else:
        os.mkdir("cache")
clean_cache() 
 
#2.
#import zipfile
def cache_zip(zip_file_path, cache_dir_path):
    print("Caching the zip file...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:     ## Open the ZIP file for reading
        zip_ref.extractall(cache_dir_path)        #Extracts the specified zip file into the cache directory.
        print(f"Extracted {zip_file_path} to {cache_dir_path}")
    print("Zip file cached.")

#3.
def cached_files():   #    Returns a list of all files in the cache directory, including their absolute paths.
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
    
    # print("List of files:", files)
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
