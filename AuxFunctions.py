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

# Get all teams from event text
def getTeams(event):
    # Decleration
    noTime = ''
    teams  = []
    # Cut off time
    if event.count(':') is not 0:
        noTime = event[:event.index(':')]
        noTime = noTime[:noTime.rfind(' ')]
    
    
    # Get team if it exsits
    while noTime.count('-') is not 0:
        # Get age
        teamAge = noTime[:noTime.index('-')].strip()
        noTime = noTime[noTime.index('-')+1:]
    
        # Get coach or number
        if noTime.count(' ') is not 0:
            coach = noTime[:noTime.index(' ')].strip()
        else:
            coach = noTime.strip()
        
        # Remove any commas
        coach = coach.replace(',','')
        
        # Remove coach from notime
        noTime = noTime[noTime.index(coach) + len(coach):]
        if noTime.count('/') is not 0:
            noTime = noTime[noTime.index('/') + 1:]
        
        # create the team
        team = {
            'Age': teamAge,
            'Coach': coach
            }

        # Add to  list of teams
        teams.append(team)
        
    return teams

# Get time range of event
def getTime(content):
    
    # If easy time
    if content.count(':') is not 0:
        # Remove event description
        timeText = content[content.index(':')-2:]
        timeText = timeText.strip()
    
        # Get start time components
        startHour = timeText[:timeText.index(':')]
        startMin  = timeText[timeText.index(':')+1:5]
        isAM      = startMin[-1:] == 'a'
        
        # Get end time
        endHour = timeText[timeText.index(startMin):]
        endHour = endHour[:endHour.index(':')]
        endHour = endHour[endHour.rfind(' '):].strip()
        endMin  = timeText[-4:].strip()
        endMin  = endMin[:2]
        
        # Remove am/pm
        if len(startMin) is not 2:
            startMin = startMin[:2]
        
        # Check if hour is int
        try:
            x = int(startHour) + 1
        except:
            # If not try again
            return getTime(timeText[4:])
    
        # Create time objects
        startTime = {
            'hour'  : int(startHour),
            'minute': int(startMin)
            }
        endTime = {
            'hour'  : int(endHour),
            'minute': int(endMin)
            }

        time = {
            'start': startTime,
            'end'  : endTime,
            'AM'   : isAM
            }

        return time
    else:
        return None
        timeText = content[content.rfind(' '):]
    return timeText
# Return event object
def getEventObject(dayContent):
    # Call function to remove first event from day
    eventContent = getEventText(dayContent)
    
    # If the practice is not at tstreet it has location
    if dayContent.index('span') < 200:
        
        # Get location text
        locationContent = getLocationText(dayContent)

#    print(getTeams(eventContent))
    print(getTime(eventContent))
#    event = {
#        "Teams" : getTeams(eventContent)
#    }

