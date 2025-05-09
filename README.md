# Web Contact Scraper

A privacy-focused web scraping tool that extracts contact information (emails, phone numbers, and addresses) from websites using Firefox with Tor routing.

## Features

- Uses Tor network and Ubuntu for anonymous browsing
- Firefox WebDriver integration on Ubuntu
- Extracts emails, phone numbers, and addresses using regex patterns
- Outputs results in a clean HTML format

## Requirements

- Python 3.8+
- Firefox browser
- Tor service running on port 9050
- Dependencies listed in `requirements.txt`

## Installation

1. Ensure Tor is installed and running:
```bash
# For Debian/Ubuntu:
sudo apt-get install tor
sudo service tor start

# For macOS (using Homebrew):
brew install tor
brew services start tor

# For Windows:
# Download and install Tor Browser from https://www.torproject.org/
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Ensure Firefox is installed and the path in the script is correct.

## Usage

1. Update the URL in the script to the website you want to scrape:
```python
url = "https://example.com/"  # Replace with your target URL
```

2. Run the script:
```bash
python web_scraper.py
```

3. View the results in the generated `scraped_data.html` file.

## Customization

- Adjust the regex patterns in the script to refine the extraction process
- Modify the waiting time (`time.sleep(5)`) based on the website's loading speed
- Add more patterns to extract different types of information

## Legal Disclaimer

This tool is provided for educational and research purposes only. Users are responsible for ensuring that their use of this tool complies with applicable laws, including:

- The Computer Fraud and Abuse Act
- Website Terms of Service
- Local data protection and privacy laws

Always respect robots.txt and rate limits when scraping websites. Unauthorized access to systems and data may be illegal in your jurisdiction.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
