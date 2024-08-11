#!/usr/bin/python3
"""
This script converts a Markdown file to HTML, handling headings, lists, paragraphs, and text emphasis.
Usage: ./markdown2html.py <input_file> <output_file>
"""

import sys
import os
import re

def convert_emphasis(text):
    """Convert bold and italic markdown to HTML"""
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)  # Bold
    text = re.sub(r'__(.+?)__', r'<em>\1</em>', text)    # Italic
    return text

def convert_markdown_to_html(input_file, output_file):
    """
    Converts Markdown to HTML and writes the result to the output file.
    """
    with open(input_file, 'r') as md_file:
        lines = md_file.readlines()

    html_lines = []
    in_list = False
    list_type = None
    in_paragraph = False
    paragraph_lines = []

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append(f'</{list_type}>')
            in_list = False
            list_type = None

    def close_paragraph():
        nonlocal in_paragraph, paragraph_lines
        if in_paragraph:
            html_lines.append('<p>')
            html_lines.extend(convert_emphasis(line) for line in paragraph_lines)
            html_lines.append('</p>')
            in_paragraph = False
            paragraph_lines = []

    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            close_list()
            close_paragraph()
            # Handle headings
            heading_level = len(line.split()[0])
            if 1 <= heading_level <= 6:
                heading_text = line.lstrip('#').strip()
                html_line = f"<h{heading_level}>{convert_emphasis(heading_text)}</h{heading_level}>"
                html_lines.append(html_line)
        elif line.startswith('- ') or line.startswith('* '):
            close_paragraph()
            # Handle list items
            if not in_list or (in_list and list_type != ('ul' if line.startswith('- ') else 'ol')):
                close_list()
                list_type = 'ul' if line.startswith('- ') else 'ol'
                html_lines.append(f'<{list_type}>')
                in_list = True
            list_item = line[2:].strip()
            html_lines.append(f"<li>{convert_emphasis(list_item)}</li>")
        elif line:
            close_list()
            # Handle paragraph content
            if not in_paragraph:
                close_paragraph()
                in_paragraph = True
            paragraph_lines.append(line)
        else:
            close_list()
            close_paragraph()

    close_list()
    close_paragraph()

    with open(output_file, 'w') as html_file:
        html_file.write('\n'.join(html_lines))

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)

    # If we've reached this point, everything is okay
    sys.exit(0)

if __name__ == "__main__":
    main()
