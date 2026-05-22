import requests
import pyttsx3
import winsound
import json
import datetime
date = datetime.date.today()
d,a,b = str(date).split("-")
date1 = f"{d}-{a}-{int(b)-1}"
api = "e5afe8e9a7cf4048b3c99327b579f08c"
sname = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", "META", "NVDA", "NFLX"]
r = []
for stock in sname:
    url = f"https://eodhd.com/api/eod/{stock}.US?api_token=6a1038a759cb95.52446464&fmt=json"
    response = requests.get(url)
    data = response.json()
    for data1 in data:
        if date1 == data1["date"]:
            r.append((data1["close"],stock))
            print("-----------------------------------------------------------")
            print(f"STOCK NAME : {stock}")
            print(f"DATE : {date1}")
            print(f"OPENING PRICE : {data1["open"]}")
            print(f"HIGH PRICE : {data1["high"]}")
            print(f"LOW PRICE : {data1["low"]}")
            print(f"CLOSING PRICE : {data1["close"]}")
            print("-----------------------------------------------------------")
t = max(r)
s , e = str(t).split(",")
S = s.replace(")","")
E = e.replace(")","")
engine = pyttsx3.init()
message = f"GOOD EVENING SIR THE HIGHEST STOCK OF TODAY IS {E} AT CLOSING PRICE IS {S} DOLLAR. THANK YOU"

print("\nALERT MESSAGE:")
print(message)
winsound.Beep(1000, 2000)
engine.say(message)
engine.runAndWait()