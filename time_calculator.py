def add_time(start, duration, init_weekday = None):
    # Extract hours, minutes, AM/PM from start time and duration
    init_time, init_ampm = start.split()[0], start.split()[1]
    init_hr = int(init_time.split(":")[0])
    init_min = int(init_time.split(":")[1])
    add_hr = int(duration.split(":")[0])
    add_min = int(duration.split(":")[1])
    # Convert hours to 24-hours clock format
    init_hr = init_hr + 12 * int(init_ampm == "PM")

    # Add minutes
    final_min = init_min + add_min
    # Check if this adds up to more than one hour
    single_hr = int(final_min / 60)
    # Calculate final minutes
    final_min = final_min % 60

    # Add hours
    final_hr = init_hr + add_hr + single_hr
    # Check how many times we cross the midnight
    days_later = int(final_hr / 24)
    # Calculate final hour
    final_hr = final_hr % 24
    # Extract final AM/PM sign
    final_ampm = "AM"
    if final_hr > 11:
        final_ampm = "PM"
    # Convert hours back to 12-hours clock format
    if final_hr > 12:
        final_hr -= 12
    if final_hr == 0:
        final_hr = 12
    
    # Construct final string with time
    final_time = str(final_hr) + ":" + str(final_min).zfill(2) + " " + final_ampm
    # In case the day of the week is provided
    if init_weekday != None:
        weekday = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
        # Find index of the current day in a weekday array
        index = weekday.index(init_weekday.lower().capitalize())
        # Append final weekday to the time string
        final_time = final_time + ', ' + weekday[(index + days_later) % 7]
    
    # Append information about the number of days later to the string
    if days_later == 1:
        final_time += " (next day)"
    elif days_later > 1:
        final_time = final_time + " (" + str(days_later) + " days later)"

    return final_time