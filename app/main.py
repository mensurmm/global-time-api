from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import pytz
from ethiopian_date import EthiopianDateConverter as ethiopian

app = FastAPI()

# Tell FastAPI where to find your HTML and CSS
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

day_translations = {
    "Monday": "ሰኞ", "Tuesday": "ማክሰኞ", "Wednesday": "ረቡዕ",
    "Thursday": "ሐሙስ", "Friday": "አርብ", "Saturday": "ቅዳሜ", "Sunday": "እሁድ"
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # This serves your attractive UI
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/today")
def get_today(
    timezone: str = "Africa/Addis_Ababa",
    lang: str = "en",
    calendar: str = "gregorian"
):
    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        day_en = now.strftime("%A")
        
        day = day_translations.get(day_en, day_en) if lang == "am" else day_en

        if calendar == "ethiopian":
            # TRY THIS FIRST (Most common for newer versions):
            try:
                eth_date = ethiopian.from_gregorian(now.year, now.month, now.day)
            except AttributeError:
                # USE THIS IF THE FIRST ONE FAILS (Common in older versions):
                eth_date = ethiopian.to_ethiopian(now.year, now.month, now.day)
            
            # Formats the result as Day/Month/Year
            date = f"{eth_date.day}/{eth_date.month}/{eth_date.year}"
        else:
            date = now.strftime("%Y-%m-%d")

        return {
            "timezone": timezone,
            "day": day,
            "date": date,
            "calendar": calendar,
            "language": lang
        }
    except pytz.UnknownTimeZoneError:
        return {"error": "Invalid timezone"}