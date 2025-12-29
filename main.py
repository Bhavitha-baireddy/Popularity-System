import json
from pathlib import Path
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="n8n Popularity System",
    description="API that returns popular n8n workflows across platforms",
    version="1.0.0"
)

DATA_FILE = Path("data/workflows.json")


@app.get("/")
def read_root():
    return {"message": "n8n Popularity System API is running"}


@app.get("/workflows")
def get_workflows():
    if not DATA_FILE.exists():
        raise HTTPException(status_code=500, detail="Data file not found")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return {"count": len(data), "data": data}


@app.get("/workflows/{platform}")
def get_workflows_by_platform(platform: str):
    if not DATA_FILE.exists():
        raise HTTPException(status_code=500, detail="Data file not found")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    filtered = [w for w in data if w["platform"].lower() == platform.lower()]

    return {
        "platform": platform,
        "count": len(filtered),
        "data": filtered
    }


@app.get("/workflows/country/{country}")
def get_workflows_by_country(country: str):
    if not DATA_FILE.exists():
        raise HTTPException(status_code=500, detail="Data file not found")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    filtered = [w for w in data if w["country"].upper() == country.upper()]

    return {
        "country": country,
        "count": len(filtered),
        "data": filtered
    }
