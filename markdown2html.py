#!/usr/bin/python3
"""
This script converts a Markdown file to HTML.
Usage: ./markdown2html.py <input_file> <output_file>
"""

import sys
import os

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

    # If we've reached this point, everything is okay
    sys.exit(0)

if __name__ == "__main__":
    main()
