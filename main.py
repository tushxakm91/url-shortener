from shortener import create_short_url, resolve_short_url, is_valid_url
from database import get_all_urls, delete_url, get_stats

def print_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("         URL SHORTENER - MAIN MENU")
    print("="*50)
    print("1. Shorten a URL")
    print("2. Resolve a shortened URL")
    print("3. View all shortened URLs")
    print("4. View URL statistics")
    print("5. Delete a shortened URL")
    print("6. Exit")
    print("="*50)

def shorten_url_option():
    """Handle URL shortening"""
    print("\n--- Shorten a URL ---")
    url = input("Enter the URL you want to shorten: ").strip()
    
    if not is_valid_url(url):
        print("❌ Invalid URL! Make sure it starts with http:// or https://")
        return
    
    short_code, message = create_short_url(url)
    if short_code:
        print(f"\n✅ Success!")
        print(f"Original URL: {url}")
        print(f"Shortened URL: short:///{short_code}")
    else:
        print(f"❌ Error: {message}")

def resolve_url_option():
    """Handle URL resolution"""
    print("\n--- Resolve a Shortened URL ---")
    short_code = input("Enter the short code: ").strip()
    
    original_url, message = resolve_short_url(short_code)
    if original_url:
        print(f"\n✅ Found!")
        print(f"Original URL: {original_url}")
    else:
        print(f"❌ {message}")

def view_all_urls():
    """Display all shortened URLs"""
    print("\n--- All Shortened URLs ---")
    urls = get_all_urls()
    
    if not urls:
        print("No shortened URLs yet!")
        return
    
    print(f"\n{'Short Code':<12} {'Original URL':<50} {'Clicks':<8} {'Created':<20}")
    print("-" * 90)
    
    for short_code, data in urls.items():
        original = data['original_url'][:47] + "..." if len(data['original_url']) > 50 else data['original_url']
        print(f"{short_code:<12} {original:<50} {data['clicks']:<8} {data['created_at']:<20}")

def view_stats_option():
    """View statistics for a shortened URL"""
    print("\n--- URL Statistics ---")
    short_code = input("Enter the short code: ").strip()
    
    stats = get_stats(short_code)
    if stats:
        print(f"\n✅ Statistics for '{short_code}':")
        print(f"   Original URL: {stats['original_url']}")
        print(f"   Created: {stats['created_at']}")
        print(f"   Total Clicks: {stats['clicks']}")
    else:
        print(f"❌ Short code '{short_code}' not found!")

def delete_url_option():
    """Delete a shortened URL"""
    print("\n--- Delete a Shortened URL ---")
    short_code = input("Enter the short code to delete: ").strip()
    
    confirm = input(f"Are you sure you want to delete '{short_code}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        if delete_url(short_code):
            print(f"✅ Short code '{short_code}' deleted successfully!")
        else:
            print(f"❌ Short code '{short_code}' not found!")
    else:
        print("❌ Deletion cancelled!")

def main():
    """Main application loop"""
    print("\n" + "="*50)
    print("    Welcome to URL Shortener! 🔗")
    print("="*50)
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            shorten_url_option()
        elif choice == '2':
            resolve_url_option()
        elif choice == '3':
            view_all_urls()
        elif choice == '4':
            view_stats_option()
        elif choice == '5':
            delete_url_option()
        elif choice == '6':
            print("\n👋 Thank you for using URL Shortener. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
