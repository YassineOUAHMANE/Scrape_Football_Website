# Football Match Scraper 🏟️⚽
This project is a Python script that scrapes football match data from a website using BeautifulSoup. It allows users to enter any specific date and retrieves the matches scheduled for that day, saving the data in an organized CSV file.
## Features
📅 User Input for Date: The script prompts the user to enter a specific date.
🏆 Match Data Scraping: It fetches details like match time, teams, and score from a football website.
📂 CSV Output: The match details are saved in a CSV file for easy access and analysis.
# Prerequisites 🛠️
To run this project, you'll need to have the following installed:
Python 3.x
requests library: To send HTTP requests to the website.
BeautifulSoup (from bs4): To parse the HTML and extract data.
csv: To save the data in a csv file

# How It Works ⚙️
User Input: The user is asked to input a date in the format YYYY-MM-DD.
Send Request to the Website: The script uses requests to send a GET request to the football website to fetch the data for the specified date.
HTML Parsing: BeautifulSoup is used to parse the HTML content and extract match details like:
Match Time ⏰
Teams 🏃‍♂️
Match Score 🏟️
Save to CSV: Once the data is extracted, it is organized into a table and saved as a .csv file using pandas.

