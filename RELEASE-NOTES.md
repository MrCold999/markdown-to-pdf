# markdown-to-pdf Skill - 发布指南

## 📦 包信息

| 属性 | 值 |
|------|-----|
| 名称 | markdown-to-pdf |
| 版本 | 1.0.0 |
| 描述 | Markdown 转 PDF 工具，支持中文排版 |
| 作者 | Boss 学术加速器 |
| 许可证 | MIT |
| 大小 | 15.7 KB (ZIP) |
| 依赖 | markdown, xhtml2pdf, reportlab |

---

## ✅ 已完成准备工作

- [x] 技能文件创建完成
- [x] clawhub.json 元数据配置
- [x] 测试用例验证通过
- [x] ZIP 包已生成
- [x] 文档齐全（SKILL.md, README.md, PUBLISH.md）

---

## 📁 包内容

```
markdown-to-pdf/
├── SKILL.md              # 技能说明（中文）
├── README.md             # 使用文档（英文）
├── PUBLISH.md            # 发布指南
├── clawhub.json          # 包元数据
├── convert-lite.py       # 主转换脚本（推荐）
├── convert.py            # 完整版（需要 GTK3）
├── styles/
│   └── default.css       # 默认 CSS 主题
├── examples/
│   ├── sample.md         # 示例文件
│   └── sample.pdf        # 示例输出
└── RELEASE-NOTES.md      # 发布说明
```

---

## 🚀 发布方式

### 方式 1：通过 ClawHub 网站（推荐）

1. **访问 ClawHub**
   - 网址：https://clawhub.com
   - 登录账号

2. **提交技能**
   - 点击 "Submit Skill" 或 "发布技能"
   - 上传 `markdown-to-pdf-skill.zip`
   - 填写元数据（从 clawhub.json 复制）

3. **填写信息**
   ```
   Name: markdown-to-pdf
   Version: 1.0.0
   Description: Convert Markdown files to professional PDF documents. 
                No GTK3 dependency required. Supports Chinese language.
   Category: document / productivity
   Tags: markdown, pdf, convert, document, chinese
   ```

4. **提交审核**
   - 确认信息无误
   - 提交等待审核（通常 1-2 个工作日）

---

### 方式 2：GitHub + ClawHub 集成

1. **创建 GitHub 仓库**
   ```bash
   # 在 GitHub 创建新仓库：markdown-to-pdf
   
   # 本地操作
   cd C:\Users\share\.openclaw\workspace\skills\markdown-to-pdf
   git init
   git add .
   git commit -m "Initial release: markdown-to-pdf skill v1.0.0"
   git remote add origin https://github.com/YOUR_USERNAME/markdown-to-pdf.git
   git push -u origin main
   ```

2. **在 ClawHub 注册**
   - 访问 https://clawhub.com
   - 关联 GitHub 账号
   - 选择仓库进行发布

---

### 方式 3：命令行发布（需修复 CLI）

```bash
# 当前 ClawHub CLI 有依赖问题，暂时不推荐
# 待修复后使用：

cd C:\Users\share\.openclaw\workspace\skills\markdown-to-pdf
clawhub publish
```

---

## 📝 发布清单

发布前确认：

- [x] SKILL.md 包含完整使用说明
- [x] README.md 提供英文文档
- [x] clawhub.json 元数据正确
- [x] 代码测试通过（sample.pdf 已生成）
- [x] 依赖明确列出
- [x] 许可证文件（可选）
- [ ] 发布到 ClawHub（待执行）

---

## 🔧 发布后验证

发布成功后：

1. **搜索技能**
   ```bash
   clawhub search markdown-to-pdf
   ```

2. **安装测试**
   ```bash
   clawhub install markdown-to-pdf
   ```

3. **功能验证**
   ```bash
   uv run python skills/markdown-to-pdf/convert-lite.py test.md test.pdf
   ```

---

## 📞 支持资源

| 资源 | 链接 |
|------|------|
| ClawHub | https://clawhub.com |
| OpenClaw 文档 | https://docs.openclaw.ai |
| 技能开发指南 | https://docs.openclaw.ai/skills |
| 社区 Discord | https://discord.com/invite/clawd |

---

## 📊 技能特性亮点

1. **无 GTK3 依赖** - 简化安装流程
2. **中文优化** - 微软雅黑/宋体字体支持
3. **轻量快速** - 仅依赖 3 个 Python 包
4. **跨平台** - Windows/macOS/Linux 通用
5. **专业输出** - A4 打印优化布局

---

**创建时间**: 2026-03-03  
**最后更新**: 2026-03-03 23:10  
**包位置**: `C:\Users\share\.openclaw\workspace\skills\markdown-to-pdf-skill.zip`

---

## ⏭️ 下一步

选择一种发布方式执行：

1. **快速发布** → 方式 1（ClawHub 网站上传）
2. **开源协作** → 方式 2（GitHub + ClawHub）
3. **等待 CLI 修复** → 方式 3（命令行）

推荐：**方式 1** - 最简单快捷，5 分钟内完成发布。
