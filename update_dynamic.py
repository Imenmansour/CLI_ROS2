from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup  # Import BeautifulSoup here
import urllib.parse
import re

def setup_driver():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run headless Chrome (no GUI)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Set up the Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_and_clean(url, driver):
    try:
        # Load the webpage
        driver.get(url)

        # Wait for the page to load and check for elements
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        # Get the page source and parse it
        page_source = driver.page_source

        # Parse the HTML content
        soup = BeautifulSoup(page_source, 'html.parser')

        # Remove unwanted elements
        for unwanted in soup(['header', 'footer', 'nav', 'aside']):
            unwanted.decompose()

        # Extract the body content
        body_content = soup.body.get_text(separator=' ', strip=True)

        # Normalize the text
        cleaned_content = normalize_text(body_content)

        return cleaned_content
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""  # Return empty content if there was an error

def normalize_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove common unwanted words/phrases
    common_words = [
        'contact us', 'signin', 'signup', 'about', 'blog', 
        'privacy', 'terms', 'copyright', 'all rights reserved', 
        'marketing', 'advertisement', 'contact', 'cookie'
    ]
    
    for word in common_words:
        text = text.replace(word, '')

    # Remove special characters except for underscores and hyphens
    text = re.sub(r'[^\w\s\.,;:!?\-+*/%<>=&|^~`\'"@#\[\]{}()\\]', '', text)

    return text.strip()

def save_to_file(url, content):
    # Extract the page name from the URL
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path
    page_name = path.rstrip('/').split('/')[-1]

    # Define the filename with .txt extension
    filename = f"{page_name}.txt"

    # Save the cleaned content to a .txt file only if it's not empty
    if content:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Data saved to {filename}")
    else:
        print(f"No content to save for {url}.")
        return True  # Indicate that the content was empty

def process_urls(url_list):
    empty_content_urls = []  # List to store URLs with empty content
    driver = setup_driver()  # Initialize the WebDriver

    for url in url_list:
        print(f"Scraping {url}...")
        cleaned_data = scrape_and_clean(url, driver)
        if save_to_file(url, cleaned_data):
            empty_content_urls.append(url)  # Add URL to the list if content was empty

    driver.quit()  # Close the WebDriver
    return empty_content_urls

# Example usage
url_list = [
    "https://www.hadabot.com/setup-esp32-using-cli-to-work-with-ros2.html?step=publish-ros2-topic-to-blink-led",
    "https://canonical.com/blog/optimise-your-ros-snap-part-7"
]



empty_urls = process_urls(url_list)

# Print the list of URLs that had empty content
if empty_urls:
    print("The following URLs had empty content:")
    for empty_url in empty_urls:
        print(empty_url)
else:
    print("All URLs had content.")
