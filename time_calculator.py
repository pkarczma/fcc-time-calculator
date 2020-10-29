def add_time(start, duration, initweekday = None):
    # Extract hours, minutes, AM/PM from start time and duration
    inittime, initampm = start.split()
    inithr, initmin = inittime.split(":")
    addhr, addmin = duration.split(":")
    # Convert to 24-hours clock format
    inithr = str(int(inithr) + 12 * int(initampm == "PM"))

    # Add minutes
    finalmin = int(initmin) + int(addmin)
    # Check if this adds up to more than one hour
    singlehr = int(finalmin / 60)
    # Calculate final minutes
    finalmin = finalmin % 60
    # Check if we should add '0' in front of minutes
    zeromin = ""
    if finalmin < 10:
        zeromin = "0"

    # Add hours
    finalhr = int(inithr) + int(addhr) + singlehr
    # Check how many times we cross the midnight
    dayslater = int(finalhr / 24)
    #print(dayslater)
    # Calculate final hour and AM/PM
    finalhr = finalhr % 24
    finalampm = "AM"
    if finalhr > 11:
        finalampm = "PM"
    if finalhr > 12:
        finalhr -= 12
    if finalhr == 0:
        finalhr = 12
    
    # Construct final string with time
    finaltime = str(finalhr) + ":" + zeromin + str(finalmin) + " " + finalampm
    # In case day of the week is provided
    if initweekday != None:
        weekday = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
        index = weekday.index(initweekday.lower().capitalize())
        finaltime = finaltime + ', ' + weekday[(index + dayslater) % 7]
    
    # Add information about the number of days later
    if dayslater == 1:
        finaltime += " (next day)"
    elif dayslater > 1:
        finaltime = finaltime + " (" + str(dayslater) + " days later)"

    return finaltime