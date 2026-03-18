from fastapi import FastAPI
from datetime import datetime
import pytz


# from ethiopian_date import EthiopianDateConverter as ethiopian
app = FastAPI()

#from fastapi import FastAPI
from datetime import datetime
import pytz
from ethiopian_date import EthiopianDateConverter as ethiopian

app = FastAPI()
day_translations = {
    "Monday": "ሰኞ",
    "Tuesday": "ማክሰኞ",
    "Wednesday": "ረቡዕ",
    "Thursday": "ሐሙስ",
    "Friday": "አርብ",
    "Saturday": "ቅዳሜ",
    "Sunday": "እሁድ"
}

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
            eth = ethiopian.to_ethiopian(now.year, now.month, now.day)
            date = f"{eth[2]}/{eth[1]}/{eth[0]}"
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
day_translations = {
        "Monday": "ሰኞ",
        "Tuesday": "ማክሰኞ",
        "Wednesday": "ረቡዕ",
        "Thursday": "ሐሙስ",
        "Friday": "አርብ",
        "Saturday": "ቅዳሜ",
        "Sunday": "እሁድ"             
    }
@app.get("/today")
def get_today(timezone:str ="Africa/Addis_Ababa",
                  lang:str = "en",
                  calander:str="gregorian"
                  ):
        try:
            tz =pytz.timezone(timezone)
            now = datetime.now(tz)

            day_en = now.strftime("%A")
            if lang == "am":
                day = day_translations.get(day_en,day_en)
            else:
                day = day_en
            if calander =="ethiopian":
                 eth_date = ethiopian.from_gregorian(now.year,now.month,now.day)
                 date = f"{eth_date[2]}/{eth_date[1]}/{eth_date[0]}"
            else:date = now.strftime("%Y-%m-%d")
            return{
                "timezone":timezone,
                "day":day,
                "date":date,
                "calendar":calander,
                "language":lang
            
            }
        except pytz.UnknownTimeZoneError:
            return{"error":"Invalid timezone"}