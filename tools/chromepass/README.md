# ChromePass

ChromePass is a simple Python script that retrieves passwords stored in Google Chrome.

## Requirements

- Python 3.x
- `win32crypt` (for Windows only)

## Usage

`python chromepass.py [-o [CSV|JSON]]|-d]`

- `-o [CSV|JSON]`: Output passwords to a CSV or JSON file.
- `-d`: Dump passwords to stdout.

## Limitations

- Mac OSX is not supported.
- The script may not work if Google Chrome is running in the background.

## Note

The default path for Google Chrome's data is set to `C:\Users\$USER\AppData\Local\Google\Chrome\User Data\Default\` in the `getpath()` function. You may need to modify it to match the path on your system.
