## Latest News Streamlit App

This project is a Streamlit app that dynamically scrapes and displays the latest news based on user-selected dates. Utilizing Python libraries such as Streamlit for the web app interface, BeautifulSoup for web scraping, and Requests for HTTP requests, it provides an easy-to-use interface for accessing news from a specific source.

## Features

- Dynamic Date Selection: Users can select a year, month, and day to view the news from that specific date.
- Language Toggle: A toggle switch allows users to switch the news language display between English and Hindi.
- News Scraping: Upon user request, the app scrapes news from the specified source for the selected date and displays the titles and links.
- Customizable UI: The app includes custom CSS for styling, including a blue background and modified button appearances.

## Installation

To run this app, you need to have Python installed on your system. Follow the steps below:

```
pip install streamlit
```
```
pip install beautifulsoup4
```
```
pip install requests
```
Firstly import the `streamlit`, `beautifulsoup4` and `requests` libraries through the terminal that will help in the program.

-----

## How to run:

Download the zip file and extract the files. Then open your terminal or command prompt, navigate to the directory where the `main.py` python file is saved, and run the following command:

```
streamlit run main.py
```

## How to Use
After starting the app, follow these steps:

Select a Date: Use the dropdown menus to select a year, month, and day.
Choose Language: Toggle the switch if you prefer to view the news in Hindi.
Scrape News: Click on the "Scrap" button to fetch the news for the selected date.
View Results: The news titles along with their links will be displayed on the page. Click on any link to read the full news article.