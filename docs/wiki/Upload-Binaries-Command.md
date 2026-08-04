# Upload Binaries Command

Use local Git for workbook and image assets.

```bash
git clone https://github.com/samusa099/Bangladesh-MPO-School-College-Salary-Tax-Toolkit.git
cd Bangladesh-MPO-School-College-Salary-Tax-Toolkit
mkdir -p excel/school_college assets/previews

# copy files into these paths, then:
git add excel/school_college/MPO_School_College_Salary_Tax_BD_TY2026_27.xlsx
git add assets/previews/cover-banner.jpg assets/previews/project-icon.jpg assets/previews/social-preview.jpg assets/previews/dashboard-preview.jpg
git commit -m "assets: add v0.1.2 workbook and preview images"
git push origin main
```

Only push trusted generated files.
