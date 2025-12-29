import json
from pathlib import Path
from datetime import datetime, timezone

DATA_FILE = Path("data/workflows.json")


def update_dataset():
    if not DATA_FILE.exists():
        return

    # Load current dataset
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    # Append an automated update log entry
    data.append({
        "workflow": "dataset_refresh_log",
        "platform": "system",
        "popularity_metrics": {
            "updated_at": datetime.now(timezone.utc).isoformat()
        },
        "country": "GLOBAL"
    })

    # Save the updated dataset
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("Dataset updated at", datetime.now(timezone.utc))


if __name__ == "__main__":
    update_dataset()
