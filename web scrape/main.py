import requests
from bs4 import BeautifulSoup

# pip install requests beautifulsoup4
# Function to get the HTML content from the URL
def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Function to scrape data from the website
def scrape_website(url, tag, class_name=None):
    # Get the HTML content
    html = get_html(url)

    if html:
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # If class_name is provided, scrape elements by tag and class
        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)

        # Extract and print the text from the scraped elements
        for i, element in enumerate(elements, 1):
            print(f"{i}. {element.get_text(strip=True)}")


# Main function to prompt user for input and run the scraper
if __name__ == "__main__":
    print("Welcome to the Web Scraper!")
    url = input("Enter the URL of the website you want to scrape: ")
    tag = input("Enter the HTML tag you want to scrape (e.g., 'h2', 'p', 'a'): ")
    class_name = input("Enter the class name for more specific scraping (or press Enter to skip): ").strip() or None

    # Scrape the website with the given parameters
    scrape_website(url, tag, class_name)
