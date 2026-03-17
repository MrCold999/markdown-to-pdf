# weasyprint 安装状态

> 更新时间：2026-03-05 13:20

---

## ⚠️ 安装失败

### 问题

**GTK3 运行时无法通过 winget 安装**

```
winget install --id GTK.GTK3 -e --silent
错误：找不到与输入条件匹配的程序包
```

---

## 🔧 替代方案

### 方案 A：手动下载 GTK3（推荐）

**步骤**:
1. 访问：https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
2. 下载最新版本（如 `gtk3-releases-3.24.38-1-win64.exe`）
3. 运行安装程序
4. 测试：`uv run python -c "from weasyprint import HTML"`

**预计时间**: 10 分钟

---

### 方案 B：使用飞书文档导出（立即可用）⭐

**流程**:
```
1. 创建飞书云文档（中文正常）✅
2. 飞书菜单 → 导出为 → PDF
3. 获得完美中文排版的 PDF
```

**耗时**: 1 分钟

**优点**:
- ✅ 立即可用
- ✅ 无需安装
- ✅ 中文完美

---

### 方案 C：使用其他 PDF 库

**选项**:
- **pdfkit**: 需要 wkhtmltopdf
- **reportlab**: 直接生成，需配置中文字体
- **PyMuPDF**: 读取为主，生成有限

---

## 💡 建议

**当前最佳**: 使用飞书文档导出 PDF

**原因**:
- ✅ 立即可用（1 分钟）
- ✅ 中文显示完美
- ✅ 无需安装额外软件
- ❌ weasyprint 需要 GTK3（安装复杂）

---

**状态**: 推荐使用飞书导出方案
