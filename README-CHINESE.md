# Markdown to PDF 中文支持说明

> 更新时间：2026-03-05 11:13

---

## ⚠️ 当前限制

### xhtml2pdf（convert-lite.py）
- ❌ **不支持中文字体**
- ✅ 无需额外依赖
- ⚠️ 仅适用于英文文档

### weasyprint（convert.py）
- ✅ **支持中文完美**
- ❌ 需要 GTK3 运行时
- ⚠️ Windows 安装复杂

---

## ✅ 推荐方案

### 方案一：飞书文档导出 PDF（推荐）⭐

**流程**:
```
1. 创建飞书云文档（中文正常）
2. 飞书菜单 → 导出为 → PDF
3. 获得完美中文排版的 PDF
```

**优点**:
- ✅ 中文显示完美
- ✅ 排版专业
- ✅ 无需安装额外软件

**缺点**:
- ⚠️ 需要手动操作（1 分钟）

---

### 方案二：安装 GTK3 使用 weasyprint

**Windows 安装步骤**:

1. **下载 GTK3**:
   https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
   下载 `gtk3-releases-3.24.38-1-win64.exe`

2. **安装 GTK3**:
   ```
   运行安装程序 → 默认选项 → 完成
   ```

3. **安装 Python 依赖**:
   ```bash
   uv pip install weasyprint markdown pygments
   ```

4. **测试**:
   ```bash
   uv run python skills/markdown-to-pdf/convert.py input.md output.pdf
   ```

---

### 方案三：使用在线转换工具

**推荐工具**:
- **Markdown Live Preview**: https://markdownlivepreview.com/
- **Dillinger**: https://dillinger.io/
- **StackEdit**: https://stackedit.io/

**流程**:
1. 打开网站
2. 粘贴 Markdown 内容
3. 导出为 PDF

---

## 📋 当前可用方案

| 方案 | 中文支持 | 安装难度 | 推荐度 |
|------|----------|----------|--------|
| 飞书文档导出 | ✅ 完美 | ⭐ 简单 | ⭐⭐⭐⭐⭐ |
| weasyprint + GTK3 | ✅ 完美 | ⭐⭐⭐⭐ 复杂 | ⭐⭐⭐ |
| xhtml2pdf | ❌ 不支持 | ⭐ 简单 | ⭐ |
| 在线工具 | ✅ 好 | ⭐ 简单 | ⭐⭐⭐⭐ |

---

## 💡 最佳实践

### 当前推荐（立即可用）

```python
# Agent 输出流程
1. 创建飞书云文档 ✅
2. 保存本地 Markdown ✅
3. 需要 PDF 时：飞书 → 导出为 PDF
```

### 代码示例

```python
# 在 agent-integration.py 中
def create_document(content, title, channel):
    # 1. 创建飞书文档
    result = feishu_doc(action="create", title=title)
    feishu_doc(
        action="update_block",
        doc_token=result["document_id"],
        block_id=result["document_id"],
        content=content
    )
    
    # 2. 保存本地 Markdown
    write_file(path, content)
    
    # 3. 返回消息（不自动生成 PDF）
    return f"""
✅ 文档已创建

📄 飞书链接：https://feishu.cn/docx/{result['document_id']}
📂 本地路径：{path}

💡 提示:
- 飞书文档支持在线编辑
- 需要 PDF 时：飞书菜单 → 导出为 PDF
"""
```

---

## 🔮 后续优化

### 自动化飞书 PDF 导出（预计 2-3h）

如果能找到飞书 API 的 PDF 导出接口，可以实现：

```python
# 伪代码
pdf_bytes = feishu_doc.export_pdf(doc_token)
write_file(pdf_path, pdf_bytes)
```

### 评估其他 PDF 库

- **pdfkit**: 基于 wkhtmltopdf，支持中文
- **reportlab**: 直接生成，完全控制
- **fpdf2**: 简单易用，中文需配置

---

**最后更新**: 2026-03-05 11:13  
**状态**: 推荐使用飞书文档导出 PDF
