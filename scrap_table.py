#Certainly! You can use the `requests` library to fetch the HTML content of a web page and then use `BeautifulSoup` (bs4) to parse and extract tables from it. Here's a simple example:


import requests
from bs4 import BeautifulSoup

# Replace 'your_url_here' with the actual URL of the web page you want to scrape
url = 'https://www.boursorama.com/bourse/devises/taux-de-change-euro-dong-EUR-VND/'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables on the page
    tables = soup.find_all('table')

    # Iterate through each table and extract data
    for table in tables:
        # Process the table data as needed
        rows = table.find_all('tr')
        for row in rows:
            # Extract and print the data in each row
            columns = row.find_all(['td', 'th'])
            row_data = [column.text.strip() for column in columns]
            print(row_data)

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

'''
Replace 'your_url_here' with the actual URL of the web page you want to scrape. This code will print the content of each row in every table on the page.

Remember to check and respect the terms of service of the website you are scraping data from. Some websites may prohibit or restrict web scraping.'''