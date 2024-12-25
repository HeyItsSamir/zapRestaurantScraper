# zapRestaurantScraper

##This is a forked project from Sagi Nevet

zapRest Scraper is a Python tool for scraping restaurant information from [zapRest](https://www.rest.co.il/restaurants/israel/).
It uses Selenium for web scraping and Pandas for data manipulation.
The tool collects details such as restaurant name, image URL, reviews, type of restaurant, address, phone number, and more. The results are saved in a CSV file with a timestamped filename.

In this script, restaurants are automatically loaded by clicking "Show More" multiple times, allowing the scraper to gather data from multiple pages of listings.

## Prerequisites

Before running zapRest Scraper, make sure you have the following installed:

- **Python 3.x**
- **ChromeDriver**
- **Selenium**
- **Pandas**

You can install the required Python packages using:

```bash
pip install selenium pandas webdriver-manager
```
Also, download the appropriate version of ChromeDriver from here and ensure it's in your system's PATH or adjust the driver_path in the script to point to the correct location on your machine.

Getting Started
Clone the repository:

```bash
git clone https://github.com/yourusername/zapRest-scraper.git
cd zapRest-scraper
```
Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```
Install project dependencies:

```bash
pip install -r requirements.txt
```
## Usage
To run the scraper, simply execute the following command:

```bash
python zapRest_scraper.py
```
The tool will scrape restaurant information and save the results to a CSV file named restaurants_data_<timestamp>.csv in the same directory as the script.

## Configuration
You can adjust the settings in the zapRest_scraper.py file to customize the scraping behavior. For example, you can:

- Modify the time.sleep() values to adjust the waiting time for page loading.
- Change the number of times the "Show More" button is clicked.
- Adjust the Chrome options in the WebDriver setup for headless browsing or proxy settings.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Thanks to the contributors of Selenium and Pandas for their excellent tools that made this scraper possible.

