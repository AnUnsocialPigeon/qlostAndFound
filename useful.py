import os
import zipfile

def unzip_and_filter_zip(zip_file_path):
    """
    Check if a file is a zip file, unzip it to the same location, and delete files that don't end with .xml.

    Parameters:
        zip_file_path (str): The path of the zip file.

    Returns:
        None
    """
    if not zip_file_path.lower().endswith('.zip'):
        print(f"{zip_file_path} is not a zip file.")
        return

    # Unzip the file to the same location
    unzip_folder = os.path.dirname(zip_file_path)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_folder)

    # Delete files that don't end with .xml
    for root, _, files in os.walk(unzip_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.lower().endswith('.asc') and not file.lower().endswith('.zip'):
                os.remove(file_path)
                print(f"Deleted: {file_path}")


if __name__ == "__main__":
    for root, _, files in os.walk(".\\big_data"):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.lower().endswith('.zip'):
                print(f"Processing: {file_path}")
                unzip_and_filter_zip(file_path)
                os.remove(file_path)
