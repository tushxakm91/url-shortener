import string
import random
from database import add_url, url_exists, get_url

def generate_short_code(length=6):
    """Generate a random short code"""
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code

def create_short_url(original_url):
    """Create a shortened URL with unique short code"""
    # Validate URL
    if not original_url.startswith(('http://', 'https://')):
        return None, "URL must start with http:// or https://"
    
    # Generate unique short code
    while True:
        short_code = generate_short_code()
        if not url_exists(short_code):
            break
    
    # Store in database
    add_url(short_code, original_url)
    return short_code, "Success"

def resolve_short_url(short_code):
    """Get original URL from short code"""
    original_url = get_url(short_code)
    if original_url:
        return original_url, "Success"
    return None, "Short code not found"

def is_valid_url(url):
    """Validate URL format"""
    return url.startswith(('http://', 'https://')) and len(url) > 10
