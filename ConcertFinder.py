# pip install requests
import requests

# pip install beautifulsoup4
from bs4 import BeautifulSoup

# pip install datetime
from datetime import datetime

def concertfinder():

    # Enter band to search
    band = input("Enter band name: ")

    # Create url to search band on songkick.com
    url = "https://www.songkick.com/search?page=1&per_page=10&query=" + str(band) + "&type=upcoming"

    # Issue HTTP GET request to retrieve data from above url
    page = requests.get(url)

    # Create a Beautiful Soup object using the retrieved data
    soup = BeautifulSoup(page.content, "html.parser")

    # Find all list items with the class 'concert event'
    results = soup.find_all("li", class_="concert event")

    # Contains the %b formatting of each month
    months = {
                "January": "Jan",
                "February": "Feb",
                "March": "Mar",
                "April": "Apr",
                "May": "May",
                "June": "Jun",
                "July": "Jul",
                "August": "Aug",
                "September": "Sep",
                "October": "Oct",
                "November": "Nov",
                "December": "Dec",
            }

    # List of concert dates and their locations
    concerts = []

    # Iterate through each concert date
    for element in results:
        
        # Filter band name
        band = element.find("p", class_="summary").text.strip()
        band = "".join(filter(str.isalpha, band.split()[0]))

        # Filter concert date
        date = element.find("p", class_="date").text.strip()
        date = date.split()[1] + " " + months[date.split()[2]] + " " + date.split()[3]

        # Get concert location
        location = element.find("p", class_="location").text.strip()

        # Save the concert's date and location
        concerts.append((date, location))

    # Sort the list of concerts by its date
    concerts.sort(key = lambda date: datetime.strptime(date[0], '%d %b %Y'))

    # Displays the nearest concert date only if it exists
    try:
        # Retrieve the nearest concert date
        nearest_date = concerts[0][0]

        print("The nearest concert is on " + nearest_date + " at " + location + ".")
    except:
        print("There are no upcoming concerts for " + band + ".")

concertfinder()