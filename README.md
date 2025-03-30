# 🗂️ Async File Sorter

This Python script asynchronously reads all files from a source folder and copies them into subfolders in a destination folder, sorted by file extension.

## 🚀 Features

- Recursively scans the source folder and its subfolders
- Asynchronously copies files using asyncio for better performance
- Automatically creates subfolders based on file extensions
- Logs all errors into a file file_sorter_errors.log
- Works cross-platform using pathlib

## 📦 Requirements

- Python 3.8+
- aiofiles package

Install dependencies:

pip install aiofiles

## 🛠️ Usage

python main.py <source_folder> <destination_folder>

### Example

python main.py ./unsorted ./sorted

If unsorted contains:

file.txt  
image.jpg  
code.py

After running the script, sorted will contain:

sorted/  
├── txt/  
│ └── file.txt  
├── jpg/  
│ └── image.jpg  
└── py/  
 └── code.py

## 🧪 Testing

You can test the script with your own folders. Make sure the source folder contains files. The destination folder will be populated automatically based on extensions.

## 📄 Error Logging

If something goes wrong, check the log file:

file_sorter_errors.log

It will contain timestamps and detailed error messages.

## 📚 Project Structure

main.py # Main script  
file_sorter_errors.log # Log file for errors  
README.md # Project documentation

## 👨‍💻 Author

Made with ❤️ for educational purposes.
