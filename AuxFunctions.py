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

    # If no teams return it
    if len(teams) is 0:
        return None
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
        isStartAM = startMin[-1:] == 'a'
        
        
        # Get end time
        endHour = timeText[timeText.index(startMin):]
        endHour = endHour[:endHour.index(':')]
        endHour = endHour[endHour.rfind(' '):].strip()
        endMin  = timeText[-4:].strip()
        endMin  = endMin[:3]
        isEndAM = endMin[-1:] == 'a'
        
        # Remove am/pm
        if len(startMin) is not 2:
            startMin = startMin[:2]
        if len(endMin) is not 2:
            endMin   = endMin[:2]
        
        # Check if hour is int
        try:
            x = int(startHour) + 1
        except:
            # If not try again
            return getTime(timeText[4:])
    
        # Adjust time for pm
        if not isStartAM:
            startHour = int(startHour)+12
        if not isEndAM:
            endHour   = int(endHour)+12
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
            'end'  : endTime
            }

        return time
    else:
        return None

# Gets the title of an event
def getTitleEvent(content):
    # DECLERATION
    time = ''
    title = ''
    
    # Get time and title of the event
    if content.count(':') is not 0:
        # Get time
        timeText = content[content.rfind(':')-11:].strip()
        
        # Start time
        startHour = int(timeText[:timeText.index(':')])
        startMin  = int(timeText[timeText.index(':')+1:timeText.index(':')+3])
        isStartAM = timeText[timeText.index(':')+3] is 'a'
        
        # End time
        endTime = timeText[timeText.rfind(' '):].strip()
        endHour = endTime[:endTime.index(':')]
        endMin  = endTime[endTime.index(':')+1:-1]
        isEndAM = endMin[-1] is 'a'
        
        # Remove am/pm
        if len(endMin) is not 2:
            endMin   = endMin[:2]
        
        # Check if hour is int
        try:
            x = int(startHour) + 1
        except:
            # If not try again
            return getTime(timeText[4:])
        
        # Adjust time for pm
        if not isStartAM:
            startHour = int(startHour)+12
        if not isEndAM:
            endHour   = int(endHour)+12
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
            'end'  : endTime
        }
        
        
        title = content[:-len(timeText)].strip()

        # Create event object
        event = {
            'title': title,
            'time' : time
        }
    
        return event

    # If no time, only a title
    else:
        title = content
        # Create event object
        event = {
            'title': title
        }
        
        return event
    


# Get a location object
def getLocation(content):
    if content is None:
        locationName = 'Tstreet'
    else:
        locationName = content
    # Create location object
    location = {
        'location': locationName
    }

    return location

def getTitle(content):
    if
# Return event object
def getEventObject(dayContent):
    # Call function to remove first event from day
    eventContent = getEventText(dayContent)
    
    # If the practice is not at tstreet it has location
    if dayContent.index('span') < 200:
        
        # Get location text
        locationContent = getLocationText(dayContent)
    else:
        locationContent = None

    # Get teams and times
    teams    = getTeams(eventContent)
    time     = getTime(eventContent)
    location = getLocation(locationContent)
    
    # If event has no teams get the title
    if teams is None:
            event = getTitleEvent(eventContent)
            return event

    # Create event
    event = {
        'teams'   : teams,
        'time'    : time,
        'location': location
    }

    return event
