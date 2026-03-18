# 🌍 Global Time & Calendar API

A FastAPI-based backend service that provides:

- 🌐 Global timezone support
- 🗓️ Gregorian & Ethiopian calendar conversion
- 🌍 Multilingual day names (English + Amharic)

## 🚀 Features

- Get current time for any timezone
- Convert date to Ethiopian calendar
- Translate day names to Amharic
- REST API with auto documentation

## 📌 Endpoints

### 1. Get Current Time
GET /time?timezone=Africa/Addis_Ababa

### 2. Get Today Info
GET /today

Optional query params:
- lang=am
- calendar=ethiopian

Example:
GET /today?calendar=ethiopian&lang=am

## 🛠️ Tech Stack

- FastAPI
- Uvicorn
- pytz
- ethiopian-date

## ▶️ Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```


---

# 2️⃣ Add `.gitignore`

Create:

```text
.gitignore
venv/
__pycache__/
*.pyc
.env
```