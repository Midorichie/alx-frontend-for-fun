#!/usr/bin/python3
"""
This script converts a Markdown file to HTML, focusing on heading syntax.
Usage: ./markdown2html.py <input_file> <output_file>
"""

import sys
import os

def convert_markdown_to_html(input_file, output_file):
    """
    Converts Markdown headings to HTML and writes the result to the output file.
    """
    with open(input_file, 'r') as md_file:
        lines = md_file.readlines()

    html_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            # Count the number of '#' symbols
            heading_level = len(line.split()[0])
            if 1 <= heading_level <= 6:
                # Extract the heading text
                heading_text = line.lstrip('#').strip()
                # Generate the HTML heading
                html_line = f"<h{heading_level}>{heading_text}</h{heading_level}>"
                html_lines.append(html_line)
        else:
            # For now, we'll ignore non-heading lines
            continue

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
