from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import re

# Set up Tor to run with Firefox
options = Options()
options.headless = True
options.binary_location = "/usr/bin/firefox"  # Ensure this is the correct path to your Firefox binary
options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.socks", "127.0.0.1")
options.set_preference("network.proxy.socks_port", 9050)
options.set_preference("network.proxy.socks_remote_dns", True)

# Launch Firefox with Tor
driver = webdriver.Firefox(options=options)

try:
    # Replace this with the actual .onion site URL you want to scrape
    url = "https://learn.deepcytes.io/"
    driver.get(url)
    time.sleep(5)  # Adjust this based on page load speed

    # Scrape the page content
    page_content = driver.page_source

    # Regex patterns for emails, phone numbers, and addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+\d{1,3})?[\s.-]?\(?\d{1,4}?\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4}[\s.-]?\d{1,9}'
    address_pattern = r'\d{1,5}\s\w+\s(?:[A-Za-z0-9\'\.\-\s\,]+)'  # Simple pattern for addresses

    # Find all matches for each pattern
    emails = re.findall(email_pattern, page_content)
    phones = re.findall(phone_pattern, page_content)
    addresses = re.findall(address_pattern, page_content)

    # Combine the extracted data
    scraped_data = {
        "emails": emails,
        "phone_numbers": phones,
        "addresses": addresses,
    }

    # Save the scraped data to an HTML file
    with open("scraped_data.html", "w") as file:
        file.write("<html><body>\n")
        file.write("<h1>Scraped Data</h1>\n")
        file.write("<h2>Emails:</h2>\n<ul>\n")
        for email in emails:
            file.write(f"<li>{email}</li>\n")
        file.write("</ul>\n")
        file.write("<h2>Phone Numbers:</h2>\n<ul>\n")
        for phone in phones:
            file.write(f"<li>{phone}</li>\n")
        file.write("</ul>\n")
        file.write("<h2>Addresses:</h2>\n<ul>\n")
        for address in addresses:
            file.write(f"<li>{address}</li>\n")
        file.write("</ul>\n")
        file.write("</body></html>\n")

    print("Data scraped and saved to scraped_data.html")

finally:
    driver.quit()
