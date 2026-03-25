# 🌍 Global Time & Calendar API

A professional FastAPI-based service that provides a real-time web dashboard and API for global time tracking .

- 🌐 Global timezone support
- 🗓️ Gregorian & Ethiopian calendar conversion
- 🌍 Multilingual day names (English + Amharic)

## 🚀 Features

- **Interactive Dashboard:** A modern, responsive UI built with Tailwind CSS.
- **Global Timezone Support:** Get the current time for any location using `pytz`.
- **Calendar Conversion:** Seamlessly switch between Gregorian and Ethiopian calendars.
- **Multilingual Support:** Day names available in both English and Amharic.
- **Auto-Documentation:** Interactive API exploration via Swagger UI.

## 📁 Project Structure

```text
global-time-api/
├── app/
│   ├── main.py          # Backend logic & API routes
│   ├── static/          # CSS and frontend assets
│   └── templates/       # HTML UI (Jinja2)
├── .gitignore           # Git exclusion rules
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies

 ```

## 📌 Endpoints

### 1. Get Current Time
GET /time?timezone=Africa/Addis_Ababa

### 2. Get Today Info
GET /today

Query Parameters:
- timezone: (e.g., Africa/Addis_Ababa)

- lang: en or am

- calendar: gregorian or ethiopian

Example:
GET /today?calendar=ethiopian&lang=am

## 🛠️ Tech Stack

- Backend: FastAPI, Uvicorn

- Templating: Jinja2

- Styling: Tailwind CSS (CDN)

- Libraries: pytz, ethiopian-date

## ▶️ Run Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/global-time-api.git](https://github.com/your-username/global-time-api.git)
cd global-time-api

```
**2. Set up the Virtual Environment:**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```
**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```
**4. Start the Server:**
```bash
uvicorn app.main:app --reload 

```
---

**5. Access the App:**
Open 
```bash

http://127.0.0.1:8000 
``` 
in your browser to see the dashboard.

---


