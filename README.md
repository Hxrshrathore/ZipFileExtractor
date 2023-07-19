# Zip File Extractor

This Python script is designed to unzip all the .zip compressed files in the same directory and create a newly created folder named after the Zip file name to store the extracted contents.

## Usage

1. Place the Python script (`unzip_files.py`) in the same directory as the .zip files you want to extract.
2. Open a terminal or command prompt and navigate to the directory containing the script and the .zip files.

### Running the Script

```bash
python unzip_files.py
```

The script will automatically:

- Create a new folder named "Extracted" in the same directory if it doesn't already exist.
- Extract the contents of each .zip file into a folder with the same name as the .zip file (without the .zip extension) inside the "Extracted" folder.

Please ensure you have Python installed on your system before running the script.

## License

This project is licensed under the [MIT License](LICENSE).
