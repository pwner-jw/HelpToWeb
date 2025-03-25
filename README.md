# HelpToWeb - Command Help to HTML Viewer

HelpToWeb is a Python tool that captures a command-line tool's help menu, formats it for readability, and opens it as a styled webpage.

## Features
- Extracts help output from any CLI command.
- Formats output into a structured, readable HTML page.
- Uses **Times New Roman** font with a clean, book-like theme.
- Adds a header with the command name and a footer indicating the tool.

## Installation
Ensure you have Python installed, then install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage
Run the script with a command whose help menu you want to display:

```sh
python help_to_web.py "<command> --help"
```

### Example:
```sh
python help_to_web.py "nmap --help"
```
This will generate an HTML page displaying the `nmap --help` output in a structured format.
