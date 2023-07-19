import os
import zipfile

def unzip_files_in_directory():
    # Get the current script's directory as the target directory
    target_directory = os.path.dirname(os.path.abspath(__file__))

    # Get a list of all files in the directory
    file_list = os.listdir(target_directory)

    for file_name in file_list:
        if file_name.endswith(".zip"):
            # Create a folder with the same name as the zip file (without the .zip extension)
            zip_file_path = os.path.join(target_directory, file_name)
            folder_name = os.path.splitext(file_name)[0]
            folder_path = os.path.join(target_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # Extract the contents of the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)

if __name__ == "__main__":
    unzip_files_in_directory()
