from pytrends.request import TrendReq
import json
from pathlib import Path

DATA_FILE = Path("data/workflows.json")

def fetch_google_trends():
    pytrends = TrendReq(hl="en-US", tz=330)

    keywords = [
        "n8n automation",
        "n8n slack integration",
        "n8n google sheets workflow",
        "n8n email automation"
    ]

    pytrends.build_payload(keywords, timeframe="today 3-m", geo="US")
    us_data = pytrends.interest_over_time()

    pytrends.build_payload(keywords, timeframe="today 3-m", geo="IN")
    india_data = pytrends.interest_over_time()

    with open(DATA_FILE, "r") as f:
        workflows = json.load(f)

    def add_entries(dataframe, country):
        for keyword in keywords:
            values = dataframe[keyword].tolist()
            avg_interest = sum(values) / len(values)

            workflows.append({
                "workflow": keyword,
                "platform": "Google",
                "popularity_metrics": {
                    "avg_search_interest": round(avg_interest, 2)
                },
                "country": country
            })

    add_entries(us_data, "US")
    add_entries(india_data, "IN")

    with open(DATA_FILE, "w") as f:
        json.dump(workflows, f, indent=2)

    print("Google Trends data added successfully.")
