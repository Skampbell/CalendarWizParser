# Gets a date object for the event
def getFullDate(content):
    
    # Get month
    dateText = content[content.index('data-month="')+12:]
    dateText = dateText[0:10]
    month    = dateText[:dateText.index('"')]
    
    # Get Year
    dateText = content[content.index('data-year="')+11:]
    dateText = dateText[0:10]
    year     = dateText[:dateText.index('"')]
    
    date = {
        "month" : month,
        "year"  : year
    }

    return date

# Removes only the shown event text on calender
def getEventText(dayContent):

    # Remove the event from preciding and trailing html
    eventContent = dayContent[:dayContent.index('<')]
    eventContent = eventContent[1:]
    eventContent = eventContent[eventContent.index('>')+1:].strip()

    return eventContent

# Returns on the location in text '@ location'
def getLocationText(dayContent):

    locationContent = dayContent[dayContent.index('span')+4:]
    locationContent = locationContent[:dayContent.index('<')]
    locationContent = locationContent[locationContent.index('@')+2:]
    locationContent = locationContent[:locationContent.index('<')]

    return locationContent


# Return event object
def getEventObject(dayContent):
    # Call function to remove first event from day
    eventContent = getEventText(dayContent)
    
    # Print the event name
    print(eventContent)
        
        # If the practice is not at tstreet it has location
        if dayContent.index('span') < 200:
            
            # Get location text
            locationContent = getLocationText(dayContent)
            
            # Print location
            print(locationContent)

    event = {

}

