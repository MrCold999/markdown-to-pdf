# markdown-to-pdf Skill Package

## Package Info

- **Name**: markdown-to-pdf
- **Version**: 1.0.0
- **Description**: Convert Markdown files to professional PDF documents
- **Author**: Boss 学术加速器
- **License**: MIT

## Files

```
markdown-to-pdf/
├── SKILL.md           # Skill description and usage
├── README.md          # Documentation (English)
├── clawhub.json       # Package metadata
├── convert-lite.py    # Main converter script
├── convert.py         # Full-featured converter (optional)
├── styles/
│   └── default.css    # Default CSS theme
└── examples/
    └── sample.md      # Example file
```

## Installation Requirements

```bash
uv pip install markdown xhtml2pdf reportlab
```

## Usage

```bash
uv run python convert-lite.py input.md output.pdf --title "Document Title"
```

## Publishing to ClawHub

### Option 1: Via ClawHub CLI (if available)

```bash
# Navigate to skill directory
cd skills/markdown-to-pdf

# Publish
clawhub publish
```

### Option 2: Manual Submission

1. **Create GitHub Repository**
   ```bash
   # Create repo at: https://github.com/your-username/markdown-to-pdf
   git init
   git add .
   git commit -m "Initial release: markdown-to-pdf skill"
   git remote add origin https://github.com/your-username/markdown-to-pdf.git
   git push -u origin main
   ```

2. **Submit to ClawHub**
   - Visit: https://clawhub.com
   - Navigate to "Submit Skill"
   - Provide GitHub repository URL
   - Fill in metadata from `clawhub.json`

3. **Alternative: Direct Upload**
   - Package as ZIP:
     ```bash
     Compress-Archive -Path * -DestinationPath markdown-to-pdf.zip
     ```
   - Upload via ClawHub web interface

## Testing

Before publishing, test the skill:

```bash
# Test conversion
uv run python convert-lite.py examples/sample.md test-output.pdf

# Verify output
test-output.pdf should be created with proper formatting
```

## Support

- Documentation: See README.md
- Issues: GitHub Issues
- Contact: Boss 学术加速器 team

---

**Created**: 2026-03-03
**Updated**: 2026-03-03
