FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

Then press **Ctrl + S** to save.

---

**Your folder should now look like this:**
```
📁 SmartHire
 ├── 📁 smarthire
 ├── 📁 tracker
 ├── 📁 venv
 ├── 📄 .gitignore
 ├── 📄 Dockerfile    ← NEW FILE
 ├── 📄 manage.py
 ├── 📄 requirements.txt
 └── 📄 db.sqlite3