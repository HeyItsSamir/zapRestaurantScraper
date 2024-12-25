import time
import yelpapi
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime  # Import datetime module for timestamp
from selenium.webdriver.chrome.options import Options  # Import Options

# Initialize the WebDriver (make sure to adjust the path to your WebDriver and Chrome browser)
driver_path = r'C:\Users\Sargo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Update this path
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Update this path

# Set Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_path

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the Yelp website
url = 'https://www.yelp.com'
driver.get(url)

# Wait for the page to load fully
time.sleep(3)  # Adjust this based on your internet speed or implement WebDriverWait for dynamic loading

# Initialize Yelp API client
api_key = 'xzLVZmJCOC6UYLPE-Cqyv8uDFcLDoMYvv_8yIb1O0YgrpYWPyv72ekOeo8FaKLFGI7XiHVBnzOVdEQ_7uhMvJVctIhLAs90Qg9w1VlFtWSbSbebM8FolhN7hsD5sZ3Yx'  # Replace with your actual Yelp API key
yelp = yelpapi.YelpAPI(api_key)

# Search for restaurants in a specific location
search_results = yelp.search_query(term='restaurants', location='Hyde Park, IL')

# Extract the restaurant data elements
restaurant_data = []

# Loop through each restaurant in the search results
for result in search_results['businesses']:
    # Extract restaurant name
    name = result['name']

    # Extract image URL
    image_url = result['image_url']

    # Extract reviews and number of reviews
    reviews = result['review_count']

    # Extract type of restaurant and address
    address = result['location']['address1']
    restaurant_type = result['categories'][0]['title']

    # Extract phone number
    phone_number = result['phone']

    # Extract email (if available)
    email = result.get('email', 'No email available')

    # Extract opening hours
    opening_hours = result['hours'] if 'hours' in result else 'No opening hours'

    # Extract link to restaurant page
    restaurant_link = result['url']

    # Append the data for this restaurant to the list
    restaurant_data.append({
        'Name': name,
        'Image URL': image_url,
        'Reviews': reviews,
        'Type': restaurant_type,
        'Address': address,
        'Phone Number': phone_number,
        'Email': email,
        'Opening Hours': opening_hours,
        'Restaurant Page Link': restaurant_link
    })

# Convert the data to a pandas DataFrame
df = pd.DataFrame(restaurant_data)

# New filename without timestamp
filename = 'my_restaurant_data.csv'  # New filename

# Export to CSV, ensuring that Hebrew characters are properly encoded with UTF-8
df.to_csv(filename, encoding='utf-8-sig', index=False)

# Close the WebDriver
driver.quit()

print(f"Scraping complete, data saved to '{filename}'.")
