# Python-project-university-task-
# Week 3 Python Tasks  ## 📌 Overview This repository contains the completed tasks for **Week 3** including: - File I/O operations - JSON handling - OS &amp; SYS module usage - Virtual Environment setup - Requirements management - Git &amp; GitHub workflow - CLI Notes Manager (Weekly Challenge)  ---



## 🛠 Step-by-Step Instructions

### 1️⃣ Navigate to Project Folder
```bash
cd C:\Users\4BMOIN\Downloads\week3_tasks
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Required Packages
```bash
pip install requests pandas
```

### 5️⃣ Inside venv: Check Installed Packages
```bash
pip list
```
> Take a screenshot for submission.

### 6️⃣ Deactivate Virtual Environment
```bash
deactivate
```

### 7️⃣ Outside venv: Check Installed Packages
```bash
pip list
```
> Take a screenshot for submission.

### 8️⃣ Reactivate venv
```bash
venv\Scripts\activate
```

### 9️⃣ Generate requirements.txt
```bash
pip freeze > requirements.txt
```

### 🔟 Run Python Scripts
```bash
python file_merge_count.py
python student_json.py
python csv_to_json.py
python list_py_files.py
python argv_filenames.py file1.txt file2.txt
python notes_manager.py
```

### 1️⃣1️⃣ Initialize Git and First Commit
```bash
git init
git add .
git commit -m "Initial Week 3 tasks"
```

### 1️⃣2️⃣ Connect to GitHub Repository
```bash
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
```

### 1️⃣3️⃣ Push to GitHub
```bash
git push -u origin main
```

### 1️⃣4️⃣ View Commit History
```bash
git log --oneline --graph --decorate --all
```

---

## 📄 Submission Checklist
- [ ] Inside venv `pip list` screenshot + description
- [ ] Outside venv `pip list` screenshot + description
- [ ] `requirements.txt` file
- [ ] GitHub repo link
- [ ] Python scripts outputs (optional screenshots)

---

## 🧠 Notes
- Use virtual environments to keep project dependencies isolated.
- Always freeze requirements before sharing your project.
- Commit changes frequently with clear messages.

