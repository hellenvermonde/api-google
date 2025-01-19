import json
from datetime import datetime

def to_json(data):
    """Convert a Python dictionary to a JSON string."""
    return json.dumps(data)

def from_json(json_str):
    """Convert a JSON string to a Python dictionary."""
    return json.loads(json_str)

def format_date(date_str, format='%Y-%m-%d'):
    """Convert a date string to a specific format."""
    return datetime.strptime(date_str, format).strftime('%d/%m/%Y')