# password-protected-zip-file-
This Python script creates a password-protected ZIP file using the pyzipper library. It allows you to specify the files to include in the ZIP and set a password for encryption. The resulting ZIP file requires the provided password to access its contents, providing an additional layer of security.


To create a password-protected ZIP file in Python, you can use the `zipfile` module along with the `pyzipper` library to set a password. Here's an example:

```python
import zipfile
import pyzipper

def create_password_protected_zip(file_paths, zip_file_path, password):
    with pyzipper.AESZipFile(zip_file_path, 'w', compression=zipfile.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())
        for file_path in file_paths:
            zf.write(file_path)

if __name__ == "__main__":
    # List of file paths to be included in the ZIP file
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]
    
    # Path to the output ZIP file
    zip_file_path = "output.zip"
    
    # Password for the ZIP file
    password = "your_password_here"
    
    # Create the password-protected ZIP file
    create_password_protected_zip(file_paths, zip_file_path, password)
```

In this script:
- Replace `"file1.txt"`, `"file2.txt"`, `"file3.txt"` with the paths of the files you want to include in the ZIP file.
- Replace `"output.zip"` with the desired name and path for the output ZIP file.
- Replace `"your_password_here"` with the desired password for the ZIP file.

This script will create a password-protected ZIP file containing the specified files. When you open the ZIP file, you'll be prompted to enter the password to access its contents. Make sure to keep your password secure and not to lose it, as it will be required to open the ZIP file.
