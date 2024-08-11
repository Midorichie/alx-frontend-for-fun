#!/usr/bin/python3
"""
This script converts a Markdown file to HTML, handling headings and unordered lists.
Usage: ./markdown2html.py <input_file> <output_file>
"""

import sys
import os

def convert_markdown_to_html(input_file, output_file):
    """
    Converts Markdown headings and unordered lists to HTML and writes the result to the output file.
    """
    with open(input_file, 'r') as md_file:
        lines = md_file.readlines()

    html_lines = []
    in_list = False

    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Handle headings
            heading_level = len(line.split()[0])
            if 1 <= heading_level <= 6:
                heading_text = line.lstrip('#').strip()
                html_line = f"<h{heading_level}>{heading_text}</h{heading_level}>"
                html_lines.append(html_line)
        elif line.startswith('- '):
            # Handle unordered list items
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            list_item = line[2:].strip()
            html_lines.append(f"<li>{list_item}</li>")
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # For now, we'll ignore other lines
            continue

    if in_list:
        html_lines.append('</ul>')

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
