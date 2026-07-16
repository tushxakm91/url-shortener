import json
import os
from datetime import datetime

DATABASE_FILE = 'urls.json'

def load_database():
    """Load URLs from JSON file"""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_database(data):
    """Save URLs to JSON file"""
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_url(short_code, original_url):
    """Add a new shortened URL"""
    db = load_database()
    db[short_code] = {
        'original_url': original_url,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'clicks': 0
    }
    save_database(db)

def get_url(short_code):
    """Retrieve original URL by short code"""
    db = load_database()
    if short_code in db:
        db[short_code]['clicks'] += 1
        save_database(db)
        return db[short_code]['original_url']
    return None

def url_exists(short_code):
    """Check if short code already exists"""
    db = load_database()
    return short_code in db

def get_all_urls():
    """Get all shortened URLs"""
    return load_database()

def delete_url(short_code):
    """Delete a shortened URL"""
    db = load_database()
    if short_code in db:
        del db[short_code]
        save_database(db)
        return True
    return False

def get_stats(short_code):
    """Get statistics for a shortened URL"""
    db = load_database()
    if short_code in db:
        return db[short_code]
    return None
