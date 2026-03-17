#!/usr/bin/env python3
"""
Markdown to PDF Converter
Convert Markdown files to professional PDF documents.
"""

import argparse
import sys
from pathlib import Path

try:
    import markdown
    from markdown.extensions.codehilite import CodeHiliteExtension
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.toc import TocExtension
    from pygments.formatters import HtmlFormatter
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
except ImportError as e:
    print(f"Error: Missing required package: {e}")
    print("\nInstall dependencies:")
    print("  uv pip install markdown weasyprint pygments")
    print("\nWindows users may also need GTK3:")
    print("  https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases")
    sys.exit(1)


# Default CSS styles
DEFAULT_CSS = """
@page {
    size: A4;
    margin: 25mm;
    @bottom-right {
        content: counter(page);
        font-size: 10pt;
        color: #666;
    }
}

body {
    font-family: "Microsoft YaHei", "SimHei", "Segoe UI", sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #24292e;
    max-width: 800px;
    margin: 0 auto;
}

h1, h2, h3, h4, h5, h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
    color: #1a1a1a;
}

h1 {
    font-size: 24pt;
    border-bottom: 2px solid #eaecef;
    padding-bottom: 0.3em;
}

h2 {
    font-size: 20pt;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 0.3em;
}

h3 { font-size: 16pt; }
h4 { font-size: 14pt; }
h5 { font-size: 12pt; }
h6 { font-size: 11pt; }

p {
    margin: 12px 0;
}

a {
    color: #0366d6;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

code {
    background-color: rgba(27,31,35,0.05);
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-family: "Consolas", "Monaco", monospace;
    font-size: 0.9em;
}

pre {
    background-color: #f6f8fa;
    padding: 16px;
    overflow: auto;
    border-radius: 3px;
    font-size: 0.9em;
    line-height: 1.45;
}

pre code {
    background: none;
    padding: 0;
    font-size: 100%;
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

tr:nth-child(even) {
    background-color: #fbfcfc;
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

li {
    margin: 6px 0;
}

li > ul, li > ol {
    margin: 4px 0;
}

hr {
    border: none;
    border-top: 1px solid #eaecef;
    margin: 24px 0;
}

img {
    max-width: 100%;
    height: auto;
}

/* Print optimizations */
@media print {
    body {
        font-size: 10pt;
    }
    
    a {
        color: #000;
        text-decoration: underline;
    }
    
    pre, code {
        background: #f5f5f5 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
}
"""

GITHUB_CSS = """
/* GitHub-style CSS - similar to default but with GitHub colors */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #24292e;
}

h1 { border-bottom: 2px solid #eaecef; }
h2 { border-bottom: 1px solid #eaecef; }

code {
    background-color: rgba(27,31,35,0.05);
    padding: 0.2em 0.4em;
    border-radius: 3px;
}

pre {
    background-color: #f6f8fa;
    padding: 16px;
    border-radius: 3px;
}

table th {
    background-color: #f6f8fa;
}

blockquote {
    border-left: 4px solid #dfe2e5;
    color: #6a737d;
}
"""

PRINT_CSS = """
/* Print-optimized CSS - black and white, ink-saving */
@page {
    size: A4;
    margin: 20mm;
}

body {
    font-family: "Microsoft YaHei", "SimHei", sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #000;
}

h1, h2, h3 {
    color: #000;
}

h1 { border-bottom: 1px solid #000; }
h2 { border-bottom: 1px solid #333; }

code, pre {
    background: #f0f0f0 !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

a {
    color: #000;
    text-decoration: underline;
}

blockquote {
    border-left: 2px solid #333;
    color: #333;
}

table th {
    background: #e0e0e0 !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
"""


def get_css(theme: str = "default") -> str:
    """Get CSS by theme name."""
    themes = {
        "default": DEFAULT_CSS,
        "github": GITHUB_CSS,
        "print": PRINT_CSS,
    }
    return themes.get(theme, DEFAULT_CSS)


def markdown_to_html(md_path: Path, title: str = None) -> str:
    """Convert Markdown file to HTML string."""
    
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    
    # Read markdown content
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
        extensions=[
            "extra",
            "codehilite",
            "tables",
            "toc",
            "fenced_code",
        ],
        output_format="html5",
    )
    
    # Build complete HTML document
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        {DEFAULT_CSS}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""
    
    return html


def convert_to_pdf(
    md_path: Path,
    pdf_path: Path,
    title: str = None,
    css_path: Path = None,
    theme: str = "default",
) -> bool:
    """Convert Markdown file to PDF."""
    
    try:
        # Convert to HTML
        html_content = markdown_to_html(md_path, title)
        
        # Load CSS
        if css_path and css_path.exists():
            css = CSS(filename=str(css_path))
        else:
            css_content = get_css(theme)
            css = CSS(string=css_content)
        
        # Generate PDF
        font_config = FontConfiguration()
        html = HTML(string=html_content)
        html.write_pdf(
            str(pdf_path),
            stylesheets=[css],
            font_config=font_config,
        )
        
        print(f"✓ Successfully converted: {md_path.name} → {pdf_path.name}")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {md_path.name}: {e}")
        return False


def batch_convert(input_dir: Path, output_dir: Path, **kwargs) -> dict:
    """Batch convert all Markdown files in a directory."""
    
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results = {"success": [], "failed": []}
    
    md_files = list(input_dir.glob("*.md")) + list(input_dir.glob("*.markdown"))
    
    for md_file in md_files:
        pdf_file = output_dir / f"{md_file.stem}.pdf"
        
        if convert_to_pdf(md_file, pdf_file, **kwargs):
            results["success"].append(md_file.name)
        else:
            results["failed"].append(md_file.name)
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.md output.pdf
  %(prog)s input.md output.pdf --title "My Document"
  %(prog)s input.md output.pdf --theme github
  %(prog)s --batch ./docs/ ./output/
        """,
    )
    
    parser.add_argument("input", nargs="?", type=Path, help="Input Markdown file")
    parser.add_argument("output", nargs="?", type=Path, help="Output PDF file")
    parser.add_argument("--title", "-t", type=str, help="Document title")
    parser.add_argument("--css", "-c", type=Path, help="Custom CSS file path")
    parser.add_argument(
        "--theme",
        type=str,
        choices=["default", "github", "print"],
        default="default",
        help="Built-in CSS theme (default: default)",
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Batch convert mode: input=output directory",
    )
    
    args = parser.parse_args()
    
    if args.batch:
        if not args.input or not args.output:
            parser.error("Batch mode requires input and output directories")
        
        results = batch_convert(args.input, args.output, theme=args.theme)
        
        print(f"\n{'='*50}")
        print(f"Batch conversion complete!")
        print(f"  Success: {len(results['success'])} files")
        print(f"  Failed:  {len(results['failed'])} files")
        
        if results["failed"]:
            print(f"\nFailed files:")
            for f in results["failed"]:
                print(f"  - {f}")
        
        sys.exit(0 if not results["failed"] else 1)
    
    else:
        if not args.input or not args.output:
            parser.error("Input and output files are required")
        
        success = convert_to_pdf(
            args.input,
            args.output,
            title=args.title,
            css_path=args.css,
            theme=args.theme,
        )
        
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
