# markdown-to-pdf

Convert Markdown files to professional PDF documents with a single command. No external dependencies like GTK3 required.

## Features

- ✅ Markdown → PDF conversion
- ✅ Chinese language support (Microsoft YaHei, SimHei fonts)
- ✅ Code syntax highlighting
- ✅ Table styling
- ✅ Print-optimized layout
- ✅ No GTK3 dependency (uses xhtml2pdf)
- ✅ Single command conversion

## Installation

```bash
# Install the skill
clawhub install markdown-to-pdf

# Install Python dependencies
uv pip install markdown xhtml2pdf reportlab
```

## Usage

```bash
# Basic conversion
uv run python skills/markdown-to-pdf/convert-lite.py input.md output.pdf

# With custom title
uv run python skills/markdown-to-pdf/convert-lite.py input.md output.pdf --title "My Document"
```

## Example

```bash
# Convert the import guide
uv run python skills/markdown-to-pdf/convert-lite.py \
  projects/backup/IMPORT-GUIDE.md \
  projects/backup/IMPORT-GUIDE.pdf \
  --title "Project Import Guide"
```

## Output

The generated PDF includes:
- Professional typography
- Chinese font support
- Styled code blocks
- Formatted tables
- Print-ready A4 layout

## Technical Details

- **Parser**: Python markdown
- **PDF Engine**: xhtml2pdf (ReportLab)
- **CSS**: Built-in professional theme
- **Encoding**: UTF-8

## Troubleshooting

### Issue: PDF is empty
**Solution**: Check that the Markdown file has content and uses UTF-8 encoding.

### Issue: Chinese characters not displaying
**Solution**: Ensure Windows has Chinese fonts installed (Microsoft YaHei, SimHei).

### Issue: Code blocks not styled
**Solution**: The lite version uses basic styling. For advanced highlighting, use the full version with weasyprint.

## File Structure

```
skills/markdown-to-pdf/
├── SKILL.md           # This file
├── convert-lite.py    # Lite version (no GTK3 needed)
├── convert.py         # Full version (requires GTK3)
├── styles/
│   └── default.css    # Default CSS theme
└── examples/
    └── sample.md      # Example file
```

## Version

v1.0.0 (2026-03-03) - Initial release

## License

MIT License

## Author

Created for Boss 学术加速器 project
