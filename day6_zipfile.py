import zipfile
import os

def zip_file(file_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, os.path.basename(file_path))
    print(f"File {file_path} zipped successfully to {zip_path}")

# Example usage
file_to_zip = 'example.txt'  # Replace with your file path
zip_destination = 'example.zip'  # Replace with your desired zip file path
zip_file(file_to_zip, zip_destination)
