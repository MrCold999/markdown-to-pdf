---
name: markdown-to-pdf
description: Convert Markdown files to PDF with professional styling. Uses Python + markdown + weasyprint for high-quality output. Supports custom CSS themes, batch conversion, and HTML intermediate format.
---

# Markdown to PDF Converter

将 Markdown 文档转换为专业排版的 PDF 文件。

## 功能特性

- ✅ Markdown → HTML → PDF 高质量转换
- ✅ 支持自定义 CSS 主题
- ✅ 批量转换多个文件
- ✅ 保留代码高亮、表格、引用等格式
- ✅ 支持中文排版优化
- ✅ 可生成打印优化的 PDF

## 依赖安装

首次使用前安装依赖：

```bash
# 使用 uv 安装 Python 依赖（推荐，无需 GTK3）
uv pip install markdown xhtml2pdf reportlab
```

**注意**: 使用 `convert-lite.py` 脚本，基于 xhtml2pdf，无需安装 GTK3。

## 使用方法

### 基础用法

```bash
# 转换单个文件（推荐，无需 GTK3）
uv run python skills/markdown-to-pdf/convert-lite.py input.md output.pdf

# 指定标题
uv run python skills/markdown-to-pdf/convert-lite.py input.md output.pdf --title "文档标题"
```

### 高级用法（需要 GTK3）

```bash
# 使用完整功能版本（支持更多 CSS 特性）
uv run python skills/markdown-to-pdf/convert.py input.md output.pdf

# 使用自定义 CSS
uv run python skills/markdown-to-pdf/convert.py input.md output.pdf --css custom.css

# 批量转换
uv run python skills/markdown-to-pdf/convert.py --batch ./docs/ ./output/
```

### 在 OpenClaw 中使用

```markdown
@markdown-to-pdf 请将 IMPORT-GUIDE.md 转换为 PDF
```

## 输出示例

转换后的 PDF 特性：
- 专业字体（中文使用思源黑体/微软雅黑）
- 代码块语法高亮
- 表格样式优化
- 打印友好的页边距
- 自动目录生成（可选）

## CSS 主题

内置主题：
- `default` - 简洁专业风格
- `github` - GitHub 风格
- `print` - 打印优化（黑白、省墨）

自定义 CSS 示例：

```css
body {
  font-family: "Microsoft YaHei", "SimHei", sans-serif;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
  padding: 40px;
}

h1 { border-bottom: 2px solid #333; }
code { background: #f5f5f5; padding: 2px 6px; }
pre { background: #f8f8f8; padding: 16px; overflow-x: auto; }
```

## 技术实现

使用 Python 工具链：
- **markdown**: Markdown 解析
- **pygments**: 代码语法高亮
- **weasyprint**: HTML/CSS → PDF 渲染

## 故障排除

### 问题 1: weasyprint 安装失败
**解决**: Windows 需要先安装 GTK3 运行环境
```bash
# 下载并安装 GTK3
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
```

### 问题 2: 中文字体缺失
**解决**: 修改 CSS 使用系统字体
```css
body { font-family: "Microsoft YaHei", sans-serif; }
```

### 问题 3: PDF 乱码
**解决**: 确保文件使用 UTF-8 编码，并在 HTML 中声明
```html
<meta charset="UTF-8">
```

## 文件结构

```
skills/markdown-to-pdf/
├── SKILL.md              # 本文件
├── convert.py            # 转换脚本
├── styles/
│   ├── default.css       # 默认主题
│   ├── github.css        # GitHub 主题
│   └── print.css         # 打印主题
└── examples/
    └── sample.md         # 示例文件
```

## 相关技能

- **nano-pdf**: PDF 文件处理
- **summarize**: 文档摘要（可与本技能配合使用）

## 版本历史

- v1.0.0 (2026-03-03) - 初始版本，支持基础转换功能

## 许可证

MIT License

---

*Skill created for Boss 学术加速器 project*
