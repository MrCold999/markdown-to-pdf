#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to PDF Converter (using xhtml2pdf - no GTK3 dependency)
Convert Markdown files to PDF documents.
"""

import argparse
import sys
import os
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')

try:
    import markdown
    from xhtml2pdf import pisa
except ImportError as e:
    print(f"Error: Missing required package: {e}")
    print("\nInstall dependencies:")
    print("  uv pip install markdown xhtml2pdf reportlab")
    sys.exit(1)


# Simplified CSS styles for xhtml2pdf compatibility
DEFAULT_CSS = """
body {
    font-family: "Microsoft YaHei", "SimHei", sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #24292e;
    margin: 20mm;
}

h1 {
    font-size: 24pt;
    color: #1a1a1a;
    border-bottom: 2px solid #eaecef;
    padding-bottom: 6px;
    margin-top: 24px;
}

h2 {
    font-size: 20pt;
    color: #1a1a1a;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 6px;
    margin-top: 24px;
}

h3 { font-size: 16pt; color: #1a1a1a; }
h4 { font-size: 14pt; }
h5 { font-size: 12pt; }
h6 { font-size: 11pt; }

p { margin: 12px 0; }

a { color: #0366d6; text-decoration: none; }

code {
    background-color: #f6f8fa;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: "Consolas", monospace;
    font-size: 0.9em;
}

pre {
    background-color: #f6f8fa;
    padding: 12px;
    border-radius: 3px;
    overflow: auto;
    font-size: 0.9em;
    white-space: pre-wrap;
    word-wrap: break-word;
}

pre code {
    background: none;
    padding: 0;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
    font-size: 10pt;
}

th, td {
    border: 1px solid #dfe2e5;
    padding: 8px 12px;
    text-align: left;
}

th {
    background-color: #f6f8fa;
    font-weight: 600;
}

blockquote {
    border-left: 4px solid #dfe2e5;
    padding: 0 16px;
    color: #6a737d;
    margin: 16px 0;
}

ul, ol {
    padding-left: 2em;
    margin: 12px 0;
}

li { margin: 6px 0; }

hr {
    border: none;
    border-top: 1px solid #eaecef;
    margin: 24px 0;
}
"""


def markdown_to_html(md_path: Path, title: str = None) -> str:
    """Convert Markdown file to HTML string."""
    
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Extract title from first heading if not provided
    if not title:
        import re
        match = re.search(r"^#\s+(.+)$", md_content, re.MULTILINE)
        if match:
            title = match.group(1).strip()
        else:
            title = md_path.stem
    
    # Convert to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=["extra", "codehilite", "tables"],
        output_format="html5",
    )
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{DEFAULT_CSS}</style>
</head>
<body>
{html_body}
</body>
</html>"""
    
    return html


def convert_to_pdf(md_path: Path, pdf_path: Path, title: str = None) -> bool:
    """Convert Markdown file to PDF using xhtml2pdf."""
    
    try:
        html_content = markdown_to_html(md_path, title)
        
        with open(pdf_path, "wb") as pdf_file:
            result = pisa.CreatePDF(html_content, dest=pdf_file, encoding="utf-8")
            
            if result.err:
                print(f"PDF generation errors occurred")
                return False
        
        # Verify file was created
        if pdf_path.exists() and pdf_path.stat().st_size > 0:
            print(f"Success: {md_path.name} -> {pdf_path.name}")
            print(f"PDF size: {pdf_path.stat().st_size / 1024:.1f} KB")
            return True
        else:
            print(f"PDF file was not created or is empty")
            return False
        
    except Exception as e:
        print(f"Error converting {md_path.name}: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF")
    parser.add_argument("input", type=Path, help="Input Markdown file")
    parser.add_argument("output", type=Path, help="Output PDF file")
    parser.add_argument("--title", "-t", type=str, help="Document title")
    
    args = parser.parse_args()
    
    success = convert_to_pdf(args.input, args.output, title=args.title)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
