# Take CalendarWiz html and parse it to events
# ParseCalendar.py

import urllib2
from   AuxFunctions      import *
from   FirebaseFunctions import *

# Set url to calendar page made by CalendarWiz
url = 'https://www.calendarwiz.com/calendars/calendar.php?crd=tstreetvolleyballclub&op=cal&month=4&year=2019'

# Use library to open socket request to url
response = urllib2.urlopen(url)

# Read the html from the url request
webContent = response.read()

# DECLERTION
days   = []

# Start parsing each day
# Strip the content above the calendar
for day in range(1, webContent.count("data-day")-1):
    # DECLERATION
    events = []

    # Strip table cell content away
    dayContent   = webContent[webContent.index('data-day="'+str(day)+'"'):len(webContent)]

    # For each event
    while dayContent.count('Click for event details') is not 0:
        # Remove the preceding events dialog
        dayContent = dayContent[dayContent.index('Click for event details')+20:]

        # Call function to get event object and add to list of events
        events.append(getEventObject(dayContent))

    # Define day object
    day = {
        'events': events
    }

    days.append(day)

# Get month and year
fullDate = getFullDate(webContent)

# Post to firebase
postToFirebase(days, fullDate)
