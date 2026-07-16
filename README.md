# URL Shortener 🔗

A simple Python application to shorten long URLs, store them, and track click statistics.

## Features

✅ **Shorten URLs** - Convert long URLs into short, easy-to-share codes
✅ **Resolve URLs** - Retrieve original URLs from short codes
✅ **Track Statistics** - Monitor clicks and creation dates
✅ **Manage URLs** - View, delete, and organize your shortened URLs
✅ **Local Storage** - All data stored in a JSON file (no database setup needed)

## Project Structure

```
url-shortener/
├── main.py           # Main application with CLI interface
├── shortener.py      # Core URL shortening logic
├── database.py       # Database operations (JSON-based)
├── requirements.txt  # Python dependencies
└── README.md        # Project documentation
```

## Installation

### 1. Clone or Download the Project
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

## Usage

When you run the application, you'll see a menu with these options:

### 1. Shorten a URL
```
Enter the URL: https://www.example.com/very/long/url/path
Shortened URL: short:///abc123
```

### 2. Resolve a Shortened URL
```
Enter short code: abc123
Original URL: https://www.example.com/very/long/url/path
```

### 3. View All URLs
Shows a table of all shortened URLs with statistics

### 4. View URL Statistics
```
Enter short code: abc123
Original URL: https://www.example.com/very/long/url/path
Created: 2024-01-15 10:30:45
Total Clicks: 5
```

### 5. Delete a Shortened URL
Remove a shortened URL from the database

### 6. Exit
Quit the application

## How It Works

1. **URL Shortening Process**
   - Takes a long URL as input
   - Generates a random 6-character short code
   - Stores the mapping in `urls.json`

2. **Data Storage**
   - All URLs stored locally in `urls.json`
   - Each entry contains:
     - Original URL
     - Creation timestamp
     - Click count

3. **URL Resolution**
   - Look up short code in database
   - Return original URL
   - Increment click counter

## Data Storage

URLs are stored in `urls.json` with this format:

```json
{
  "abc123": {
    "original_url": "https://www.example.com/long/url",
    "created_at": "2024-01-15 10:30:45",
    "clicks": 5
  },
  "xyz789": {
    "original_url": "https://github.com/some/repo",
    "created_at": "2024-01-15 11:45:20",
    "clicks": 2
  }
}
```

## Example Workflow

```bash
$ python main.py

==================================================
    Welcome to URL Shortener! 🔗
==================================================

==================================================
         URL SHORTENER - MAIN MENU
==================================================
1. Shorten a URL
2. Resolve a shortened URL
3. View all shortened URLs
4. View URL statistics
5. Delete a shortened URL
6. Exit
==================================================
Enter your choice (1-6): 1

--- Shorten a URL ---
Enter the URL you want to shorten: https://www.wikipedia.org/wiki/Python_(programming_language)

✅ Success!
Original URL: https://www.wikipedia.org/wiki/Python_(programming_language)
Shortened URL: short:///kR2pQx
```

## Future Enhancements

- 🌐 Web interface using Flask
- 📊 Advanced analytics dashboard
- 🔐 Custom short codes
- 🌍 QR code generation
- 📧 Email sharing
- 🔒 User authentication
- ☁️ Cloud storage integration

## Requirements

- Python 3.7+
- Flask 2.3.0
- Requests 2.31.0

## License

MIT License - Feel free to use this project however you like!

## Support

If you encounter any issues, try:
1. Ensure Python 3.7+ is installed
2. Check that all dependencies are installed: `pip install -r requirements.txt`
3. Make sure the `urls.json` file has write permissions

---

Happy URL Shortening! 🚀
