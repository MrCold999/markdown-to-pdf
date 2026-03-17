#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to PDF Converter with Chinese Support (Inline Font Method)
使用内联字体样式确保中文正确显示
"""

import argparse
import sys
import os
import re
from pathlib import Path

if sys.platform == 'win32':
    os.system('chcp 65001 > nul')

try:
    import markdown
    from xhtml2pdf import pisa
except ImportError as e:
    print(f"Error: Missing required package: {e}")
    sys.exit(1)

# Minimal CSS - use inline fonts instead
CSS = """
body { font-size: 11pt; line-height: 1.6; margin: 20mm; }
h1 { font-size: 24pt; border-bottom: 2px solid #eaecef; padding-bottom: 6px; }
h2 { font-size: 20pt; border-bottom: 1px solid #eaecef; padding-bottom: 6px; }
h3 { font-size: 16pt; }
table { border-collapse: collapse; width: 100%; margin: 16px 0; }
th, td { border: 1px solid #dfe2e5; padding: 8px 12px; }
th { background-color: #f6f8fa; }
code { background: #f6f8fa; padding: 2px 6px; }
pre { background: #f6f8fa; padding: 12px; overflow: auto; }
"""

def add_inline_fonts(html):
    """Add inline font-family to HTML elements for Chinese support"""
    # Add font to common elements
    replacements = [
        (r'<h1>', '<h1 style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<h2>', '<h2 style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<h3>', '<h3 style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<h4>', '<h4 style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<p>', '<p style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<li>', '<li style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<td>', '<td style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<th>', '<th style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
        (r'<body>', '<body style="font-family: Microsoft YaHei, SimHei, sans-serif;">'),
    ]
    
    for old, new in replacements:
        html = html.replace(old, new)
    
    return html

def markdown_to_html(md_path: Path, title: str = None) -> str:
    """Convert Markdown to HTML with inline Chinese fonts"""
    
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    if not title:
        match = re.search(r"^#\s+(.+)$", md_content, re.MULTILINE)
        title = match.group(1).strip() if match else md_path.stem
    
    html_body = markdown.markdown(
        md_content,
        extensions=["extra", "codehilite", "tables"],
        output_format="html5",
    )
    
    # Add inline fonts
    html_body = add_inline_fonts(html_body)
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{CSS}</style>
</head>
<body style="font-family: Microsoft YaHei, SimHei, sans-serif;">
{html_body}
</body>
</html>"""
    
    return html

def convert_to_pdf(md_path: Path, pdf_path: Path, title: str = None) -> bool:
    """Convert Markdown to PDF"""
    
    try:
        html_content = markdown_to_html(md_path, title)
        
        with open(pdf_path, "wb") as pdf_file:
            result = pisa.CreatePDF(html_content, dest=pdf_file, encoding='utf-8')
            
            if result.err:
                print(f"PDF errors: {result.err}", file=sys.stderr)
                return False
        
        if pdf_path.exists() and pdf_path.stat().st_size > 0:
            print(f"Success: {md_path.name} -> {pdf_path.name}")
            print(f"PDF size: {pdf_path.stat().st_size / 1024:.1f} KB")
            return True
        else:
            print("PDF not created", file=sys.stderr)
            return False
            
    except Exception as e:
        print(f"Failed: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF')
    parser.add_argument('input', type=Path, help='Input Markdown')
    parser.add_argument('output', type=Path, help='Output PDF')
    parser.add_argument('--title', type=str, help='Title')
    args = parser.parse_args()
    
    success = convert_to_pdf(args.input, args.output, args.title)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
