# Directory Context Copier

This is a Python application that allows you to copy the contents of a directory, including subdirectories and files, to a specified destination.

## Overview

The Directory Context Copier provides a convenient way to duplicate the structure and contents of a directory to another location. It is particularly useful when you need to replicate a directory's context for testing, backup, or other purposes.

## How to Build with PyInstaller

To build the Directory Context Copier using PyInstaller, follow these steps:

1. Install PyInstaller by running the following command in your terminal:

  ```
  pip install pyinstaller
  ```

2. Navigate to the root directory of the application in your terminal.

3. Run the following command to build the application:

  ```
  pyinstaller --onefile copier.py
  ```

  This will create a single executable file in the `dist` directory.

4. You can now run the application by executing the generated executable file.

Please note that PyInstaller may have additional options and configurations depending on your specific requirements. Refer to the PyInstaller documentation for more information.
