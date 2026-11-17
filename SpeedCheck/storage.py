import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "history.csv"
FIELDS = [
    "timestamp",
    "average_ping",
    "jitter",
    "packet_loss",
    "quality"
]


def save_measurement(measurement, result):
    """Añade una medición al archivo CSV."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_exists = DATA_FILE.exists() and DATA_FILE.stat().st_size > 0

    row = {
        "timestamp": measurement.timestamp,
        "average_ping": round(result["average_ping"], 2),
        "jitter": round(result["jitter"], 2),
        "packet_loss": round(result["packet_loss"], 2),
        "quality": result["quality"]
    }

    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def load_measurements():
    """Lee todas las mediciones guardadas."""
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
