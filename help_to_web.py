import subprocess
import sys
import os
import tempfile
import webbrowser
from markdown import markdown
import re

def get_help_output(command):
    """Runs the command and captures the help output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error: {str(e)}"


def format_markdown(help_text):
    """Converts plain text help output to markdown for better readability."""
    lines = help_text.split("\n")
    formatted_lines = []
    
    for line in lines:
        if line.strip().startswith("-") or line.strip().startswith("--"):
            formatted_lines.append(f"**{line.strip()}**  ")  # Bold for options
        elif ":" in line:
            parts = line.split(":", 1)
            formatted_lines.append(f"**{parts[0].strip()}**: {parts[1].strip()}  ")  # Key-value formatting
        else:
            formatted_lines.append(line.strip())
    
    return "\n".join(formatted_lines)


def generate_html(markdown_content, command_name):
    """Converts markdown to styled HTML with a book-like theme."""
    html_content = markdown(markdown_content)
    styled_html = f"""
    <html>
    <head>
        <title>Help Viewer - {command_name}</title>
        <style>
            body {{ font-family: 'Times New Roman', serif; padding: 50px; background-color: #f5f1e9; color: #3c3c3c; line-height: 1.8; font-size: 18px; }}
            .container {{ max-width: 1400px; margin: auto; padding: 40px; background: #fffaf0; border-radius: 15px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); }}
            h1, h2, h3 {{ color: #5a3e2b; text-align: center; }}
            pre {{ background: #f4eee4; color: #333; padding: 15px; border-radius: 8px; overflow-x: auto; }}
            b {{ color: #8b4513; }}
            .header, .footer {{ text-align: center; padding: 15px; background: #eae0d5; border-radius: 10px; margin-bottom: 20px; font-size: 20px; }}
            .header h1 {{ font-size: 40px; margin: 0; color: #4a2c1f; }}
            .footer p {{ font-size: 18px; margin: 0; color: #4a2c1f; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>{command_name} Help Menu</h1>
        </div>
        <div class="container">
            {html_content}
        </div>
        <div class="footer">
            <p>Help menu for: <strong>{command_name}</strong></p>
        </div>
    </body>
    </html>
    """
    return styled_html


def save_and_open(html_content):
    """Saves the HTML content to a temporary file and opens it in the browser."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
        tmp_file.write(html_content.encode("utf-8"))
        tmp_path = tmp_file.name
    webbrowser.open(f"file://{tmp_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py '<command> <options>'")
        sys.exit(1)
    
    command = " ".join(sys.argv[1:])
    help_output = get_help_output(command)
    markdown_content = format_markdown(help_output)
    html_content = generate_html(markdown_content, command)
    save_and_open(html_content)


if __name__ == "__main__":
    main()
